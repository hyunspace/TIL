# 11. 7계층 프로토콜 HTTP

> 7계층 어플리케이션 계층의 프로토콜 중 가장 많이 사용하는 HTTP 프로토콜
> 
> 소켓 통신 => 7계층 프로토콜 만드는 것!

* HTTP 프로토콜

* HTTP 요청 프로토콜

* HTTP 응답 프로토콜

* HTTP 헤더 포맷

* 실습

<br/>

## HTTP 프로토콜

### 웹을 만드는 기술들

<img src="11장-HTTP-프로토콜.assets/2022-07-30-21-29-12-image.png" title="" alt="" width="551">

* `HTML + JavaScript + CSS`
  
  * **웹 표준** => 
  
  * 서버에 저장 but 클라이언트 컴퓨터에서 동작
    
    => 프론트엔드
  
  * HTML : 웹페이지를 채울 내용
  
  * JavaScript : 웹페이지에 들어갈 기능
  
  * CSS : 웹 페이지를 예쁘게 꾸밀 디자인

* `HTTP`
  
  * 위의 웹 표준 데이터를 받아오는 프로토콜
  
  * **HyperText Transfer Protocol**
  
  * HTTPS == HTTP + SSL/TLS(보안)

* `ASP/ASP.NET, JSP, PHP`
  
  * 웹표준과 달리 서버에서 동작. 클라이언트는 볼 수 없음
    
    => 백엔드
  
  * ASP/ASP.NET : MS가 만든 것. 그래서 활용도가 낮음
  
  * JSP : 자바 기반. 호환성 높고, 국내 공공기관은 모두 자바 기반이라 수요 많음.
  
  * PHP : 독자적임

<br/>

### HTTP 프로토콜의 특징

* **HyperText Transfer Protocol**

* www에서 쓰이는 핵심 프로토콜. 문서 전송을 위해 쓰이고 오늘날 거의 모든 웹 애플리케이션에서 사용
  
  * 음성, 화상 등 여러 종류의 데이터를 MIME로 정의하여 전송 가능

* 특징
  
  * Request(요청)과 Response(응답) 동작에 기반하여 서비스 제공

#### HTTP 1.0

* 요즘은 잘 안 쓰임

* `연결 수립 / 동작 / 연결 해제` 의 단순함이 특징
  
  * 하나의 URL은 하나의 TCP 연결

* HTML 문서를 전송 받은 뒤 연결을 끊고 다시 연결하여 데이터를 전송
  
  => 데이터가 적은 과거에는 괜찮았음

* 네트워크 부하가 심하다는 문제점
  
  <img src="11장-HTTP-프로토콜.assets/2022-07-30-21-53-45-image.png" title="" alt="" width="460">
  
  * 요청 한 번 보내고 응답 받으면 연결을 종료 해버려서 다시 3Way Handshake를 해야함
    
    => HTTP/1.1이 보완. 한 번 연결 하면 끝
    
    <img src="11장-HTTP-프로토콜.assets/2022-07-30-21-54-24-image.png" title="" alt="" width="459">

<br/>

## HTTP 요청 프로토콜

### HTTP 요청 프로토콜의 구조

* 요청하는 방식을 정의하고 클라이언트의 정보를 담고 있음
  
  ![](11장-HTTP-프로토콜.assets/2022-07-30-21-55-12-image.png)
  
  * 우리가 알고 있는 영어와 특수 문자를 쓴다! (16진수X)
  
  * `Headers`: 패킷의 헤더X 옵션과 유사함.
    
    * 10개 넘게 들어가기도 함!
  
  * `공백` : 한 줄
  
  * `Body` : 데이터
  
  * 예시
    
    ![](11장-HTTP-프로토콜.assets/2022-07-30-22-00-17-image.png)
    
    * 첫번째줄이 Request
    
    * 나머지 모두 Headers

#### Request Line

![](11장-HTTP-프로토콜.assets/2022-07-30-22-02-07-image.png)

* 띄어쓰기 필수!

* 요청 타입
  
  ![](11장-HTTP-프로토콜.assets/2022-07-30-22-03-43-image.png)
  
  * `GET` : 데이터 요청
  
  * `HEAD` : 페이지를 보내달라고X 페이지 정보만 따로 요청
  
  * `PUT` : 사진 업로드와는 다름!
  
  * `COPY`, `MOVE`, `DELETE`
    
    * 클라이언트 마음대로 서버 데이터를 조작한다? => 안돼! 막아버림

* 예시
  
  * POST
    
    ![](11장-HTTP-프로토콜.assets/2022-07-30-22-41-48-image.png)
    
    Request Line + HEADER + 공백 + Data(uid~)
    
    * 데이터는 BODY에 넣어서 보냄.
  
  * GET
    
    ![](11장-HTTP-프로토콜.assets/2022-07-30-22-44-00-image.png)
    
    * 데이터를 주소창에 포함시켜서 보냄

* GET 방식과 POST 방식의 차이점
  
  ![](11장-HTTP-프로토콜.assets/2022-07-30-22-44-30-image.png)
  
  * GET은 주소창에 포함 되어서 사람들이 볼 수 있음
    
    * 중요한 데이터는 GET방식으로 보내지 않는다
  
  * POST는 body에 들어가므로 패킷 캡쳐하지 않는 이상 볼 수 없음


