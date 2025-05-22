from enum import Enum, auto


class TokenType(Enum):
    # Single-character tokens
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()

    # Literals
    NUMBER = auto()

    # Misc
    EOF = auto()


class Token:
    def __init__(self, type, lexeme, literal, line):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line

    def __str__(self):
        return f'{self.type} {self.lexeme} {self.literal}'

    if __name__ == "__main__":
        print("Token module loaded successfully.")
