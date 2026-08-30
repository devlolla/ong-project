from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class CoreViewsTests(TestCase):

    def test_home_redirects_anonymous_user_to_login(self):
        response = self.client.get(reverse("core:home"))

        login_url = reverse("accounts:login")
        home_url = reverse("core:home")
        self.assertRedirects(response, f"{login_url}?next={home_url}")

    def test_authenticated_user_can_access_home(self):
        user = User.objects.create_user(
            username="usuario_teste",
            password="senha_teste"
        )
        self.client.force_login(user)
        response = self.client.get(reverse("core:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/home.html")

    def test_health_check_returns_ok(self):
        response = self.client.get(reverse("core:health_check"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"ok")
        self.assertEqual(response["Content-Type"], "text/plain")
