from rest_framework import generics
from .serializers import RegitrationSerializer , CustomAuthTokenSerializer , ChangePasswordSerializer , ProfileSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken , APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from accounts.models import Profile
from django.shortcuts import get_object_or_404
from .utils import EmailThread

from django.core.mail import send_mail

from mail_templated import send_mail , EmailMessage




user = get_user_model()


class RegitrationApiView(generics.GenericAPIView) :
    serializer_class = RegitrationSerializer

    def post(self,request,*args,**kwargs) :
        serializer = RegitrationSerializer(data = request.data)
        if serializer.is_valid() :
            serializer.save()
            data = {
                'email':serializer.validated_data['email']
            }
            return Response(data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class CustomObtainAuthToken(ObtainAuthToken) :
    serializer_class = CustomAuthTokenSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token , created = Token.objects.get_or_create(user=user)
        return Response({
            'token':token.key,
            'user_id':user.pk,
            'email':user.email
        })
    
class CustomDiscardAuthToken(APIView) :
    permission_classes = [IsAuthenticated]
    def post(self,request) :
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class ChangePasswordApiView(generics.UpdateAPIView) :
    model = user
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj
    
    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response({'detail':'password changed successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class ProfileApiView(generics.RetrieveUpdateAPIView) :
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset,user=self.request.user)
        return obj
    

class TestEmail(generics.GenericAPIView) :
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    def get(self,request,*atgs,**kwargs) :
        # send_mail(
        #     "Subject here",
        #     "Here is the message.",
        #     "from@example.com",
        #     ["to@example.com"],
        #     fail_silently=False,
        #     )
        # return Response ('email tests')
        
        
        # send_mail('email/hello.tpl', {'name': 'ali'}, 'mehrab88.kh.2425@gmail.com', ['programmer.py.mail@gmail.com'])

        email_object = EmailMessage('email/hello.tpl', {'name': 'ali'}, 'mehrab88.kh.2425@gmail.com', to=['programmer.py.mail@gmail.com'])
        EmailThread(email_object).start()
        return Response('email test')