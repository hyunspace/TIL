# 파이썬 자료형(Python Datatype)

![img](3_Datatype.assets/12.jpg)





## None

*  `NoneType` is the type for the `None` object, which is an object that indicates __*no value*__. `None` is the return value of functions that "don't return anything".  [Stack Overflower](https://stackoverflow.com/questions/21095654/what-is-a-nonetype-object)

  ```python
  print(type(None))
  ```

  <Class 'NoneType'>





## Boolean Type

* True / False

* 0, 0.0, ( ), [], {}, '', None ➡ False

  * something empty reutrns False

    ```python
    bool([0])
    ```

    True





---





## Numeric Type 수치형

### Int 정수

* The type of every integer is **int**
  * no long type, just int
* There's **no overflow** (산술 오버플로우)
  * overflow : over the memory which a data type can use

* Notation expression
  * binary number : 0b
  * octal number : 0o
  * hexadecimal : 0x 





### Float 실수

* Every number excep integer is **float**
* **floating point** (부동소수점)
  * Computers express float by binary beats. And it leads to floating point rounding error.

#### Floating point rounding error

* Be cafeful when you compare float type values

  ```python
  # Are they same?
  3.14 - 3.02 == 0.12
  ```

  False

  ```python
  3.14 - 3.02
  ```

  0.120000000000000**1**

* **Check if the float value is smaller than very small value**

  ```python
  # 1. a tiny value
  abs(num1 - num2) <= 1e-10
  ```

  True

  ```python
  # 2. machine epslion
  
  # 3. math.isclose(a, b)
  import math
  math.isclose(num1, num2)
  ```





### Complex 복소수





---





## String Type 문자열

### String Type

**IMMUTABLE, ORDERED, ITERABLE**

* sequences of **character data**

* String literals may be delimited using either single('') or double quotes(""). [Real Python](https://realpython.com/python-data-types/#strings)

  ```python
  print('Jen, "Hi"')
  ```

  Jen, "Hi"

* Immutable
* Iterable





#### Triple Quotes 삼중따옴표

* Quotes in quotes
* Multiline strings





#### Escape Sequence `\`

* When make Python interpret a charater or sequence of characters within a string differently

  ```pyton
  print('Jen, \'Hi'\')
  ```

  Jen, Hi.

  | Escape Sequence | Escaped Interpretation |
  | :-------------: | :--------------------: |
  |       \n        |  Enter key(new line)   |
  |       \t        |          Tab           |
  |       \r        |    Carriage return     |
  |       \0        |          Null          |
  |       \\        |          `\`           |
  |       \\'       |   Single quote(`'`)    |
  |       \\"       |   Double quote(`"`)    |

  ```python
  # make a rectagle with *
  n, m = 3, 4
  print((('*' * n) + '\n') * m)
  ```
  





### String Interpolation 문자열 사이 변수

* Method to make string sequence using variables

  * %-formatting
  
    ```python
    print('Hello, %s' % name)
    print('My GPA is %d' % gpa)
    print('My GPA is %.2f' % gpa)
    ```
  
  * **str.format()** : Python 3.5v

    ```python
    print('Hi, {}!'.format(name))
    # print('Hi, {} and {}!'.format(name, name2))
    ```
  
  * **f-strings** : python 3.6+ v
  
    ```python
    print(f'Hi, {name}!')
    ```

    
  









