from datetime import datetime
from decimal import Decimal

class Quote():
    time: datetime
    open: Decimal
    hight: Decimal
    low: Decimal
    close: Decimal