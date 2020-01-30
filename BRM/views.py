from django.shortcuts import render
from BRM.forms import SearchForm,NewBookForm
from BRM.models import Book
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse

def userLogin(request):
    data={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            request.session['username']=username
            return HttpResponseRedirect('/BRM/view-books')
        else:
            data['error']="Username or password incorrect"
            return render(request,'BRM/User_login.html',data)
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect('/BRM/view-books')
        else:
            return render(request,'BRM/User_login.html',data)
@login_required(login_url='/BRM/login')
def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/BRM/login')

@login_required(login_url='/BRM/login')
def editBook(request):
    username=request.session['username']
    book=Book.objects.get(id=request.GET['bookid'])
    fields={'title':book.title,'price':book.price,"author":book.author,'publisher':book.publisher}
    form=NewBookForm(initial=fields)
    res=render(request,'BRM/edit_book.html',{'form':form,'book':book,'username':username})
    return res


@login_required(login_url='/BRM/login')   
def edit(request):
    if request.method=='POST':
        username=request.session['username']
        form=NewBookForm(request.POST)
        book=Book()
        book.id=request.POST['bookid']
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
        return HttpResponseRedirect('/BRM/view-books',{'username':username})
@login_required(login_url='/BRM/login')
def deleteBook(request):
    username=request.session['username']
    bookid=request.GET['bookid']
    book=Book.objects.filter(id=bookid)
    book.delete()
    return HttpResponseRedirect('/BRM/view-books')
@login_required(login_url='/BRM/login')
def searchBook(request):
    username=request.session['username']
    form=SearchForm()
    res=render(request,'BRM/search_book.html',{'form':form,'username':username})
    return res
@login_required(login_url='/BRM/login')
def search(request):
    username=request.session['username']
    print(request.POST)
    form =SearchForm(request.POST)
    title=form.data['title']
    books=Book.objects.filter(title=title)
    res=render(request,'BRM/search_book.html',{'books':books,'form':form,'username':username})
    return res


@login_required(login_url='/BRM/login')
def newBook(request):
    username=request.session['username']
    form=NewBookForm()
    res=render(request,'BRM/new_book.html',{'form':form,'username':username})
    return res
@login_required(login_url='/BRM/login')
def add(request):
    username=request.session['username']
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=Book()
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
        s="Record Stored <a href='/BRM/view-books'> View All Book</a>"
        return HttpResponse(s)


@login_required(login_url='/BRM/login')
def viewBook(request):
    username=request.session['username']
    books=Book.objects.all()
    res=render(request,"BRM/View_book.html",{'books':books,'username':username})
    return res


# Create your views here.
