from datetime import datetime
from decimal import Decimal

class Quote():
    __slots__ = 'time', 'open', 'high', 'low', 'close'

    def __init__(self, time: datetime, 
        open: Decimal, high: Decimal, low: Decimal, close: Decimal
    ):
        self.time = time
        self.open = open
        self.high = high
        self.low = low
        self.close = close
