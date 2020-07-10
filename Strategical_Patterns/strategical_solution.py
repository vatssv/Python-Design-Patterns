import sys
sys.path.append('.after_strategy')
from after_strategy.Order import Order
from after_strategy.ShippingCost import ShippingCost
from after_strategy.FedExStrategy import FedExStrategy
from after_strategy.UPSStrategy import UPSStrategy
from after_strategy.PostalStrategy import PostalStrategy

#Test fedex shipping
order = Order()
strategy = FedExStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 3.0

#Test ups shipping
order = Order()
strategy = UPSStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 4.0

#Test postal shipping
order = Order()
strategy = PostalStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 5.0

print('Tests Passed')