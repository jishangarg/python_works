import random
def my_guess():
    return list(input("-Guess a 3 digit no. with non-repeating digits "))

def generate_code():
    digit=[]
    for num in range(10):
        digit.append(str(num))
    random.shuffle(digit)
    if digit[0]=='0':
        digit[0]=digit[9]
    return digit[:3]
    #return ['4','5','6']

def comparision(secret_code,guess):
    if len(guess)!=len(secret_code) or ord(guess[0])<ord('0') or ord(guess[0])>ord('9') or ord(guess[1])<ord('0') or ord(guess[1])>ord('9') or ord(guess[2])<ord('0') or ord(guess[2])>ord('9'):
        return '**Invalid guess ! Dont\'t u know d meaning of 3 digit no. !'
    if guess[0]=='0' and guess[1]=='0' and guess[2]=='0':
        return '**Hey Kid! This is just ZERO, Not a 3 digit no.'
    elif guess[0]=='0' and guess[1]=='0':
        return '**Hey Kid! This is single digit no. , Not a 3 digit no.'
    elif guess[0]=='0':
        return '**Hey Kid! This is two digit no. , Not a 3 digit no.'

    if guess[0]==guess[1] or guess[0]==guess[2] or guess[1]==guess[2]:
        return '**Bro read carefully! All digits should be distinct'
    if secret_code==guess:
        return 'H U R R A Y ! CODE CRACKED !'
    clue=[]

    for ind,num in enumerate(guess):
        if secret_code[ind]==num:
            clue.append('match')
        elif num in secret_code:
            clue.append('close')

    if clue==[]:
        return ['Nope']
    else:
        return clue

print("Hare Krishna everyone and Welcome to code Breaker !")
secret_code=generate_code()
guess='1'
count=0
while guess!=secret_code:
    guess=my_guess()
    count+=1
    print('Status of ur guess: ')
    clue_arr=comparision(secret_code,guess)
    if(type('rr')==type(clue_arr)):
        print(clue_arr)
    else:
        for clue in clue_arr:
            print(clue)

print('u took {x} turns to guess correctly'.format(x=count))

