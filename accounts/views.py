from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout
from accounts.models import UserRegister, AddToCart, Order, Product
from homepage.models import Item
from django.views.decorators.csrf import csrf_exempt


from django.http import HttpResponse
from django.views.generic import View
from datetime import date, datetime
from accounts.utils import render_to_pdf #created in step 4
# Create your views here.



def Register(request):                                  # New user registration
    if request.method == 'POST':

        user = UserRegister()


        user.user_name = request.POST['Candidate_Name']
        user.user_email = request.POST['Candidate_Emailid']
        user.user_gender = request.POST['Candidate_Gender']
        user.user_dob = request.POST['Candidate_DOB']
        user.user_phonenumber = request.POST['Candidate_Phonenumber']
        user.user_address = request.POST['Candidate_Adderss']
        user.user_city = request.POST['Candidate_City']
        user.user_state = request.POST['Candidate_State']
        user.user_password = request.POST['Candidate_Password']
        conform_password = request.POST['Candidate_Conformpassword']

        user.save()


        if user.user_password == conform_password:
            if User.objects.filter(username=user.user_name).exists():
                messages.info(request, "Username already exits")
                return redirect('Register')
            elif User.objects.filter(email=user.user_email).exists():
                messages.info(request, "Email already exits")
                return redirect('Register')
            else:
                user = User.objects.create_user(username = user.user_name, password = user.user_password, email= user.user_email)
                user.save()
                messages.info(request, "Registered successfully")
                return redirect('Login')
                
                
        else:
            print("User paswword unmatched")
            messages.info(request, "Password not matched")
            return redirect('Register')
        return redirect('index')
    else:
        return render(request, 'register.html')



def Login(request):                                             #User Login Function
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username= username, password = password)
         
        if user is not None : 
            auth.login(request, user)
            items = Item()
            items = Item.objects.all()
            
            return redirect("../../", {'items': items})

        else:
            messages.info(request, "invalid credentials")
            return redirect('Login')
    else:
        return render(request, 'login.html')


def logout_user(request):                                            # Logout Function
    logout(request)
    return render(request, 'logout.html')

def dropdown(request):
    text = "All functions of drop down menu will come into work as soon as possible"
    return render(request, 'dropdown.html', {'text':text})



def orders_view(request, userid):
    login_user = User.objects.get(pk= userid)
    try:
        user = UserRegister.objects.get(user_email= login_user.email)
    except UserRegister.DoesNotExist:
        text = "No Orders yet"
        return render(request, 'note.html', {'text': text})
    order = Order.objects.filter(order_useremail= login_user.email)
    return render(request, 'orders_view.html', {'order': order})

   

    

def addtocart_view(request, userid):                                 # Add to cart all items
    if User.is_authenticated:
        current_user = User.objects.get(pk = userid)
        cart_all_items = AddToCart.objects.get(cart_useremail= current_user.email )
        if AddToCart.objects.filter(cart_useremail= current_user.email).exists():
            cart_all_items = AddToCart.objects.filter(cart_useremail= current_user.email )
            return render(request, 'addtocart.html', {'cart_all_items': cart_all_items})

        else:
        
            text = "No Items in your cart !!!"
            return render(request, 'note.html', {'text': text})

    else:
        text="Please Login in to your account !!!"
        return render(request, 'note.html', {'text': text})

        


