from lexer import Lexer
from lexer import Token

class Parser:
    def __init__(self, lexer, writeFile) -> None:
        self.lexer = lexer
        self.writeFile = writeFile

    def askForTokens(self):
        while True:
            token = self.lexer.nextToken()
            if token == None:
                continue
            elif token.lexeme == '\0':
                self.writeFile.write("<{}, {}>\n".format(token.type, token.lexeme))
                print("LEXER FINISHED!!!")
                break
            else:
                self.writeFile.write("<{}, {}>\n".format(token.type, token.lexeme))
            