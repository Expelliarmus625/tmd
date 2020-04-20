from django.urls import path
from . import views
# from django.conf.urls.static import static
# from django.conf import settings

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name= "login"),
    path('logout/', views.logout, name = "logout"),
    path('upload/', views.upload, name = "upload"),
    # path('result/', views.result, name = "result")
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)