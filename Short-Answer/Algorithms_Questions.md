# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):
      a = a + n * n
```


```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1
```

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.


if n = the amount of floors
if f = max non-breaking point
find the pivot/half point n//2
bottom floors and top floors
if dropped egg breaks from pivot (=True)
find pivot point of bottom floors
bottom floors and top floors
if dropped egg breaks from this pivot (=True) repeat the pivot process
if dropped egg does NOT break from pivot(=False)
  increase floor by 1
    if dropped egg breaks there, prior floor was f
    if dropped egg does NOT break, repeat the increase floor

  OR (probably better)
  test upper floor and pivot and repeat until you have one floor left that floor will be f

