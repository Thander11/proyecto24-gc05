from django.apps import apps
from django.test import TestCase
from usuarios.apps import UsuariosConfig


class TestUsuariosConfig(TestCase):
    def test_apps_name(self):
        """Verifica que el nombre de la aplicación sea correcto."""
        self.assertEqual(UsuariosConfig.name, 'usuarios', "El nombre de la aplicación debería ser 'usuarios'.")

    def test_default_auto_field(self):
        """Verifica que el campo predeterminado sea BigAutoField."""
        self.assertEqual(UsuariosConfig.default_auto_field, 'django.db.models.BigAutoField',
                         "El campo predeterminado debería ser 'django.db.models.BigAutoField'.")

    def test_apps_registry(self):
        """Verifica que la aplicación esté registrada correctamente."""
        self.assertEqual(apps.get_app_config('usuarios').name, 'usuarios',
                         "La aplicación 'usuarios' debería estar registrada en apps.")
