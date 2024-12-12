even_ints = [2, 4, 6, 8, 10,]
odd_ints = [1, 3, 5, 7, 9]

for num in even_ints:
    print("even")
    print(num)
for num in odd_ints:
    print("odd")
    print(num)
total = sum(even_ints + odd_ints)
print("the sum is:")
print(total)