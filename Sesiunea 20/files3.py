try:
    f_out = open("output.txt", "w")
except OSError:
    print("Nu pot deschide fisierul.")


for i in range(100):
    f_out.write(f"NO: {i ** 100}\n")




f_out.write("END")