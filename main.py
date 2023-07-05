from lexer import Lexer
from parserx import Parser

file = open('input.txt', mode='r')
out_tokens = open('outtokens.txt', mode='w')

content = file.read()
lex = Lexer(content)
parser = Parser(lex, out_tokens)
parser.askForTokens()

out_tokens.close()
file.close()