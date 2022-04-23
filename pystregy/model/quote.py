from datetime import datetime

class Quote():
    __slots__ = 'time', 'open', 'high', 'low', 'close'

    def __init__(self, time: datetime, 
        open: float, high: float, low: float, close: float
    ):
        self.time = time
        self.open = open
        self.high = high
        self.low = low
        self.close = close
