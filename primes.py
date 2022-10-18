#List of prime numbers generator.
#ENTER YOUR SOLUTION HERE!

def primes(number_of_primes):
    list = [2]
    i =3
    while len(list) < number_of_primes:
        prime = True
        for j in list:
            if i % j == 0:
                prime = False
                break
        if prime:
            #print(i)
            list.append(i)
    print(list)
    return list


primes (2)