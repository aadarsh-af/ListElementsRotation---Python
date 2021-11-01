def rightRotate(targetArray, rightRotations):
    """
    Bring the last index to the first one rightRotations times
    """
    for i in range(0,rightRotations):
        targetArray = targetArray[-1:] + targetArray[:-1]
        
    return targetArray[::]
    
def leftRotate(targetArray, leftRotations):
    """
    Bring the 0th index to the last one leftRotations times
    """
    for i in range(0,leftRotations):
        targetArray = targetArray[1:] + targetArray[:-(len(targetArray)-1)]
        
    return targetArray[::]

array = [1,2,3,4,5,6,7,8,9]
rightRotations = 3 
leftRotations = 4 

rightRotate(array, rightRotations) # should print [7,8,9,1,2,3,4,5,6]
leftRotate(array, leftRotations) # should print [5,6,7,8,9,1,2,3,4]
