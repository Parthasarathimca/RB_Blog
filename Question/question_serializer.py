from rest_framework import serializers

from .models import Questions


class QuestionSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField()
    

    class Meta:
            model = Questions
            fields = '__all__'

