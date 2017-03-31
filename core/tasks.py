from django.conf import settings
from django.core.mail import send_mail
from celery import shared_task,task
from celery.result import AsyncResult
from .models import *

@shared_task
def email_send(to_address,message,subject):
    print "inside email"
    send_mail(subject, message, settings.EMAIL_HOST_USER,
    [to_address], fail_silently=False)

@shared_task
def success_callback(result,mail_id):
    print "inside success callback %s" % (mail_id)
    cur_mail = Mailer.objects.get(id=mail_id)
    cur_mail.status='success'
    cur_mail.save()


@shared_task
def error_callback(uuid):
    print "error callback"
    result = AsyncResult(uuid)
    exc = result.get(propagate=False)
    print('Task {0} raised exception: {1!r}\n{2!r}'.format(
          uuid, exc, result.traceback))
