#Set

## Immutable vs Hasable
All immutable objects are hashable, but not the other way around

### Immutable

- Tuples
- Strings
- Integers
- Booleans

## Functions
.union()
- x1.union(x2, [, x3...])
- x1 | s2 [|x3...]
.intersection()
- a.intersection(b,c,d)
.difference()
.symmetric_difference() or ^
.disjoint() : common elements or not 
.issubset() : 
.remove()
.add()
.discard() : won't raise error if there elem doesn't exist
.pop()
.clear()
.update()
.intersection_update() : &= 



# Generator
next()

```
>>> g = (x for x in [1, 2, 3])
>>> g
<generator object>
>>> next(g)
1
>>> next(g)
2
>>> next(g)
3
>>> next(g)
StopIteration
```