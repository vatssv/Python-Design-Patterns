import sys
sys.path.append('.before_strategy')
from before_strategy.Order import Order
from before_strategy.ShippingCost import ShippingCost
from before_strategy.Shipper import Shipper

#Test fedex shipping
order = Order(Shipper.fedex)
cost_calculator = ShippingCost()
cost = cost_calculator.shipping_cost(order)
assert cost == 3.0

#Test ups shipping
order = Order(Shipper.ups)
cost_calculator = ShippingCost()
cost = cost_calculator.shipping_cost(order)
assert cost == 4.0

#Test postal shipping
order = Order(Shipper.postal)
cost_calculator = ShippingCost()
cost = cost_calculator.shipping_cost(order)
assert cost == 5.0

print('Tests Passed')