num =list(map(int,input("enter numbers sapereted by space :").split()))
unique_numbers=list(set(num)) 
if len(unique_numbers) < 2 :
    print("secound largest does not exist")
else :
    unique_numbers.sort()
    print("secound largest number is :",unique_numbers[-2])