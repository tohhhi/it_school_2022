import os

file_descriptor = open("c:/Users/tohan/Desktop/IT-SCHOOL/Sesiunea 20/practice.txt")


file_descriptor.seek(10, os.SEEK_END)


file_descriptor.close()