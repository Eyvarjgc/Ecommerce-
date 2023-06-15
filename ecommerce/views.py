from django.shortcuts import render,redirect
from .form import RegisterUser,ProductForm
from .models import CustomUser,Product,car
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout

# Create your views here.


# "GET /?save=savePasta
def home(request):
    products = Product.objects.all()
    cars =  car.objects.all()
    if request.method == 'GET':
        for car_instance in products:
            if request.GET.get('save' + str(car_instance.id)):
                # return redirect('delivery')
                addcar = car.objects.create(
                    host = request.user,
                    product = car_instance
                )
                
    context = {
        'product':products
    }

    return render(request,'home.html',context)


def delivery(request):
    Listproduct = car.objects.all()
    # Priceproduct = car.

    if request.method == 'POST':
        for i in Listproduct:
            # if request.POST.get('delete' + str(i.id)):
            if request.POST.get(str(i.id)): 
                n = str(i.id)
                print(n)
                Idproduct = car.objects.get(id = n)
                print(f"{Idproduct}  {Idproduct.id}")

        #         Idproduct.delete()


    context = {
        'ProductsList':Listproduct
    }
    return render(request,'delivery.html',context)




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
    return render(request, 'register.html',context)


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