def addtocart(request, userid, itemsid):                        # Add to cart current item display at top
    if User.is_authenticated:
        current_user = User.objects.get(pk = userid)
        #print(current_user.email)
        #print(itemsid)
        cart_item = Item.objects.get(pk = itemsid)
        cart_add_item = AddToCart()
        cart_add_item.cart_useremail = current_user.email
        cart_add_item.cart_name = cart_item.item_name
        cart_add_item.cart_image = cart_item.item_image
        cart_add_item.cart_price = cart_item.item_price
        cart_add_item.cart_publisher = cart_item.item_publisher
        cart_add_item.cart_origin = cart_item.item_origin
        cart_add_item.cart_description = cart_item.item_description
        if AddToCart.objects.filter(cart_useremail= current_user.email).exists():
            print("1st if")
            fetch_all_cart_items = AddToCart.objects.filter(cart_useremail= current_user.email)
            if fetch_all_cart_items.filter(cart_name= cart_item.item_name).exists():
                print("2nd if")
                cart_add_item = fetch_all_cart_items.get(cart_name= cart_item.item_name)
                cart_add_item.cart_quantity += 1
                cart_add_item.save()

                cart_add_item.cart_quantity += 1
                cart_add_item.save()
            else:
                print("1st else part")
                cart_add_item.cart_quantity = 1
                cart_add_item.save()

        else:
            print("2nd else")
            cart_add_item.cart_quantity = 1
            cart_add_item.save()

        cart_add_item.cart_total_price = cart_add_item.cart_quantity * cart_add_item.cart_price
        cart_add_item.save()

        cart_add_item.cart_total_price = cart_add_item.cart_quantity * cart_add_item.cart_price
        cart_add_item.save()

            

        cart_all_items = AddToCart.objects.filter(cart_useremail = current_user.email).exclude(pk = cart_add_item.id)


        return render(request, 'addtocart.html', {'cart_add_item': cart_add_item, 'cart_all_items': cart_all_items})
    else:
        text="Please Login in to your account !!!"
        return render(request, 'note.html', {'text': text})


def addtocart_inactiveuser(request):                                    # Add to cart INACTIVE user
    text = "Please login to add it in your cart"
    return render(request, 'note.html', {'text': text})

def deleteitem(request, itemid, userid):
    if User.is_authenticated:
        if AddToCart.objects.filter(pk= itemid).exists():
            login_user = User.objects.get(pk= userid)
            item = AddToCart.objects.get(pk=itemid ,cart_useremail= login_user.email)
            item.delete()
        
        else:
            text = "No Item exists in your cart. Please go to Homepage and add items in your cart."
            return render(request, 'note.html', {'text': text})
    else:
        text="Please Login in to your account !!!"
        return render(request, 'note.html', {'text': text})


    cart_all_items = AddToCart.objects.filter(cart_useremail= login_user.email)
    return render(request, 'addtocart.html', {'cart_all_items': cart_all_items})

def increase_quantity(request, itemid, userid):                       # Increasing qunatity
    if User.is_authenticated:
        if AddToCart.objects.filter(pk= itemid).exists():
            login_user = User.objects.get(pk= userid)
            item = AddToCart.objects.get(pk=itemid ,cart_useremail= login_user.email)
            item.cart_quantity += 1
            item.save()    
        
        item.cart_total_price = item.cart_quantity * item.cart_price
        item.save()
        cart_all_items = AddToCart.objects.filter(cart_useremail= login_user.email)
        return render(request, 'addtocart.html', {'cart_all_items': cart_all_items})

    else:
        text="Please Login in to your account !!!"
        return render(request, 'note.html', {'text': text})

def decrease_quantity(request, itemid, userid):                     #decrease quantity
    if User.is_authenticated:
        if AddToCart.objects.filter(pk= itemid).exists():
            login_user = User.objects.get(pk= userid)
            item = AddToCart.objects.get(pk= itemid, cart_useremail= login_user.email)
            if item.cart_quantity == 1:
                pass
            else:
                item.cart_quantity -= 1
                item.save()    

    
        item.cart_total_price = item.cart_quantity * item.cart_price
        item.save()
        cart_all_items = AddToCart.objects.filter(cart_useremail= login_user.email)
        return render(request, 'addtocart.html', {'cart_all_items': cart_all_items})

    else:
        text="Please Login in to your account !!!"
        return render(request, 'note.html', {'text': text})

