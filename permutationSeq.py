def get_permutation(n, k):
    numbers = []
    fact = 1

    # Prepare numbers list and factorial
    for i in range(1, n + 1):
        numbers.append(i)
        fact *= i

    k -= 1  
    result = ""

    for i in range(n):
        fact //= (n - i)
        index = k // fact

        result += str(numbers[index])
        numbers.pop(index)
        k %= fact

    return result

# Example usage:
print(get_permutation(3, 3))   
print(get_permutation(4, 9))   
print(get_permutation(1, 1))   
print(get_permutation(3, 6))   
print(get_permutation(4, 1))  