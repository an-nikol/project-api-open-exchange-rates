import requests
import json
from datetime import datetime

global dict_symbols_currency
if 'dict_symbols_currency' not in globals():
    dict_symbols_currency = {
        'AED': 'United Arab Emirates Dirham',
        'AFN': 'Afghan Afghani',
        'ALL': 'Albanian Lek',
        'AMD': 'Armenian Dram',
        'ANG': 'Netherlands Antillean Guilder',
        'AOA': '(Angolan Kwanza)',
        'ARS': 'Argentine Peso',
        'AUD': 'Australian Dollar',
        'AWG': 'Aruban Florin',
        'AZN': 'Azerbaijani Manat',
        'BAM': 'Bosnia - Herzegovina Convertible Mark',
        'BBD': 'Barbadian Dollar',
        'BDT': 'Bangladeshi Taka',
        'BGN': 'Bulgarian Lev',
        'BHD': 'Bahraini Dinar',
        'BIF': 'Burundian Franc',
        'BMD': 'Bermudan Dollar',
        'BND': 'Brunei Dollar',
        'BOB': 'Bolivian Boliviano',
        'BRL': 'Brazilian Real',
        'BSD': 'Bahamian Dollar',
        'BTC': 'Bitcoin',
        'BTN': 'Bhutanese Ngultrum',
        'BWP': 'Botswanan Pula',
        'BYN': 'Belarusian Ruble',
        'BYR': 'Belarusian Ruble(pre - 2016)',
        'BZD': 'Belize Dollar',
        'CAD': 'Canadian Dollar',
        'CDF': 'Congolese Franc',
        'CHF': 'Swiss Franc',
        'CLF': 'Chilean Unit of Account(UF)',
        'CLP': 'Chilean Peso',
        'CNH': 'Chinese Yuan(Offshore)',
        'CNY': 'Chinese Yuan',
        'COP': 'Colombian Peso',
        'CRC': 'Costa Rican Colón',
        'CUC': 'Cuban Convertible Peso',
        'CUP': 'Cuban Peso',
        'CVE': 'Cape Verdean Escudo',
        'CZK': 'Czech Republic Koruna',
        'DJF': 'Djiboutian Franc',
        'DKK': 'Danish Krone',
        'DOP': 'Dominican Peso',
        'DZD': 'Algerian Dinar',
        'EEK': 'Estonian Kroon',
        'EGP': 'Egyptian Pound',
        'ERN': 'Eritrean Nakfa',
        'ETB': 'Ethiopian Birr',
        'EUR': 'Euro',
        'FJD': 'Fijian Dollar',
        'FKP': 'Falkland Islands Pound',
        'GBP': 'British Pound Sterling',
        'GEL': 'Georgian Lari',
        'GGP': 'Guernsey Pound',
        'GHS': 'Ghanaian Cedi',
        'GIP': 'Gibraltar Pound',
        'GMD': 'Gambian Dalasi',
        'GNF': 'Guinean Franc',
        'GTQ': 'Guatemalan Quetzal',
        'GYD': 'Guyanaese Dollar',
        'HKD': 'Hong Kong Dollar',
        'HNL': 'Honduran Lempira',
        'HRK': 'Croatian Kuna',
        'HTG': 'Haitian Gourde',
        'HUF': 'Hungarian Forint',
        'IDR': 'Indonesian Rupiah',
        'ILS': 'Israeli New Sheqel',
        'IMP': 'Manx pound',
        'INR': 'Indian Rupee',
        'IQD': 'Iraqi Dinar',
        'IRR': 'Iranian Rial',
        'ISK': 'Icelandic Króna',
        'JEP': 'Jersey Pound',
        'JMD': 'Jamaican Dollar',
        'JOD': 'Jordanian Dinar',
        'JPY': 'Japanese Yen',
        'KES': 'Kenyan Shilling',
        'KGS': 'Kyrgystani Som',
        'KHR': 'Cambodian Riel',
        'KMF': 'Comorian Franc',
        'KPW': 'North Korean Won',
        'KRW': 'South Korean Won',
        'KWD': 'Kuwaiti Dinar',
        'KYD': 'Cayman Islands Dollar',
        'KZT': 'Kazakhstani Tenge',
        'LAK': 'Laotian Kip',
        'LBP': 'Lebanese Pound',
        'LKR': 'Sri Lankan Rupee',
        'LRD': 'Liberian Dollar',
        'LSL': 'Lesotho Loti',
        'LYD': 'Libyan Dinar',
        'MAD': 'Moroccan Dirham',
        'MDL': 'Moldovan Leu',
        'MGA': 'Malagasy Ariar',
        'MKD': 'Macedonian Denar',
        'MMK': 'Myanma Kyat',
        'MNT': 'Mongolian Tugrik',
        'MOP': 'Macanese Pataca',
        'MRO': 'Mauritanian Ouguiya(pre - 2018)',
        'MRU': 'Mauritanian Ouguiya',
        'MTL': 'Maltese Lira',
        'MUR': 'Mauritian Rupee',
        'MVR': 'Maldivian Rufiyaa',
        'MWK': 'Malawian Kwacha',
        'MXN': 'Mexican Peso',
        'MYR': 'Malaysian Ringgit',
        'MZN': 'Mozambican Metical',
        'NAD': 'Namibian Dollar',
        'NGN': 'Nigerian Naira',
        'NIO': 'Nicaraguan Córdoba',
        'NOK': 'Norwegian Krone',
        'NPR': 'Nepalese Rupee',
        'NZD': 'New Zealand Dollar',
        'OMR': 'Omani Rial',
        'PAB': 'Panamanian Balboa',
        'PEN': 'Peruvian Nuevo Sol',
        'PGK': 'Papua New Guinean Kina',
        'PHP': 'Philippine Peso',
        'PKR': 'Pakistani Rupee',
        'PLN': 'Polish Zloty',
        'PYG': 'Paraguayan Guarani',
        'QAR': 'Qatari Rial',
        'RON': 'Romanian Leu',
        'RSD': 'Serbian Dinar',
        'RUB': 'Russian Ruble',
        'RWF': 'Rwandan Franc',
        'SAR': 'Saudi Riyal',
        'SBD': 'Solomon Islands Dollar',
        'SCR': 'Seychellois Rupee',
        'SDG': 'Sudanese Pound',
        'SEK': 'Swedish Krona',
        'SGD': 'Singapore Dolla',
        'SHP': 'Saint Helena Pound',
        'SLL': 'Sierra Leonean Leone',
        'SOS': 'Somali Shilling',
        'SRD': 'Surinamese Dollar',
        'SSP': 'South Sudanese Pound',
        'STD': 'São Tomé and Príncipe Dobra(pre - 2018)',
        'STN': 'São Tomé and Príncipe Dobra',
        'SVC': 'Salvadoran Colón',
        'SYP': 'Syrian Pound',
        'SZL': 'Swazi Lilangeni',
        'THB': 'Thai Baht',
        'TJS': 'Tajikistani Somoni',
        'TMT': 'Turkmenistani Manat',
        'TND': 'Tunisian Dinar',
        'TOP': 'Tongan Paʻanga',
        'TRY': 'Turkish Lira',
        'TTD': 'Trinidad and Tobago Dollar',
        'TWD': 'New Taiwan Dollar',
        'TZS': 'Tanzanian Shilling',
        'UAH': 'Ukrainian Hryvnia',
        'UGX': 'Ugandan Shilling',
        'USD': 'United States Dollar',
        'UYU': 'Uruguayan Peso',
        'UZS': 'Uzbekistan Som',
        'VES': 'Venezuelan Bolívar Soberano',
        'VND': 'Vietnamese Dong',
        'VUV': 'Vanuatu Vatu',
        'WST': 'Samoan Tala',
        'XAF': 'CFA Franc BEAC',
        'XAG': 'Silver(troy ounce)',
        'XAU': 'Gold(troy ounce)',
        'XCD': 'East Caribbean Dollar',
        'XDR': 'Special Drawing Rights',
        'XOF': 'CFA Franc BCEAO',
        'XPD': 'Palladium Ounce',
        'XPF': 'CFP Franc',
        'XPT': 'Platinum Ounce',
        'YER': 'Yemeni Rial',
        'ZAR': 'South African Rand',
        'ZMK': 'Zambian Kwacha(pre - 2013)',
        'ZMW': 'Zambian Kwacha'
    }


