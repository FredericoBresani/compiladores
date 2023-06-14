from enum import Enum
import sys

class Lexer:
    def __init__(self, source) -> None:
        self.source = source
        self.cursorBegin = 0
        self.cursorEnd = 0
        

    def nextToken(self) -> None:
        self.nextCharacter()
        self.cursorEnd += 1
        self.cursorBegin = self.cursorEnd 

    def nextCharacter(self) -> bool:
        token = None
        while True:
            char = self.source[self.cursorEnd]
            self.cursorEnd += 1
            if char != ' ' and char != ';':
                break
            elif char == '+':
                token = Token(TokenTypes.PLUS, char)
                break
            elif char == '-'
            





class Token:
    def __init__(self, type, lexeme) -> None:
        self.type = type
        self.lexeme = lexeme

class TokenTypes(Enum):
    EOF = -1
    # RESERVER WORDS ( (100, 200] )
    INCLUDE = 100
    LINE_BREAK = 101
    LITERAL = 102
    ASSIGN = 103
    ELSE = 104
    IF = 105
    ELSE_IF = 106
    WHILE = 107
    FOR = 108
    IDENTIFIER = 109
    # DATA TYPE ( (200, 300] )
    INT = 200
    FLOAT = 201
    DOUBLE = 202
    STRING = 203
    LONG = 204
    # ESPECIAL SYMBOLS ( (300, 400] )
    DOT = 300
    HYFEN = 301
    HASHTAG = 302
    SEMICOLON = 303
    PARENTHESES = 304
    CURLY_BRACES = 305
    SQUARE_BRACKETS = 306
    # OPERATORS ( (400, 500] )
    EQUAL = 400
    LESS = 401
    LESS_EQUAL = 402
    GREATER = 403
    GREATER_EQUAL = 404
    PLUS = 405
    MINUS = 406
    DIVIDE = 407
    MULTIPLY = 408
    REST_DIVIDE = 409