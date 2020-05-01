#input_array = [3, 6, -2, -5, 7, 3]
input_array = [-23, 4, -3, 8, -12]

def adjacentElementsProduct(inputArray):
    maxProduct = -10000000000
    for i in range(len(inputArray)-1):
        maxProduct = max(maxProduct, inputArray[i] * inputArray[i+1])
    return  maxProduct

print(adjacentElementsProduct(input_array))