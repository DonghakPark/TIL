## 인터페이스 구현

### 모듈 간 공통 기능 및 데이터 인터페이스 확인

1. 모듈 간 공통 기능 및 데이터 인터페이스의 개요
   - 공통 기능은 모듈의 기능 중에서 공통적으로 제공되는 기능을 의미한다.
   - 데이터 인터페이스는 모듈 간 교환되는 데이터가 저장될 파라미터를 의미한다.
   - 모듈 간 공통 기능 및 데이터 인터페이스는 인터페이스 설계서에서 정의한 모듈의 기능을 기반으로 확인한다.
   - 확인된 공통 기능 및 데이터 인터페이스는 모듈 간 연계가 필요한 인터페이스의 기능을 식별하는데 사용된다.
   - 모듈 간 공통 기능 및 데이터 인터페이스 확인 순서
     - 인터페이스 설계서를 통해 모듈별 기능을 확인한다.
     - 외부 및 내부 모듈을 기반으로 공통적으로 제공되는 기능과 각 데이터의 인터페이스를 확인한다.
2. 인터페이스 설계서
   - 인터페이스 설계서는 시스템 사이의 데이터 교환 및 처리를 위해 교환 데이터 및 관련 업무 송,수신 시스템 등에 대한 내용을 정의한 문서이다.
     - 인터페이스 설계서는 일반적인 형태의 설계서와 정적,동적 모형을 통한 설계서로 구분된다.
   - 일반적인 인터페이스 설계서
     - 시스템의 인터페이스 목록, 각 인터페이스의 상세 데이터 명세, 각 기능의 세부 인터페이스 정보를 정의한 문서이다.
     - 일반적인 인터페이스 설계서는 시스템 인터페이스 설계서와 상세 기능별 인터페이스 명세서로 구분된다.
     - 시스템 인터페이스 설계서 : 시스템 인터페이스 목록을 만들고 각 인터페이스 목록에 대한 상세 데이터 명세를 정의하는 것이다.
     - 상세 기능별 인터페이스 명세서
       - 각 기능의 세부 인터페이스 정보를 정의한 문서이다.
       - 인터페이스를 통한 각 세부 기능의 개요, 세부 기능이 동작하기 전에 필요한 사전/사루 조건, 인터페이스 데이터, 호출 이후 결과를 확인하기 위한 반환값등으로 구성된다.
   - 정적, 동적 모형을 통한 인터페이스 설계서
     - 정적, 동적 모형으로 각 시스템의 구성 요소를 표현한 다이어그램을 이용하여 만든 문서이다.
     - 시스템 구성하는 주요 구성 요소 간의 트랜잭션을 토해 해당 인터페이스가 시스템의 어느 부분에 속하고, 해당 인터페이스를 통해 상호 교환되는 트랜잭션의 종류를 확인 할 수 있다.
3. 인터페이스 설계서별 모듈 기능 확인
   - 인터페이스 설계서에서 정의한 모듈을 기반으로 각 모듈의 기능을 확인한다.
     - 시스템 인터페이스 목록에서 송신 및 전달 부분은 외부 모듈, 수신 부분은 내부 모듈에 해당한다.
     - 시스템 인터페이스 설계서에서 데이터 송신 시스템 부분은 외부 모듈, 데이터 수신 시스템 부분은 내부 모듈에 해당된다.
     - 상세 기능 인터페이스 명세서에서 오퍼레이션과 사전 조건은 외부 모듈, 사후 조건은 내부 모듈에 해당된다.
     - 정적, 동적 모형을 통한 인터페이스 설계에서 인터페이스 영역은 내부 모듈, 나머지 부분은 외부 모듈에 해당된다.
4. 모듈 간 공통 기능 및 데이터 인터페이스 확인
   - 내 외부 모듈 기능을 통해 공통적으로 제공되는 기능을 확인하다.
   - 내 외부 모듈 기능과 공통 기능을 기반으로 필요한 데이터 인터페이스 항목을 확인한다.

### 모듈 연계를 위한 인터페이스 기능 식별

