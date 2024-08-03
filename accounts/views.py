from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework.views import APIView
from .serializers import UserSerializer
from django.views.generic import TemplateView
from .models import User
from .authentication import create_access_token,create_refresh_token, JwtAuthentication, decode_refresh_token





class HomePage(TemplateView):
    template_name = "home.html"


class RegisterApiView(APIView):
    def post(self, request):
        data = request.data

        if data['password'] != data ['password_confirm']:
            raise exceptions.APIException('passwords dont match!!!')
        
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_excption=True)
        serializer.save()
        return Response(serializer.data)
    


class LoginApiView(APIView):
    def post (self, request):
        email = request.dat ['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()
        if user is None:
            raise exceptions.AuthenticationFailed('invalid cerdantals')
        
        access_token = create_access_token(user.id)
        refresh_thoken = create_refresh_token(user.id)

        serializer = UserSerializer(user)
        return Response(serializer.data)
    

class UserApiView(APIView):
    authentication_classes = [JwtAuthentication]

    def get(self, request):
        return Response(UserSerializer(request.user).data)
    

class RefreshApiView(APIView):
    def post(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        id = decode_refresh_token(refresh_token)
        access_token = create_access_token(id)
        return Response(
                    {
                      'token': access_token

                    }
                        )
    
class LogoutApiView(APIView):
    def post(self,request):
        response = Response()
        response.delete_cookie(key='refresh_token')
        response.data = {
            'message' : 'success'
        }
        return response