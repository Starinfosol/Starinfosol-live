from django.shortcuts import render, HttpResponse, redirect
from appointment.models import Appointment
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User
# from math import ceil
# import json
# from django.views.decorators.csrf import csrf_exempt
# from PayTm import Checksum

# MERCHANT_KEY = 'Your-Merchant-Key-Here'

# @csrf_exempt
# def handlerequest(request):
#     # paytm will send you post request here
#     form = request.POST
#     response_dict = {}
#     for i in form.keys():
#         response_dict[i] = form[i]
#         if i == 'CHECKSUMHASH':
#             checksum = form[i]

#     verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
#     if verify:
#         if response_dict['RESPCODE'] == '01':
#             print('order successful')
#         else:
#             print('order was not successful because' + response_dict['RESPMSG'])
#     return render(request, 'shop/paymentstatus.html', {'response': response_dict})


def Appointmentadd(request):
    # return HttpResponse("this is Appointment page")

    if request.method == "POST":
        # Get the post parameters
        amount = request.POST.get('amount', '')
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
            inc = Appointment(amount=amount, name=name, email=email, phone=phone, date=date, department=department, doctor=doctor, information=information)
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