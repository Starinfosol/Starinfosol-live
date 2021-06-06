from django.shortcuts import render, HttpResponse, redirect
from Education.models import Education
from django.contrib.auth.models import User


# Create your views here.




def Educationhome(request):
    allEducation = Education.objects.all()
    context = {'allEducation': allEducation}
    return render(request, 'Education.html', context)



def Educationpost(request, slug): 
    post=Education.objects.filter(slug=slug).first()
    # comments= BlogComment.objects.filter(Edu=Edu, parent=None)
    # replies= BlogComment.objects.filter(Edu=Edu).exclude(parent=None)
    # replyDict={}
    # for reply in replies:
    #     if reply.parent.sno not in replyDict.keys():
    #         replyDict[reply.parent.sno]=[reply]
    #     else:
    #         replyDict[reply.parent.sno].append(reply)

    context={'Education':post}
    return render(request, "Educationpost.html", context)
    
