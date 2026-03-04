import math

# Use the Gauss-Legendre Algorithm to estimate Pi

pi_estimate = 0

# Step 1: initialize variables
a = 1.0
b = 1.0 / math.sqrt(2.0)
t = 1.0 / 4.0
p = 1.0

# perform 10 iterations
for i in range(1, 11):

    # store old a value
    a_old = a

    # update values
    a = (a_old + b) / 2.0
    b = math.sqrt(a_old * b)
    t = t - p * (a_old - a) ** 2
    p = 2.0 * p

    print("Loop Iteration: ", i)

# Step 3: compute PI estimate
pi_estimate = ((a + b) ** 2) / (4.0 * t)

print("Final estimate for PI: ", pi_estimate)
print("Error on estimate: ", abs(pi_estimate - math.pi))
