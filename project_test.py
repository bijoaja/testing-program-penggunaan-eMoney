import unittest
from unittest.mock import patch
from main import *
from projek import *

class EmoneyTest(unittest.TestCase):
    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
    
    def setUp(self):
        self.emoney = EMoneyCard("Joel")
        self.halte = Halte("Cikampek", "Bogor", "Ekonomi")

    ### START TEST FOR MAIN FUNCTION ###
    @patch('builtins.input', side_effect=[1, "n"])
    def test_payment_top_up(self, mock_input):
        result = payment_top_up()
        self.assertEqual(result, 5000)
        
    @patch('builtins.input', side_effect=[0])
    def test_payment_top_up_error_input(self, mock_input):
        with self.assertRaises(Exception):
            payment_top_up()
        
    @patch('builtins.input', side_effect=[1, "y", 2, "y", 1, "n"])
    def test_payment_top_up_again(self, mock_input):
        result = payment_top_up()
        self.assertEqual(result, 20000)
        
    @patch('builtins.input', side_effect=[1, 1, 1])
    def test_destination(self, mock_input):
        result = destination()
        self.assertEqual(result, ["Cikampek", "Bogor", "Ekonomi"])
        
    @patch('builtins.input', side_effect=[0])
    def test_destination_error_start_input(self, mock_input):
        with self.assertRaises(Exception):
            destination()
        
    @patch('builtins.input', side_effect=[1,0])
    def test_destination_error_middle_input(self, mock_input):
        with self.assertRaises(Exception):
            destination()
        
    @patch('builtins.input', side_effect=[1,1,0])
    def test_destination_error_end_input(self, mock_input):
        with self.assertRaises(Exception):
            destination()

    @patch('builtins.input', side_effect=[1, 1, "n", 3])
    def test_main_test_topup(self, mock_input):
        result = main()
        self.assertEqual(result, "Your Saldo: 5,000")

    @patch('builtins.input', side_effect=[1, 1, "y", 2, "y", 1, "n", 3])
    def test_main_test_topup_again(self, mock_input):
        result = main()
        self.assertEqual(result, "Your Saldo: 20,000")

    @patch('builtins.input', side_effect=[1, 1, "n", 2, 1, 1, 1])
    def test_main_go_to_destination(self, mock_input):
        result = main()
        self.assertEqual(result, "Payment successful. Remaining balance: 1,000")

    @patch('builtins.input', side_effect=[2, 1, 1, 1])
    def test_main_go_to_destination_less_balance(self, mock_input):
        result = main()
        self.assertEqual(result, 'Insufficient balance. Please top-up your card.')
        
    @patch('builtins.input', side_effect=[1, 1, 'n', 3])
    def test_main_check_balance(self, mock_input):
        result = main()
        self.assertEqual(result, "Your Saldo: 5,000")

    @patch('builtins.input', side_effect=[3])
    def test_main_check_without_balance(self, mock_input):
        result = main()
        self.assertEqual(result, "Your Saldo: 0")

    @patch('builtins.input', side_effect=[0])
    def test_main_logout(self, mock_input):
        result = main()
        self.assertEqual(result, "Thank You")
        
    @patch('builtins.input', side_effect=[4])
    def test_main_error_input(self, mock_input):
        with self.assertRaises(Exception):
            main()
    ### FINISH TEST FOR MAIN FUNCTION ###
    
    ### START TEST FOR EMONEY###
    def test_get_name_emoney(self):
        name = self.emoney.name
        self.assertEqual(name, "Joel")
        
    def test_check_balance_without_balance(self):
        balance = self.emoney.check_balance()
        self.assertEqual(balance, "0")
        
    def test_check_balance_when_topup(self):
        self.emoney.top_up(5000)
        balance = self.emoney.check_balance()
        self.assertEqual(balance, "5,000")
        
    def test_topup(self):
        topup = self.emoney.top_up(5000)
        self.assertEqual(topup, "Top-up successful. Current balance: 5,000")
        
    def test_deduct(self):
        self.emoney.top_up(15000)
        deduct = self.emoney.deduct(3000)
        self.assertEqual(deduct, "Payment successful. Remaining balance: 12,000")
        
    def test_deduct_without_balance(self):
        topup = self.emoney.deduct(5000)
        self.assertEqual(topup, "Insufficient balance. Please top-up your card.")
    ### FINISH TEST FOR EMONEY ###
    
    ### START TEST FOR HALTE ###
    def test_get_cost_lines(self):
        getCostLines = self.halte.getCostLines()
        self.assertEqual(getCostLines, 2000)
        
    def test_get_cost_transportation(self):
        getCostTransportation = self.halte.getCostTransportation()
        self.assertEqual(getCostTransportation, 2000)
        
    def test_get_cost(self):
        self.halte.totalCost()
        cost = self.halte.getCost()
        self.assertEqual(cost, 4000)
    ### FINISH TEST FOR HALTE ###
    
    def tearDown(self):
        self.emoney.balance = 0
    
if __name__ == '__main__':
    unittest.main()