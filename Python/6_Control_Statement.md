# Control Statement 제어문

## Conditional Statement 조건문





## Loop statement 반복문

### while



### for

#### 딕셔너리 순회

* 기본적으로 key를 순회, key를 통해 값을 활용

  ```python
  menus = {'신전떡볶이': '매운치즈김밥', '불스떡볶이': '페퍼로니떡볶이'}
  for menu in menus:
      print(menu)
  ```

  신전떡볶이

  불스떡볶이

   ```python
   menus = {'신전떡볶이': '매운치즈김밥', '불스떡볶이': '페퍼로니떡볶이'}
   for menu in menus:
   	print(menu, menus[menu])
   ```

  신전떡볶이 매운치즈김밥

  불스떡볶이 페퍼로니떡볶이

  ```python
  menus = {'신전떡볶이': ['매운치즈김밥', '로제치즈떡볶이'], '불스떡볶이': ['페퍼로니떡볶이', '꿀구마추가']}
  # 신전떡볶이의 메뉴 출력하고, 개수 세기
  cnt = 0
  # 일단 키 값을 찾자
  for menu in menus:
      if menu == '신전떡볶이':
          # 찾은 키값으로 value에 접근한다
          for i in menus[menu]:
              print(i)
              cnt += 1
  print(cnt)
  ```

  매운치즈김밥

  로제치즈떡볶이

  2

  

  

