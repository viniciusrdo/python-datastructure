listOne = [3, 6, 9, 12, 15, 18, 21]

listTwo = [4, 8, 12, 16, 20, 24, 28]



list_x = [listOne,listTwo]

listFinal = [0]

#for eachList in list_x:

count = 0

for eachValue in listOne:
    if int(listOne.index(eachValue)) % 2 != 0:
        listFinal =  listFinal.append(eachValue)   
        
       # print ('eachList = ' , eachList)
       # print ('eachValue = ' , eachValue)

print (listFinal)