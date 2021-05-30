from django.shortcuts import render, HttpResponse, redirect
from appointment.models import Appointment
from home.models import Contact, Edu
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy


###############################################################################

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")

def Terms_conditions(request):
    return render(request, 'Terms_conditions.html')

def Education(request):
    allEdu = Edu.objects.all()
    context = {'allEdu': allEdu}
    return render(request, 'Education.html', context)

def Pricing(request):
    return render(request, 'Pricing.html')

def Technical(request):
    return render(request, 'Technical.html')

def Educationpost(request, slug): 
    post=Edu.objects.filter(slug=slug).first()
    # comments= BlogComment.objects.filter(Edu=Edu, parent=None)
    # replies= BlogComment.objects.filter(Edu=Edu).exclude(parent=None)
    # replyDict={}
    # for reply in replies:
    #     if reply.parent.sno not in replyDict.keys():
    #         replyDict[reply.parent.sno]=[reply]
    #     else:
    #         replyDict[reply.parent.sno].append(reply)

    context={'Edu':post}
    return render(request, "Educationpost.html", context)
    


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
            contact = Contact(name=name, email=email,phone=phone, content=content)
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
        allEdu = Edu.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsAuthor = Post.objects.filter(author__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent, allPostsAuthor)
        allEduTitle = Edu.objects.filter(title__icontains=query)
        allEduAuthor = Edu.objects.filter(author__icontains=query)
        allEduContent = Edu.objects.filter(content__icontains=query)
        allEdu = allEduTitle.union(allEduContent, allEdusAuthor)
    if allPosts.count() == 0:
        messages.warning(
            request, "No search results found. Please refine your query.")
    params = {'allPosts': allPosts, 'query': query}
    params = {'allEdu': allEdu, 'query': query}
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
            return redirect('index')

        if not username.isalnum():
            messages.error(
                request, " User name should only contain letters and numbers")
            return redirect('index')
        if (pass1 != pass2):
            messages.error(request, " Passwords do not match")
            return redirect('index')

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, " Your iCoder has been successfully created")
        return redirect('index')

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
            return redirect("index")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("index")

    return HttpResponse("404- Not found")

    return HttpResponse("login")

#################################################################################################


def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('index')

#################################################################################################
