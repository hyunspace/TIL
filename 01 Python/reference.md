# References and Sources

## Definition

* [Python Tutorial](https://docs.python.org/3/tutorial/index.html)





## Image

#### 4_

* [continue flow chart](https://www.guru99.com/python-break-continue-pass.html)
* [break flow chart](https://www.guru99.com/python-break-continue-pass.html)





5_

* [function definition](https://www.fireblazeaischool.in/blogs/functions-in-python/)
* [parameters & arguments](https://velog.io/@dooyeonk/Python-Function-Parameters)
* [function scope](https://velog.io/@idnnbi/Python-Variable-Scope)
* [function scope2](https://community.dataquest.io/t/python-scope-of-a-variable/3396)









---

정리중

* * replace

    ```python
    word = 'hello' # string is IMMUTABLE
    
    def new():
        word.replace('h', '')
        # replace를 써도 string 규칙 안 깨짐
        # 문자열을 바꾼 게 아니라, h를 뺀 ello를 return 해준 것 뿐
        a = word.replace('h', '')
        # return 값을 a에 담아두자
        print(word) # immutable하므로 그대로
        print(a)
    
    new()
    print(word)
    ```

    hello

    ello

    hello

<br/>