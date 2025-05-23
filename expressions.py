class Expr:
    pass


class Literal(Expr):
    def __init__(self, value):
        self.value = value


class Grouping(Expr):
    def __init__(self, expression):
        self.expression = expression


class Unary(Expr):
    def __init__(self, operator, right):
        self.operator = operator
        self.right = right


class Binary(Expr):
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right


class Variable(Expr):
    def __init__(self, name):
        self.name = name


class Assign(Expr):
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Call(Expr):
    def __init__(self, name):
        self.name = name
