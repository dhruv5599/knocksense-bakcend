from rest_framework import serializers

from users.models import User
       
        
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id','firstname','lastname','username','phone_number','address','professional_email','dob','gender','email','is_author']