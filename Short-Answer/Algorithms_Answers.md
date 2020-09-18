#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
```
a = 0
while (a < n * n * n):
    a = a + n * n
```

The time complexity would be O(n) (linear).
The loop runs linear to the input size "n".
n^3/n^2 

b)
```
sum = 0
for i in range(n):
    j = 1
    while j < n:
        j *= 2
        sum += 1
```

The time complexity is O(n log(n)) (Linearithmic)
The for loop is O(n) and while loop is O(log n) - this is because j is incremented *2 each time, halving the computation time.

c)
```
def bunnyEars(bunnies):
    if bunnies == 0:
        return 0

    return 2 + bunnyEars(bunnies-1)
```

Runtime here is O(n) (linear) because the number of times bunnyEars runs is directly proportional to the quantity of input bunnies.
1 recursive call, reducing the input by 1 each call.


## Exercise II
```
Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.
```

Instead of checking every floor, we can start at the middle floor and narrow down the options from there. This is how binary search works, which has a runtime complexity of O(log n) (Logarithmic)

If there's 10 floors, we don't need to manually go one by one. We can start a floor 5 (midpoint). Then we can drop it from there. If it breaks, we're too high. So we can narrow down to the lower floors. If it doesn't break, we can focus on the higher floors.

In other words, we compare the "target value" to the "midpoint" like in our previous binary search problems. We are using the midpoint as a way to determine if we should focus up or focus down. And keep finding the next midpoint and doing the same process until we get the exact target value (in this case, the optimal floor).





