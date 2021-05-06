from django.urls import path, include
from . import views
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="Student Management API",
      default_version='v1',
      description="Document for API",
      terms_of_service="https://www.pbl5.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    #path('', views.UserTypesView, name="api-overview"),
    path('user-types', views.UserTypesAPIView.as_view()),
    path('user-types', views.UserTypesAPIView.as_view()),

    path('users', views.UserAPIView.as_view()),
    path('users/by-id', views.UserGetAPIView.as_view()),
    path('users/sign-up', views.SignUpAPIView.as_view()),
    path('users/log-in', views.LoginAPIView.as_view()),

    path('subjects', views.SubjectsAPIView.as_view()),
    path('classes', views.ClasssAPIView.as_view()),
    path('dates', views.DateAPIView.as_view()),
    path('date-classes', views.DateClassAPIView.as_view()),

    path('doc', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]