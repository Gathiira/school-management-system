from rest_framework import serializers

from .models import CertificateModel


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificateModel
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        return CertificateModel.objects.create(**validated_data)