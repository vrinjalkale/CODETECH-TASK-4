from pulp import *

# Create the problem
model = LpProblem("MaximizeProfit", LpMaximize)

# Decision variables
A = LpVariable("ProductA", lowBound=0)
B = LpVariable("ProductB", lowBound=0)

# Objective function
model += 40*A + 30*B

# Constraints
model += 2*A + 1*B <= 100   # labor hours
model += A + 2*B <= 80      # machine hours

# Solve
model.solve()

# Output
print("Status:", LpStatus[model.status])
print("Product A:", A.varValue)
print("Product B:", B.varValue)
print("Maximum Profit =", value(model.objective))