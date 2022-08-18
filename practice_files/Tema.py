import csv
import pathlib



with open('C:\\Users\\tohan\\Desktop\\IT-SCHOOL\\practice_files\\salarii.csv') as f:
    cf = csv.reader(f)
    user = []
    for row in cf:
        user.append(f"{row[0]} {row[1]}")
        





# file_descriptor = open("C:\\Users\\tohan\\Desktop\\IT-SCHOOL\\practice_files\\salarii.csv", "r")


# content = file_descriptor.read()


# file_descriptor.close()

# new_string = content.replace(","," ")



# write to output.txt

write_to_file = open("C:\\Users\\tohan\\Desktop\\IT-SCHOOL\\practice_files\\nume.txt","w")

write = write_to_file.writelines('\n'.join(user))





write_to_file.close()
