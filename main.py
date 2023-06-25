from lexer import Lexer

file = open('input.txt', mode='r')
out_tokens = open('outtokens.txt', mode='w')

content = file.read()
lex = Lexer(content)
while True:
    token = lex.nextToken()
    if token == None:
        continue
    elif token.lexeme == '\0':
        break
    else:
        print("<{}, {}>".format(token.type, token.lexeme))

out_tokens.close()
file.close()