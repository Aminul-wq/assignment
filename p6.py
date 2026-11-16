def multiplication(one,two):
    multi = one*two
    return multi
result = multiplication(5,25)

print(result)


# checking prime number

def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if i%n == 0:
            return False
    return True

print(is_prime(13))
print(is_prime(89))
print(is_prime(1))