"""
URL configuration for BookShelfW41 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from books import views


urlpatterns = [
    path("dodaj_ksiazke/", views.AddBookView.as_view(), name="add_book"),
    path("dodaj_autora/", views.AddAuthorView.as_view(), name="add_author"),
    path("usun_autora/<int:pk>/", views.DeleteAuthorView.as_view(), name="delete_author"),
    path("zmien_autora/<int:pk>/", views.UpdateAuthorView.as_view(), name="update_author"),
    path("add_publisher/", views.AddPublisherView.as_view(), name="add_publisher"),
    path("add_genre/", views.AddGenereView.as_view(), name="add_genre"),
    path("list_book/", views.BookListView.as_view(), name="list_book"),
]
