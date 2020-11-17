from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action

from users.serializers import UserSerializer
from users import models
from users.permissions import IsLoggedInUserOrAdmin, IsAdminUser

class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """ 

    def get_queryset(self):
        return []
    

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [AllowAny]
            # permission_classes = [IsLoggedInUserOrAdmin]
        elif self.action == 'list' or self.action == 'destroy':
            # permission_classes = [IsAdminUser]
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    @action(methods=['GET'], detail=False, url_path='list-users', url_name='list-users')
    def list_customers(self, request):
        queryset = models.User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=False, url_path='list-user-by-email', url_name='list-user-by-email')
    def get_users_by_email(self, request):
        request_email = request.query_params.get('email')
        if request_email is None or not request_email:
            return Response({'detail':"Enter a valid email"}, status=status.HTTP_400_BAD_REQUEST)

        user_detail = models.User.objects.filter(email=request_email)
        print(user_detail)
        if user_detail.count() >=1:
            selected_user = user_detail.first()
            user_info = UserSerializer(selected_user, many=False)
            return Response(user_info.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail":"User does not exist"}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'], detail=False, url_path='list-user-by-id', url_name='list-user-by-id')
    def get_user_info_by_id(self, request):
        user_id = request.query_params.get('userid')
        print('the user id ===== ',user_id)
        if user_id is None or not user_id:
            return Response({"detail":'User not found'}, status=status.HTTP_400_BAD_REQUEST)

        user_detail = models.User.objects.filter(id=user_id)
        print(user_detail)
        if user_detail:
            selected_user = user_detail.first()
            user_info = UserSerializer(selected_user, many=False)
            return Response(user_info.data, status=status.HTTP_200_OK)
        return Response({'detail':'User not found'}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['POST'], detail=False, url_path='create-user', url_name='create-user')
    def create_user(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk=None):
        queryset = models.User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        queryset = models.User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        user.delete()
        cust_response = {
            'detail':'User deleted'
        }
        return Response(cust_response, status=status.HTTP_404_NOT_FOUND)

