from rest_framework import serializers

from .models import Lecture


class LectureSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Lecture
        fields = ['id','user','title'
            ,'lecturer_name','duration'
            ,'description','date','slides_url']

    def create(self, validated_data):
        print(validated_data)
        return {'detail':'created'}