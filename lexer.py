from enum import Enum
import sys

class Lexer:
    def __init__(self, source) -> None:
        self.source = source
        self.cursorBegin = 0
        self.cursorEnd = 0
        self.currentToken = None
        self.EOF = False
        

    def nextToken(self):
        token = None
        char = self.source[self.cursorEnd - self.EOF]
        if self.EOF:
            token = Token(TokenTypes.EOF, '\0')
        elif char == '\n':
            token = None
        elif char == ' ':
            token = None
        elif char == ';':
            token = Token(TokenTypes.SEMICOLON, char)
        elif char == '+':
            token = Token(TokenTypes.PLUS, char)
        elif char == '-':
            if self.isDigit(self.peek()):
                c = self.peek()
                self.nextCharacter()
                token = self.numberToken(c)
            else:
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
        elif char == '<':
            if self.peek() == '=':
                self.nextCharacter()
                token = Token(TokenTypes.LESS_EQUAL, self.source[self.cursorBegin: self.cursorEnd + 1])
            elif self.isLetter(self.peek()) or self.peek() == '.':
                while self.peek() != '>':
                    self.nextCharacter()
                token = Token(TokenTypes.LIB, self.source[self.cursorBegin: self.cursorEnd + 2])
                self.nextCharacter()
            else:
                token = Token(TokenTypes.LESS, char)
        elif char == '>':
            if self.peek() == '=':
                self.nextCharacter()
                token = Token(TokenTypes.GREATER_EQUAL, self.source[self.cursorBegin: self.cursorEnd + 1])
            else:
                token = Token(TokenTypes.GREATER, char)
        elif char == '.':
            token = Token(TokenTypes.POINT, char)
        elif char == '\"':
            while self.peek() != '\"':
                self.nextCharacter()
            self.nextCharacter()
            token = Token(TokenTypes.STRING, self.source[self.cursorBegin: self.cursorEnd + 1]) 
        elif char == ',':
            token = Token(TokenTypes.COMMA, char)
        elif char == '=':
            if self.peek() == '=':
                self.nextCharacter()
                token = Token(TokenTypes.EQUAL, self.source[self.cursorBegin: self.cursorEnd + 1])
            else:
                token = Token(TokenTypes.ASSIGN, char)
        elif self.isLetter(char):
            while self.isDigit(self.peek()) or self.isLetter(self.peek()):
                self.nextCharacter()
            lexema = self.source[self.cursorBegin : self.cursorEnd + 1]
            tipo = Token.checkToken(lexema) 
            if tipo == None:
                token = Token(TokenTypes.IDENTIFIER, lexema)
            else:
                token = Token(tipo, lexema)
        elif self.isDigit(char):
            token = self.numberToken(char)
        else:
            self.abort("Simbolo desconhecido: "+char)
        self.cursorEnd += 1
        self.cursorBegin = self.cursorEnd
        self.currentToken = token

        if self.cursorEnd == len(self.source):
            self.EOF = True

        return token


    def numberToken(self, c):
        while self.isDigit(self.peek()):
                self.nextCharacter()
        if self.peek() == '.':
            self.nextCharacter()
            if self.isDigit(self.peek()):
                while self.isDigit(self.peek()):
                    self.nextCharacter()
            else:
                self.abort("Esperava por um digito mas encontrei um: "+self.peek())
        token = Token(TokenTypes.NUMBER, self.source[self.cursorBegin : self.cursorEnd + 1])
        return token
    
    def nextCharacter(self):
        self.cursorEnd += 1
    
    def peek(self):
        return self.source[self.cursorEnd + 1]
    
    def isLetter(self, c):
        if (ord(c) >= 65 and ord(c) <= 90) or (ord(c) == 95) or (ord(c) >= 97 and ord(c) <= 122):
            return True
        return False

    def isDigit(self, c):
        if ord(c) >= 48 and ord(c) <= 57:
            return True
        return False
    
    def endOfTerm(self, c):
        return (not self.isDigit(c)) and (not self.isLetter(c))
    
    def abort(self, message):
        sys.exit("Erro léxico: \n" + message)





class Token:
    def __init__(self, type, lexeme) -> None:
        self.type = type
        self.lexeme = lexeme
    @staticmethod
    def checkToken(lexema):
        for token in TokenTypes:
            if token.name == lexema.upper() and token.value < 200 and token.value >= 100:
                return token
        return None

class TokenTypes(Enum):
    EOF = -1
    LITERAL = 1
    IDENTIFIER = 2
    LIB = 3
    NUMBER = 4
    POINT = 5
    # RESERVER WORDS ( (100, 200] )
    INCLUDE = 100
    ELSE = 104
    IF = 105
    WHILE = 107
    FOR = 108
    PRINT = 110
    POW = 111 
    INT = 112
    FLOAT = 113
    DOUBLE = 114
    STRING = 115
    LONG = 116
    READ = 117
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
    COMMA = 312
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