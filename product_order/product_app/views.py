from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import permissions

from product_app import serializer

from .serializer import LoginSerializer
from .permissions import IsOwnerOrReadOnly
from .models import Order, Product


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializer.UserSerializer


class UserWithId(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializer.UserSerializer


class UserDetail(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializer.UserSerializer


class Login(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        username = request.data['username']
        usr_pswd = request.data['password']
        if username is None:
            return Response("Username is required")
        if usr_pswd is None:
            return Response("Password is required")
        user = authenticate(username=username, password=usr_pswd)
        if user:
            if user.is_active:
                login(request, user)
                return Response("User logged in successfully", status=status.HTTP_200_OK)
            else:
                return Response("User not active", status=status.HTTP_400_BAD_REQUEST)
        return Response('User not exist', status=status.HTTP_404_NOT_FOUND)


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = serializer.OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class OrderDetail(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = serializer.OrderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializer.ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ProductDetail(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = serializer.ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = serializer.ProductSerializer
    permission_classes = [IsOwnerOrReadOnly]