# Fibonacci test

a, b = 0, 1
n = 15
fibonacci_sequence = []

for _ in range(n):
    print(a, end=' ')
    fibonacci_sequence.append(a)
    a, b = b, a + b
print()
print("Fibonacci sequence:", fibonacci_sequence)



# Code for simple Additive Random Walk:
import random

num_steps = 15
position = 0
trajectory = [position]

for _ in range(num_steps):              
    
    step = random.choice([-1, 1])
    temp_position = position
    position += step
    
    trajectory.append(position)
print("Random walk trajectory:", trajectory)



# Compare with Multiplicative Random Walk, log y axis:

# 100 Time steps, 100 trajectories:
num_steps2 = 100
num_simulations = 100
all_trajectories = []

for _ in range(num_simulations):
    position2 = 1
    trajectory2 = [position2]

    for _ in range(num_steps2):

        step2 = random.choice([0.6, 1.5])       # Weights
        temp_position2 = position2
        position2 *= step2                      # Multiplicative Dynamic
        trajectory2.append(position2)

    all_trajectories.append(trajectory2)
# optional: print("Random walk trajectory 2:", trajectory2)

# Plotting the trajectories to show surprising result:
# Despite positive expectation value, negative divergence.

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))

for trajectory in all_trajectories:
    plt.plot(trajectory, alpha=0.6)  # Plot each trajectory with some transparency


plt.yscale('log')

plt.title('Random Walk Trajectories (Logarithmic Scale)')
plt.xlabel('Step')
plt.ylabel('Position (log scale)')

plt.show()



