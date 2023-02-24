t = []
with open('channels.txt', 'r') as file:
    for i in file.readlines():
        t.append(i[:-1])

with open('channels2.txt', 'w') as file:
    file.write(', '.join(t))
