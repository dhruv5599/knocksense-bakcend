from rest_framework import serializers

from explore.models import News, Tag


class NewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = News
        fields = ['id','headline','subheadline','image','mianbody','tag','author','category','locality','city','is_activate']

class Tagerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = ['id','tag']