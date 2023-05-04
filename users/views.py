from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User
from .serializers import UserSerializer, UserDetailSerializer
from .permissions import IsEmployee, IsEmployeeOrOwner
from rest_framework import generics


class UserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployee]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployee]
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_url_kwarg = "user_id"

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs.get("user_id"))


class UserDetailDeleteView(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeeOrOwner]
    queryset = User.objects.all()
    lookup_url_kwarg = "user_id"