1. 모듈 연계의 개요
   - 모둘 연계는 내부 모듈과 외부 모듈 또는 내부 모듈 간 데이터의 교환을 위해 관계를 설정하는 것으로, 대표적인 모듈 연계 방법에는 EAI,ESB 방식이 있다.
   - EAI (Enterprice Application Integration)
     - EAI는 기업 내 각종 어플리케이션 및 플랫폼 간의 정보 전달, 연계, 통합 등 상호 연동이 가능하게 해주는 솔루션이다.
     - EAI는 비즈니스 간 통합 및 연계성을 증대시켜 효율성 및 각 시스템 간의 확정성을 높여준다.
     - EAI의 구축 유형은 다음과 같다.
       - Point - to - Point : 가장 기본적인 어플리케이션 통합 방식으로, 어플리케이션을 1대1로 연결한다.
       - Hub & Spoke : 단일 접점인 허브 시스템을 통해 데이터를 전송하는 중앙 집중형 방식이다, 확장 및 유지 보수가 용이하다, 허브 장애 발생 시 시스템 전체에 영향을 미친다.
       - Message Bus : 어플리케이션 사이에 미들웨어를 두어 처리하는 방식이다, 확장성이 뛰어나며 대용량 처리가 가능하다.
       - Hybrid : 허브와 메시지의 혼합 방식이다, 그룹 내에서는 허브 방식을 그룹 간에는 메시지 방식을 사용한다, 데이터 병목 현상을 최소화 할 수 있다.
   - ESB (Enterprise Sevice Bus)
     - ESB는 어플리케이션 간 연계, 데이터 변환, 웹 서비스 지원 등 표준 기반의 인터페이스를 제공하는 솔류션이다.
     - ESB는 어플리케이션 통합 측면에서 EAI와 유사하지만 어플리케이션 보다는 서비스 중심의 통합을 지향한다.
     - ESB는 특정 서비스에 국한되지 않고 범용적으로 사용하기 위하여 어플리케이션과의 결합도를 약하게 유지한다.
     - 관리 및 보안 유지가 쉽고, 높은 수준의 품질 지원이 가능하다.
2. 모듈 간 연계 기능 식별
   - 모듈 간 공통 기능 및 데이터 인터페이스를 기반으로 모듈과 연계된 기능을 시나리오 형태로 구체화하여 식별한다.
   - 식별된 연계 기능은 인터페이스 기능을 식별하는데 사용된다.
3. 모듈 간 인터페이스 기능 식별
   - 식별된 모듈 간 관련 기능을 검토하여 인터페이스 동작에 필요한 기능을 식별한다.
   - 인터페이스 동작은 대부분 외부 모듈의 결과 또는 요청에 의해 수행되므로 외부 및 인터페이스 모듈 간 동작하는 기능을 통해 인터페이스 기능을 식별한다.
   - 내부 모듈의 동작은 외부 모듈에서 호출된 인터페이스에 의해 수행되고 결과를 나타내는 것이므로 해당 업무에 대한 시나리오를 통해 내부 모듈과 관련된 인터페이스 기능을 식별한다.
   - 식별된 인터페이스 기능 중에서 실제적으로 필요한 인터페이스 기능을 최종적으로 선별한다.
   - 식별된 인터페이스 기능은 인터페이스 기능 구현을 정의하는데 사용된다.

### 모듈 간 인터페이스 데이터 표준 확인

1. 인터페이스 데이터 표준의 개요
   - 인터페이스 데이터 표준은 모듈 간 인터페이스에 사용된느 데이터 형식을 표준화하는 것이다.
     - 인터페이스 데이터 표준은 기존의 데이터 중에서 공통 영역을 추출하거나 어느 한쪽의 데이터를 변환하여 정의한다.
     - 확인된 인터페이스 데이터 표준은 인터페이스 기능 구현을 정의하는데 사용된다.
     - 모듈 간 인터페이스 데이터 표준 확인 순서
       - 데이터 인터페이스를 통해 인터페이스 데이터 표준을 확인한다.
       - 인터페이스 기능을 통해 인터페이스 표준을 확인하다.
       - 데이터 인터페이스와 인터페이스 기능을 통해 확인된 인터페이스 표준을 검토하여 최족적인 인터페이스 데이터 표준을 확인한다.
