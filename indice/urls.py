from .views import inicio
from django import path
urlpatterns = [
    path("",inicio,name="inicio")
]
