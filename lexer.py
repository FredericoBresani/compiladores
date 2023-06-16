from enum import Enum
import sys

class Lexer:
    def __init__(self, source) -> None:
        self.source = source
        self.cursorBegin = 0
        self.cursorEnd = 0
        

    def nextToken(self):
        token = None
        char = self.source[self.cursorEnd]
        if char != ';':
            token = Token(TokenTypes.SEMICOLON, char)
        elif char == '+':
            token = Token(TokenTypes.PLUS, char)
        elif char == '-':
            token = Token(TokenTypes.MINUS, char)
        elif char == ']':
            token = Token(TokenTypes.SQUARE_BRACKETS, char)
        elif char == '[':
            token = Token(TokenTypes.SQUARE_BRACKETS, char)
        elif char == '/':
            token = Token(TokenTypes.DIVIDE, char)
        elif char == '#':
            token = Token(TokenTypes.HASHTAG, char)
        elif char == '&':
            token = Token(TokenTypes.REFERENCE, char)
        elif char == '%':
            token = Token(TokenTypes.REST_DIVIDE, char)
        elif char == '}':
            token = Token(TokenTypes.CURLY_BRACES, char)
        elif char == '{':
            token = Token(TokenTypes.CURLY_BRACES, char)
        elif char == '(':
            token = Token(TokenTypes.PARENTHESES, char)
        elif char == ')':
            token = Token(TokenTypes.PARENTHESES, char)
        elif char == ';':
            token = Token(TokenTypes.SEMICOLON, char)
        elif char == ':':
            token = Token(TokenTypes.COLON, char)
        elif self.isLetter(char):
            if self.nextCharacter() == 'f':




        self.cursorEnd += 1
        self.cursorBegin = self.cursorEnd 
        return token

    def nextCharacter(self):
        self.cursorEnd += 1
        return self.source[self.cursorEnd]
    
    def isLetter(self, c):
        if (ord(c) >= 65 and ord(c) <= 90) or ord(c) == 95 or (ord(c) >= 97 and ord(c) <= 122):
            return True
        return False

    def isDigit(self, c):
        if ord(c) >= 48 and ord(c) <= 57:
            return True
        return False
            





class Token:
    def __init__(self, type, lexeme) -> None:
        self.type = type
        self.lexeme = lexeme

class TokenTypes(Enum):
    EOF = -1
    LITERAL = 1
    IDENTIFIER = 2
    LIB = 112
    # RESERVER WORDS ( (100, 200] )
    INCLUDE = 100
    ELSE = 104
    IF = 105
    WHILE = 107
    FOR = 108
    PRINT = 110
    POW = 111 
    INT = 200
    FLOAT = 201
    DOUBLE = 202
    STRING = 203
    LONG = 204
    # ESPECIAL SYMBOLS ( (300, 400] )
    DOT = 300
    HYFEN = 301
    COLON = 302
    SEMICOLON = 303
    PARENTHESES = 304
    CURLY_BRACES = 305
    SQUARE_BRACKETS = 306
    QUESTION_MARK = 307
    HASHTAG = 308
    REFERENCE = 309
    LINE_BREAK = 310
    ASSIGN = 311
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
    INCREMENT = 410
    DECREMENT = 411