HOUR_PER_DAY = 24
MINUTES_PER_HOUR = 60


class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        return f"{self.hour:02}:{self.minute:02}"

    def __eq__(self, other):
        if isinstance(other, Clock):
            return (self.hour, self.minute) == (other.hour, other.minute)
        return NotImplemented

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)

    @property
    def hour(self):
        return self._hour

    @hour.setter
    def hour(self, value):
        _, value = divmod(value, HOUR_PER_DAY)
        self._hour = value

    @property
    def minute(self):
        return self._minute

    @minute.setter
    def minute(self, value):
        quotient, value = divmod(value, MINUTES_PER_HOUR)
        self.hour += quotient
        self._minute = value
