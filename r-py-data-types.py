#installed packages
import numpy as np
import pandas as pd

#py_install("numpy")
#py_install("pandas")

teddy = [1,2,8]
teddy_vec = np.array(teddy)
teddy_vec

type(teddy_vec)

#a list is mutable - can change it directly
teddy[1] = 1000
teddy

#a tuple is immutable - cant change
khora = (1,5,12)
type(khora)

# khora[1] = 16 Nope

waffle = [["cat", "dog", "penguin"], 2,"a burrito", [1,2,5]]

waffle

# Access an element from the list waffle:
waffle[0] #default just returns that piece (not as a list)

#we can reassign piece of a list:

waffle[1] = "AN EXTRAVAGANZA""
waffle

#Make a pandas DataFrame in python
# rst, a dictionary example
fox = {'sound' : ["screech", "squel", "bark"], 'age' : [2,6,10]}

fox['sound']

fox['age']

cows = {'name' : ["moo", "spots", "happy"], 'location': ["pasture","prairie", "barn"], 'height' :[5.7, 5.4, 4.9]}

cows_df = pd.DataFrame(cows)



















