# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import *
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import APIException
#from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import *
from .serializers import *
from itertools import chain

# Create your views here.

class RecipeDetails(APIView):
    #permission_classes = (IsAuthenticatedOrReadOnly,)
    def get_object(self, pk):
        try:
            return Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)


#FALTA TRATAMENTO DE IMAGENS
class RecipeRegister(APIView):
    #permission_classes = (IsAuthenticatedOrReadOnly,)
    
    def post(self, request, format=None):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDuplicationError(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = u'Duplicate user'

class ProfileSignUp(APIView):
    #permission_classes = (IsAuthenticatedOrReadOnly,)

    #see if User already exists
    def get_object(self, data):
        try:
            retrievedUser = User.objects.filter(username = data)
            raise UserDuplicationError()
        except User.DoesNotExist:
            return True

    def post(self, request, format=None):
        self.get_object(request.data['email'])
        createdUser = User.objects.create_user(request.data['email'], None, request.data['password'])
        request.data.pop('email', None)
        request.data.pop('password', None)
        request.data['user'] = createdUser.pk
        serializer = CreateProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileLogin(APIView):
    #permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_object(self, data):
        try:
            retrievedUser = authenticate(username=data['email'], password=data['password'])
            if retrievedUser is not None:
                user = Profile.objects.get(user = retrievedUser)
                print("achou usuario" + retrievedUser.username)
                return user
            else:
                print("NAO achou usuario")
                raise Http404
        except User.DoesNotExist:
            raise Http404

    def post(self, request, format=None):
        print("request body: " +request.data['email'] + " " + request.data['password'])
        profile = self.get_object(request.data) 
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


class MostThreeRecentRecipeFromEveryCategory(APIView):
    #permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        categories = Category.objects.all()
        listOfRecipes = []
        for cat in categories:
            recipes = Recipe.objects.filter(category = cat)[:3]
            listOfRecipes.append(recipes)
        qs = list(chain.from_iterable(listOfRecipes))
        serializer = ThreeRecentSerializer(qs, many=True)
        return Response(serializer.data)









class RecipesFromCategory(APIView):
    #permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_object(self, pk):
        try:
            category = Category.objects.get(pk=pk)
            return Recipe.objects.filter(category = category)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print("PK: " +pk)
        recipes = self.get_object(pk)
        serializer = CategorySerializer(recipes, many=True)
        print(serializer.data)
        return Response(serializer.data)
