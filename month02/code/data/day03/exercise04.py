def serch(list_,num):
    low,high = 0,len(list_) - 1
    while low <= high:
        mid = (low+high) //2
        mid_value = list_[mid]
        if list_[mid] > num:
            high = mid-1
        elif list_[mid]< num:
            low = mid+1
        else:
            return mid




l = [1,2,3,4,5,6,7,8,9]
print(serch(l,8))