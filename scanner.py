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
        if c == '(': self.add_token(TokenType.LEFT_PAREN)
        elif c == ')': self.add_token(TokenType.RIGHT_PAREN)
        elif c == '+': self.add_token(TokenType.PLUS)
        elif c == '-': self.add_token(TokenType.MINUS)
        elif c == '*': self.add_token(TokenType.STAR)
        elif c == '/': self.add_token(TokenType.SLASH)
        elif c.isdigit() or c == '.':
            self.number()
        elif c in [' ', '\r', '\t']:
            pass  # ignore whitespace
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
