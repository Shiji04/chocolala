from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import Order, District, Branch,Chocolate
from .forms import OrderCreationForm


# Create your views here.
def indexpage(request):
    return render(request, "index.html")


def tvm(request):
    return render(request, "tvm.html")


def ekm(request):
    return render(request, "ekm.html")


def alappuzha(request):
    return render(request, "alappuzha.html")


def kottayam(request):
    return render(request, "kottayam.html")


def palakkad(request):
    return render(request, "palakkad.html")


def thrissure(request):
    return render(request, "thrissure.html")


def kozhikode(request):
    return render(request, "kozhikode.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('login')
    return render(request, 'login.html')


def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already taken")
                return redirect('registration')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
        else:
            messages.info(request, "password not matched")
            return redirect('registration')
        return redirect('/')
    return render(request, "registration.html")

def customerorder(request):
    form = OrderCreationForm()
    if request.method == 'POST':
        form = OrderCreationForm(request.POST)
        if form.is_valid():
            messages.success(request, "your order is place")
            form.save()


            return redirect('customerorder')

    return render(request, 'customerorder.html', {'form': form})


def load_cities(request):
    district_id = request.GET.get('district_id')
    branch = Branch.objects.filter(district_id=district_id).all()
    return render(request, 'branchdropdown.html', {'branch': branch})

# return HttpResponse("hello world")
#
# def getdist(request):
#     ans=request.Get['district']
#     return render(request, "customer_order.html",{'ans':ans})
