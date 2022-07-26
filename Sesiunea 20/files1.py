# TEXT
# biti pe HD ----> decodare ----> vizualizare
#                   utf-8

# BINAR
# biti pe HD ---> decodare ----> vizualizare
#                  codec


# Mod de lucru cu text
# w = write
# r = read
# a = append


# Mod de lucru cu binar
# wb = write binary
# rb = read binary
# ab = append binary

# IO = input/output



file_descriptor = open("c:/Users/tohan/Desktop/IT-SCHOOL/Sesiunea 20/practice.txt")

print(type(file_descriptor))
print(file_descriptor)

content = file_descriptor.read()


for i in range(10):
    print(file_descriptor.read())

# CLOSE THE FILE !!!!!!!!!!
file_descriptor.close()

# 1 caracter = 1 byte

#print(f"Fisierul are: {len(content)} linii")

print(content)