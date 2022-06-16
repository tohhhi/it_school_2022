magic_numbers = {1, 44, 3, 23, 2, 33}
wrong_numbers = {88, 22, 34, 44}



print(magic_numbers)


#magic_numbers.update([1, 2, 3, 99])

intersection = magic_numbers.intersection(wrong_numbers)
difference = magic_numbers.difference(wrong_numbers)


print(magic_numbers)
print(intersection)
print(difference)