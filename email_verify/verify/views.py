from verify.models import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, VerifySerializer
from django.views.decorators.csrf import csrf_exempt

from django.core.mail import send_mail
import random
from django.conf import settings

class RegisterAPI(APIView):
    
    @csrf_exempt
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_otp_via_mail(serializer.data['email'])
            return Response({
                'status' : '200',
                'message': 'User registration successfull, Please check your email',
                'data' : serializer.data
                })
        else:
            return Response({
                'status' : '200',
                'message': 'somthing went wrong',
                'data' : serializer.errors
                })

class VerifyOTP(APIView):
    
    @csrf_exempt
    def post(self, request):
        serializer = VerifySerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data['email']
            otp = serializer.data['otp']
            user = User.objects.filter(email=email)
          
            if not user.exists():
                return Response({
                'status' : '200',
                'message': 'something went wrong please try again.',
                'data' : 'Invalid email'
                }) 
                
            if user[0].otp != otp:
                    return Response({
                    'status' : '200',
                    'message': 'something went wrong please try again.',
                    'data' : 'Wrong OTP'
                    })
            
            user = user.first()        
            user.is_verified = True
            user.save()
            return Response({
                'status' : '200',
                'message': 'Account Verified.',
                'data' : {}
                })
           
        return Response({
        'status' : '200',
        'message': 'something went wrong please try again.',
        'data' : serializer.errors
        })     
        
        
# For genrate OTP           
def send_otp_via_mail(email):
        subject = "Your account verification email"
        otp = random.randint(1000, 9999)
        message = f'Your otp is {otp}'
        email_from = settings.EMAIL_HOST
        send_mail(subject, message, email_from, [email])
        user_obj = User.objects.get(email=email)
        user_obj.otp = otp
        user_obj.save()        