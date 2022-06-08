from functools import partial
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomUser, Profile
from .serializers import CustomUserSerializer, ProfileSerializer
from rest_framework import status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        token['id'] = user.id

        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CustomUserCreate(APIView):
    permission_classes = (permissions.AllowAny,) # why we are doing this?

    def get(self, request, format=None):
        user = CustomUser.objects.all()
        serializer = CustomUserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data) # recieving the data, but how? and in which format
        if serializer.is_valid():  # checking whether data the is valid or not, pm basis of is_valid() function defined in DRF sourcecode
            
            user = serializer.save()  # saving the data
            if user:
                json = serializer.data  # no idea what it's doing, need to ask
                print(json)
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # def partial_update(request, *args, **kwargs):
    #     serializer = CustomUserSerializer(data=request.data, partial=True) # recieving the data, but how? and in which format
    #     if serializer.is_valid():
    #         return Response(serializer.data, status=status.HTTP_202_ACCEPTED)




class ProfileViewSets(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def create(self, request):
        mydata = request.data
        serializer = ProfileSerializer(data=mydata)
        if serializer.is_valid():
            print(request)
            print(request.user)
            print(request.data)
            serializer.save(user= request.user)
            print(serializer.data)
            print(type(serializer.data))
            # newdata = serializer.data['image']
            # serializer.data['image']= f"http://http://
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    # def list(self, request):
    #     # username =  request.GET.get('username', 1)
    #     # #userid = CustomUser.objects.get(username=username).id
    #     # userid = get_object_or_404(CustomUser, username = username).id
    #     userid = get_object_or_404(CustomUser, id = request.GET.get('id', 1)).id
    #     print(userid)
    #     #profile = Profile.objects.get(user__username=username)
    #     # obj = get_object_or_404(Comment, id = request.GET.get('getid', 1) )
    #     # profile = Profile.objects.get(user_id = userid)
    #     profile = get_object_or_404(Profile, user_id = userid)
    #     serializer = ProfileSerializer(profile)
    #     return Response(serializer.data)

    # def partial_update(self, request, *args, **kwargs):
    #     super().partial_update(request, *args, **kwargs)
    #     mydata = request.data
    #     serializer = ProfileSerializer(data=mydata, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    #     print("_______________________________________")
    #     print(serializer.errors)
    #     print("_______________________________________")
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @action(detail=True, methods=['patch', 'put'])
    # def reset_profile(self, request, pk=None):
    #     userid = get_object_or_404(CustomUser, id = request.GET.get('id', 1)).id
    #     profile = get_object_or_404(Profile, user_id = userid)
    #     serializer = ProfileSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






        




# class ProfilePage(APIView):
#     def get(self, request, format=None):
#         data = Profile.objects.all()
#         serializer = ProfileSerializer(data, many=True)
#         return Response(serializer.data)

#     def post(self, request, format='json'):
#         serializer = ProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             profile = serializer.save()
#             if profile:
#                 json = serializer.data
#                 print(json)
#                 return Response(json, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def partial_update(request, *args, **kwargs):
#         serializer = ProfileSerializer(data=request.data, partial=True)
#         if serializer.is_valid():
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

#     def retrieve(request, *args, **kwargs):
#         super().retrieve(request, *args, **kwargs)
#         userid = get_object_or_404(CustomUser, id = request.GET.get('id', 1)).id
#         print(userid)
#         profile = get_object_or_404(Profile, user_id = userid)
#         serializer = ProfileSerializer(profile)
#         return Response(serializer.data)










