from rest_framework import generics
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post

'''제네릭 방식
GET, POST, PUT, DELETE 한번에 다 가능
'''
# class PublicPostListApiView(generics.ListAPIView):
#     queryset = Post.objects.filter(is_public=True)
#     serializer_class = PostSerializer

'''APIView 클래스 방식
메소드별 상세하게 컨트롤 가능?
'''
# class PublicPostListAPIView(APIView):
#     def get(self, request):
#         qs = Post.objects.filter(is_public=True)
#         serializer = PostSerializer(qs, many=True)
#         return Response(serializer.data)
#
# public_post_list = PublicPostListAPIView.as_view()

''' APIView 함수방식
간단하게 한개의 뷰만 만들때 사용하면 좋을듯 하다
'''
# @api_view(['GET'])
# def public_post_list(request):
#     qs = Post.objects.filter(is_public=True)
#     serializer = PostSerializer(qs, many=True)
#     return Response(serializer.data)


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    '''/post/ 뒤에 url이 추가로 붙어 메소드별로 컨트롤할 수 있음
    rest_framework.routers.DefaultRouter 에서 지원하는 기능
    ex) localhost:8000/post/{함수명}
    '''
    @action(detail=False, methods=['GET'])
    def public(self, request):
        qs = self.get_queryset().filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)

        return Response(serializer.data)

    @action(detail=True, methods=['PATCH'])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save(update_fields=['is_public'])
        serializer = self.get_serializer(instance)

        return Response(serializer.data)
