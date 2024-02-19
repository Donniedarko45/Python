#Scan n values in range 0-3 and print the number of times each value has occurred.
n = int(input("enter total number of numbers you want to enter: "))
s = []
for i in range(n):
    num = int(input("Enter number: "))
    s.append(num)

count = [0,0,0,0] # 0 se 3 tak total 4 number honge isliye 0,0,0,0 count initialised kr diya hai count mtlb 0 -> 0 baar 1->0 baar 2->0 baar and 3->0 baar

# Counting occurrences of numbers in the range 0 to 3
for i in s:
    if 0 <= i <= 3:
        count[i] += 1

for i in range(4):
    print("Number", i, "occurred", count[i], "times.")
