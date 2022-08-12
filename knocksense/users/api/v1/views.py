from rest_framework.views import APIView
from rest_framework import status

from users.models import User

from .serializers import UserSerializer
from utils.helperfunction import get_context

        
class UserList(APIView):
    
    def get(self, request, pk=None):
        if pk is not None:
            user = User.objects.filter(id=pk, is_activate =True)
            serializer = UserSerializer(user, many=True)
            return get_context(
                status= status.HTTP_200_OK,
                success= True,
                message= "you get perticular author",
                data = serializer.data
            )
        user = User.objects.filter(is_activate =True)
        serializer = UserSerializer(user, many=True)
        return get_context(
            status= status.HTTP_200_OK,
            success= True,
            message= "you get all of your all user with deatils",
            data = serializer.data
        )

    
    def post(self , request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return get_context(
                    status= status.HTTP_201_CREATED,
                    success= True,
                    message= "You Created Account Successfully",
                    data =  serializer.data
                )
            except Exception as e:
                return get_context(
                    status= status.HTTP_400_BAD_REQUEST,
                    success= True,
                    message= "Error", 
                    data =  serializer.errors
                )
        else:
            return get_context(
                status= status.HTTP_404_NOT_FOUND,
                success= False,
                message=f"OOPS Something went wrong !! correct srializer",
                data =  serializer.errors
            )
                        
    def put(self, request, pk):
        user = User.objects.get(id=pk,is_activate =True)
        serializer = UserSerializer(user, data =request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return get_context(
                    status= status.HTTP_202_ACCEPTED,
                    success= True,
                    message= "your data is update",
                    data = serializer.data
                )
            except:
                return get_context(
                    status= status.HTTP_400_BAD_REQUEST,
                    success= False,
                    message= "OOPS something went wrong",
                    data = "OOPS something went wrong"
                )
        else:
            return get_context(
                    status= status.HTTP_404_NOT_FOUND,
                    success= False,
                    message= "OOPS Something went wrong !! correct srializer",
                    data = serializer.errors
                )
            
 
    def delete(self , request, pk):
        user = User.objects.get(id=pk,is_activate =True)
        user.is_activate = False
        user.save()
        data = f"your user {user.firstname} was deleted"
        return get_context(
            status= status.HTTP_204_NO_CONTENT,
            success= True,
            message= "your user is delete",
            data =  data
        )

class AutherList(APIView):
    
    def get(self, request, pk=None):
        if pk is not None:
            author = User.objects.filter(id=pk, is_activate =True, is_author=True)
            serializer = UserSerializer(author, many=True)
            return get_context(
                status= status.HTTP_200_OK,
                success= True,
                message= "you get perticular author",
                data = serializer.data
            )
        author = User.objects.filter(is_activate =True, is_author=True)
        serializer = UserSerializer(author, many=True)
        return get_context(
            status= status.HTTP_200_OK,
            success= True,
            message= "you get all of your all author deatils",
            data = serializer.data
        )
