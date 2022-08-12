from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from users.models import User
from explore.models import News, Category, Locality, City, Tag

from .serializers import NewsSerializer
from utils.helperfunction import get_context


class NewsList(APIView):
    
    def get(self, request, pk=None):
        if pk is not None:
            news = News.objects.filter(id=pk,is_activate =True)
            serializer = NewsSerializer(news , many=True)
            
            return get_context(
                status= status.HTTP_200_OK,
                success= True,
                message= "you get perticular news",
                data = serializer.data
            )
            
        filter_query = {}
        
        if request.GET.get('author'):
            user = User.objects.filter(id=request.GET.get('author')).first()
            if user.is_author and user.is_activate:
                filter_query['author'] = request.GET.get('author')
            else:
                return Response({"error": True, "Message": 'Author is not found'}, status=status.HTTP_404_NOT_FOUND)

        if request.GET.get('headline'):
            filter_query['headline__icontains'] = request.GET.get('headline')
            
        if request.GET.get('subheadline'):
            filter_query['subheadline__icontains'] = request.GET.get('subheadline')
            
        if request.GET.get('mianbody'):
            filter_query['mianbody__icontains'] = request.GET.get('mianbody')
            
        if request.GET.get('category'):
            filter_query['category__icontains'] = request.GET.get('category')
            
        if request.GET.get('locality'):
            filter_query['locality__icontains'] = request.GET.get('locality')
            
        if request.GET.get('city'):
            filter_query['city__icontains'] = request.GET.get('city')
            
            
            
#https://stackoverflow.com/questions/9304908/how-can-i-filter-a-django-query-with-a-list-of-values


        # if request.GET.get('tag'):
        #     all_tag = Tag.objects.filter(id__in=[5, 6])
        #     print(all_tag)
        #     filter_query['tag__in'] = request.GET.get('tag')
            
        news = News.objects.filter(**filter_query,is_activate =True)
        serializer = NewsSerializer(news , many=True)
        return get_context(
            status= status.HTTP_200_OK,
            success= True,
            message= "you get all of your NEWS",
            data = serializer.data
        )

    def post(self , request):
        serializer = NewsSerializer(data = request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return get_context(
                    status= status.HTTP_201_CREATED,
                    success= True,
                    message= "You Created NEWS Successfully",
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
        news = News.objects.get(id=pk,is_activate =True)
        serializer = NewsSerializer(news, data =request.data)
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
        news = News.objects.get(id=pk,is_activate =True)
        news.is_activate = False
        news.save()
        data = f"your news {news.headline[:10]} was deleted"
        return get_context(
            status= status.HTTP_204_NO_CONTENT,
            success= True,
            message= "your News is delete",
            data =  data
        )



