def in_range(num):
    if num in range(10,101):
        return True
    
    return False

print(in_range(42))
print(in_range(100))
print(in_range(101))