#Comparing the speed of searching lists vs. dictionaries.

# Introduction #

For things like listing the abilities a player had I decided to switch from using "if x in list" to "if x in dictionary" even if the dictionary is simply the key with a value of None.

I tested this by seeding a list and a dictionary with the same 10,000 random keys and profiling 10,000 lookups.


## Integers ##

  * 10,000 searches using "X in list" took **5.552706** seconds.
  * 10,000 searches using "dictionary.has\_key(X)" took **0.005892** seconds.
  * 10,000 searches using "X in dictionary" took **0.004039** seconds.

## Floats ##

  * 10,000 searches using "X in list" took **5.849660** seconds.
  * 10,000 searches using "dictionary.has\_key(X)" took **0.007736** seconds.
  * 10,000 searches using "X in dictionary" took **0.005855** seconds.

## Strings (3 - 19 characters each) ##

  * 10,000 searches using "X in list" took **4.114208** seconds.
  * 10,000 searches using "dictionary.has\_key(X)" took **0.005970** seconds.
  * 10,000 searches using "X in dictionary" took **0.004010** seconds.

I honestly didn't expect strings to perform as well as they did, which is encouraging because I'll be using them as keys throughout the code.