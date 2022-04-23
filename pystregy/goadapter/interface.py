# from pystregy import Strategy, Position, Order
# from pystregy.goadapter.repository import Repository
# from pystregy.goadapter.broker import GoBroker
# from pystregy.goadapter.service import Service

# BROKER = GoBroker()
# STRATEGY = Strategy(BROKER)


# def on_position(position: Position) -> Repository:
#     STRATEGY.on_position(position)
#     return Service.GetRepo()

# def on_order(order: Order) -> Repository: 
#     STRATEGY.on_order(order)
#     return Service.GetRepo()