inp = open("image(9).txt")
out = open("image.txt", 'w')

s = inp.read()

d = s.split('\n\n')

for s in d:
    s = s.replace('-\n', '')
    s = s.replace('\n', ' ')
    
    out.write(s)

    out.write('\n\n')