def prime_gen(max_num):
    prime_list      = [3]
    n               = 0

    while max_num > prime_list[-1]:                         
        if prime_list[-1] % prime_list[n] != 0:
            n += 1
            if prime_list[-1] == prime_list[n] or (prime_list[-1] / prime_list[n]) < prime_list[n]: #Equilbrium factor
                prime_list.append(prime_list[-1]+2)
                n = 0
                continue 
        else:
            if prime_list[-1] == prime_list[n] or (prime_list[-1] / prime_list[n]) < prime_list[n]:       
                prime_list.append(prime_list[-1]+2)
                n = 0
                continue
            else: 
                prime_list.append(prime_list[-1]+2)
                prime_list.pop(-2)
                n = 0
    prime_list.insert(0, 2)
    print(prime_list)
    # print([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149])
# prime_gen(3, 1000000000)
print("welcome to the python prime  number gen")
print("This prolly won't be updated for quite some time, just wanted it on the cloud in case I lose it")
print("")
prime_input_number = int(input("Please enter your value to which you want the primes until: "))
prime_gen(prime_input_number)
print("-------------------------------------------------")
print("Note the last number tends to sometimes not be prime, not sure if I fixed it or not lmao")

# Last number seems to not work as intended unless it is prime
# Need to a create equilibrium factor for larger numbers

# Don't use for loops as the number of items intergers within the list will constantly increase
