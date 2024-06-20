from rest_framework import serializers
from .models import Topic, Task, UserDefinedUnits

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Topic
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Task
        fields = '__all__'

class UserDefinedUnitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDefinedUnits
        fields = '__all__'