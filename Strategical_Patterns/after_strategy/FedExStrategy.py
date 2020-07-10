from after_strategy.AbsStrategy import AbsStrategy

class FedExStrategy(AbsStrategy):
    def calculate(self, order):
        return 3.0