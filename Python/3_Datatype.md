# 파이썬 자료형(Python Datatype)

![img](3_Datatype.assets/12.jpg)

<br/>

<br/>

## None

*  `NoneType` is the type for the `None` object, which is an object that indicates __*no value*__. `None` is the return value of functions that "don't return anything".  [Stack Overflower](https://stackoverflow.com/questions/21095654/what-is-a-nonetype-object)

  ```python
  print(type(None))
  a = None
  print(type(a))
  ```
  
  <Class 'NoneType'>
  
  <Class 'NoneType'>

<br/>

<br/>

## Boolean Type

* True / False

* 0, 0.0, ( ), [], {}, '', None ➡ False

  * something empty reutrns False

    ```python
    bool([0])
    ```

    True



<br/>

---

<br/>

<br/>

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

<br/>

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

* **Check if the float value is smaller than a very small value**

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

<br/>

<br/>

### Complex 복소수

* 실수 + 허수
* 허수부는 j로 표현

<br/>

---

<br/>

## String Type 문자열

### String Type

**IMMUTABLE, ORDERED, ITERABLE(순회가능)**

* sequences of **character data**

* String literals may be delimited using either single('') or double quotes(""). [Real Python](https://realpython.com/python-data-types/#strings)

  ```python
  print('Jen, "Hi"')
  ```

  Jen, "Hi"

* Immutable 변경X

  ```python
  a = python
  a[-1] = '!'
  # TypeError
  ```

* Iterable

  ```python
  b = '9256'
  for char in b:
      print(char)
  ```

  ​	[결과]
  ​	9
  ​	2
  ​	5
  ​	6

<br/>

#### Triple Quotes 삼중따옴표

* Quotes in quotes
* Multiline strings

<br/>

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
  

<br/>

<br/>

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

    * formating / 형식 지정이 가능하다
    
      ```python
      import datetime
      today = datetime.datetime.now()
      # 현재 시각과 날짜 출력하기
      print(today)
      2022-01-22 03:06:~
      
      # 출력 형식을 지정해보자
      # 년/월/일/요일 : %y, %m, %d, %A
      
      print(f'오늘은 {today:%y}년 {today:%m}월 {today: %d}일이야.')
      ```
    
    
    * 연산도 가능하다
    
      ```python
      a = 2.123
      b = 4.351
      print(f'가로가 {a:0.2f}, 세로가 {b:0.2f}일 때 사각형의 넓이는 {a * b:0.2f}')
      ```
    
      가로가 2.12, 세로가 4.35일 때 사각형의 넓이는 9.24
