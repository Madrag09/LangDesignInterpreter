from lditoken import TokenType, Token


class Scanner:
    def __init__(self, source):
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1

    def scan_tokens(self):
        while not self.is_at_end():
            self.start = self.current
            self.scan_token()
        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens

    def scan_token(self):
        c = self.advance()
        if c == '(':
            self.add_token(TokenType.LEFT_PAREN)
        elif c == ')':
            self.add_token(TokenType.RIGHT_PAREN)
        elif c == '+':
            self.add_token(TokenType.PLUS)
        elif c == '-':
            self.add_token(TokenType.MINUS)
        elif c == '*':
            self.add_token(TokenType.STAR)
        elif c == '/':
            self.add_token(TokenType.SLASH)
        elif c == '!':
            self.add_token(TokenType.BANG_EQUAL if self.match('=') else TokenType.BANG)
        elif c == '=':
            if self.match('='): self.add_token(TokenType.EQUAL_EQUAL)
        elif c == '<':
            self.add_token(TokenType.LESS_EQUAL if self.match('=') else TokenType.LESS)
        elif c == '>':
            self.add_token(TokenType.GREATER_EQUAL if self.match('=') else TokenType.GREATER)
        elif c.isdigit() or c == '.':
            self.number()
        elif c.isalpha():
            self.identifier()
        elif c in [' ', '\r', '\t']:
            pass
        elif c == '\n':
            self.line += 1
        else:
            print(f"[Line {self.line}] Unexpected character: {c}")

    def number(self):
        while self.peek().isdigit():
            self.advance()
        if self.peek() == '.' and self.peek_next().isdigit():
            self.advance()
            while self.peek().isdigit():
                self.advance()
        value = float(self.source[self.start:self.current])
        self.add_token(TokenType.NUMBER, value)

    def identifier(self):
        while self.peek().isalnum():
            self.advance()
        text = self.source[self.start:self.current]
        keywords = {
            "true": TokenType.TRUE,
            "false": TokenType.FALSE,
            "and": TokenType.AND,
            "or": TokenType.OR,
        }
        token_type = keywords.get(text)
        if token_type:
            self.add_token(token_type)
        else:
            print(f"[Line {self.line}] Unknown identifier: {text}")

    def match(self, expected):
        if self.is_at_end(): return False
        if self.source[self.current] != expected: return False
        self.current += 1
        return True

    def peek(self):
        if self.is_at_end(): return '\0'
        return self.source[self.current]

    def peek_next(self):
        if self.current + 1 >= len(self.source): return '\0'
        return self.source[self.current + 1]

    def is_at_end(self):
        return self.current >= len(self.source)

    def advance(self):
        self.current += 1
        return self.source[self.current - 1]

    def add_token(self, type, literal=None):
        text = self.source[self.start:self.current]
        self.tokens.append(Token(type, text, literal, self.line))
