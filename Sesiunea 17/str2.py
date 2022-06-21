list1 = ['a', 'b', 'c']
# vrem sa obtinem a>b>c
# sau a_b_c

# join

# \ = escape character
new_str = ">".join(list1)

# c-b-a
new_str2 = "-".join(reversed(list1))
print(new_str2)

