def no_of_tens(amount):
    count=0
    if(amount<10):
        return amount,count
    while(1):
        if(amount<10):
            return amount,count
        amount-=10
        count+=1
def no_of_fives(amount):
    count=0
    if(amount<5):
        return amount,count
    while(1):
        if(amount<5):
            return amount,count
        amount-=5
        count+=1

def no_of_twos(amount):
    count=0
    if(amount<2):
        return amount,count
    while(1):
        if(amount<2):
            return amount,count
        amount-=2
        count+=1

def no_of_ones(amount):
    count=0
    if(amount<1):
        return amount,count
    while(1):
        if(amount<1):
            return amount,count
        amount-=1
        count+=1

amount=int(input("Enter the Bill Amount:"))
if(amount<0):
    print('Invalid Amount')
result10,tens_count=no_of_tens(amount)
result5,fives_count=no_of_fives(result10)
result2,twos_count=no_of_twos(result5)
result1,ones_count=no_of_ones(result2)
total_coin=thousand_count+five_hundered_count+hundered_count+fifties_count+tens_count+fives_count+twos_count+ones_count
print('The Amount to be paid is:',amount)
print('Total number of Notes/coins required is:',total_coin)
print('Number of Tens Notes Required is:',tens_count)
print('Number of Fives Required is:',fives_count)
print('Number of twos Required is:',twos_count)
print('Number of ones Required is:',ones_count)
