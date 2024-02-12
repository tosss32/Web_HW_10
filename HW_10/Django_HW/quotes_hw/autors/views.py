from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Author
from .serializer import AuthorSerializer

from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from .serializer import UserRegistrationSerializer

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_authors(request):
    queryset = Author.objects.all()

    serializer = AuthorSerializer(queryset, many=True)


    return Response(serializer.data)



class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]