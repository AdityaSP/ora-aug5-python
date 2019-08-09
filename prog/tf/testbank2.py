import unittest
import bank
import sys
import HtmlTestRunner

class TestAccount2(unittest.TestCase):
    def test_sa_account_creation2(self):
        sa = bank.SA('Aditya')
        assert sa.b == 100, 'def balance should be 100'
    def test_ca_account_creation2(self):
        ca = bank.CA('abc inc')
        assert ca.b == 10, 'def balance should be 10'
    def test_sa_account_credit2(self):
        sa = bank.SA('Aditya')
        sa.credit(100)
        assert sa.b == 200, 'def balance should be 100'
    def test_ca_account_credit2(self):
        ca = bank.CA('abc inc')
        ca.credit(100)
        assert ca.b == 100, 'def balance should be 10'
