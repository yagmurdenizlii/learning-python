
def search(list, number, index):

    if len(list) > 1:
        mid = (len(list) // 2)  #floor division
    else: 
        mid = 0

    if mid != 0:
        if list[mid] == number:
            return mid + index
        elif list[mid] > number:
            first_half = list[0:mid]
            return search(first_half, number, index)
        else:
            second_half = list[mid + 1:]
            return search(second_half, number, index + mid + 1)
    else:
        if list[mid] == number:
            return index
        elif len(list) > 1:
            if list[mid + 1] == number:
                return index + 1
        else:
            print('Number is not in the list.')
            return None

num = search([1,2,3,4,5,7,9,11], 7, 0)
print(num)








