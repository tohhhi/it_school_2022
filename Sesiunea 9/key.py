cfr = ["petrescu", "omrani", "debeljiuc", "boateng", "deac" , "petrila", "grahovac"]

def longest_strings (lst) :
    def len_is (string):
        return len(string)

    lst.sort(key=len_is, reverse=True)
    print (lst[:5])

longest_strings (cfr)