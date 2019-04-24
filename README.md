# Recursive Descent Parser
I don't know how did it took me as much as ~2 hours to write this


# Nani?
```
Recursive Descent Parser by TimeTraveller for a certain grammar:
- It supports floating point numbers
- It supports operations: +, *, ^
- It's tailored for the infamous and simple grammar:
    E -> E+T|T
    T -> T*F|F
    F -> G^F|G
    G -> numberG|number.Q|number
    Q -> numberQ|epsilon
*number: Any floating point number. 123. is a valid floating point number. So is 00000.0

Making the grammar compatible for RDP which is a top down parser:
- Remove left recursion
RDP is a top down parser and it can not handle left recursion so we remove the
Left recursion from the above grammar:
    E -> TE'
    E' -> +TE'|epsilon
    T -> FT'
    T' -> *FT'|epsilon
    F -> G^F|G
    G -> numberG|number.Q|epsilon
    Q -> numberQ|epsilon

- Remove non-determinism
Top down parsers also don't like non-determinism so the fixed (deterministic)
productions are:
    E -> TE'
    E' -> +TE'|epsilon
    T -> FT'
    T' -> *FT'|epsilon
    F -> GK
    K -> ^F|epsilon
    G -> numberR
    R -> S|.S
    S -> numberS|epsilon

Learning source: https://www.youtube.com/watch?v=SH5F-rwWEog
```
### I am sleepy
![](https://i.imgur.com/ygA4I7Q.png)


