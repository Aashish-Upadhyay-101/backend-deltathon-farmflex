from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import ProfileSerializer, ProfileUpdateSerailizer
from .models import Profile
from apps.common.exceptions import ProfileNotFound, NotYourProfile

# Create your views here.
class GetMyProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        profile = request.user.profile
        serializer = ProfileSerializer(instance=profile)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetUpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username, format=None):
        try: 
            profile = Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            raise ProfileNotFound
        
        serializer = ProfileSerializer(instance=profile)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, username, format=None):
        try:
            Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            raise ProfileNotFound
    
        if request.user.username != username:
            raise NotYourProfile
        print('hello')

        serializer = ProfileUpdateSerailizer(instance=request.user.profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
