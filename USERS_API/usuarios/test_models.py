from django.test import TestCase
from usuarios.models import Usuario, Pago, Perfiles

class TestUsuarioModel(TestCase):
    def setUp(self):
        """Crea un usuario de prueba para usar en los tests."""
        self.usuario = Usuario.objects.create(
            correoelectronico="test@example.com",
            contrasena="testpassword",
            nombreusuario="testuser"
        )

    def test_usuario_creation(self):
        """Verifica que un usuario se cree correctamente."""
        self.assertEqual(self.usuario.correoelectronico, "test@example.com")
        self.assertEqual(self.usuario.contrasena, "testpassword")
        self.assertEqual(self.usuario.nombreusuario, "testuser")

    def test_usuario_unique_correoelectronico(self):
        """Verifica que 'correoelectronico' sea único."""
        with self.assertRaises(Exception):
            Usuario.objects.create(
                correoelectronico="test@example.com",  # Duplicado
                contrasena="anotherpassword",
                nombreusuario="anotheruser"
            )


class TestPagoModel(TestCase):
    def setUp(self):
        """Crea un usuario y un pago de prueba."""
        self.usuario = Usuario.objects.create(
            correoelectronico="test2@example.com",
            contrasena="password2",
            nombreusuario="user2"
        )
        self.pago = Pago.objects.create(
            idusuario=self.usuario,
            numerotarjeta="1234567890123456",
            fechacaducidad="12/25",
            cvc="123"
        )

    def test_pago_creation(self):
        """Verifica que un pago se cree correctamente."""
        self.assertEqual(self.pago.idusuario, self.usuario)
        self.assertEqual(self.pago.numerotarjeta, "1234567890123456")
        self.assertEqual(self.pago.fechacaducidad, "12/25")
        self.assertEqual(self.pago.cvc, "123")

    def test_pago_relationship(self):
        """Verifica la relación entre Pago y Usuario."""
        self.assertEqual(self.usuario.pagos.first(), self.pago)


class TestPerfilesModel(TestCase):
    def setUp(self):
        """Crea un usuario y un perfil de prueba."""
        self.usuario = Usuario.objects.create(
            correoelectronico="test3@example.com",
            contrasena="password3",
            nombreusuario="user3"
        )
        self.perfil = Perfiles.objects.create(
            idusuario=self.usuario,
            nombreperfil="Perfil de prueba",
            fotoperfil=1
        )

    def test_perfil_creation(self):
        """Verifica que un perfil se cree correctamente."""
        self.assertEqual(self.perfil.idusuario, self.usuario)
        self.assertEqual(self.perfil.nombreperfil, "Perfil de prueba")
        self.assertEqual(self.perfil.fotoperfil, 1)

    def test_perfil_relationship(self):
        """Verifica la relación entre Perfiles y Usuario."""
        self.assertEqual(self.usuario.perfiles.first(), self.perfil)
