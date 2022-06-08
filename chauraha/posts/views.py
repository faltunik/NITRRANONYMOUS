from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Post, Comment
from rest_framework.views import APIView
from .serializers import PostSerializer, CommentSerializer
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

class PostView(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by('-id')
    #ordering = [-'id']
    permission_classes = [IsAuthenticated]

    def create(self, request):
        mydata = request.data
        serializer = PostSerializer(data=mydata)
        if serializer.is_valid():
            print(request)
            print(request.user)
            print(request.data)
            serializer.save(author= request.user)
            print(serializer.data)
            print(type(serializer.data))
            # newdata = serializer.data['image']
            # serializer.data['image']= f"http://http://127.0.0.1:8000{newdata}"
            # print(serializer.data.get['image'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None, *args, **kwargs):
        super().update(request, *args, **kwargs)
        serializer = PostSerializer(data=request.data)
        postauth = Post.objects.get(pk=pk).author
        if serializer.is_valid() and request.user == postauth:
            print(request)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None, *args, **kwargs):
        super().partial_update(request, *args, **kwargs)
        serializer = PostSerializer(data=request.data, partial=True)
        postauth = Post.objects.get(pk=pk).author
        if serializer.is_valid() and request.user == postauth:
            print(request)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        if post.author != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        

class CommentView(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def create(self, request):
        mydata = request.data
        print(request)
        print(mydata)
        # print(request.user)
        # self.printLine()
        serializer = CommentSerializer(data=mydata)
        if serializer.is_valid():
            print(request)
            print(request.user)
            print(request.data)
            serializer.save(author= request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        print(request)
        post = Post.objects.get(id = request.GET.get('id', 1))
        #queryset = post.comments.all().order_by('-id')
        queryset = Comment.objects.filter(post=post, parent=None)
        serializer = CommentSerializer(queryset, many= True)        
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        comment = get_object_or_404(Comment, pk=pk)
        if comment.author != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, pk=None, *args, **kwargs):
        super().update(request, *args, **kwargs)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            print(request)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None, *args, **kwargs):
        super().partial_update(request, *args, **kwargs)
        serializer = CommentSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            print(request)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReplyView(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def list(self, request):
        print(request)
        comment = Comment.objects.get(id = request.GET.get('id', 1))
        #post = Post.objects.get(id = request.GET.get('id', 1))
        #queryset = post.comments.all().order_by('-id')
        queryset = Comment.objects.filter(parent=comment)
        serializer = CommentSerializer(queryset, many= True)
        return Response(serializer.data)



@api_view(['GET', 'POST'])
def commentreply(request):
    # slug = self.kwargs.get("slug")
    print(request)
    obj = get_object_or_404(Comment, id = request.GET.get('getid', 1) )
    returnobj = obj.children()
    serializer = CommentSerializer(returnobj, many= True)
    return Response(serializer.data)

# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def hello_world(request):
#     if request.method == 'POST':
#         return Response({"message": "Got some data!", "data": request.data})
#     return Response({"message": "Hello, world!"})

# @api_view(['GET', 'POST'])
# def likepost(request):
#     # slug = self.kwargs.get("slug")
#     print(request)
#     obj = get_object_or_404(Post, id = request.GET.get('getid', 1) )
#     user = request.user
#     updated = False
#     liked = False
#     if user in obj.like.all():
#         liked = False
#         obj.like.remove(user)
#         print('User is removed')
#     else:
#         liked = True
#         obj.like.add(user)
#         print('User is added')
#     updated = True
#     data = {
#         "updated": updated,
#         "liked": liked,            
#     }
#     # serializer = SublySerializer(obj, many= True)
#     return Response(data, status=status.HTTP_202_ACCEPTED)


class PostLikeAPI(APIView):
    def get(self, request):
        # slug = self.kwargs.get("slug")
        print(request)
        print(request.data)
        obj = get_object_or_404(Post, id = request.GET.get('getid', 1) )
        user = self.request.user
        updated = False
        liked = False
        if user.is_authenticated:
            if user in obj.like.all():
                liked = False
                obj.like.remove(user)
                print('Liked')
            else:
                liked = True
                obj.like.add(user)
            updated = True
        data = {
            "updated": updated,
            "liked": liked,            
        }
        return Response(data, status=status.HTTP_202_ACCEPTED )
