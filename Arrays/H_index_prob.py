# we are given an array of positive integers representing the amount of citations per article
# for example [1,2,3,2,4,1,6,10] with first article being cited 1 time and the last one 10 times
# we want to get the h-index counting the number of publications for which an author has been 
#cited by other authors at least that same number of times

given_array = [1,4,1,4,2,1,3,5,6]

hashmap = {}

for i in given_array:
    if i not in hashmap:
        hashmap[i] = 1
    else:
        hashmap[i] += 1
    
print(hashmap)

