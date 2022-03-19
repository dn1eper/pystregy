from decimal import Decimal

class Order():
    id: int
    size: Decimal
    price: Decimal
    commission: Decimal
    status: int
    Created, Accepted, Partial, Completed, Cancelled, Expired, Margin = range(7)

    def __init__(self, size=0, price=0.0):
        self.tradeid = None
        self.size = size
        self.price = price
        self.commission = None

        self.status = self.Created