class Currency:
    def __init__(self):
        self.api_key = open('api_key').readline().strip()
        self.url = f'https://openexchangerates.org/api/latest.json?app_id={self.api_key}'
        self.output = ''
        self.current_currency = ''
        self.amount = 0

    def do_request_01(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.output = response.json()['rates']
            str_response = json.dumps(self.output)
            dict_response = json.loads(str_response)
            for key in dict_response:
                print(key, "     -     ", dict_response[key])
        else:
            return f'Unexpected error. Type of error: {response.status_code}'

    def do_request_02(self, current_currency):
        self.current_currency = current_currency

        response = requests.get(self.url, choice)
        if response.status_code == 200:
            self.output = response.json()['rates']
            str_response = json.dumps(self.output)
            dict_response = json.loads(str_response)
            is_valid_currency = False
            if current_currency in dict_response:
                is_valid_currency = True
                print(f'The current rate for 1 USD is {dict_response[current_currency]} {current_currency}')
            if not is_valid_currency:
                print(f'Please enter a valid currency.')
        else:
            return f'Unexpected error. Type of error: {response.status_code}'

    # fix me
    def do_request_03(self, current_currency, amount):
        self.current_currency = current_currency
        self.amount = amount
        response = requests.get(self.url)
        if response.status_code == 200:
            self.output = response.json()['rates']
            str_response = json.dumps(self.output)
            dict_response = json.loads(str_response)



        else:
            return f'Unexpected error. Type of error: {response.status_code}'

while True:

    # i want users to click these icons
    print('Menu')
    print('Please choose one of the options below:')
    print('1. All current currency rates')
    print('2. A specific currency rate')
    print('3. Convert from USD to another currency')
    print('4. Statistics for usage')
    print('5. Quit')

    choice = int(input('Enter your choice (1/2/3/4): '))
    if choice == 1:
        # call object
        current_date = datetime.now().strftime('%d %b %Y')
        print()
        print(f'The date of the request: {current_date}')
        print('Currency - Corresponding rate per 1 USD')
        choice_01 = Currency()
        choice_01.do_request_01()

    elif choice == 2:
        print()
        for symbol, currency in dict_symbols_currency.items():
            print(f'{symbol} ({currency})')

        print()

        chosen_currency = input('Enter one of the currencies you would want to convert to USD: ')
        choice_02 = Currency()
        choice_02.do_request_02(chosen_currency)

    elif choice == 3:

        for symbol, currency in dict_symbols_currency.items():
            print(f'{symbol} ({currency})')
        type_of_currency = input('Enter one of the currency you would like to convert to USD: ')
        currency_amount = int(input('Enter the amount: '))

        choice_03 = Currency()
        choice_03.do_request_03(type_of_currency, currency_amount)
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        pass
