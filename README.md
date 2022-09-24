# FantasyNomes

FantasyNomes is one python package that able to do operation like add, sub on polynome.
FantasyNomes optimise the memorie space by using dict for store coef and power

    Development Status :: 1 - Beta
    License :: OSI Approved :: Apache Software License
    Natural Language :: English
    Programming Language :: Python
    Programming Language :: Python :: 3.9
    Operating System :: OS Independent
    Intended Audience :: Science/Research
    Topic :: School :: Mathematics :: Polynome


## Features

    - Addition : With int, float or polynome

    - Substraction : 

    - Multiplication :

    - Division euclidienne


## Installation 

```bash
pip install FantasyNomes
```

## Quickstart



```python
>>>import FantasyNomes as fn

>>># x0, x1, x2, ... ,xn

>>>poly1 = fn.Polynome([1,1,2])
>>>poly2 = fn.Polynome([0,1])

>>>poly1
2*X^2+1*X^1+1

>>>print(poly2)
1*X^1

>>>poly2 - 4
1*X^1-4

>>>type(poly1)
FantasyNomes.polynome.Polynome

>>># degree
>>>len(poly1)
2

>>>print(poly1 * -1 )
-2*X^2-1*X^1-1

>>>div, res = poly1/poly2

>>>print(div)
2.0*X^1+1.0

>>>print(res)
1

>>>poly1==poly1
True

>>>poly1==poly2
False

>>>poly3 = fn.Polynome([1])
>>>print( poly3*poly2)
1*X^2



```