# 2) Remove all the items from months dict with value greater then 6




months = {
'January': 1,
'February': 2,
'April': 4,
'May': 5,
'March': 3,
'October': 10,
'July': 7,
'August': 8,
'June': 6,
'September': 9,
'November': 11,
'December': 12
}

           
def trim_by_six(dictionary):
    for keys in list(dictionary.keys()):
        if dictionary[keys] > 6:
            del dictionary[keys]
    print(dictionary)
    
    

trim_by_six(months)


