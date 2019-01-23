import re

NANP_RE = re.compile(r'''
    ^
    \+?([0-9])?          # country code
    [\s|\-|\.]*          # separator
    \(?([2-9]\d{2})\)?   # area code
    [\s|\-|\.]*          # separator
    ([2-9]\d{2})         # exchange code
    [\s|\-|\.]*          # separator
    (\d{4})              # subscriber number
    [\s|\-|\.]*          # separator
    $
    ''', re.VERBOSE)


class Phone:
    def __init__(self, phone_number):
        self.from_string(phone_number)

    def from_string(self, phone_number):
        """Parse and extract phone number from string."""
        matched = NANP_RE.match(phone_number)
        if matched:
            self.number = ''.join(matched.group(2, 3, 4))
            self.country_code = matched.group(1)
            self.area_code = matched.group(2)
            self.exchange_code = matched.group(3)
            self.subscriber_number = matched.group(4)

            if self.country_code and self.country_code != '1':
                raise ValueError("Phone number is not valid.")
        else:
            raise ValueError("Phone number is not valid.")

    def pretty(self):
        return f'({self.area_code}) {self.exchange_code}-{self.subscriber_number}'
