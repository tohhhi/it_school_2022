import sys 
# argumente

# print(sys.argv[0])  # numele executabilului 

#print(sys.argv)

#n = 0
#name = sys.argv[1] 

#rep = int(sys.argv[2])

#while n < rep:
#    print(name)
#    n += 1



name = None
rep = 10

def show_help():
    print("""Usage: script_name.py NAME [REPS]

NAME = nume de afisat
REPS = de cate ori se afiseaza
""")
    sys.exit(1)


if len(sys.argv) > 1:
    name = sys.argv[1]
else:
    show_help()

if len(sys.argv) > 2:
    rep = sys.argv[2]

for i in range(rep):
    print(name)


# https://docs.python.org/3.8/library/argparse.html

# https://github.com/myshy93/Training-Python-Intermediate/blob/master/Lecture%204/Lecture%204.ipynb

# https://docs.python.org/3.8/library/index.html