2. 데이터 인터페이스 확인
   - 데이터 표준을 위해 식별된 데이터 인터페이스에서 입출력값의 의미와 데이터 특성 등을 구체적으로 확인한다.
   - 확인된 데이터 인터페이스의 각 항목을 통해 데이터 표준을 확인한다.
3. 인터페이스 기능 확인
   - 데이터 표준을 위해 식별된 인터페이스 기능을 기반으로 인터페이스 기능 구현을 위해 필요한 데이터 항목을 확인한다.
   - 확인된 데이터 항목과 데이터 인터페이스에서 확인된 데이터표준에서 수정 추가 삭제될 항목이 있는지 확인한다.
4. 인터페이스 데이터 표준 확인
   - 데이터 인터페이스에서 확인된 데이터 표준과 인터페이스 기능을 통해 확인된 데이터 항목들을 검토하여 최종적으로 뎅터 쵸준을 확인한다.
   - 확인된 데이터 표준은 항목별로 데이터 인터페이스와 인터페이스 기능 중 출처를 구분하여 기록한다.

### 인터페이스 기능 구현 정의

1. 인터페이스 기능 구현의 정의에 대한 개요
   - 인터페이스 기능 구현의 정의는 인터페이스를 실제로 구현하기 위헤 인터페이스 기능에 대한 구현 방법을 기능별로 기술한 것이다.
   - 인터페이스 기능 구현 정의 순서
     - 컴포넌트 명세서를 확인한다.
     - 인터페이스 명세서를 확인한다.
     - 일관된 인터페이스 기능 구현을 정의한다.
     - 정의된 인터페이스 기능 구현을 정형화한다.
2. 모듈 세부 설계서
   - 모듈 세부 설계서는 모듈의 구성 요소와 세부적인 동작 등을 정의한 설계서이다.
     - 대표적인 모듈 세부 설계서에는 컴포넌트 명세서와 인터페이스 명세서가 있다.
   - 컴포넌트 명세서
     - 컴포넌트 명세서는 컴포넌트의 개요 및 내부 클래스의 동작, 인터페이스를 통해 외부와 통신하는 명세등을 정의한 것이다.
   - 인터페이스 명세서
     - 인터페이스 명세서는 컴포넌트 명세서의 항목 중 인터페이스 클래스의 세부 조건 및 기능 등을 정의한 것이다.
3. 모듈 세부 설계서 확인
   - 각 모듈의 컴포넌트 명세서와 인터페이스 명세서를 기반으로 인터페이스에 필요한 기능을 확인한다.
   - 컴포넌트 명세서의 컴포넌트의 개요, 내부 클래스의 클래스명과 설명 등을 통해 컴포넌트가 가지고 있는 주요 기능을 확인한다.
   - 컴포넌트 명세서의 인터페이스 클래스를 통해 인터페이스에 필요한 주요 기능을 확인한다.
   - 인터페이스 명세서를 통해 컴포넌트 명세어의 인터페이스 클래스에 명시된 인터페이스의 세부 조건 및 기능을 확인한다.
4. 인터페이스 기능 구현 정의
   - 인터페이스의 기능, 인터페이스 데이터 표준, 모듈 세부 설계서를 기반으로 일관성 있고 정형화된 인터페이스 기능 구현에 대해 정의한다.
   - 일관성 있는 인터페이스 기능 구현 정의
     - 인터페이스의 기능, 인터페이스 데이터 표준, 모듈 세부 설계서를 통해 인터페이스의 기능 구현을 정의한다.
     - 정의한 인터페이스 기능 구현에 대해 송,수신 측에서 진행해야 할 절차까지 다시 세부적으로 정의한다.
   - 정의된 인터페이스 기능 구현 정형화
     - 정의한 인터페이스 기능 구현을 특정 하드웨어나 소프트웨어에 외존적이지 않게 사람들이 보기 쉽고 표준화되도록 정형화한다.
     - 정의한 인터페이스 기능 구현을 특정 하드웨어나 소프트웨어 의존적이지 않게 사람들이 보기 쉽고 표준화되도록 정형화한다.
     - 가독성을 높이려면 프로세스 형태나 유스케이스 다이어그램 형태로 정형화 한다.

