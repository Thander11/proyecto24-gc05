import unittest
from django.conf import settings

class TestSettings(unittest.TestCase):
    def test_debug_mode(self):
        """Verifica que el modo DEBUG esté configurado correctamente."""
        self.assertIsInstance(settings.DEBUG, bool, "DEBUG debe ser un valor booleano.")

    def test_installed_apps(self):
        """Verifica que las aplicaciones esenciales estén instaladas."""
        required_apps = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'rest_framework',
            'usuarios',
        ]
        for app in required_apps:
            self.assertIn(app, settings.INSTALLED_APPS, f"El app {app} debería estar en INSTALLED_APPS.")

    # Resto de las pruebas...

if __name__ == "__main__":
    unittest.main()
