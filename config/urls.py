from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API de Estudantes",
        default_version="v1",
        description="""Exemplo de API em REST para o desafio da Generation Brasil e Potencia Tech
                        \n\nConfira o código-fonte: [GitHub](https://github.com/oicaroabreu/django-potencia-tech)""",  # noqa
        contact=openapi.Contact(name="Ícaro Abreu", email="icaro.labreu@gmail.com"),
        license=openapi.License(
            name="MIT LICENSE",
            url="https://github.com/oicaroabreu/django-potencia-tech/blob/master/LICENSE",
        ),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("students.urls")),
    path(
        "api/v1/docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
