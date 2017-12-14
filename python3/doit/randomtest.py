import random as rd

def random_pop(data):
    number = rd.randint(0,len(data)-1)
    return data.pop(number)

def random_pop_choice(data):
    number = rd.choice(data)
    data.remove(number)
    return number

if __name__ == "__main__":
    data = [1,2,3,4,5]
    while data:
        print(random_pop(data))
    
    data2 = [6,7,8,9,10]
    print(random_pop_choice(data2))

    data3 = ['a','b','c','d','e']
    rd.shuffle(data3)
    print(data3)