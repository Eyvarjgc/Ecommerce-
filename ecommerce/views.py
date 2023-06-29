from django.shortcuts import render,redirect
from .form import RegisterUser,ProductForm,changepassword,PasswordResetForm
from .models import CustomUser,Product,car,Genre,Comment
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.query_utils import Q
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
# Create your views here.


# "GET /?save=savePasta
def home(request):
    products = Product.objects.all()
    cars =  car.objects.all()
    genre = Genre.objects.all()
    Search = request.GET.get('search') if request.GET.get('search') != None else ''
    SearchObjects = Product.objects.filter(
        Q(name__icontains = Search)
    )
    favoriteproduct = Product.objects.get(id = 2)
    numbers = range(1, 1000)
    if request.method == 'GET':
        for car_instance in products:
            if request.GET.get('save' + str(car_instance.id)):
                homeamount = request.GET.get('cantidad')
                IdProduct = Product.objects.get(id = car_instance.id) 
                IdProduct.amount = homeamount
                Amount = IdProduct.amount
                addcar = car.objects.create(
                    host = request.user,
                    product = car_instance,
                    carprice = IdProduct.price,
                    caramount = Amount
                )
                messages.success(request,'Producto exitosamente añadido al carrito')
            else:
                messages.error(request,'Error al guardar el producto')

    CarCount = cars.count()
    context = {
        'product':SearchObjects,
        'CarCount': CarCount,
        'genre':genre,
        'numbers':numbers,
        'favoriteproduct':favoriteproduct
    }

    return render(request,'home.html',context)


def carrito(request):
    Listproduct = car.objects.all()

    if request.method == 'POST':
        for i in Listproduct:
            if request.POST.get('eliminar' + str(i.id)):
                IdProduct = car.objects.get(id = i.id)
                
                IdProduct.delete()
                return redirect('carrito')

    total = 0
    for n in Listproduct: 
        ntotal = n.carprice * n.caramount
        Price = ntotal
        total += Price 
        
    context = {
        'ProductsList':Listproduct,
        'PriceProduct' : total,
        'ntotal':ntotal
    }
    return render(request,'carrito.html',context)


def genre(request, pk):
    Listproduct = Product.objects.filter(id = pk)
    # filter_genre = Genre.objects.filter(id = pk) 
    if request.method == 'GET':
        for car_instance in Listproduct:
            if request.GET.get('save' + str(car_instance.id)):
                # return redirect('delivery')
                IdProduct = Product.objects.get(id = car_instance.id)
                addcar = car.objects.create(
                    host = request.user,
                    product = car_instance,
                    carprice = IdProduct.price
                )

    context = {
        # 'genre': filter_genre,
        'Listproduct': Listproduct
    }
    return render(request,'genre.html',context)


def detail(request,pk):
    product = Product.objects.get(id = pk)
    # genre = Genre.objects.get(id=pk)
    coment = product.comment_set.all()
    if request.method == 'GET':
        if request.GET.get('save'):
            # return redirect('delivery')
            IdProduct = Product.objects.get(product.id)
            addcar = car.objects.create(
                host = request.user,
                product = IdProduct.name,
                carprice = IdProduct.price
            )
    if request.method == 'POST':
        message = Comment.objects.create(
            host = request.user,
            commentto = product,
            body = request.POST.get('body')
        )

        return redirect('detail',pk = product.id)
    context = {
        'product': product,
        'genre':genre,
        'coment':coment,
    }
    return render(request,'detail.html',context)



def login(request):

    return render(request,'registration/login.html')


def register(request):
    form = RegisterUser()
    if request.method == 'POST':
        form = RegisterUser(request.POST)
        if form.is_valid:
            # CustomUser = form.save(commit=False)
            # CustomUser.username = CustomUser.username.lower()
            # CustomUser.save()
            # login(request,CustomUser)
            form.save()
            return redirect('home')
        else:
                messages.error(request,'no ha ingresado las contraseñas correctamente')
    context = {
        'form':form,
    }
    return render(request, 'users/register.html',context)


def LogoutUser(request):
    logout(request)
    return redirect(home)



def addproduct(request):
    products = ProductForm()
    if request.method == 'POST':
        products = ProductForm(request.POST ,request.FILES)
        if products.is_valid:
            products.save()
            return redirect('home')

    return render(request,'add-product.html',{'form':products})


def profile(request,pk):
    user = CustomUser.objects.get(id = pk)
    context = {
        'user':user
    }
    return render(request,'users/profile.html',context)


def updateamount(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.post)
        if form.is_valid():
            form.save()
    return render(request,'updateamount.html',{'form':form})






# @login_required
# def change_password(request):
#     user = request.user
#     form = changepassword(user)
#     if request.method == 'POST':
#         form = changepassword(user,request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Se ha cambiado la contraseña correctamente')
#         else:
#             for error in list(form.errors.values()):
#                 messages.error(request,error)

#     context = {
#         'form':form
#     }
#     return render(request,'change_password.html',context)


# def reset_password(request):
#     user = request.user
#     form = PasswordResetForm()
#     if request.method == 'POST':
#         form = PasswordResetForm(user,request.POST)
#         if form.is_valid():
#             user_mail = form.cleaned_data['email']
#             associateduser = get_user_model().objects.filter(Q(email = user_mail)).first()
#             if associateduser:
#                 subject = 'Solicitud para cambiar contraseña '
#                 Messages = render_to_string('reset_password.html',{
#                     'user': associateduser
#                 })
#                 email = EmailMessage.send(subject,Messages, to=[associateduser.email])
#                 if email.send():
#                     messages.success(request,'Por favor revise su email')
#                 else:
#                     messages.error(request, 'Error al enviar email')
#             return redirect('home')
#     context = {
#         'form':form
#     }
#     return render(request, 'reset_password.html', context)