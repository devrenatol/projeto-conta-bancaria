from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class ContaBancariaViewTest(TestCase):

    def __init__(self, methodName = "runTest"):
        super().__init__(methodName)

    def setUp(self):
        self.client = APIClient()

