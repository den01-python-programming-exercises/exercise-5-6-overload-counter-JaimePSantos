# Exercise 5.6 Overload counter

## Multiple constructors

Implement a class called `Counter`. The class contains a number whose value can be incremented and decremented. The class must have the following constructor:

-  `def __init__(self, start_value)` which sets the start value of the counter to 0.

overloaded with a `@classmethod`:

-  `def with_start_value(cls, start_value)` to set the start value of the counter to start_value.

And the following methods:

- `def value()` returns the current value of the counter
- `def increase()` increases the value by 1
- `def decrease()` decreases the value by 1

## Alternative methods

Implement versions which are given one parameter of the methods `increase` and `decrease`.

 - `def increase(self, increase_by)` increases the value of the counter by the value of increase_by. If the value of increase_by is negative, the value of the counter does not change.

 -  `def decrease(self, decrease_by)` decreases the value of the counter by the value of decrease_by. If the value of decrease_by is negative, the  value of the counter does not change.
