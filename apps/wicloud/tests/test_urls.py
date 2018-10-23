from django.urls import reverse, resolve

from test_plus.test import TestCase


class TestInstallationURLs(TestCase):
    """Test URL patterns for users app."""

    # def setUp(self):
    #     self.user = self.make_user()
    #
    def test_installation_list_reverse(self):
        """users:list should reverse to /documents/."""
        self.assertEqual(reverse("api:installation_list"), "/api/installation/list/")

    def test_installation_detail_reverse(self):
        """users:list should reverse to /documents/."""

        self.assertEqual(reverse("api:installation_retrieve", kwargs={"pk": "testuuid" }), "/api/installation/retrieve/testuuid/")

    def test_installation_list_resolve(self):
        """/users/ should resolve to users:list."""
        self.assertEqual(resolve("/api/installation/list/").view_name, "api:installation_list")



