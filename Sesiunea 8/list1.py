leader_board = ['Alex', 'George', 'Ionut']
# leader_board = list()

print(type(leader_board))
print(leader_board)

print("-" * 30)

print("Nr castigatori: ", len(leader_board))

print("Locul 1: " , leader_board[0])
#print("Ultimul loc: " , leader_board[len(leader_board) - 1])
print("Locul 1: " , leader_board[-1])

print("-" * 30)


print("Locul 2 initial:", leader_board[1])

leader_board[1] = "Andrei"
print("Dupa modificare")
print("Locul 2:", leader_board[1])

print(leader_board)


print("-" * 30)

del leader_board[-1]
print("Dupa stergerea ultimului element, lungimea este:", len(leader_board))
print(leader_board)

print("-" * 30)
print("Castigatorii sunt:")
for name in leader_board:
    print(name)



print("STOP")


