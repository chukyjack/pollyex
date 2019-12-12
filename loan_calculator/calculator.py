import logging
from loan_calculator.input_validator import InputValidator


validate = InputValidator


class LoanCalculator:
    """
    Loan calculator accepts loan data, then calculates and displays the payment schedule
    """

    def __init__(self):
        logger = logging.getLogger(self.__class__.__name__)

    @staticmethod
    def get_payment(data_dict):
        """
        Method to calculate and return payment schedule.
        :param data_dict: dictionary containing loan amount, interest rate, term in years and down payment
        :return: dictionary containing monthly payment, total interest and total payment.
        """
        payment_schedule = {}

        principal = float(data_dict['amount']) - float(data_dict['down_payment'])
        rate = float(data_dict['interest']) / (100 * 12)
        term = float(data_dict['term']) * 12

        monthly_payment = principal * ((rate * pow(1 + rate, term)) / (pow(1+rate, term) - 1))
        total_payment = monthly_payment * term
        total_interest = total_payment - principal

        payment_schedule['total_payment'] = '%.2f' % total_payment
        payment_schedule['monthly_payment'] = '%.2f' % monthly_payment
        payment_schedule['total_interest'] = '%.2f' % total_interest
        logging.info(payment_schedule)

        return payment_schedule