### 인터페이스 구현

1. 인터페이스 구현
   - 인터페이스 구현은 송,수신 시스템 간의 데이터 교환 및 처리를 실현해 주는 작업을 의미한다.
     - 정의된 인터페이스 기능 구현을 기반으로 구현 방법 및 범위 등을 고혀하여 인터페이스 구현 방법을 분석한다.
     - 분석된 인터페이스 구현 정의를 기반으로 인터페이스를 구현한다.
     - 인터페이스를 구현하는 대표적인 방법에는 데이터 통신을 이용한 방법과 인터페이스 엔티티를 이용한 방법이 있다.
2. 데이터 통신을 이용한 인터페이스구현
   - 데이터 통신을 이용한 인터페이스 구현은 어플리케이션 영역에서 인터페이스 형식에 맞춘 데이터 포맷을 인터페이스 대상으로 전송하고 이를 수신 측에서 파싱하여 해석하는 방식이다.
     - 주로 JSON이나 XML 형식의 데이터 포맷을 사용하여 인터페이스를 구현한다.
       - 인터페이스의 객체 생성 및 전송을 위해 인터페이스 객체를 생성할 데이터를 각 시스템 및 환경에 맞게 선택한다.
       - 선택한 데이터를 JSON을 이용하여 인터페이스 객체를 생성한다.
       - 송신 측에서 JSON으로 생성한 인터페이스 객체를 AJAX 기술등을 이용하여 수신측으로 보낸다.
       - 수신 측에서 인터페이스 객체를 수신해 파싱한 후 처리한다.
       - 수식 측에서 송신 측에 처리 결과를 보낸다.
3. 인터페이스 엔티티를 이용한 인터페이스 구현
   - 인터페이스 엔티티를 이용한 인터페이스 구현은 인터페이스가 필요한 시스템 사이에 별도의 인터페이스 엔티티를 두어 상호 연계하는 방식이다.
     - 일반적으로 인터페이스 테이블을 엔티티로 활용한다.
     - 인터페이스 테이블은 한 개 또는 송신 및 수신 인터페이스 테이블을 각각 두어 활용한다.
     - 송신 및 수신 인터페이스 테이블의 구조는 대부분 같지만 상황에 따라 서로 다르게 설계할 수도 있다.
       - 인터페이스 테이블을 이용한 인터페이스 구현 순서
         - 인터페이스 이벤트가 발생하면 인터페이스 테이블에 인터페이스 데이터를 기록한다.
         - 송신 측 인터페이스 테이블에서 정해진 주기에 따라 인터페이스 데이터를 전송한다.
         - 수신 측 인터페이스 테이블에 인터페이스 데이터가 입력되면 정해진 주기에 따라 인터페이스 데이터를 읽는다.
         - 수신 측 인터페이스 테이블에서 인터페이스 데이터를 읽은 후 사전에 정의된 데이터 트랜잭션을 수행한다.

### 인터페이스 예외 처리

1. 인터페이스 예외 처리의 개요
   - 인터페이스 예외 처리의 개요
     - 인터페이스 예외 처리는 구현된 인터페이스가 동작하는 과정에서 기능상 예외 상황이 발생 했을 때 이를 처리하는 절차를 말한다.
     - 인터페이스 예외 처리는 인터페이스를 구현하는 방법에 따라 데이터 통신을 이용하는 방법과 인터페이스 엔티티를 이용한 방법으로 나뉜다.
2. 데이터 통신을 이용한 인터페이스 예외 처리
   - 데이터 통신을 이용한 인터페이스 예외 처리 방법은 JSON, XML 등 인터페이스 객체를 이용해 구현한 인터페이스 동작이 실패한 경우를 대비한 것으로, 인터페이스 객체의 송 수신 시 발생할 수 있는 예외 케이스를 정의하고 각 예외 케이스마다 예외 처리 방법을 기술한다.
     - 시스템 환경, 송,수신 데이터, 프로그램 자체 원인 등 다양한 원인으로 인해 예외 상황이 발생한다.
