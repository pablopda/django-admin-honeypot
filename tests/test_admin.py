from django.test import TestCase
from django.urls import reverse
from admin_honeypot.models import LoginAttempt

class AdminHoneypotAdminTest(TestCase):
    def setUp(self):
        self.login_attempt = LoginAttempt.objects.create(
            username='test_user',
            ip_address='127.0.0.1',
            session_key='test_session',
            user_agent='test_agent',
            path='/admin/'
        )

    def test_admin_list_view(self):
        url = reverse('admin:admin_honeypot_loginattempt_changelist')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Redirects to login

    def test_admin_detail_view(self):
        url = reverse('admin:admin_honeypot_loginattempt_change', args=[self.login_attempt.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)  # Redirects to login