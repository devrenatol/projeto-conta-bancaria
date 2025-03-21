from django.test import TestCase
import os
from unittest.mock import MagicMock
from application.services import ContaBancariaService
from domain.interfaces import IContaBancariaRepository
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'setup.settings'
django.setup()

class ContaBancariaTestCase(TestCase):

    def setUp(self):
        self.conta_repository = MagicMock(spec=IContaBancariaRepository)
        self.conta_service = ContaBancariaService(self.conta_repository)

    def test_create_conta_bancaria_ok(self):
        self.conta_repository.create.return_value = {
            'id': '1', 
            'account_number': '11111-11',
            'account_holder': 'Teste',
            'balance': '0.00'
        }

        conta_dict = {
            'account_number': '11111-11',
            'account_holder': 'Teste',
            'balance': '0.00'
        }

        conta_bancaria = self.conta_service.post(conta_dict)

        self.conta_repository.create.assert_called_once()
        self.assertEqual(conta_bancaria['account_number'], '11111-11')
    
    def test_create_conta_bancaria_holder_failed(self):
        self.conta_repository.create.return_value = {
            'id': '1',
            'account_number': '11111-11',
            'account_holder': 'Teste2',
            'balance': '0.00'
        }

        conta_dict = {
            'account_number': '11111-11',
            'account_holder': 'Teste2',
            'balance': '0.00'
        }

        with self.assertRaises(ValueError):
            self.conta_service.post(conta_dict)

    def test_create_conta_bancaria_number_failed(self):
        self.conta_repository.create.return_value = {
            'id': '1',
            'account_number': '1111111',
            'account_holder': 'Teste',
            'balance': '0.00'
        }

        conta_dict = {
            'account_number': '1111111',
            'account_holder': 'Teste',
            'balance': '0.00'
        }

        with self.assertRaises(ValueError):
            self.conta_service.post(conta_dict)

    def test_update_conta_bancaria_ok(self):
        self.conta_repository.update.return_value = {
            'id': '1', 
            'account_number': '11111-11',
            'account_holder': 'Teste',
            'balance': '0.00'
        }

        conta_dict = {
            'account_number': '11111-11',
            'account_holder': 'Teste',
            'balance': '0.00'
        }

        conta_bancaria = self.conta_service.put(conta_dict, 1)

        self.conta_repository.update.assert_called_once()
        self.assertEqual(conta_bancaria['account_number'], '11111-11')

    def test_update_conta_bancaria_holder_failed(self):
        self.conta_repository.update.return_value = {
            'id': '1',
            'account_number': '11111-11',
            'account_holder': 'Teste2',
            'balance': '0.00'
        }

        conta_dict = {
            'account_number': '11111-11',
            'account_holder': 'Teste2',
            'balance': '0.00'
        }

        with self.assertRaises(ValueError):
            self.conta_service.post(conta_dict)

    def test_update_conta_bancaria_balance(self):
        self.conta_repository.update.return_value = {
            'id': '1',
            'account_number': '11111-11',
            'account_holder': 'Teste2',
            'balance': '-10.00'
        }

        conta_dict = {
            'account_number': '11111-11',
            'account_holder': 'Teste2',
            'balance': '-10.00'
        }

        with self.assertRaises(ValueError):
            self.conta_service.post(conta_dict)

