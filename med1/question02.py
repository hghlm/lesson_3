def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

print(factors(-2))
print(factors(0))
print(factors(5))
print(factors(10))
print(factors(20))

print("number % divisor == 0 determines if number is factor")