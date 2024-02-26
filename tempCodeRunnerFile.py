def sum_list(numbers):
    sum=0
    for i in numbers:
        if i%2==0:
            sum+=i
    print(sum)
           
numbers=input("Enter the numbers into : ").split(',')
sum_list(numbers)
        