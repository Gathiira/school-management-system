from rest_framework import serializers
from django.contrib.auth import authenticate

from users.models import User, UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('first_name','last_name','preffered_name'
                ,'discord_name','github_username','phone'
                ,'linkedin_profile_url','current_level','gender')

        extra_kwargs = {
            'first_name':{'required':True}
        }

        lookup_field = "pk"

class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(required=True)
    class Meta:
        model = User
        fields = ['id','email','password','profile']
        extra_kwargs = {
            'password':{
                'write_only':True, 'min_length':8
            }
        }

    def create(self, validated_data):
        print(validated_data)
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        user.is_student = True
        user.save()
        print(user)
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.first_name = profile_data.get('first_name', profile.first_name)
        profile.last_name = profile_data.get('last_name', profile.last_name)
        profile.preffered_name = profile_data.get('preffered_name', profile.preffered_name)
        profile.discord_name = profile_data.get('discord_name', profile.discord_name)
        profile.github_username = profile_data.get('github_username', profile.github_username)
        profile.phone = profile_data.get('phone', profile.phone)
        profile.linkedin_profile_url = profile_data.get('linkedin_profile_url', profile.linkedin_profile_url)
        profile.current_level = profile_data.get('current_level', profile.current_level)
        profile.gender = profile_data.get('gender', profile.gender)
        profile.save()

        return instance

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError({'details':'Invalid email or password'})

