## OpenGL 렌더링 파이프라인

OpenGL의 렌더링 파이프라인에 대해서 알아보도록 한다.

![image](https://user-images.githubusercontent.com/44962038/126598319-b247e57d-584e-402c-bba4-7f967f02d6d8.png)

OpenGL 렌더링 파이프라인 특징

- 제공한 Geometric 자료(정점들)로 시작한다.

- 여러 쉐이딩 단계를 거친다.

  - 정점 쉐이딩

  - 테셀레이션 쉐이딩

  - Geometry 쉐이딩

- 이후에 Rasterizer에 보내진다.

  - Clipping 영역에 있는 모든 Primitive들에 대한 Fragment를 생성한다.

- 생성된 Fragment에 대해 Fragment Shader를 실행한다.

#### 1. OpenGL에 자료를 보낼 준비하기

모든 자료는 버퍼 오브젝트에 저장되어야한다. 여기서 버퍼 오브젝트는 OpenGL이 관리하는 메모리를 뜻한다.

이러한 버퍼를 채우는 가장 흔한 방법은 glNamedBufferStorage()를 통해 데이터와 버퍼의 크기를 설정해주는 것이다.

#### 2. OpenGL에 자료 보내기

버퍼를 초기화한 이후 glDrawArrays()라는 그리기 명령을 실행해서 geometric Primitives들을 렌더링 하도록 요청할 수 있다.
