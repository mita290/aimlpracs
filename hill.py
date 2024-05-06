import random

def hill_climb(max_iter,step_size,objectiveFunction):
    current_state=random.uniform(-10,10)
    for _ in range(max_iter):
        next_state=current_state+random.uniform(-step_size,step_size)
        if objectiveFunction(current_state)<=objectiveFunction(next_state):
            current_state=next_state
    return current_state

def objectiveFunction(x):
    return -x**2

if __name__ =="__main__":
    max_iter=1000
    step_size=0.1
    result=hill_climb(max_iter,step_size,objectiveFunction)
    print(f"Maximum value found: {objectiveFunction(result)} at x={result}")