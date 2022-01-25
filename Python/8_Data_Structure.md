# Data Structure 데이터 구조

## 순서가 있는 데이터 구조

### 1. String Type 문자열

**IMMUTABLE** : 문자열 내의 어떤 글자를 바꾸는 것 불가능

<br/>

#### 문자열 조회/탐색 및 검증 메소드

* `s.find(x)`, `s.index(x)`, `s.isalpha()`, `s.isupper()`, `s.islower()`, `s.istitle()`, etc

| 문법        | 설명                                             |
| ----------- | ------------------------------------------------ |
| s.find(x)   | x의 첫 번째 위치를 반환. 없으면 **-1**을 반환함. |
| s.index(x)  | x의 첫 번째 위치를 반환. 없으면 **오류** 발생    |
| s.isalpha() | 알파벳 문자 여부                                 |
| s.isupper() | 대문자 여부                                      |
| s.islower() | 소문자 여부                                      |
| s.istitle() | 타이틀 형식 여부                                 |

#### .find(x)

* x의 첫 번째 위치를 반환. 없으면 **-1**을 반환함.
  * 만약 x의 모든 위치를 알고 싶다 => 반복문

#### .index(x)

* x의 첫 번째 위치를 반환. 없으면 **오류** 발생
  * 오류 발생 => 코드가 멈춘다

##### .isdecimal() < .isdigit() < .isnumeric()

<br/>

#### 문자열 변경 메소드

* 문자열은 변경불가능한 데이터. 즉, 변경 메소드를 쓰더라도 원본이 변경되는 것은 아니다.

| 문법                         | 설명                                           |
| ---------------------------- | ---------------------------------------------- |
| s.replace(old, new[,count])  | old의 글자를 새로운 글자 new로 **바꿔서** 반환 |
| s.strip([chars])             | 공백이나 특정 문자를 **제거**                  |
| s.split([chars])             | 공백이나 특정 문자를 기준으로 **분리**         |
| 'separator'.join([iterable]) | 구분자로 iterable을 합침                       |
| s.capitalize()               | 가장 첫 번째 글자를 대문자로                   |
| s.title()                    | `'`나 공백 이후를 대문자로(타이틀 형식)        |
| s.upper()                    | 모두 대문자                                    |
| s.lower()                    | 모두 소문자                                    |
| s.sawpcase()                 | 대문자와 소문자를 변경하여                     |

#### .replace(old, new[,count])

* old를 new로 바꿔서 반환 **!실제 원본이 바뀌는 것은 아니다!**

* count를 지정하면 해당 개수만큼만 시행 (기본값이 있으므로 필수X)

  ```python
  'tomato'.replace('t','p')
  ```

  'pomapo'

  ```python
  'woooooooooow!'.repalce('o','@',4)
  ```

  'w@@@@oooooow!'

#### .strip([chars])

* 특정한 문자들을 지정하면,
  * `strip`: 양쪽을 제거하거나
  * `lstrip` : 왼쪽을 제거하거나
  * `rstrip` : 오른쪽을 제거
* 문자열을 지정하지 않으면 **공백을 제거**

#### .split(sep = None, maxsplit = -1) / .split([chars])

* 문자열을 특정한 단위로 나눠 리스트로 반환
* 



