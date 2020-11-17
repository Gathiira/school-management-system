from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import CertificateModel
from .serializers import CertificateSerializer

class CertificateView(viewsets.ViewSet):
    def list(self, request):
        queryset = CertificateModel.objects.all()
        serializer = CertificateSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CertificateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = CertificateModel.objects.all()
        certificate = get_object_or_404(queryset, pk=pk)
        certificate.delete()
        cust_response = {
            'detail':'Item was deleted'
        }
        return Response(cust_response,status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, pk=None):
        queryset = CertificateModel.objects.all()
        certificate = get_object_or_404(queryset, pk=pk)
        serializer = CertificateSerializer(certificate)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = CertificateModel.objects.all()
        certificate = get_object_or_404(queryset, pk=pk)
        serializer = CertificateSerializer(certificate, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)