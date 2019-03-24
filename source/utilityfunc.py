# File containing support functions for Pycrypto

import time
def primegen(num_range):
    width = num_range

    print("Width=", width)
    counter = 0
    num_list = []
    start_time = time.time()
    for i in range (3, width+1, 2):
        num_list.append(i)

    for prime in num_list:

        counter+=1
        for multiplyer in num_list[num_list.index(prime):]:

            try:
                num_list.remove(prime*multiplyer)
            except:
                if prime*multiplyer > width:
                    break
                print("Redundant!!!!!!!!!!!!!!!!!!!!!!1", multiplyer, " ", prime)
    num_list.insert(0, 2)
    print("--- %s seconds ---" % (time.time() - start_time))
    return num_list
