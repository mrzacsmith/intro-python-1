# Print out 2 to the 65536 power
# (try doing the same thing in the JS console and see what it outputs)

# YOUR CODE HERE
power = 65536
answer = (2 ** power)

print(f'The answer is {answer}')
print(f'The total number of digits in 2 ** {power} is {len(str(abs(answer)))}')