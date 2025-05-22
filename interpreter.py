from lditoken import TokenType
from expressions import *
from statements import Print, Var, ExpressionStmt


class Interpreter:
    def __init__(self):
        self.environment = {}

    def interpret(self, statements):
        for stmt in statements:
            self.execute(stmt)

    def execute(self, stmt):
        if isinstance(stmt, Print):
            value = self.evaluate(stmt.expression)
            print(value)
        elif isinstance(stmt, Var):
            value = self.evaluate(stmt.initializer)
            self.environment[stmt.name.lexeme] = value
        elif isinstance(stmt, ExpressionStmt):
            self.evaluate(stmt.expression)

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
                if isinstance(left, str) and isinstance(right, str):
                    return left + right
                elif isinstance(left, (int, float)) and isinstance(right, (int, float)):
                    return left + right
                else:
                    raise Exception("Operands must be two numbers or two strings.")
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
        elif isinstance(expr, Variable):
            name = expr.name.lexeme
            if name in self.environment:
                return self.environment[name]
            raise Exception(f"Undefined variable '{name}'.")
        elif isinstance(expr, Assign):
            value = self.evaluate(expr.value)
            self.environment[expr.name.lexeme] = value
            return value

    def is_truthy(self, value):
        if value is None: return False
        if isinstance(value, bool): return value
        return bool(value)
