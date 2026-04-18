class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        if iterations == 0:
            return round(init,5)
        else:
            init= init-(learning_rate*(2*init))

            return self.get_minimizer(iterations-1,learning_rate,init)
