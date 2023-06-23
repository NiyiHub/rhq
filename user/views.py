from django.contrib.auth import get_user_model
User = get_user_model
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status


class RegisterView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):

        try:
            data = request.data

            name = data['name']
            email = data['email']
            username = data['username']
            phone = data['phone']
            password = data['password']
            re_password = data['re_password']

            if password == re_password:
                if len(password) >= 8:
                    if not User.objects.filter(email=email).exists():
                        User.objects.create_user(name=name, email=email, username=username, phone=phone, password=password)
                        
                        return Response(
                                    {'success': 'User created successfully'},
                                    status=status.HTTP_201_CREATED
                                )
                    
                    else:
                        return Response(
                                {'error': 'User with this email already exists'},
                                status=status.HTTP_400_BAD_REQUEST
                            )

                else:
                    return Response(
                            {'error': 'Password must be at least 8 characters in length'},
                            status=status.HTTP_400_BAD_REQUEST
                        )
            else:
                return Response(
                        {'error': 'Password do not match'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            
        except:
            return Response(
                    {'error': 'Something went wrong when retrieving user datails.'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        

class RetrieveUserView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user
            user = UserSerializer(user)

            return Response(
                {'user': user.data},
                status=status.HTTP_200_OK
            )
        
        except:
            return Response(
                    {'error': 'Something went wrong when retrieving user details.'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )