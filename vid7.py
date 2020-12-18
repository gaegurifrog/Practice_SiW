o# -*- coding: utf-8 -*-

#%%
import re,random

a_list=[1,2,3,3,3,4,5,6]
a_set={1,1,1,10,20,30}


print("found it!") if re.search('p', 'Python') else print("couldn't find it")

print("found it!") if re.search('p', 'Python', re.I) else print("couldn't find it")

#%%

birth_years={'John':1988,'Bob':1997, 'George':2003}

#%%
class StudentInfo:
    """Basic information about a student"""
    
    def __init__(self, name,id,major=""):
        self.name=name
        self.id=id
        self.major=major

    def get_id(self):
        """return the id of the student"""       
        return self.id
 
    def get_name(self):
        """return the student's name"""
        return self.name
    
    def get_major(self):
        """return the students major"""
        return self.major
    
    def set_major(self, major):
        """set the student's major"""
        self.major=major

#%%

for index, value in enumerate(a_list):
    print('Value #%d of A is %d' % (index, value))
    
    
#%%
#Let's write some docstrings for these functions

def roll_dice(num_dice=1, die=range(1,7)):
    """Return a list of num_dice randomly selected elements of the iterable die.
    
    This function simulates rolling dice; therefore the elements are selected with replacement. 
    num_dice is an integer representing the number of dice we want to roll.
    die is an iterable that the function selects from. By default, it is a 6-sided standard die.
    
    """
    
    return random.choices(die, k=num_dice)



#%%


def shuffle_string(s):
    """Returns a string in which the order of the characters in the string s have been rearranged.
    
    s is any string, and the function will randomly change the order of these characters and return it as a new string.
    
    """

    
    shuffle_order=[x for x in range(len(s))]
    random.shuffle(shuffle_order)
    return ''.join([s[i] for i in shuffle_order])




















