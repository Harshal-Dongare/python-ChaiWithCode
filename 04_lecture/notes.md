# Immutable Objects:

When you define an immutable object, like an integer (`x = 10`), the value (in this case, `10`) is stored in a specific memory location.
If you reassign x to a new value (`x = 15`), a new memory location is created for the value `15`, and `x` is updated to point to this new location.
The crucial point is that the original memory location holding the value `10` is unchanged. The value itself cannot be modified; instead, a new value and memory location are created.

# Mutable Objects:

In contrast, mutable objects like lists or dictionaries allow modifications to their internal state. If you change an element in a list, for example, the same memory location is used, and the object's state is altered.

![image](./Screenshot%202024-01-31%20201656.jpg)