# Define String.prototype.toAlternatingCase (or a similar function/method such as to_alternating_case/toAlternatingCase/ToAlternatingCase in your selected language; see the initial solution for details) such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase. For example:
def to_alternating_case(string):
    s=""
    for i in string:
        if i.isupper:
            s+=i.lower()
        else:
            s+=i.upper()
    return s 
print(to_alternating_case("I loVE yOu,MISS YOU"))

        