def profile(request, userid):                                   # Profile data page
    if User.is_authenticated:
        text = "Your details"
        print(userid)
        print(type(userid))
        current_user = User.objects.get(pk = userid)
        print(type(current_user))
        profile_user = UserRegister.objects.get(user_name= current_user.username)

        

       
        print(type(profile_user))
        return render(request, 'profile.html', {'profile_user':profile_user, 'text':text})

    else:
        text="Please Login in to your account !!!"
        return render(request, 'note.html', {'text': text})

def editprofile(request, userid):                           # Editing profile data
    if User.is_authenticated:
        login_user = User.objects.get(pk= userid)
        current_user = UserRegister.objects.get(user_email=login_user.email)
        return render(request, 'editprofile.html', {'profile_user': current_user})

    else:
        text="Please Login in to your account !!!"
        return render(request, 'note.html', {'text': text})

def update(request, userid):                                # Updating profile data sucessfully
    if User.is_authenticated:
        login_user = User.objects.get(pk= userid)
        user = UserRegister.objects.get(user_email=login_user.email)

        if request.method == "POST":

            user.user_name = request.POST['Candidate_Name']
            user.user_email = request.POST['Candidate_Emailid']
            user.user_gender = request.POST['Candidate_Gender']
            user.user_dob = request.POST['Candidate_DOB']
            user.user_phonenumber = request.POST['Candidate_Phonenumber']
            user.user_address = request.POST['Candidate_Address']
            user.user_city = request.POST['Candidate_City']
            user.user_state = request.POST['Candidate_State']    

            user.save()

            return redirect('index')

    else:
        text="Please Login in to your account !!!"
        return render(request, 'note.html', {'text': text})

def buynow(request, itemid, userid):                            # Homepage BUYNOW function
    if User.is_authenticated:
        #Request paytm to add money from user account to your account
        login_user = User.objects.get(pk= userid)
        user = UserRegister.objects.get(user_email=login_user.email)

        orderitem = Item.objects.get(pk= itemid)
        if Order.objects.filter(order_name= orderitem.item_name, order_useremail= login_user.email).exists():
            order = Order.objects.get(order_name= orderitem.item_name, order_useremail= login_user.email)
            return render(request, "order.html", {'order': order})

        else:
            ordereditem = Item.objects.get(pk= itemid)
            order = Order()
            order.order_useremail = login_user.email
            order.order_name = ordereditem.item_name
            order.order_image = ordereditem.item_image
            order.order_price = ordereditem.item_price
            order.order_publisher = ordereditem.item_publisher
            order.order_description = ordereditem.item_description
            order.order_origin = ordereditem.item_origin
            order.order_phonenumber = user.user_phonenumber
            order.order_address = user.user_address
            order.save() 
            return render(request, "order.html", {'order': order})

    else:
        text="Please Login in to your account !!!"
        return render(request, 'note.html', {'text': text})

def buynow_cart(request, itemid, userid):           # Buynow button in addtocart
    if User.is_authenticated:
        login_user = User.objects.get(pk= userid)
        user = UserRegister.objects.get(user_email=login_user.email)

        ordereditem = AddToCart.objects.get(pk= itemid, cart_useremail= login_user.email)

        if Order.objects.filter(order_name= ordereditem.cart_name, order_useremail= login_user.email).exists():
            order = Order.objects.get(order_name= ordereditem.cart_name, order_useremail= login_user.email)
            return render(request, "order.html", {'order': order})

        else:
            ordereditem = Item.objects.get(pk= itemid)
            order = Order()
            order.order_useremail = login_user.email
            order.order_name = ordereditem.cart_name
            order.order_image = ordereditem.cart_image
            order.order_price = ordereditem.cart_price
            order.order_publisher = ordereditem.cart_publisher
            order.order_description = ordereditem.cart_description
            order.order_origin = ordereditem.cart_origin
            order.order_phonenumber = user.user_phonenumber
            order.order_address = user.user_address
            order.save() 
            return render(request, "order.html", {'order': order})


    else:
        text="Please Login in to your account !!!"
        return render(request, 'note.html', {'text': text})




