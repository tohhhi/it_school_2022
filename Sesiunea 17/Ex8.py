# 8) Using commit variable, print short-version commit number (11 chars) alongside username

commit = """commit 30c06bce50eeb7a8856e18df2dc64e76fec14cc9
Author: Dinu Mihai <mihai.dinu93@gmail.com>
Date:   Thu Jun 9 18:18:02 2022 +0300
    shuffle method"""


commit_number = commit[7:18]


user_name = commit.split()[4] + " " +commit.split()[3] 

print(f"{commit_number} {user_name}")