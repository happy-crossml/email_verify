from rest_framework import serializers
from verify.models import User

        
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User       
        fields = ['email', 'password', 'is_verified']
    
    
class VerifySerializer(serializers.ModelSerializer):        
        
    email = serializers.EmailField()
    otp = serializers.CharField()    
    
    class Meta:
        model = User
        fields =  ['email', 'otp']
    