def quickSort( sequence ):
    length = len(sequence)
    if length == 0 or length == 1:
        return sequence
     
    pivot = sequence[len(sequence)//2] #middle of sequence
    under = []
    equal = []
    over = []
    for i in sequence:
        if i < pivot:
            under.append(i)
        elif i > pivot:
            over.append(i)
        else: 
            #if i == pivot:
            equal.append(i)

    sortedUnder = quickSort(under)
    sortedOver = quickSort(over)
    
    finale = sortedUnder + equal + sortedOver

    return finale

list = ["coventry", "birmingham", "leicester", "london", "exeter"]
print(quickSort(list))