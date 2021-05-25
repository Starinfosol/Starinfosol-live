from django.shortcuts import render, HttpResponse, redirect
from appointment.models import Appointment
from home.models import Contact
from blogs.models import Post
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy


#################################################################################################


def home(request):
    return render(request, "home/index.html")


def about(request):
    return render(request, "home/about.html")


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")


def health(request):
    return render(request, 'health.html')
    # return HttpResponse("this is health-page")


def blogs(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'blogs.html', context)


def updates(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, "updates.html", context)


def blog_single(request):
    return render(request, 'blog-single.html')


def blog_education(request):
    return render(request, 'blog-education.html')


def Terms_conditions(request):
    return render(request, 'Terms_conditions.html')

################################################################################


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email,
                              phone=phone, content=content)
            contact.save()
            messages.success(
                request, "Your message has been successfully sent")
    return render(request, "index.html")

################################################################################


def Appointmentadd(request):
    if request.method == "POST":
        # Get the post parameters
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        department = request.POST['department']
        doctor = request.POST['doctor']
        information = request.POST['information']
        if len(name) < 2 or len(email) < 3 or len(phone) < 10:
            messages.error(request, "Please fill the form correctly")
        else:
            inc = Appointment(name=name, email=email, phone=phone, date=date, department=department, doctor=doctor, information=information)
            inc.save()
            # send_mail(
            #     'Appointment',
            #     '{{name}}',
            #     'starinfosol954@gmail.com',
            #     ['starinfosol954@gmail.com'],
            #     fail_silently=False,
            # )
            messages.success(request, "Your Appointment has been booked successfully")
    return render(request, "index.html")

#################################################################################################


def search(request):
    query = request.GET['query']
    if len(query) > 78:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsAuthor = Post.objects.filter(author__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count() == 0:
        messages.warning(
            request, "No search results found. Please refine your query.")
    params = {'allPosts': allPosts, 'query': query}
    return render(request, 'updates.html', params)

#################################################################################################


def handleSignUp(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous input
        if len(username) < 10:
            messages.error(
                request, " Your user name must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(
                request, " User name should only contain letters and numbers")
            return redirect('home')
        if (pass1 != pass2):
            messages.error(request, " Passwords do not match")
            return redirect('home')

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('home')

    else:
        return HttpResponse("404 - Not found")

#################################################################################################


def handeLogin(request):
    if request.method == "POST":
        # Get the post parameters
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")

    return HttpResponse("404- Not found")

    return HttpResponse("login")

#################################################################################################


def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')

#################################################################################################
