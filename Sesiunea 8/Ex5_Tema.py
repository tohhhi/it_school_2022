#8) Make a function to remove all the element with a maximal value from a list; return a new list (original list does not modify)
#9) Make a function for printing the first 5 longest strings in a list ; (len("test"))
#10) Make a function to check if the elements of a lists are equals (without using for) -> return bool



cfr = ["petrescu", "omrani", "debeljiuc", "boateng", "deac" , "petrila", "grahovac"]

def longest_strings (lst) :
    def len_is (string):
        return len(string)

    lst.sort(key=len_is, reverse=True)
    print (lst[:5])

longest_strings (cfr)


