from unittest import TestCase

from loan_calculator.input_validator import InputValidator, InputValidatorError


class InputValidatorTest(TestCase):

    def setUp(self):
        self.normal_data = '''
                            amount: 90
                            interest: 8.5%
                            downpayment: 70
                            term: 60
                            '''
        self.data_with_delimiter = '''
                            amount: 90,
                            interest: 8.5%,
                            downpayment: 70,
                            term: 60,
                            '''
        self.data_with_different_case = """amOunt:90 interest: 8.5 TERM : 60 downPayment :70"""
        self.data_with_noise = """amount:90 this is noise interest: 8.5 TERM : 60 downPayment :70  loan details"""
        self.data_without_percent = """amount:90 this is noise interest: 8.5 TERM : 60 downPayment :70  loan details"""
        self.data_with_missing_key_field = """interest: 80 TERM : 6.5 downPayment :70 """
        self.data_with_missing_number_in_value_field = """ amount : nan interest: 80 TERM : 60 downPayment :70 """
        self.data_with_more_than_one_key_field = """amount:90 interest: 8.5 TERM : 60 downPayment :70 amount"""
        self.expected_output = {'amount': '90', 'interest': '8.5', 'term': '60', 'down_payment': '70'}
        super(InputValidatorTest, self).setUp()

    def test_is_valid(self):
        validator = InputValidator(self.normal_data)
        self.assertTrue(validator.is_valid)
        self.assertEqual(validator.get_dict_from_input(), self.expected_output)

    def test_get_dict_from_input(self):
        validator = InputValidator(self.normal_data)
        self.assertTrue(validator.is_valid)
        self.assertEqual(validator.get_dict_from_input(), self.expected_output)

        validator = InputValidator(self.data_with_missing_key_field)
        self.assertRaises(InputValidatorError, validator.get_dict_from_input)

    def test_input_is_case_insensitive(self):
        validator = InputValidator(self.data_with_different_case)
        self.assertTrue(validator.is_valid)
        self.assertEqual(validator.get_dict_from_input(), self.expected_output)

    def test_filter_noise_from_input(self):
        validator = InputValidator(self.data_with_noise)
        self.assertTrue(validator.is_valid)
        self.assertEqual(validator.get_dict_from_input(), self.expected_output)

    def test_interest_valid_without_percent(self):
        validator = InputValidator(self.data_without_percent)
        self.assertTrue(validator.is_valid)
        self.assertEqual(validator.get_dict_from_input(), self.expected_output)

    def test_data_with_delimiter_is_valid(self):
        validator = InputValidator(self.data_with_delimiter)
        self.assertTrue(validator.is_valid)
        self.assertEqual(validator.get_dict_from_input(), self.expected_output)

    def test_invalid_input(self):
        invalids = [
            self.data_with_missing_key_field,
            self. data_with_missing_number_in_value_field,
            self.data_with_more_than_one_key_field
        ]
        for invalid in invalids:
            validator = InputValidator(invalid)
            self.assertFalse(validator.is_valid)
            self.assertRaises(InputValidatorError, validator.get_dict_from_input)

