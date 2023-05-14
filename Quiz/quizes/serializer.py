from .models import QuizData
from rest_framework import serializers

class quizSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizData
        fields = ['question', 'options', 'rightAnswer', 'startDate','endDate']
        

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance