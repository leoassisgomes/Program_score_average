# Program that calculates an average

# Here is the algorithm:

# 1. get the first test score.
# 2. get the second test score.
# 3. get the third test score.
# 4. calculate the average by adding the three test scores and dividing the sum by 3.
# 5. display the average.

# Get three test scores and assign them to the 

# test1, test2, and test3 variables

test1 = float(input('Enter the first test score: '))

test2 = float(input('Enter the second test score: '))

test3 = float(input('Enter the third test score: '))


# calculate the average of the three scores and assign the result to the average variable

average = (test1 + test2 + test3) // 3.0	

# display avarage

print('The average score is ', average)
