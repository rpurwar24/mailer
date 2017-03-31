from django.shortcuts import render,get_object_or_404
from django.http import Http404, HttpResponseRedirect,HttpResponse
from .models import *

from rest_framework.response import Response

from rest_framework import serializers
from .serializers import *

from rest_framework import viewsets
from .tasks import email_send,success_callback,error_callback

class MailerViewSet(viewsets.GenericViewSet):
    def create(self,request):
        # from_address = request.POST.get('from_address', "")
        to_address = request.POST.get('to_address', "")
        subject = request.POST.get('subject', "")
        message = request.POST.get('message', "")
        mail = Mailer(to_address=to_address,subject=subject,message=message)
        mail.save()
        email_send.apply_async((to_address,message,subject),link=success_callback.s(mail.id),link_error=error_callback.s())
        response_data = {'id' : mail.id,'subject':subject}
        return Response(response_data,201)