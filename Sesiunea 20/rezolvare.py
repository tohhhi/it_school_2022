file_descriptor = open("c:/Users/tohan/Desktop/IT-SCHOOL/Sesiunea 20/practice.txt")


content = file_descriptor.read()

print(content)

for i in content:
    print (i, end="")



stuff_to_write = []
with open("c:/Users/tohan/Desktop/IT-SCHOOL/Sesiunea 20/practice.txt") as f:
    for line in f.readlines():
        if any(phrase in line for phrase in keep_phrases):
            do_not_write = False
            if 'note' in line:
                if any(phrase in line.split('note')[1] for phrase in remove_phrases):
                    do_not_write = True
            if not do_not_write:
                stuff_to_write.append(line)

with open('C:/b.txt','w') as f:
    f.write('\r\n'.join(stuff_to_write))


## asta e bun 

try:
    with open("practice.txt", "r") as f_in:
        content = f_in.readlines()
except OSError as err:
    print(err)

else:
    print(content)
    try: 
        with open("output.txt", "w") as o_in:
            o_in.writelines(content[:3])
    except OSError as err:
        print(err)



