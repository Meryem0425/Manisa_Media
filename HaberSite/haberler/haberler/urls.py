from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from AppHaberler import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path("category/<slug:category>/", views.category, name="category"),
    path('search/', views.search, name='search'),
    path('add_favorite/', views.add_favorite, name='add_favorite'),
    path('favorites/', views.favorites_list, name='favorites_list'),

    path('register/', views.register, name='register'),

    path('login/', auth_views.LoginView.as_view(template_name='register.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),

    path("remove-favorite/<int:fav_id>/", views.remove_favorite, name="remove_favorite"),
]

