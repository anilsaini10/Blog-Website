from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login ,logout
from home.models import Contact,HomeBlog
from django.contrib import messages
from blog.models import Post
from . import views

# Create your views here.
def home(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        author = request.POST['author']
        print("123")
        homeblog = Post.objects.create(title =title, content = content,author=author)
        # print(homeblog  +"anil anil")
        # homeblog.save()
        messages.success(request,  "Your article is posted successfully")

    return render(request,'home/home.html')


def about(request):
    return render(request,'home/about.html')
    


def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<3 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request,"Please fill form correctly")
        else:
            contact = Contact(name=name, email=email,phone = phone, content=content)
            contact.save()
            messages.success(request,"Your message is successfully added")
    return render(request,'home/contact.html')
    

def search(request):
    query = request.GET['query']
    if len(query)>20 :
        allPosts=[]
    else:
        allPostsTitle= Post.objects.filter(title__icontains = query)
        allPostsContent= Post.objects.filter(title__icontains = query)
        allPosts= allPostsTitle.union(allPostsContent)
    params = {'allPosts': allPosts}
    return render(request,'home/search.html',params)

def handleSignup(request):
    if(request.method =='POST'):
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        if len(username) > 10:
            messages.error(request,"username must be under 10")
            return redirect('home')

        if pass1!=pass2:
            messages.error(request,"password is not matching")
            return redirect('home')
        
        if not username.isalnum():
            messages.error(request,"must contain alphabat or number")
            return redirect('home')

        myuser.save()
        messages.success(request,"Sign Up success")
        return redirect('home')

    else:
        return HttpResponse("404 -Not Found")



def handleLogin(request):
    if request.method =="POST":

        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username =loginusername, 
               password = loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"login successfully")
            return redirect('home')
        else:
            messages.success(request,"try again")
            return redirect('home')
    return HttpResponse("404 error")

def handleLogout(request):

    logout(request)
    messages.success(request,"logout success")
    return redirect('home')
    