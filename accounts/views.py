from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.models import User
from accounts.user_serializer import *


class UsersView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response({"users": serializer.data})

    
    def post(self, request):
        user = request.data
        # Create an question from the above data
        serializer = UserSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"success": "User saved Successfully    "})


