



file_descriptor = open("C:\\Users\\tohan\\Desktop\\IT-SCHOOL\\practice_files\\practice.txt")


content = file_descriptor.readlines()



file_descriptor.close()

# print(content[0])

first = "".join(content[0])
two = "".join(content[2])
three = "".join(content[4])

print(type(first))

# write to output.txt

write_to_file = open("C:\\Users\\tohan\Desktop\\IT-SCHOOL\\practice_files\\output.txt","w")

write = write_to_file.write(first)
write = write_to_file.write(two)
write = write_to_file.write(three)

write_to_file.close()


