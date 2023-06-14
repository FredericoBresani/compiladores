file = open('input.txt', mode='r')
out = open('output.txt', mode='w')
for line in file.readlines():



    
    out.write(line)
out.close()
