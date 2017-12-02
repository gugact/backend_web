from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

"""
home -> initial page with 3 most-recent recipes per category
recipe/id -> recipe details
login -> login request
signup -> create user request
create-recipe -> request for creating a recipe
category/id -> show all recipes of category
"""

urlpatterns = [
    url(r'^home/$', views.MostThreeRecentRecipeFromEveryCategory.as_view()),
    url(r'^recipe/(?P<pk>\d+)$', views.RecipeDetails.as_view()),
    url(r'^category/(?P<pk>\d+)$', views.RecipesFromCategory.as_view()),
    url(r'^reciperegister/$', views.RecipeRegister.as_view()),
    url(r'^login/$', views.ProfileLogin.as_view()),
    url(r'^sign-up/$', views.ProfileSignUp.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)