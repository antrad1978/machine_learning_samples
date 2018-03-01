#Find the mean, median, and range for the following list of values:
#4,7,9,3,5,10,12,18

def median(list):
    sorted = sorted(list)
    lenght = len(list)
    index = (lenght - 1) // 2

    if (lenght % 2):
        return sorted[index]
    else:
        return (sorted[index] + sorted[index + 1])/2.0

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

def range(list):
    sorted = sorted(list)
    length = len(sorted)
    if (length>0):
        return sorted[length-1] - sorted[0]

numbers=[4,7,9,3,5,10,12,18]

numbers_tuple=(4,7,9,3,5,10,12,18)

res1 = median(numbers)

print(res1)

res2=mean(numbers)

print(res2)

res3 = median(numbers_tuple)

print(res3)

res4 = range(numbers_tuple)

print(res4)