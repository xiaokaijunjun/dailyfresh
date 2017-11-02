from django.shortcuts import render,HttpResponse,render,redirect
from django.http import JsonResponse,HttpResponseRedirect
from df_user.models import *
from df_goods.models import GoodsInfo
from hashlib import sha1
from df_user import user_decorator
#首页
def index(request):
    return render(request,'df_user/index.html')
#注册
def register(request):
    if request.method == 'GET':
        return render(request,'df_user/register.html')
    elif request.method == 'POST':
        uname = request.POST.get('user_name')
        upwd = request.POST.get('pwd')
        upwd2 = request.POST.get('cpwd')
        uemail = request.POST.get('email')
        #判断两次密码
        if upwd !=upwd2:
            return redirect('/user/register/')
        #密码加密
        s1 = sha1()
        s1.update(upwd.encode('utf-8'))
        upwd3 = s1.hexdigest()
        UserInfo.objects.create(uname=uname,upwd=upwd3,uemail=uemail)
        return redirect('/user/login/')
    else:
        return redirect('/user/login/')
def register_exist(request):
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})
#登录
def login(request):
    if request.method == 'GET':
        uname = request.COOKIES.get('uname','')
        context = {'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
        return render(request,'df_user/login.html',context)
    elif request.method == 'POST':
        uname = request.COOKIES.get('uname', '')
        uname = request.POST.get('username')
        upwd = request.POST.get('pwd')
        jizhu = request.POST.get('jizhu',0)
        users = UserInfo.objects.filter(uname=uname)
        #判断如果未查到则用户名错，如果查到判断密码是否正确，正确跳转到用户中心
        if len(users)==1:
            s1 = sha1()
            s1.update(upwd.encode('utf-8'))
            if s1.hexdigest() == users[0].upwd:
                url = request.COOKIES.get('url','/')
                red = HttpResponseRedirect(url)
                #记住用户名,session 10天失效
                if jizhu !=0:
                    request.session.set_expiry(60 * 60 * 24 * 10)
                else:
                    request.session.set_expiry(60*60)
                #判断登录
                request.session['user_id']=users[0].id
                request.session['uname']=uname
                return red
            else:
                context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 1, 'uname': uname, 'upwd': upwd}
                return render(request, 'df_user/login.html', context)
        else:
            context = {'title': '用户登录', 'error_name': 1, 'error_pwd': 0, 'uname': uname,'upwd':upwd}
            return render(request,'df_user/login.html',context)
    else:
        return redirect('/user/login/')
#注销
def logout(request):
    del request.session['uname']
    return redirect('/goods/index/')
#用户中心
@user_decorator.login
def info(request):
    v = request.session.get('uname',None)
    if not v:
        return redirect('/user/login/')
    #用户信息
    user = UserInfo.objects.get(id=request.session['user_id'])
    #最近浏览
    goods_ids=request.COOKIES.get('goods_ids','')
    goods_ids1=goods_ids.split(',')
    goods_list =[]
    for goods_id in goods_ids1:
        goods_list.append(GoodsInfo.objects.get(id=int(goods_id)))
    context = {'title':'用户中心','user':user,'page_name':1,'goods_list':goods_list}
    return render(request,'df_user/user_center_info.html',context)
#最近浏览(查看最近浏览20条记录)
def recent(request):
    goods_ids = request.COOKIES.get('goods_ids', '')
    goods_ids1 = goods_ids.split(',')
    goods_list = []
    for goods_id in goods_ids1:
        goods_list.append(GoodsInfo.objects.get(id=int(goods_id)))
    context = {'title': '最近浏览','page_name': 1, 'goods_list': goods_list}
    return render(request,'df_user/recent_view.html',context)

#订单
@user_decorator.login
def order(request):
    context = {'title':'用户中心','page_name':1}
    return render(request,'df_user/user_center_order.html',context)
#收获地址
@user_decorator.login
def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        post= request.POST
        user.ushou = post.get('ushou')
        user.uaddress = post.get('uaddress')
        user.uyoubian = post.get('uyoubian')
        user.uphone = post.get('uphone')
        user.save()
    context = {'title':'用户中心','user':user,'page_name':1}
    return render(request,'df_user/user_center_site.html',context)
#购物车
@user_decorator.login
def cart(request):
    context = {'title':'用户中心','page_name':1}
    return render(request,'df_user/cart.html',context)

