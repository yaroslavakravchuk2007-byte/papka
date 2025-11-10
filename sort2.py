def swimmers_pianists_not_french(french, swimmers, pianists):
   
    french_set = {int(x) for x in french.split()}
    swimmers_set = {int(x) for x in swimmers.split()}
    pianists_set = {int(x) for x in pianists.split()}

    result = (swimmers_set & pianists_set) - french_set
    return sorted(result)



french = "1 2 5 7 8 9"
swimmers = "3 4 8 2 10"
pianists = "10 3 2 8 5"

result = swimmers_pianists_not_french(french, swimmers, pianists)
print(" ".join(map(str, result))) 