3. 인터페이스 엔티티를 이용한 인터페이스 예외 처리
   - 인터페이스 엔티티를 이용한 예외 처리 방법은 인터페이스 동작이 실패할 경우를 대비하여 해당 엔티티에 인터페이스의 실패 상황과 원인 등을 기록하고, 이에 대한 조치를 취할 수 있도록 사용자 및 관리자에게 알려주는 방식으로 예외 처리 방법을 정의한다.

### 인터페이스 보안

1. 인터페이스 보안의 개요
   - 인터페이스는 시스템 모듈 간 통신 및 정보 교환을 위한 통로로 사용되므로 충분한 보안 기능을 갖추지 않으면 시스템 모듈 전체에 악영향을 주는 보안 취약점이 될 수 있다.
   - 인터페이스의 보안성 향상을 위해서는 인터페이스의 보안 취약점을 분석한 후 적절한 보안 기능을 적용한다.
2. 인터페이스 보안 취약점 분석
   - 인터페이스 기능이 수행되는 각 구간들의 구현 현황을 확인하고 각 구간에 어떤 보안 취약점이 있는지를 분석한다.
   - 인터페이스 기능이 수행되는 각 구간의 구현 현황은 송, 수신 영역의 구현 기술 및 특징 등을 구체적으로 확인한다.
   - 확인된 인터페이스 기능을 기반으로 송신 데이터 선택, 송신 객체 생성, 인터페이스 송수신, 데이터 처리 결과 전송 등 영역별로 발생할 수 있는ㅇ 보안 취약점을 시나리오 형태로 작성한다.
3. 인터페이스 보안 기능 적용
   - 분석한 인터페이스 기능과 보안 취약점을 기반으로 인터페이스 보안 기능을 적용한다.
   - 인터페이스 보안 기능은 일반적으로 네트웤, 애플리케이션, 데이터베이스 영역에 적용한다.
     - 네트워크 영역 : 인터페이스 송수신 간 스니핑 등을 이용한 데이터 탈취 및 변조 위협을 방지하기 위해 네트워크 트래픽에 대한 암호화를 설정한다. 암호화는 인터페이스 아키텍쳐에 따라 IPsec, SSL, S-Http 등의 다양한 방식으로 적용한다.
     - 어플리케이션 영역 : 소프트웨어 개발 보안 가이드를 참조하여 어플리케이션 코드 상의 보안 취약점을 보완하는 방향으로 어플리케이션 보안 기능을 적용한다.
     - 데이터베이스 영역 : 데이터 베이스, 스키마, 언티티의 접근 권한과 프로시저, 트리거 등 데이터 베이스 동작 객체의 보안 취약점에 보안 기능을 적용한다, 개인 정보나 업무상 민감한 데이터의 경우 암호화나 익명화 등 데이터 자체의 보안 방법도 고려한다.

### 연계 테스트

1. 연계 테스트의 개요
   - 연계 테스트는 구축된 연계 시스템과 연계 시스템의 구성 요소가 정상적으로 동작하는지 확인하는 활동이다.
     - 연계 테스트는 연계 테스트 케이스 작성, 연계 테스트 환경 구축, 연계 테스트 수행, 연계 테스트 수행 결과 검증 순으로 진행된다.
2. 연계 테스트 케이스 작성
   - 연계 테스트 케이스 작성은 연계 시스템 간의 데이터 및 프로세스의 흐름을 분석하여 필요한 테스트 항목을 도출하는 과정이다.
     - 송,수신용 연계 응용 프로그램의 단위 테스트 케이스와 연계 테스트 케이스를 각각 작성한다.
       - 송 수신용 연계 응용 프로그램의 단위 테스트 케이스
         - 송수신 시스템에서 확인해야 할 항목을 도출한다.
         - 송수신 시스템에서 단순 개별 데이터의 유효값을 확인하는 경우의 수와 데이터 간의 연관 관계를 확인하는 경우의 수로 구분하여 작성한다.
       - 연계 테스트 케이스
         - 송수신용 연계 응용 프로그램의 기능상 결함을 확인하는 단위 테스트 케이스 형태로 작성한다.
         - 단위 테스트 케이스는 연계 테이블 간 송수신 절차의 앞뒤로 연결하여 흐름을 확인할 수 있는 내용으로 작성한다.
