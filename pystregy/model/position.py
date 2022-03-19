from .order import Order

class Position():
    id: int
    main_order: Order
    take_order: Order
    stop_order: Order
    status: int
    Open, TakeProfit, StopLoss, Cancelled = range(4)
