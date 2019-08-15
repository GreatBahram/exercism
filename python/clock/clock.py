MINUTES_PER_HOUR = 60
MINUTES_PER_DAY = 1440


class Clock:
    def __init__(self, hour, minute):
        self.hour, self.minute = divmod(
            (hour * MINUTES_PER_HOUR + minute) % MINUTES_PER_DAY, 60
        )

    def __str__(self):
        return f"{self.hour:02}:{self.minute:02}"

    def __eq__(self, other):
        if isinstance(other, Clock):
            return (self.hour, self.minute) == (other.hour, other.minute)
        return NotImplemented

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
