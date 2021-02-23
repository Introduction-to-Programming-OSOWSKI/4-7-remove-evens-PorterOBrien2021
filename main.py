def removeEvens(x):
    total = x
    numpopped = 0
    for i in range(0, len(x)):
        if total[i - numpopped] % 2 == 0 and total[i - numpopped] != 0:
            total.pop(i - numpopped)
            numpopped = numpopped + 1

    return total



print(removeEvens([1, 2, 2, 3, 4]))
