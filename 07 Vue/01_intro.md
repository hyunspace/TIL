# Vue.js

* Intro
* Why Vue.js?
* Concept of Vue.js
* Quick Start
* Basic Syntax

<br/>

## Intro

### Front-End Development

* HTML, CSS 그리고 JavsScript를 활용해서 데이터를 볼 수 있게 만들어 줌
  * 이 작업을 통해 유저는 데이터와 상호작용을 하게 된다

### Vue.js

* 사용자 인터페이스(화면)를 만들기 위한 진보적인 자바스크립트 프레임워크
* 현대적인 tool과 다양한 라이브러리를 통해 SPA(Single Page Application)를 완벽하게 지원
* Django는 서버 담당, JSON으로 데이터를 보내주면 Vue.js에서 받아서 쐅쐅해서 클라이언트(브라우저)로 보내줄 거임
* 구글 Angular 개발자 출신인 Evan You가 발표

<br/>

### SPA(Single Page Application)

* a web application or website that **interacts with the user by dynamically rewriting the current web page** with new data from the web server, **instead of the default method of a web browser loading entire new pages**.
* 단일 페이지로 구성!! 최초에만 서버로부터 페이지를 다운로드, 이후에는 동적으로 DOM을 구성한다

### CSR(Client Side Rendering)

* 서버에서 화면을 구성하는 SSR(Server Side Rendering)방식과 달리 클라이언트에서 화면을 구성
* 최종적으로 사용자가 보는 것은 HTML! 이걸 누가 렌더링하느냐.
  * 뼈대만 받고 브라우저에서 동적으로 DOM을 만든다!

![img](https://miro.medium.com/max/1400/1*CRiH0hUGoS3aoZaIY4H2yg.png)

* 장점
  * 서버와 클라이언트 간 트래픽 감소
    * 가장 큰 틀은 한 번 받고 끝! 그 안에서 필요한 것만 바꾸니까
  * 사용자 경험 향상
    * 전체 페이지를 렌더링X 필요한/변경된 부분만 갱신하니까
* 단점
  * SSR에 비해 전체 페이지 최종 렌더링 시점이 느리다
    * 스크립트까지 전체가 넘어오기 때문에, 렌더링하는데 조금 걸림
  * SEO(검색 엔진 최적화)에 어려움이 있다
    * 검색 관련 봇이 모든 것을 보지 않고 문서의 마크업만 보고 돌아가기 때문에 스크립트만 가득 담긴 CSR 보면 ㅂㅂ하고 가버림(최초 문서에 데이터 마크업이 없으니까)

* 참고

  ![img](https://miro.medium.com/max/1400/1*jJkEQpgZ8waQ5P-W5lhxuQ.png)

  * The main difference is that for **SSR your server’s response to the browser is the HTML of your page that is ready to be rendered**, while for **CSR the browser gets a pretty empty document** with links to your javascript. That means your browser will start rendering the HTML from your server without having to wait for all the JavaScript to be downloaded and executed.
  * Django 템플릿에서 {% for ~ %}  코드를 넘겨도 사용자는 잘 정리된 걸 받는다. 이거 장고 서버에서 다 변환해서 보내준거임 SSR!
  * 즉, 실제 브라우저에 그려진 HTML을 누가 렌더링하는가!에 따라서 SSR과 CSR이 갈림. 비용적인 측면에서는 CSR이 좋음. 개발자 측(서버)에서 할 필요가 없고 그냥 스크립트 덩어리를 던지면 끝이니까(유저의 브라우저가 낑낑대며 해석해야함)
    그치만 그렇다고 무조건 CSR이 좋은 건 아님. 내 서비스나 프로젝트 구성, 특성에 맞춰서 골라야함
  * Vue.js나 React 등의 SPA 프레임워크는 SSR을 지원하는 SEO 기술이 존재함!

<br/>

## Why Vue.js

* 현재 인기 있는 프론트엔드 프레임워크

* Vanilla JS의 한계 극복

* `Vanilla JS` vs `Vue.js`

  * Vanilla JS: 데이터가 하나 바뀌었을 때, 해당 데이터를 받는 모든 요소를 선택해서 이벤트 등록 후 값을 변경해야함

  * Vue.js: DOM과 data가 연결 되어 있어서 Data를 변경하면 연결된 DOM이 알아서 변경됨

    => 개발자는 **Data**만 잘 관리하면된다!

<br/>

## Concepts of Vue.js

### MVVM Patterns in Vue.js

![img](/Users/hyun/Desktop/Hyun/TIL/07 Vue/01_intro.assets/mvvm.png)

* **ViewModel**

  * **An object that syncs the Model and the View**. In Vue.js, every Vue instance is a ViewModel. They are instantiated with the `Vue` constructor or its sub-classes:

    ```javascript
    const vm = new Vue({ /* options */ })
    ```

    * the primary object!

  * `DOM(HTML쪽)`과 `Data({key: value})`의 중개자 역할

    * 개발자가 데이터를 잘 보내주면 가운데에서 알아서 잘 하는 애!
    * Data를 얼마나 잘 처리해서 보여줄까?를 고민하는 애

* **Model**

  * **JavaScript Object** 이다 (Django에서 클래스 어쩌고 저쩌고 잊기!)

* **View**

  * Vue에서 View는 **DOM(HTML)**
  * Data의 변화에 따라서 바뀌는 대상!

<br/>

## Quick Start of Vue.js

### Django & Vue.js 코드 작성 순서

* Django

  * 데이터의 흐름
  * `url` => `views` => `template`

* Vue.js

  * **Data가 변화하면 DOM이 변경**
    1. Data 로직 작성
    2. DOM 작성

* 선언적 렌더링

  ![image-20220515155958692](/Users/hyun/Desktop/Hyun/TIL/07 Vue/01_intro.assets/image-20220515155958692.png)

* 사용자 입력 핸들링

  ```javascript
  const app = new Vue(
  	el: 'app',
  	data: {
    	message: '안녕하세요'
    },
    methods: {
      reverseMessage: function() {
        this.message = this.message.split('').reverse().join('')
      }
    }
  )
  ```

  * 자바스크립트 문법으로 보면 원래 this가 가리키는 건 methods에 속한 객체
    * 하지만, Vue는 data, methods등으로 각각 포장 된 걸 풀어서 내용물을 정리해서 이해하므로, Vue 인스턴스 안에 있는 message를 가리킬 수 있는 것
  * 메서드는 **절대 화살표 함수로 쓰면 안된다**
    * 동작 안합니다!!!!!!!!!!

<br/>

## References

[SPA](https://en.wikipedia.org/wiki/Single-page_application)

[SSR vs CSR](https://medium.com/walmartglobaltech/the-benefits-of-server-side-rendering-over-client-side-rendering-5d07ff2cefe8)

[MMVM](https://012.vuejs.org/guide/)

