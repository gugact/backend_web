from rest_framework import serializers
from .models import *

"""class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('id', 'name')



class ItemInListSerializer(serializers.ModelSerializer):
    shopping_list = serializers.IntegerField(source = 'shopping_list.id')
    item_name = serializers.CharField(source = 'item.name')

    class Meta:
        model = ItemInList 
        fields = ('item_name','shopping_list', 'amount', 'already_bought')

    def create(self, validated_data):
        try:
            item = Item.object.get(name= self.data['item_name'])
        except Item.DoesNotExist:
            item = Item.objects.create(name = self.data['item_name'])

        shopping_list = ShoppingList.objects.get(id= self.data['shopping_list'])
        iteminlist = ItemInList.objects.create(shopping_list = shopping_list, item = item, amount= self.data['amount'])

        return iteminlist

class ShoppingListSerializer(serializers.ModelSerializer):
	
    itens = ItemInListSerializer(source = 'iteminlist_set',many=True)

    class Meta:
        model = ShoppingList
        fields = ('id', 'date', 'itens')

    def create(self, validated_data):
        arr_itens = []
        array_coming = self.data['itens']

        for arr in array_coming:
            try:
                item = Item.objects.get(name = arr['item_name'])
            except Item.DoesNotExist:
                item = Item.objects.create(name = arr['item_name'])

            arr_itens.append(item)

        shopping_list = ShoppingList.objects.create()
        counter = 0

        for arr in arr_itens:
            iteminlist = ItemInList.objects.create(shopping_list = shopping_list, item = arr, 
                amount= array_coming[counter]['amount'])
            counter+=1

        return shopping_list
"""


class RecipeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ('id', 'name','description','images','category','ingredients',
            'preparation_time','preparation_instructions','portions',
            'nutritional_value','cooking_method','date')
        depth = 4



class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('id',"user",'birth_date','name','city','state','telephone')


class CreateProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('id', 'user','birth_date','name',
            'city','state','telephone')

"""
    def create(self, validated_data):
        userExists = False
        try:
            user = User.objects.get(username= self.data['username'])
            userExists = True
        except Item.DoesNotExist:
            #USER SHOULD NOT EXIST
            #create user first, then create Profile
            user = User.objects.create_user(self.data['username'],self.data['email'],self.data['password'])
        #gotta return some error, which one though?
        if (userExists != False):
            return Http404

        profile = Profile.objects.create(user = user , birth_date = self.data['birth_date'],
            city = self.data['city'], state = self.data['state'], telephone = self.data['telephone'])

        return profile
"""

class CategorySerializer(serializers.ModelSerializer):
	
    class Meta:
        model = Recipe
        fields = ('id', 'name','description','images','category','ingredients',
            'preparation_time','preparation_instructions','portions',
            'nutritional_value','cooking_method','date')
        depth = 4

"""
    def create(self, validated_data):
        recipeList = Recipe.objects.get(category = validated_data)

        return recipeList
"""

class ThreeRecentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('id', 'name','description','images','category','ingredients',
            'preparation_time','preparation_instructions','portions',
            'nutritional_value','cooking_method','date')
        depth = 4
"""
    def create(self, validated_data):
        recipeList = Recipe.objects.get(category = validated_data)

        return recipeList
        """