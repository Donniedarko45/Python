"""WAP to input a list of scores for N students in a list data type. Find the score of the
runner-up and print the output.
Sample Input
N = 5
Scores= 2 3 6 6 5
Sample output
5
Note: Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is 5.
Hence, we print 5 as the runner-up score."""

l=[]
n=int(input("enter how many students are participating: "))
for i in range(n):
    num=int(input("enter score of student {}:".format(i+1)))
    l.append(num)

l=sorted(l)
max_scores=l[-1]

for i in range(n-2,-1,-1):
    if(l[i]!=max_scores):
        second_max=l[i]
        break
print("second max is: {}".format(second_max))


