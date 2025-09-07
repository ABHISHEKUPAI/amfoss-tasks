with open("input.txt", "r") as f:
    n = int(f.read().strip()) 

for i in range(1, n + 1):
    spaces = " " * (n - i)

    if i == 1:
        print(spaces + "*")
    elif i == n:
        print("*" * (2 * n - 1))
    else:
        inner_spaces = " " * (2 * i - 3)
        print(spaces + "*" + inner_spaces + "*")