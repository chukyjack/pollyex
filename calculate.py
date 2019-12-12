import argparse
import json
import logging

from loan_calculator.input_validator import InputValidator, InputValidatorError
from loan_calculator.calculator import LoanCalculator


logger = logging.getLogger(__file__)


def get_data_from_file(file_path):
    data = ''
    try:
        with open(file_path) as f:
            data = f.read()
    except IOError as e:
        logger.error(e)
    finally:
        return data


def run_calculator(input_data):
    validator = InputValidator(input_data)

    try:
        valid_data = validator.get_dict_from_input()
    except InputValidatorError as e:
        logger.error(e)
        return

    logger.info('Started calculating loan........................................')
    payment_info = LoanCalculator.get_payment(valid_data)
    logger.info('Finished calculating loan.......................................')
    return payment_info


def main():
    """
    Main program entry point.
    Defines and get the program's arguments and then execute the program's logic calling run_calculator() function
    """
    verbose = ["DEBUG", "INFO", "WARNING", "ERROR", "FATAL"]

    parser = argparse.ArgumentParser(description="Loan Calculator parses input loan data and displays the repayment "
                                                 "schedule. "
                                                 "You can specify the output file where to save the JSON results. "
                                                 "Or you can omit this option and specify verbosity level to DEBUG.")
    parser.epilog = "Example: python calculate.py -t text_with_data -f sample.in -o result.out"
    parser.add_argument("-t", "--text", help="input text to parse", required=False)
    parser.add_argument("-f", "--file", help="input file to parse", required=False)
    parser.add_argument("-o", "--output", help="output file to save the JSON results", required=False)
    parser.add_argument("-v", "--verbose", help="verbosity level: %s" % verbose, required=False)
    args = vars(parser.parse_args())

    if args["verbose"] and args["verbose"].upper() in verbose:
        logging.basicConfig(level=args["verbose"].upper())
    else:
        # Default logging level
        logging.basicConfig(level=logging.FATAL)

    input_text = args['text']
    input_file_path = args["file"]
    output_file_path = args["output"]

    if input_text and input_file_path:
        logger.error('Input can be text or file not both')
        return

    if input_file_path and not input_text:
        input_text = get_data_from_file(input_file_path)

    if not input_text:
        logger.error('Please enter loan data')
        return

    payment_data = run_calculator(input_text)

    # saves payment schedule info in a specified path
    if output_file_path:
        with open(output_file_path, 'w') as f:
            f.write(json.dumps(payment_data, indent=2))


if __name__ == '__main__':
    main()
