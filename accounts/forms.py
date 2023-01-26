import unittest
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()


class accountCreation(UserCreationForm):
    email = forms.EmailField(required=True, label="Email")

    class Meta:
        model = User
        fields = ['username', 'email', "first_name", "last_name", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(accountCreation, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'email', 'first_name', 'last_name', 'password1']:
            self.fields[fieldname].help_text = None
