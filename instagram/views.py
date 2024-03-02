from rest_framework import generics
from rest_framework.decorators import api_view, action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
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
    # authentication_classes = []
    permission_classes = [IsAuthenticated] # 인증된 요청 한해서 뷰 호출 허용
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['message']
    ordering_fields = ['id']    # 정렬을 허용할 필드의 화이트 리스트 ( 미지정 시 serializer_class에 지정된 필드들 )
    ordering = ['id']           # 디폴트 정렬 지정

    def perform_create(self, serializer):
        # FIXME: 인증이 되어있다는 가정하에
        author = self.request.user #
        ip = self.request.META['REMOTE_ADDR']
        serializer.save(author=author, ip=ip)

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

class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    '''TemplateHTMLRenderer : 지정 템플릿을 통한 렌더링
    JSON 방식이 아닌 HTML 방식으로 받아야할 때?
    '''
    renderer_classes = [TemplateHTMLRenderer]

    template_name = 'instagram/post_detail.html'

    def get(self, request, *args, **kwargs):
        post = self.get_object()

        return Response({
            'post': PostSerializer(post).data,
        })