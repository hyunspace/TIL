# comprehension 코드



### 간결하다

* 코드의 길이가 줄었다고 하더라고, 의미 자체는 축소 되지 않아야 한다.



### 성능

* 일반화의 위험성



### 표현 방식

* pythonic



### [] vs list()

* 둘 중에 성능은 항상 대괄호 방식이 더 좋음

* 특히 list() 방식은 C언어 방식이라 대괄호가 더 파이썬st

* comprehension을 위해 []를 쓰다 보면 코드가 복잡해질 수 있음

  * 예시

  ```code
  list_a = []
  for i in range(3)
  	list_a.apprend(i)
  ```

* 최우선 해야할 것은 **가독성**
  * **"Simple is better than complex"**
  * **"Keep it simple, stupid!"**



## 성능 (loop & map & list comp)

* `for` : 버전이 올라가면서 비약적으로 성능이 향상되었음
* 



