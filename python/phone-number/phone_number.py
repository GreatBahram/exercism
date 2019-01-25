import re

NANP_RE = re.compile(r'''
    ^
    \+?1?                     # country code
    \D*                       # separator
    \(? ( [2-9] \d{2} ) \)?   # area code
    \D*                       # separator
    ( [2-9] \d{2} )           # exchange code
    \D*                       # separator
    ( \d{4} )                 # subscriber number
    \D*                       # separator
    $
''', re.VERBOSE)


class Phone:
    def __init__(self, phone_number):
        self.from_string(phone_number)

    def from_string(self, phone_number):
        """Parse and extract phone number from string."""
        matched = NANP_RE.match(phone_number)
        if matched:
            self.number = ''.join(matched.group(1, 2, 3))
            self.area_code = matched.group(1)
            self.exchange_code = matched.group(2)
            self.subscriber_number = matched.group(3)
        else:
            raise ValueError("Phone number is not valid.")

    def __str__(self):
        return f'({self.area_code}) {self.exchange_code}-{self.subscriber_number}'

    pretty = __str__
