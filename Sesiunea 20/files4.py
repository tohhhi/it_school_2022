# context manager

content = None


try:
    with open("google_logo.png", "rb") as f_in:
        content = f_in.read()
except OSError as err:
    print(err)


if content:
    print(content)

print(f_in.closed)
print("End")



# deschide si extrage primele 3 linii si le scire in output txt