def conformorder(request, userid, itemid):              # Conform order button in order page
    if User.is_authenticated:
        if itemid:
            login_user = User.objects.get(pk= userid)
            user = UserRegister.objects.get(user_email= login_user.email)
            order = Order.objects.get(pk= itemid, order_useremail= login_user.email)
            return render(request, 'conformationpage.html', {'order': order})

        else:
            text = "Sorry, due to some techinical issue we cannot process your request. Please try again !!!"
            return render(request, 'note.html', {'text': text})


    else:
        text = "Please Login and try again"
        return render(request, 'note.html', {'text': text})






def generatepdf(request, userid, itemid):
    login_user = User.objects.get(pk= userid)
    user = UserRegister.objects.get(user_email= login_user.email)
    order = Order.objects.get(pk= itemid, order_useremail= login_user.email)

    if request.method == "POST":
        order.order_phonenumber = request.POST['phonenumber']
        order.order_quantity = int(request.POST['quantity'])
        order.order_domain = request.POST['domainname']
        order.order_address = request.POST['address']
        order.save()
    print(order.order_price, type(order.order_price))
    print(order.order_quantity, type(order.order_quantity))
    order.order_total_price = order.order_quantity * order.order_price
    order.save()


    data = {
            'product_name': order.order_name, 
            'user_name': login_user.username,
            'email': login_user.email,
            'price': order.order_price,
            'quantity': order.order_quantity,
            'total_price': order.order_total_price,
            'publisher': order.order_publisher,
            'origin': order.order_origin,
            'billing_address': user.user_address,
            'shipping_address': order.order_address,
            'phone_number': order.order_phonenumber,
            'ordered_date': order.order_ordered_date,
            'delivery_date': order.order_delivery_date,
            'domain_name' : order.order_domain,
            'paymentstatus': order.paymentstatus

    }
    
    pdf = render_to_pdf("invoice.html", data)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        #filename = 'Invoice_12341234.pdf'
        content = 'inline; filename= "Invoice_%s.pdf" ' %(order.order_name)
        download = request.GET.get("download")
        if download:
            content = 'attachment; filename="Invoice_%s.pdf" ' %(order.order_name)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")

def Payment(request, userid):
    login_user = User.objects.get(pk= userid)
    if request.method == 'POST':
        item = request.POST['item_name']
        if item == 'Simple Web Design':
            return render(request, 'payment28.html')
        elif item == 'Website with multiple pages':
            return render(request, 'payment29.html')
        elif item == 'Complex website':
            return render(request, 'payment30.html')
        elif item == 'Website Malware Repair':
            return render(request, 'payment31.html')
        elif item == 'E-commerce Website':
            return render(request, 'payment32.html')
        elif item == 'Web design (Front-End)':
            return render(request, 'payment33.html')
        elif item == 'Design Your Website':
            return render(request, 'product.html')
        else:
            return render(request, 'payment34.html')

    else:
        text= 'Something went wrong'
        return render(request, 'note.html', {'text': text})


def Mainpayment(request):
    return render(request, 'razorpay.html')

def sproduct(request):
    return render(request, 'sproduct.html')

def Dproduct(request):
    if request.method == 'POST':

        product = Product()
        product.product_phonenumber = request.POST['phone']
        product.product_useremail = request.POST['email']
        product.product_price = request.POST['price']
        product.product_domain = request.POST['domain']
        product.product_home = request.POST['product1']
        product.product_contact = request.POST['product2']
        product.product_blog = request.POST['product3']
        product.product_news = request.POST['product4']
        product.product_event= request.POST['product5']
        product.product_product = request.POST['product6']
        product.product_shop = request.POST['product7']
        product.product_login = request.POST['product8']
        product.save()
        return render(request, "product.html")

        
            

    
    



    

