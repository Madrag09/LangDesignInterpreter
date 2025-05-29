from expressions import *


class Stmt:
    pass


class ExpressionStmt(Stmt):
    def __init__(self, expression):
        self.expression = expression


class Print(Stmt):
    def __init__(self, expression):
        self.expression = expression


class Var(Stmt):
    def __init__(self, name, initializer):
        self.name = name
        self.initializer = initializer


class Block(Stmt):
    def __init__(self, statements):
        self.statements = statements


class If(Stmt):
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch


class While(Stmt):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
