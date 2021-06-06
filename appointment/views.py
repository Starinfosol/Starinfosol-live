from django.shortcuts import render, HttpResponse, redirect
from appointment.models import Appointment
# from appointment.models import Appointment, OrderUpdate, Orders
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User
# from math import ceil
# import json
# from django.views.decorators.csrf import csrf_exempt
# from PayTm import Checksum

# MERCHANT_KEY = 'KIhJQs90429731106892'

# def checkout(request):
#     if request.method=="POST":
#         items_json = request.POST.get('itemsJson', '')
#         name = request.POST.get('name', '')
#         amount = request.POST.get('amount', '')
#         email = request.POST.get('email', '')
#         address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
#         city = request.POST.get('city', '')
#         state = request.POST.get('state', '')
#         zip_code = request.POST.get('zip_code', '')
#         phone = request.POST.get('phone', '')
#         order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
#                        state=state, zip_code=zip_code, phone=phone, amount=amount)
#         order.save()
#         update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
#         update.save()
#         thank = True
#         id = order.order_id
#         # return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})
#         # Request paytm to transfer the amount to your account after payment by user
#         param_dict = {

#                 'MID': MERCHANT_KEY,
#                 'ORDER_ID': str(order.order_id),
#                 'TXN_AMOUNT': str(amount),
#                 'CUST_ID': email,
#                 'INDUSTRY_TYPE_ID': 'Retail',
#                 'WEBSITE': 'WEBSTAGING',
#                 'CHANNEL_ID': 'WEB',
#                 'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/',

#         }
#         param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
#         return render(request, 'shop/paytm.html', {'param_dict': param_dict})

#     return render(request, 'shop/checkout.html')

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
        # amount = request.POST.get('amount', '')
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