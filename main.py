from lexer import Lexer

file = open('input.txt', mode='r')
out_tokens = open('outtokens.txt', mode='w')

content = file.read()
lex = Lexer(content)

out_tokens.close()
file.close()