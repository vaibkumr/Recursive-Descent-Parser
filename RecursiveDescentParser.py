import sys

"""
Recursive Descent Parser by TimeTraveller :
- It supports floating point numbers
- It supports operations: +, *, ^
- It uses the following grammar:
    E -> E+T|T
    T -> T*F|F
    F -> G^F|G
    G -> numberG|number.Q|number
    Q -> numberQ|epsilon

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
"""

class RDP():
    def __init__(self):
        self.loc = 0
        self.string = None

    def check(self, elem):
        if (elem == 'digit'and self.string[self.loc].isdigit()) or\
                        self.string[self.loc] == elem:
                        return True
        return False

    def match(self, elem):
        if (elem == 'digit'and self.string[self.loc].isdigit()) or\
                        self.string[self.loc] == elem:
                        self.loc += 1
        else:
            print("Parse error")
            sys.exit(0)

    def parse(self, string):
        if not string:
            return "Can't parse"
        string += "$"
        self.string = string
        self.E()
        if(self.string[self.loc]=='$'):
            return "Successful!"
        else:
            return "Can't parse"

    def E(self):
       self.T()
       self.E_prime()

    def E_prime(self):
        if self.check('+'):
            self.match('+')
            self.T()
            self.E_prime()
        else:
           return

    def T(self):
        self.F()
        self.T_prime()

    def T_prime(self):
        if self.check('*'):
            self.match('*')
            self.F()
            self.T_prime()
        else:
            return

    def F(self):
        self.G()
        self.K()

    def K(self):
        if self.check('^'):
            self.match('^')
            self.F()
        else:
           return

    def G(self):
        if self.check('digit'):
            self.match('digit')
            self.R()
        else:
            self.match("Error")

    def R(self):
        if self.check('.'):
            self.match('.')
            self.S()
            return
        else:
            self.S()

    def S(self):
        if self.check('digit'):
            self.match('digit')
            self.S()
            return
        else:
            return


if __name__ == "__main__":
    obj = RDP()
    result = obj.parse("2.817*1.1+0.901820938^9.98912")
    print(result)
