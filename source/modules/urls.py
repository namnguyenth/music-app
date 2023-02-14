from django.urls import path

# Create your views here.

from .repository.nation.nation import Nation

urlpatterns = [
    # path('nation/', Nation.as_view()),
]