from lditoken import TokenType
from expressions import *

class Interpreter:
    def evaluate(self, expr):
        if isinstance(expr, Literal):
            return expr.value
        elif isinstance(expr, Grouping):
            return self.evaluate(expr.expression)
        elif isinstance(expr, Unary):
            right = self.evaluate(expr.right)
            if expr.operator.type == TokenType.MINUS:
                return -right
        elif isinstance(expr, Binary):
            left = self.evaluate(expr.left)
            right = self.evaluate(expr.right)
            if expr.operator.type == TokenType.PLUS:
                return left + right
            elif expr.operator.type == TokenType.MINUS:
                return left - right
            elif expr.operator.type == TokenType.STAR:
                return left * right
            elif expr.operator.type == TokenType.SLASH:
                return left / right
        raise Exception("Unknown expression type.")
