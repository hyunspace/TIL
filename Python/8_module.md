# Module

### Module and Package 모듈과 패키지

#### 모듈 Module

* 특정 기능을 하는 코드를 파이썬 파일 단위로 작성한 것

  : a file containing Python definitions and statements

```python
from pprint import pprint

from random import random
```

#### 패키지 package

* 여러 모듈의 집합

  :  a way of structuring Python’s module namespace by using “dotted module names”

* `.` 으로 구분, `package.module` 형태로 모듈을 구조화

* 패키지 안에는 또 다른 서브 패키지 O

##### import

```python
import module
from module import var, function, Class
from module import *

from package import module
from package.module import var, function, Class
```

<br/>

#### 라이브러리 Library

* 다양한 패키지를 하나의 묶음으로

<br/>

---

<br/>

## Python Standard Library, PSL 파이썬 표준 라이브러리

[The Python Standard Library](https://docs.python.org/3/library/index.html#library-index)

[파이썬 표준 라이브러리](https://docs.python.org/ko/3/library/index.html#library-index)

* [내장함수](https://docs.python.org/ko/3/library/functions.html)

  