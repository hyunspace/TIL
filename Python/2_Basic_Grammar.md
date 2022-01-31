# Python Basic Grammar

## Basic Grammar

### Code style Guide

* PEP8 https://www.python.org/dev/peps/pep-0008/
* Google Style guide https://google.github.io/styleguide/pyguide.html

<br/>

### 들여쓰기(Identation)

* Space sensitive >> space key * 4 or 1 tab

<br/>

---

<br/>

### 변수(Variable)

**How to Assign** / **How to Name**

#### `=` assign (same X) `할당하다`

* A name used to refer an object in your computer memory

* Referred object is variable. That's why it's called variable

  ```python
  a = 1
  a = 2
  print(a)
  
  [result]
  2
  ```

* Variable is assigned with `=` (assignment operator)

  * 실습 문제: 각각 값을 바꿔서 저장하는 코드 작성하기

    ```python
    x = 10, y = 20
    
    temp = x # 임시변수 temp에 x를 담아두고
    x = y # y를 x에 담기
    y = temp # 다시 temp를 y에 담으면 (컵 속 물 옮기기 상상하기)
    print(x, y)
    >>> 20 10
    ```

    ```python
    x, y = 10, 20
    y, x = x, y
    print(x, y)
    >>> 20 10
    ```

<br/>

#### type()

* Type of the assigned value

#### id()

* Identity value of the assigned object.

  ```python
  i = 5
  j = 3
  ```

  ```python
  i = i - j # assign the value of i - j to i.
  i
  
  [result]
  2
  ```

#### assignment

* one value several variables

  ```python
  x = y = 1004
  print(x, y)
  ```

  1004 1004

* multiple assignment

  ```python
  x, y = 1, 2
  print(x, y)
  ```

  1 2

<br/>

---

<br/>

### 식별자(Identifiers)

* How to name variables?

* **The name used to identify Python objects**

* Rule
  * alphabet, underscore(_), numbers
  
  * No number at first
  
  * No length limit, Case-sensitive
  
  * Following keywords can't be used as reserved words
    * True, False, None, if, elif, else, is, in, except, finally, not, or, and, pass, return, try, while, with, yield, for, as, assert, async, await, break, continue, from, for, global, def, del, lambda, nonlocal, import
    
    * ```python
      import keyword  #you can see all keywords in Pyton
      print(keyword.kwlist)
      ```
    
  * Do not use **Built in function내장함수** or **Module**

<br/>

---

<br/>

### 사용자 입력 input

#### input([prompt])

* Built in function

* A user can input a value

* **Return value is always string.**

  ```python
  name = input('Write down your name: ')
  print(name)
  ```

  Write down your name: Annie

  Annie

  ```python
  type(name)
  ```

  str

<br/>

### 주석 Comment

* One line comment
  * put `#` at the front
* Multiple lines comment
  * put `#` at the every line or
  * use `"""` or `'''`
  * `ctrl + /`
* Docstring





