import logging
import re


class InputValidator:
    """
    Validator class to parse input. If input is valid, we return a dictionary
    containing the amount, term, down payment and interest rate.
    """
    logger = logging.getLogger(__name__)

    keywords = ['amount', 'term', 'interest', 'down_payment']
    amount_pattern = '(?=.*amount[\s]*\:[\s]*(?P<amount>\d+))'
    term_pattern = '(?=.*term[\s]*\:[\s]*(?P<term>\d+))'
    interest_pattern = '(?=.*interest[\s]*\:[\s]*(?P<interest>\d+\.*\d*))'
    down_payment_pattern = '(?=.*downpayment[\s]*\:[\s]*(?P<down_payment>\d+))'
    no_repeat_pattern = '(?!.*amount.*amount)(?!.*interest.*interest)(?!.*term.*term)(?!.*downpayment.*downpament)'
    flags = re.IGNORECASE | re.DOTALL

    def __init__(self, data):
        self.data = data
        regex = ''.join([
            self.no_repeat_pattern,
            self.amount_pattern,
            self.term_pattern,
            self.interest_pattern,
            self.down_payment_pattern]
        )

        # Final full regex
        self.regex = re.compile("^" + regex + ".*$", flags=self.flags)

    def get_dict_from_input(self):
        match = self.regex.match(self.data)
        if not match:
            raise InputValidatorError('The input data is invalid')
        return match.groupdict()

    @property
    def is_valid(self):
        match = self.regex.match(self.data)

        if not match:
            return False
        return all(keyword in match.groupdict() for keyword in self.keywords)


class InputValidatorError(Exception):
    """
    Custom exception raised by the InputValidator when parsing the input fails
    :param message: information about the error
    :param invalid_entry: failing input
    """

    def __init__(self, message):
        Exception.__init__(self, message)
