from django.shortcuts import render
from rest_framework.views import APIView
from .models import Room
from .serializers import RoomSerializer
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from oauth2_provider.contrib.rest_framework import OAuth2Authentication, IsAuthenticatedOrTokenHasScope
from django.shortcuts import render

class RoomListView(APIView):
    authentication_classes = [SessionAuthentication, OAuth2Authentication]
    permission_classes = [IsAuthenticatedOrTokenHasScope]
    required_scopes = ['read']

    def get(self, request):
        rooms = Room.objects.all()
        data = RoomSerializer(rooms, many=True).data
        return Response(data)

def login_view(request):
    return render(request, 'login.html')
