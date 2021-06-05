> 본 게시물은 김영한님의 HTTP 웹 기본 지식 강의를 듣고 정리, 요약한 것입니다. 더 자세히 알고 싶으시면 아래의 링크의 강의를 추천드립니다.

> https://www.inflearn.com/course/http-%EC%9B%B9-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC#

---

### URI와 웹 브라우저 요청 흐름

#### URI (Uniform Resource Identifier)

URI, URL, URN 이란 ?

- URI는 로케이터(Locator), 이름(Name) 또는 둘다 추가로 분류될 수 있다.

- 즉 URL과 URN은 URI에 포함되는 개념이고, 이는 자원을 식별하기 위한 방법을 의미한다.

그렇다면 URI라는 단어는 어떤 뜻을 가지고 있을까 ?

- Uniform : 리소스를 식별하기 위한 통일된 방식

- Resource : 자원, 필요한 모든 것

- Identifier : 다른 항목과 구분하는데 필요한 정보

URL : Uniform Resource Locator)

- ex) foo://example.com:8042/over/there?name=ferrt#nose

- 리소스가 있는 위치를 지정

URN : Uniform Resource Name

- ex) urn:example:animal:ferret:nose

- 리소스에 이름을 부여

하지만 이름만을 가지고 하기에는 한계가 있어 주로 URL을 많이 사용한다.

#### URL 분석

아래와 같은 URL은 다음의 규칙을 따라서 정해진 것이다.

```
https://www.google.com/search?q=hello&hl=ko

--> scheme://[userinfo@]host[:port][/path][?query][#fragment]
```

- scheme

  - 주로 프로토콜을 사용한다.

  - 프로토콜 : 어떤 방식으로 자원에 접근할 것인지에 대한 규칙을 약속한 것

  - 주로 http는 80, https는 443 포트를 사용

- userinfo

  - URL에 사용자정보를 포함해서 인증하는 방식이지만 거의 사용되지 않고 있음

- host

  - host 이름, 도메인명, IP주소를 직접입력가능

- port

  - 포트 번호, 생략 가능

- path

  - 리소스가 있는 경로를 명시해야함

  - 계측적인 구조를 / 를 통해서 나타냄

- query

  - key = value 형태이다.

  - ?로 시작, &로 추가 가능 ex) keya=valuea&keyb=valueb

  - 쿼리 파라미터, 쿼리 스트링으로 불림, 웹서버에 제공하는 파라미터, 문자형태로 전송하기 때문에

- Fragment

  - html 내부 북마크와 같은 정보에 사용되며, 서버로 전송되는 정보는 아님

---

### 웹 브라우저 요청 흐름

웹 브라우저가 특정 URI를 사용하면 다음과 같은 HTTP요청 메시지가 생성된다.

```
GET /search?q=hello&hi=ko HTTP/1.1
HOST : www.google.com
```

이렇게 요청 메시지가 생성되면 서버로 전송되게 된다.

- 웹 브라우저가 http 메시지 생성

- 소켓 라이브러리를 통해서 TCP/IP로 연결 (IP, PORT)한 후 데이터 전달

- TCP/IP 패킷을 생성한다. 이때 HTTP 메시지가 전송 데이터가 된다.

- 아래 계층을 통해서 서버로 이 메시지를 전송하게 된다.

전송된 메시지를 수신한 서버는 http 메시지를 분석해서 필요로 하는 정보를 다시 회신해 준다. 이때 회신해주는 메시지는 http 응답 메시지라고 한다.

```
ex)
HTTP/1.1 200 OK
Contect-Type: text/html; charset = UTF-8
Content-Length : 3444
--> meta data

<html>
<body>~~~~` </body>
~~~

</html>
--> html
```

회신하는 과정을 전송하는 과정과 동일하게 client로 전송한다.

이렇게 회신한 데이터를 웹 브라우저가 렌더링을 통해서 사용자에게 원하는 페이지를 보여준다.

즉 클라이언트가 서버로 http message 요청을 보내고 서버가 http 응답 메시지를 보내면 이를 웹 브라우저가 렌더링을 통해서 사용자에게 보여주는 것이다.
