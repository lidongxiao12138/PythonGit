"""Python3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import *
from . import testdb
from rest_framework.schemas import get_schema_view
from TestModel.views import ReturnJson
from TestModel.apitest import test_api
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# # Serializers定义了API的表现.
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'is_staff')
#
# # ViewSets 定义了 视图（view） 的行为.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
# # Routers 提供了一种简单途径，自动地配置了URL。
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', get_schema_view, name="docs"),
    url(r'^testdb$', testdb.testdb),
    url(r'^api/getjson', ReturnJson.as_view()),
    url('^test_api/', test_api, name='test_api'),

    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
