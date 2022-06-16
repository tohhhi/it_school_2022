numbers_1 = {5, 7, 10, 24, 25}

numbers_2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 25}


update_numbers = numbers_2.update(numbers_1)

intersection_numbers = numbers_2.intersection(numbers_1)

difference_numbers = numbers_2.difference(numbers_1)

print(update_numbers)

print("-" * 10)

print(intersection_numbers)

print("-" * 10)

print(difference_numbers)