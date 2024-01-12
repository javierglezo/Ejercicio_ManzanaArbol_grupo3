#!/bin/python3
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = 0
    orange_count = 0

    for apple_distance in apples:
        apple_position = a + apple_distance
        if s <= apple_position <= t:
            apple_count += 1

    for orange_distance in oranges:
        orange_position = b + orange_distance
        if s <= orange_position <= t:
            orange_count += 1

    print(apple_count)
    print(orange_count)

if __name__ == '__main__':
   if __name__ == '__main__':
    # Leer la primera línea
    first_multiple_input = input().rstrip().split()
    s = int(first_multiple_input[0])
    t = int(first_multiple_input[1])

    # Leer la segunda línea
    second_multiple_input = input().rstrip().split()
    a = int(second_multiple_input[0])
    b = int(second_multiple_input[1])

    # Leer la tercera línea
    third_multiple_input = input().rstrip().split()
    m = int(third_multiple_input[0])
    n = int(third_multiple_input[1])

    # Leer las distancias de las manzanas
    apples = list(map(int, input().rstrip().split()))

    # Leer las distancias de las naranjas
    oranges = list(map(int, input().rstrip().split()))

    # Llamar a la función principal
    countApplesAndOranges(s, t, a, b, apples, oranges)
