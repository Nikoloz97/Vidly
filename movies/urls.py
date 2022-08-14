# Purpose = "Map" the URL to view
from django.urls import path
# Below = syntax for importing modules within the project (views.py) using django
from . import views

# urlpatterns = contains paths that "map" URL endpoints to view functions
# 1st arg = http request (endpoint) - empty string to represent "root" of app
# 2nd = reference the view function (meaning no parenthesis - that would be "calling" it)
# 3rd = name the URL endpoint (best practice)
urlpatterns = [
    path('', views.index, name="index")
]
