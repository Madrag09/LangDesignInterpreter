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
            if expr.operator.type == TokenType.BANG:
                return not self.is_truthy(right)
            elif expr.operator.type == TokenType.MINUS:
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
            elif expr.operator.type == TokenType.EQUAL_EQUAL:
                return left == right
            elif expr.operator.type == TokenType.BANG_EQUAL:
                return left != right
            elif expr.operator.type == TokenType.GREATER:
                return left > right
            elif expr.operator.type == TokenType.GREATER_EQUAL:
                return left >= right
            elif expr.operator.type == TokenType.LESS:
                return left < right
            elif expr.operator.type == TokenType.LESS_EQUAL:
                return left <= right
            elif expr.operator.type == TokenType.AND:
                return self.is_truthy(left) and self.is_truthy(right)
            elif expr.operator.type == TokenType.OR:
                return self.is_truthy(left) or self.is_truthy(right)
        raise Exception("Unknown expression type.")

    def is_truthy(self, value):
        if value is None: return False
        if isinstance(value, bool): return value
        return bool(value)
