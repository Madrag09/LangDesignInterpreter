from lditoken import TokenType
from expressions import *
from statements import Print, Var, ExpressionStmt, If, While, Block


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def parse(self):
        statements = []
        while not self.is_at_end():
            statements.append(self.declaration())
        return statements

    def declaration(self):
        if self.match(TokenType.IDENTIFIER) and self.match(TokenType.EQUAL):
            name = self.previous(2)
            initializer = self.expression()
            return Var(name, initializer)
        return self.statement()

    def statement(self):
        if self.match(TokenType.PRINT): return self.print_statement()
        if self.match(TokenType.IF): return self.if_statement()
        if self.match(TokenType.WHILE): return self.while_statement()
        if self.match(TokenType.LEFT_BRACE): return Block(self.block())
        return ExpressionStmt(self.expression())

    def print_statement(self):
        value = self.expression()
        return Print(value)

    def if_statement(self):
        self.consume(TokenType.LEFT_PAREN)
        condition = self.expression()
        self.consume(TokenType.RIGHT_PAREN)
        then_branch = self.statement()
        else_branch = self.statement() if self.match(TokenType.ELSE) else None
        return If(condition, then_branch, else_branch)

    def while_statement(self):
        self.consume(TokenType.LEFT_PAREN)
        condition = self.expression()
        self.consume(TokenType.RIGHT_PAREN)
        body = self.statement()
        return While(condition, body)

    def block(self):
        statements = []
        while not self.check(TokenType.RIGHT_BRACE) and not self.is_at_end():
            statements.append(self.declaration())
        self.consume(TokenType.RIGHT_BRACE)
        return statements

    def expression(self):
        return self.assignment()

    def assignment(self):
        expr = self.or_()
        if self.match(TokenType.EQUAL):
            value = self.assignment()
            if isinstance(expr, Variable):
                return Assign(expr.name, value)
            raise Exception("Invalid assignment target.")
        return expr

    def or_(self):
        expr = self.and_()
        while self.match(TokenType.OR):
            operator = self.previous()
            right = self.and_()
            expr = Binary(expr, operator, right)
        return expr

    def and_(self):
        expr = self.equality()
        while self.match(TokenType.AND):
            operator = self.previous()
            right = self.equality()
            expr = Binary(expr, operator, right)
        return expr

    def equality(self):
        expr = self.comparison()
        while self.match(TokenType.BANG_EQUAL, TokenType.EQUAL_EQUAL):
            operator = self.previous()
            right = self.comparison()
            expr = Binary(expr, operator, right)
        return expr

    def comparison(self):
        expr = self.term()
        while self.match(TokenType.GREATER, TokenType.GREATER_EQUAL,
                         TokenType.LESS, TokenType.LESS_EQUAL):
            operator = self.previous()
            right = self.term()
            expr = Binary(expr, operator, right)
        return expr

    def term(self):
        expr = self.factor()
        while self.match(TokenType.PLUS, TokenType.MINUS):
            operator = self.previous()
            right = self.factor()
            expr = Binary(expr, operator, right)
        return expr

    def factor(self):
        expr = self.unary()
        while self.match(TokenType.STAR, TokenType.SLASH):
            operator = self.previous()
            right = self.unary()
            expr = Binary(expr, operator, right)
        return expr

    def unary(self):
        if self.match(TokenType.BANG, TokenType.MINUS):
            return Unary(self.previous(), self.unary())
        return self.primary()

    def primary(self):
        if self.match(TokenType.FALSE): return Literal(False)
        if self.match(TokenType.TRUE): return Literal(True)
        if self.match(TokenType.STRING): return Literal(self.previous().literal)
        if self.match(TokenType.NUMBER): return Literal(self.previous().literal)
        if self.match(TokenType.IDENTIFIER): return Variable(self.previous())
        if self.match(TokenType.INPUT): return Call(self.previous())
        if self.match(TokenType.LEFT_PAREN):
            expr = self.expression()
            self.consume(TokenType.RIGHT_PAREN)
            return Grouping(expr)
        raise Exception("Expected expression.")

    def match(self, *types):
        for type in types:
            if self.check(type):
                self.advance()
                return True
        return False

    def consume(self, type):
        if self.check(type): return self.advance()
        raise Exception(f"Expected token {type}")

    def check(self, type):
        return not self.is_at_end() and self.peek().type == type

    def advance(self):
        if not self.is_at_end(): self.current += 1
        return self.previous()

    def is_at_end(self):
        return self.peek().type == TokenType.EOF

    def peek(self):
        return self.tokens[self.current]

    def previous(self, steps=1):
        return self.tokens[self.current - steps]
