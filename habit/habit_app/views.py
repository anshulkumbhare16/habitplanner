import json

from django.shortcuts import render, HttpResponse

from .models import Topic, Task, UserDefinedUnits
from .models import all_records
from .serializers import TopicSerializer, TaskSerializer, UserDefinedUnitsSerializer

from manager.topic.topic_logic import calc_duration_days, insert_plan_data, add_new_task

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes, api_view
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from rest_framework_simplejwt.authentication import JWTAuthentication

from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


@permission_classes([IsAuthenticated])
class TopicApiViewSet(viewsets.ModelViewSet):
#   Authentication
    authentication_classes = [JWTAuthentication]
    permission_classes     = [IsAuthenticated]
    
    queryset         = all_records(Topic)
    serializer_class = TopicSerializer

#   Filters
    filter_backends  = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'user_id', 'topic_name',]
    search_fields    = ['^topic_name']
    ordering_fields  = ['id', 'topic_name']
    ordering         = ['id', 'topic_name']

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        data     = json.loads(request.body)
        cur_user = request.user

        # calculates the difference between start and end date in days
        duration_days = calc_duration_days(data['startdate'], data['enddate'])

        new_data = {
            "user_id"       : cur_user.id,
            "topic_name"    : data.get('topicname'),
            "start_date"    : data.get('startdate'),
            'end_date'      : data.get('enddate'),
            'duration_days' : duration_days,
        }

        serializer = TopicSerializer(data=new_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'success' : True, 'status' : 'New Topic created successfully'})
    
    def perform_update(self, serializer):
        return super().perform_update(serializer)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
 

@permission_classes([IsAuthenticated])
class TaskApiViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes     = [IsAuthenticated]
    
    queryset         = all_records(Task)
    serializer_class = TaskSerializer

    filter_backends  = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id', 'taskname', 'topic_id', 'user_id']
    search_fields    = ['^taskname']
    ordering_fields  = ['id', 'taskname', 'topic_id', 'user_id', 'created_at', 'modified_at']

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request):
        task   = json.loads(request.body)
        user   = request.user
        status = add_new_task(task, user)
        return Response(data={'success' : True, 'status' : status}, status=HTTP_201_CREATED)
    
    def perform_update(self, serializer):
        return super().perform_update(serializer)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    

@permission_classes([IsAuthenticated])
class UserDefinedUnitsAPIViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes     = [IsAuthenticated]

    queryset         = all_records(UserDefinedUnits)
    serializer_class = UserDefinedUnitsSerializer

    filter_backends  = [DjangoFilterBackend]
    filterset_fields = ['id', 'user_id', 'unit']

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_new_plan(request):
    plan    = json.loads(request.body)
    user    = request.user
    message = insert_plan_data(plan, user)    
    return Response({'success' : True, 'status' : message})