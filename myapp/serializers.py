from rest_framework import routers, serializers
from myapp.models import *



class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", 'user', 'region', 'district', "img", 'text_uz', 'text_ru', 'number', 'vaqt', 'price', 'maydon_soni')


class DistrictSerializer(serializers.ModelSerializer):
    data = PostSerializers(many=True)
    class Meta:
        model = District
        fields = ('id', "region" ,'name_uz', 'name_ru', 'data')



class RegionSerializer(serializers.ModelSerializer):
    data = DistrictSerializer(many=True)
    class Meta:
        model = Region
        fields = ("id",'name_uz', 'name_ru', 'data')



