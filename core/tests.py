from django.test import TestCase
from django.urls import reverse


class CoreViewsTests(TestCase):

    def test_home_returns_success_and_uses_correct_template(self):
        response = self.client.get(reverse("core:home"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/home.html")

    def test_health_check_returns_ok(self):
        response = self.client.get(reverse("core:health_check"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"ok")
        self.assertEqual(response["Content-Type"], "text/plain")
