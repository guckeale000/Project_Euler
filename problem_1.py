# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


if __name__ == '__main__':
    upto = 1000
    valid_increments = (3, 5)
    s = sum(sum(x for x in range(0, upto, y)) for y in valid_increments)
    print(s) # 266333
