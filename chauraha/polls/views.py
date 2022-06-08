from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Poll, Choice, Vote
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer
from rest_framework import generics
from rest_framework.decorators import api_view

# Create your views here.


class PollViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Poll.objects.all()
        serializer = PollSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Poll.objects.all()
        poll = get_object_or_404(queryset, pk=pk)
        serializer = PollSerializer(poll)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        post = get_object_or_404(Poll, pk=pk)
        if post.author != request.user:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request, pk=None, ):
        mydata = request.data
        #print(request.body)
        print(type(mydata))
        print(mydata)
        # 'id', 'owner', 'text', 'pub_date', 'active', 'choices', 'votes'
        #id = mydata.get('id')
        text = mydata.get('text')
        pollre = {'text': text}
        pollserializer = PollSerializer(data=pollre)
        #print(pollserializer)
        if pollserializer.is_valid():
            pollserializer.save(owner= request.user)
            print(mydata)
            print(type(mydata))
            # abc = mydata.lists()
            # # print(type(abc))
            # print(mydata['choice_text'])
            # print(type(mydata['choice_text']))
            # print('___________Value of List___________')
            # print(mydata.getlist('choice_text'))
            # print(type(mydata.getlist('choice_text')))
            # print('___________End Value of List___________')

            #choice_text = mydata['choice_text']
            choice_list = mydata['choice_text'] # convert to list
            print(choice_list)
            for i in choice_list:
                choice_re = {'choice_text': i}
                choiceserializer = ChoiceSerializer(data=choice_re)
                if choiceserializer.is_valid():
                    choiceserializer.save(poll=pollserializer.instance)
                    print('----------------- Validation Done-----------------')
                else:
                    print('----------------- Choice  Validation Error-----------------')
                    print(choiceserializer.errors, i)
                    return Response(choiceserializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response(choiceserializer.data, status=status.HTTP_201_CREATED)
        print('----------------- Poll  Validation Error-----------------')
        return Response(pollserializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ChoiceListView(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class ChoiceView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()


@api_view(['GET', 'POST'])
def ChoiceVote(request):
    if request.method == 'POST':
        voteserializer = VoteSerializer(data=request.data)
        if voteserializer.is_valid():
            voteserializer.save(user = request.user)
            return Response(voteserializer.data, status=status.HTTP_201_CREATED)
        return Response(voteserializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        queryset = Vote.objects.all()
        serializer = VoteSerializer(queryset, many=True)
        return Response(serializer.data)


# def hello_world(request):
#     if request.method == 'POST':
#         return Response({"message": "Got some data!", "data": request.data})
#     return Response({"message": "Hello, world!"})


        
        
        

