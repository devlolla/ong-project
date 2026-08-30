from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AuthenticationViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="usuario_teste",
            password="senha_teste"
        )

    def test_login_page_returns_success(self):
        response = self.client.get(reverse("accounts:login"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/login.html")
        self.assertContains(response, "Bem-vindo(a) novamente")
        self.assertContains(response, "Guardiões da")
        self.assertContains(response, "Causa Animal")

    def test_valid_login_redirects_to_home(self):
        response = self.client.post(
            reverse("accounts:login"),
            {
                "username": self.user.username,
                "password": "senha_teste"
            },
        )

        self.assertRedirects(response, reverse("core:home"))

    def test_logout_redirects_to_login(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse("accounts:logout"))
        self.assertRedirects(response, reverse("accounts:login"))
