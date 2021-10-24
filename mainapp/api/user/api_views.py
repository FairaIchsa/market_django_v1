from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *


class UserAPIView(APIView):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            user = self.request.user
            serializer = UserSerializer(user)
            return Response(serializer.data)
        return Response('User is not authenticated')

