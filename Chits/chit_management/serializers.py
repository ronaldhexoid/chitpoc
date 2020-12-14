from rest_framework import serializers
from django.contrib import auth
from .models import KycPanCard, KycAadharCard,KycAddress, KycBank


class PanSerializer(serializers.ModelSerializer):


    class Meta:
        model = KycPanCard
        fields = ['front', 'back', 'timestamp']

    def validate(self, attrs):

        front = attrs.get('front', '')
        back = attrs.get('back', '')
        return attrs

class AadharSerializer(serializers.ModelSerializer):


    class Meta:
        model = KycAadharCard
        fields = ['front', 'back', 'timestamp']

    def validate(self, attrs):
        front = attrs.get('front', '')
        back = attrs.get('back', '')
        return attrs

class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = KycAddress
        fields = ['address', 'timestamp']

    def validate(self, attrs):

        file = attrs.get('address', '')
        return attrs


class BankSerializer(serializers.ModelSerializer):


    class Meta:
        model = KycBank
        fields = ['statement', 'timestamp']

    def validate(self, attrs):

        file = attrs.get('statement', '')

        return attrs
