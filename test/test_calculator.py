from unittest import TestCase

from loan_calculator.calculator import LoanCalculator
from loan_calculator.input_validator import InputValidator


class LoanCalculatorTest(TestCase):

    def setUp(self):
        super(LoanCalculatorTest, self).setUp()
        self.expected_result = {
            'monthly_payment': '6174.37',
            'total_interest': '2075696.55',
            'total_payment': '2963696.55'
        }

    def test_get_payment(self):
        data = self._get_valid_data()
        payment_result = LoanCalculator.get_payment(data)
        self.assertEqual(payment_result, self.expected_result)

    def _get_valid_data(self):
        normal_data = '''
                amount: 890000
                interest: 8%
                downpayment: 2000
                term: 40
                
                '''
        validator = InputValidator(normal_data)
        return validator.get_dict_from_input()

