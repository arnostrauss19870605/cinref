from rest_framework import serializers
from . import models
from django.contrib.auth.models import User, Group


class userSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class ReferralSerializer(serializers.ModelSerializer):
    # Serializer for the Referral model, in fields we specify the model attributes we want to
    # deserialize and serialize
    class Meta:
        model = models.Referral
        fields = ['id', 'FirstName', 'Surname', 'PolicyNumber', 'Email', 'BrokerName', 'BrokerEmail', 'PolicyPhone']


class ReferredSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Referred
        fields = ['id', 'FirstName', 'Surname', 'Email', 'RefferedPhone', 'Status']


