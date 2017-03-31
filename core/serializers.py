from rest_framework import serializers
from .models import Mailer

class MailerSerializer(serializers.ModelSerializer):

	class Meta:
		fields = ['id','subject','to_address','from_address','message']
		model = Mailer