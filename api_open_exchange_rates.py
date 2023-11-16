import requests
import json
from datetime import datetime


class Currency:
    def __init__(self):
        self.api_key = open('api_key').readline().strip()
        self.url = f'https://openexchangerates.org/api/latest.json?app_id={self.api_key}'
        self.output = ''

    def do_request_01(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.output = response.json()['rates']
            str_response = json.dumps(self.output)
            dict_response = json.loads(str_response)
            final_list = []
            for key in dict_response.keys():
                print(key, "     -     ", dict_response[key])
        else:
            return f'Unexpected error. Type of error: {response.status_code}'

    def do_request_02(self):
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
    print('3. Historical currency rates ')
    print('4. Convert from USD to another currency')
    print('5. Statistics for usage')
    print('6. Quit')

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
            






        }

        \n \n \n \n\
        \n \n  \n \n\
       \n \n \n \n\
        \n \n \n \n\
       \n \n \n\
       \n \n \n  \n\
       \n \n \n \n\
        NIO (Nicaraguan Córdoba)\n NOK (Norwegian Krone)\n NPR (Nepalese Rupee)\n  NZD (New Zealand Dollar)\n\
        OMR (Omani Rial)\n PAB (Panamanian Balboa)\n PEN (Peruvian Nuevo Sol)\n PGK (Papua New Guinean Kina)\n\
        PHP	(Philippine Peso)\n PKR (Pakistani Rupee)\n PLN (Polish Zloty)\n PYG (Paraguayan Guarani)\n\
        QAR (Qatari Rial)\n RON (Romanian Leu)\n RSD (Serbian Dinar)\n RUB (Russian Ruble)\n RWF (Rwandan Franc)\n\
        SAR (Saudi Riyal)\n SBD (Solomon Islands Dollar)\n SCR (Seychellois Rupee)\n SDG (Sudanese Pound)\n\
        SEK (Swedish Krona)\n SGD (Singapore Dolla)\n SHP (Saint Helena Pound)\n SLL (Sierra Leonean Leone)\n\
        SOS (Somali Shilling)\n SRD (Surinamese Dollar)\n SSP (South Sudanese Pound)\n\
        STD (São Tomé and Príncipe Dobra (pre-2018))\n STN (São Tomé and Príncipe Dobra)\n\
        SVC	(Salvadoran Colón)\n SYP (Syrian Pound)\n SZL (Swazi Lilangeni)\n THB (Thai Baht)\n\
        TJS (Tajikistani Somoni)\n TMT (Turkmenistani Manat)\n TND (Tunisian Dinar)\n TOP (Tongan Paʻanga)\n\
        TRY (Turkish Lira)\n TTD (Trinidad and Tobago Dollar)\n TWD (New Taiwan Dollar)\n TZS (Tanzanian Shilling)\n\
        UAH (Ukrainian Hryvnia)\n UGX (Ugandan Shilling)\n USD (United States Dollar)\n UYU	(Uruguayan Peso)\n\
        UZS (Uzbekistan Som)\n VES (Venezuelan Bolívar Soberano)\n VND (Vietnamese Dong)\n VUV (Vanuatu Vatu)\n\
        WST (Samoan Tala)\n XAF (CFA Franc BEAC)\n XAG (Silver (troy ounce))\n XAU (Gold (troy ounce))\n\
        XCD (East Caribbean Dollar)\n XDR (Special Drawing Rights)\n XOF (CFA Franc BCEAO)\n XPD (Palladium Ounce)\n\
        XPF (CFP Franc)\n XPT (Platinum Ounce)\n YER (Yemeni Rial)\n ZAR (South African Rand)\n\
        ZMK (Zambian Kwacha (pre-2013))\n ZMW (Zambian Kwacha)]

        print(currencies, sep='\n')

        chosen_currency = input('Enter one of the currencies to see its corresponding rate per 1 USD')

    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        pass
