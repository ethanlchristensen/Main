# LEET CODE 

def checkIfExist(arr):
    for i in range(len(arr)):
        for j in range(i +  1, len(arr)):
            print("CHECK --> {} <-> {}".format(arr[i], arr[j]))
            if arr[i] * 2 == arr[j] or arr[i] / 2 == arr[j]:
                return True
    return False
    
nums = [10, 2, 5, 3]
print(checkIfExist(nums))
nums = [3, 1, 7, 11]
print(checkIfExist(nums))