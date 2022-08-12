from rest_framework import serializers

from explore.models import News


class NewsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = News
        fields = ['id','headline','subheadline','image','mianbody','tag','author','category','locality','city','is_activate']