3. 연계 테스트 환경 구축
   - 연계 테스트 환경 구축은 테스트의 일정, 방법, 절차, 소요 시간 등을 송수신 기관과의 협의를 통해 결정하는 것이다.
     - 연계 서버 또는 송수신용 어댑터 설치, 연계를 위한 IP 및 포트 허용 신청, 연계를 위한 DB 계정 및 테이블과 데이터 생성 등의 테스트 환경을 구축한다.
4. 연계 테스트 수행
   - 연계 테스트 수행은 연계 응용 프로그램을 실행하여 연계 테스트 케이스의 시험 항목 및 처리 절차 등을 실제로 진행하는 것이다.
   - 송 수신용 연계 응용 프로그램의 단위 테스트를 먼저 수행한다.
   - 단위 테스트의 수행을 완료한 후 연계 테스트 케이스에 따라 데이터 추출, 데이터 송수신, 데이터 반영 과정 등의 연계 테스트를 수행한다.
5. 연계 테스트 수행 결과 검증
   - 연계 테스트 수행 결과 검증은 연계 테스트 케이스의 시험 항목 및 처리 절차를 수행한 결과가 예상 결과와 동일한지를 확인하는 것이다.
     - 연계 테스트 수행 결과는 다음과 같은 테스트 케이스 항목별 검증 방법을 이용하여 검증한다.
       - 운영 DB 테이블의 건수를 확인하는 방법
       - 테이블 또는 파일을 열어 데이터를 확인하는 방법
       - 파일 생성 위치에서 파일 생성 여부 및 파일 크기를 확인하는 방법
       - 연계 서버에서 제공하는 모니터링 현황을 확인하는 방법
       - 시스템에서 기록하는 로그를 확인하는 방법

### 인터페이스 구현 검증

1. 인터페이스 구현 검증의 개요
   - 인터페이스 구현 검증은 인터페이스가 정상적으로 문제없이 작동하는지 확인하는 것이다.
     - 인터페이스 구현 검증 도구와 감시 도구를 이용하여 인터페이스의 동작 상태를 확인한다.
2. 인터페이스 구현 검증 도구
   - 인터페이스 구현을 검증하기 위해서는 인터페이스 단위 기능과 시나리오 등을 기반으로 하는 통합 테스트가 필요하다.
   - 통합 테스트는 다음과 같은 테스트 자동화 도구를 이용하면 효율적으로 수행할 수 있다.
     - Xuint : Java + C++ + .Net 등 다양한 언어를 지원하는 단위 테스트 프레임워크
     - STAF : 서비스 호출 및 컴포넌트 재사용 등 다양한 환경을 지원하는 테스트 프레임워크이다.
     - FItNesse : 웹 기반 테스트케이스 설계, 실행, 결과 확인 등을 지원하는 테스트 프레임워크
     - NTAF, Selenium, Watir 등등
3. 인터페이스 구현 감시 도구
   - 인터페이스 동작 생태는 APM을 사용하여 감시(Monitoring)을 할 수 있다.
   - 어플리케이션 성능 관리 도구를 통해 데이터베이스와 웹 어플리케이션의 트랜잭션, 변수 값, 호출 함수, 로그 및 시스템 부하 등 종합적인 정보를 조회하고 분석할 수 있다.
   - 대표적인 어플리케이션 성능 관리 도구에는 스카우터, 재나퍼등이 있다.
4. 인터페이스 구현 검즘 도구 및 감시 도구 선택
   - 인터페이스 기능 구현 정의를 통해 구현된 인터페이스 명세서의 게부 기능을 참조하여 인터페이스의 정상적인 동작 여부를 확인하기 위해 검증 도구와 감시 도구의 요구를 분석한다.
   - 분석이 끝나면 시장 및 솔류션 조사를 통해서 적절한 인터페이스 구현을 검증하고 감시하는데 필요한 인터페이스 구현 검증 도구와 감시 도구를 선택한다.
