from django.urls import path

from v0_back.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
    Create_Project,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
    path('api/nombre_empresa/create/', Create_Project, name = 'crear_proyecto'),
]
