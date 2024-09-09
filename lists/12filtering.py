#Another common functional-style programming operation is filtering elements to select only those that match a condition.
# Typically produces a list with fewer elements than the data being filtered.
list4 = [item for item in range(1, 11) if item % 2 == 0]
