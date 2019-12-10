
def get_data_dict(data):
    data = data.strip().split('\n')
    print(data)
    return dict((item.strip().split(':') for item in data))


def get_payment(data):
    data_dict = get_data_dict(data)
    print(data_dict)
    principal = int(data_dict['amount']) - int(data_dict['downpayment'])
    print(principal)
    rate = float(data_dict['interest']) / (100 * 12)
    term = data_dict['term']
    term = int(term) * 12
    monthly_payment = principal * ((rate * pow(1 + rate, term)) / (pow(1+rate, term) - 1))
    total_payment = monthly_payment * term
    total_interest = total_payment - principal
    return {'total_payment': total_payment, 'monthly_payment': monthly_payment, 'total_interest': total_interest}

if __name__=='__main__':
    data = """
    amount: 100000
    interest: 5.5
    downpayment: 20000
    term: 30
    """
    print(get_payment(data))
