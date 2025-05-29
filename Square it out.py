def square_and_filter(start, end):
    squares = [x**2 for x in range(start, end + 1)]
    print("Even:", [s for s in squares if s % 2 == 0])
    print("Odd:", [s for s in squares if s % 2 != 0])


square_and_filter(1, 10)
