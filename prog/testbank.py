import unittest
import bank
import sys
import HtmlTestRunner

class TestAccount(unittest.TestCase):
    def test_sa_account_creation(self):
        sa = bank.SA('Aditya')
        assert sa.b == 100, 'def balance should be 100'
    def test_ca_account_creation(self):
        ca = bank.CA('abc inc')
        assert ca.b == 10, 'def balance should be 10'
    def test_sa_account_credit(self):
        sa = bank.SA('Aditya')
        sa.credit(100)
        assert sa.b == 200, 'def balance should be 100'
    def test_ca_account_credit(self):
        ca = bank.CA('abc inc')
        ca.credit(100)
        assert ca.b == 100, 'def balance should be 10'

#print(sys.argv)     
#
#if len(sys.argv) == 2:
#    verbosity = int(sys.argv.pop())
    
#auto discovery of test cases     
#verbosity = 1
#unittest.main(verbosity=verbosity)

if len(sys.argv) == 2:
    ts = unittest.TestSuite()
    if sys.argv[-1] == 'SA':
        ts.addTest(TestAccount('test_sa_account_creation'))
        ts.addTest(TestAccount('test_sa_account_credit'))
    elif sys.argv[-1] == 'CA':
        ts.addTest(TestAccount('test_ca_account_creation'))
        ts.addTest(TestAccount('test_ca_account_credit'))
    #r = unittest.TextTestRunner(verbosity=3)
    r = HtmlTestRunner.HTMLTestRunner(output='reports')
    r.run(ts)
else:
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))













