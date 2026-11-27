def count_1324_quadruplets(values: list[int]) -> int:
    """Count i<j<k<l with values[i]<values[k]<values[j]<values[l]; no mutation."""
    triplets = [0]*len(values)
    answer = 0
    for last, value in enumerate(values):
        smaller = 0
        for middle in range(last):
            if values[middle] < value:
                answer += triplets[middle]
                smaller += 1
            elif values[middle] > value:
                triplets[middle] += smaller
    return answer
