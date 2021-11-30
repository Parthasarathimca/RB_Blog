from django.shortcuts import render
from Question.question_serializer import QuestionSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from Question.models import Questions
from accounts.models import User


class QuestionsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if request.user.roles in User.ROLES[1]: 
            questions = Questions.objects.filter(created_by=request.user.id)
        elif request.user.roles in User.ROLES[0]:
            questions = Questions.objects.filter(mentor=request.user.id)

        serializer = QuestionSerializer(questions, many=True)
        return Response({"questions": serializer.data})
    
    def post(self, request):
        questions = request.data
        # Create an question from the above data
        serializer = QuestionSerializer(data=questions)
        if serializer.is_valid(raise_exception=True):
            questions_saved = serializer.save()
        return Response({"success": "Question '{}' created successfully".format(questions_saved.question)})


