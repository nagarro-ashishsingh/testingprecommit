def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()


# Change the number of rows as needed
num_rows = 5
print_pattern(num_rows)
