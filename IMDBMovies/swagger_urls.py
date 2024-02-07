from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.urls import path
from drf_yasg.generators import OpenAPISchemaGenerator

class CustomOpenAPISchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, *args, **kwargs):
        schema = super().get_schema(*args, **kwargs)
        schema.basePath = '/maasai-mara/'
        return schema



schema_view = get_schema_view(
    info=openapi.Info(
        title="OMDB Movie APIS",
        default_version='v1',
        description="APIs made in submission to Roam's Technical assessment",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="akalerupe@gmail.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
]
