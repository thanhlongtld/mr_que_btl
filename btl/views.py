from django.shortcuts import render, redirect

from btl.models import Users


def index(request):
    request.session['current-page'] = ['test']
    user = None
    if 'username' in request.session:
        user = request.session['username'][0]
        print(user)
    context = {'user': user}
    return render(request, "btl/index.html", context)


def shopcart(request):
    request.session['current-page'] = ['shop-cart']
    if 'username' in request.session:
        context = {'user': request.session['username'][0]}
        return render(request, "btl/shop-cart.html", context)
    else:
        return redirect('login')


def checkout(request):
    request.session['current-page'] = ['shop-cart']
    try:
        context = {'user': request.session['username'][0]}
        return render(request, "btl/checkout.html", context)
    except:
        pass


def login(request):
    users = Users.objects.all()
    for user in users:
        print(user.name, user.password, user.username)

    if request.method == 'POST':
        uName = request.POST.get("username")
        pWord = request.POST.get("password")
        print(uName, pWord)
        print(request.session['current-page'][0])
        try:
            user = Users.objects.get(username=uName)
            if user.password == pWord:
                print("Login")
                request.session['username'] = [user.username]
                curpage = request.session['current-page']
                print(curpage)
                return redirect(request.session['current-page'][0])
            else:
                print("sai mat khau")
        except:
            print("nguoi dung khong ton tai")
        return redirect('login')
    return render(request, "btl/login.html")


def logout(request):
    del request.session['username']
    return redirect(request.session['current-page'][0])
