from django.apps import AppConfig


class {{ cookiecutter.model_name }}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = '{{ cookiecutter.repo_app }}.{{ cookiecutter.app_name }}'
