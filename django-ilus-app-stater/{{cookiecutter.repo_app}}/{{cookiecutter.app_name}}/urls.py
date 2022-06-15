from django.urls import path

urlpatterns = [
    path('', '{{ cookiecutter.model_name|lower }}_list',
         name='{{ cookiecutter.app_name }}_{{ cookiecutter.model_name|lower }}_list'),
    path('create/', '{{ cookiecutter.model_name|lower }}_create',
         name='{{ cookiecutter.app_name }}_{{ cookiecutter.model_name|lower }}_create'),
    path('<slug>/update/', '{{ cookiecutter.model_name|lower }}_update',
         name='{{ cookiecutter.app_name }}_{{ cookiecutter.model_name|lower }}_update'),
    path('<slug>/', '{{ cookiecutter.model_name|lower }}_read',
         name='{{ cookiecutter.app_name }}_{{ cookiecutter.model_name|lower }}_read'),
]
