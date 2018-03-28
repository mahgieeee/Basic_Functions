# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 13:11:57 2018

@author: tangerineworld
"""

#use a dictionary to keep track of repeated tuples
def pairs(input):
    """input is a list of ints; output is a list of unique tuple pairs"""
    unique_pairs = {}
    next_x = 1
    
    # start creating tuple from left to right, creating (keys,values) in a dictionary
    # the last item on the list won't be part of a unique pair
    for x in input[ :len(input)-1]:
        unique_pairs[x] = input[next_x:len(input)]
        next_x = next_x + 1
        
    # put the tuples in a list and return the list
    unique_tuples = []
    for key, values in unique_pairs.items():
        print (key)
        for numbers in values:
            print ("num: ", numbers)
            #return (key, numbers)
            if (key, numbers) not in unique_tuples: # no repeat
                unique_tuples.append((key, numbers))
            
    return unique_tuples

# check for nonequal in the list first, if num_nonequal > 1 return False
# can't have more than four of the same kind if num_nonequal == 0 return False
def is_four_of_kind(hand):
    """hand is a list of 5 strings representing card ranks; function is a predicate"""
    count = 0
    next_x = 1
    for x in hand:
        x = x.upper()
        if x not in hand[next_x:len(hand)]: #other than itself
            print (x)
            count = count + 1 # number of unique strings in the hand
        next_x = next_x + 1
        
    if count > 1 or count == 0:
        return False
    else:
        return True
    
def merge(a, b):
    """a and b are sorted list of ints; function returns array of sorted ints"""
    index_a = 0
    index_b = 0
    merged_list = []
    
    while index_a < len(a) and index_b < len(b):
        if a[index_a] <= b[index_b]:
            merged_list.append(a[index_a])
            index_a = index_a + 1
        else:
            merged_list.append(b[index_b])
            index_b = index_b + 1
             
        #reach to the end of the list in either a/b, attach the rest to merged list    
        if index_a > len(a)-1: 
            merged_list.extend(b[index_b: ])

        if index_b > len(b)-1: 
            merged_list.extend(a[index_a: ]) 
                
    print (merged_list)
    # Solution goes here
    
def dec_to_base_x(base, num):
    """function that converts base 10 number to a number of base from 2 to 9"""
    for x in range(8):
        if num - (base**x) > 0:
            # get the min starting exponent for each base
            start_exp = x 
            
    num_count = []
    while start_exp >= 0:
        count = 0 
        while num - base**start_exp >= 0:
            num = num - base**start_exp
            count = count + 1
            print(num)
        num_count.append(count)
            
        start_exp = start_exp - 1

    print (num_count)    
         
    # Solution goes here
    
if __name__ == '__main__':
    #print(pairs([8, 8, 8, 8, 8]))
    #print(is_four_of_kind(["K","Q","Q","K","K"]))
    #merge([1, 3, 5, 10], [2, 4, 4, 6, 8])
    dec_to_base_x(8, 140)
    #dec_to_base_x(2, 8) 