from rest_framework import serializers

from src.tasks import models

ENGINES = (
    ('google', 'google'),
    ('yandex', 'yandex'),
    ('bing', 'bing'),
    ('baidu', 'baidu'),
    ('yahoo', 'yahoo')
)

LOCATIONS = (
    ('21176', 'Texas'),
    ('21133', 'Arkansas'),
    ('21135', 'Alabama')
)


class TaskCreateSerializer(serializers.Serializer):
    """ Serializer for create task """
    engine = serializers.ChoiceField(choices=ENGINES)
    location = serializers.ChoiceField(choices=LOCATIONS)
    keyword = serializers.CharField()


class TaskSerializer(serializers.ModelSerializer):
    """ Task serializer """
    class Meta:
        model = models.Task
        fields = '__all__'


class TaskDataSerializer(serializers.ModelSerializer):
    """ Task data serializer """
    class Meta:
        model = models.TaskData
        fields = '__all__'


class TaskResultSerializer(serializers.ModelSerializer):
    """ Task result serializer """
    class Meta:
        model = models.TaskResult
        fields = '__all__'
