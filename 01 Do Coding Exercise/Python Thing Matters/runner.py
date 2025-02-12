if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    
    # Find the maximum score
    max_score = max(arr)
    
    # Remove all occurrences of the maximum score
    arr = [x for x in arr if x != max_score]
    # [expression(x) for item(x) in iterable(arr) if condition(x != max_score)]
    """
    EXAMPLE:
    arr = [2, 3, 6, 6, 5] and max_score = 6.

    list comprehension [x for x in arr if x != 6] will iterate over each element in arr:
        For x = 2, the condition 2 != 6 is true, so 2 is included.
        For x = 3, the condition 3 != 6 is true, so 3 is included.
        For x = 6, the condition 6 != 6 is false, so 6 is excluded.
        For x = 6, the condition 6 != 6 is false, so 6 is excluded.
        For x = 5, the condition 5 != 6 is true, so 5 is included.
        
        The resulting list will be [2, 3, 5]
    """
    
    # Find the new maximum, which is the runner-up score
    runner_up_score = max(arr)
    
    print(runner_up_score)