5. 인터페이스 구현 검증 확인
   - 인터페이스 구현 검증 도구를 이용하여 외부 시스템과 연계 모듈의 동작 상태를 확인한다.
   - 최초 입력값과 입력값에 의해 선택되는 데이터, 생성되는 객체의 데이터 등 전반적인 인터페이스 동작 프로세스상에서 예상되는 결과값과 실제 검증값이 동일한지를 비교한다.
   - 추가적으로 각 단계별 오류 처리도 적절하게 구현되어 있는지 확인한다.
6. 인터페이스 구현 감시 확인
   - 인터페이스 구현 감시 도구를 이용하여 외부 시스템과 연결 모듈이 서비스를 제공하는 동안 정상적으로 동작하는지 확인한다.
   - 인터페이스 동작 여부, 에러 발생 여부 등 감시 도구에서 제공해 주는 리포트를 활용한다.

### 인터페이스 오류 확인 및 처리 보고서 작성

1. 인터페이스 오류 확인 및 처리 보고서의 개요
   - 인터페이스는 독립적으로 떨어져 있는 시스템 간 연계를 위한 기능이므로 인터페이스에서 발생하는 오류는 대부분 중요한 오류이다.
   - 인터페이스 오류 발생 시 사용자 또는 관리자는 오류사항을 확인하고 오류 처리 보고서를 작성하여 보고 체계에 따라 관리 조직에 보고해야 한다.
   - 인터페이스 오류 확인 방법에는 오류 발생 즉시 확인하는 방법과 주기적인 확인 방법이 있다.
2. 인터페이스 오류 발생 즉시 확인
   - 인터페이스 오류가 발생하면 화면에 오류 메시지를 표시하고 자동으로 SMS, 이메일을 발송하므로 즉시 오류 발생을 확인할 수 있다.
   - 인터페이스 오류 발생을 즉시 처리하는 것은 가장 직관적인 방법이기에 많이 사용되고 있다.
3. 주기적인 인터페이스 오류 발생 확인
   - 시스템 관리자가 시스템의 현재 상태를 보여주는 시스템 로그나 인터페이스 오류 관련 테이블 등을 통해 주기적으로 오류 발생 여부를 확인한다.
   - 발생하는 오류에 대한 정보가 주기적으로 축적되면 오류의 원인 파악이 용이하기 때문에 오류의 재발을 방지할 수 있는 계획을 세울 수 있다.
     - 인터페이스 오류 로그 확인
     - 인터페이스 오류 테이블 확인
     - 인터페이스 감시 도구 사용
4. 인터페이스 오류 처리 보고서 작성
   - 인터페이스 오류 처리 보고서는 인터페이스 작동 시 발생하는 오류의 발생 및 종요 시점, 원인 및 증상, 처리사항 등을 정리한 문서이다.
     - 인터페이스 오류 처리 보고서는 오류 발생 즉시 신속하게 작성하여 조직의 보고체계에 따라 보고한다.
     - 인터페이스 오류 처리 보고서는 일반적인 정형화된 형식이 없기 때문에 조직 또는 오류 발생 시 상황에 맞춰 작성한다.
     - 인터페이스 오류 처리 보고서는 오류 관련 사항을 시간 경과에 따라 기록한다.
     - 다음은 보고 시기에 따른 인터페이스 오류 처리 보고서의 특징이다.
       - 최조 발생 시 : 인터페이스 오류 발생 상황을 인지하면 신속하게 조직에 보고하고 대응 조직을 만든다, 오류 발생 구간 및 시점, 영향도 등을 간이 보고서, 이메일, SMS 등으로 보고 한다.
       - 오류 처리 경과 시 : 오류 처리 진행 상황과 오류에 관한 공지사항 등록 등을 보고한다.
       - 완료 시 : 최종 조치 후 내부 조직관 고객사에 완료됐음을 보고한다, 오류 발생 시점, 오류 처리 경과, 오류 재발 방지 대책 등 종합적인 내용을 보고한다.