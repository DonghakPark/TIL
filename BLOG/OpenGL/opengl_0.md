## OpenGL이란 무엇인가 ?

### OpenGL

OPenGL이란 Open Graphics Library의 약자로 그래픽 처리를 위한 API이다.

즉 그래픽 하드웨어 제어를 위한 소프트웨어 인터페이스이다. 높은 이식성과 빠른 실행속도를 가진 3D 그래픽 & 모델링 API이다.

--> 이름과는 다르게 Library가 아닌 API임에 주목해야 한다.

이때 운영체제는 OpenGL의 인터페이스를 제공하고, GPU는 OpenGL Implementation인 그래픽 카드 드라이버를 제공한다.

### OpenGL의 특징

장점

- Cross Platform : Windows, OS X, Linux, IOS, Android 등 플랫폼에 구제박지 않고 사용할 수 있다.

- Language Independent : C, Python, Java, Javascript 등 다양한 언어에서 사용할 수 있다.

단점

- Only Drawing Things

  - Low - Level Drawing Operation에서 강력한 기능을 보인다.

  - Creat Windows, OpenGL Contexts, Handling Events 등을 처리할 수 없다.

- 다른 기능을 수행하기 위해 다른 utility library가 필요하다.

  - GLFW, FreeGLUT : OpenGL을 위한 utility Library

  - Fltk, wxWidgets, Qt, Gtk

    - 범용적인 GUI Framework

    - 강력하지만 OpenGL을 학습하기 위해서는 무겁다.

### Legacy OpenGL vs Mordern OpenGL

Legacy OpenGL

- Fixed-Function Hardware만 사용할 수 있을 때 개발되었다.

- Shader를 사용할 수 없다.

  - Shader : 소프트웨어 명령의 집합으로 주로 그래픽 하드웨어의 렌더링 효과를 계산하는데 쓰인다.

- 배우기에 쉽고 빠른 프로토타입의 개발에 적합하지만 OpenGL 3.0이후로는 업데이트 되지 않았다.
  - 앞으로 없어질 전망

Mordern OpenGL

- 현재 하드웨어 수준에서 개발됨

- Shader를 사용할 수 있다.

- 더 유연하고 강력하지만 프로그래밍이 Legacy OpenGl에 비해서는 배우기 어렵다.

#### 간단한 예제

```c

#include <Windows.h>
#include <gl/GL.h>
#include <gl/GLU.h>
#include <gl.glut.h>

void RenderScene(void)
{
    glClear(GL_COLOR_BUFFER_BIT); // 내용을 지운다.
    glFlush(); //지금까지 실행안된 OpenGL 명령어를 실행
}

void SetupRC(void)
{
    glClear(0.0f, 0.0f, 1.0f, 1.0f); //창을 지우는 색상 (R,G,B,A)
}

int main(void)
{
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB);
    glutCreateWindow("Simple Example");
    glutDisplayFunc(RenderScene);
    SetupRC();
    glutMainLoop();
}
```

#### Appendix) Library vs API

Library

- Collection of Functions, pre-compiled routines or reusable components of code : 사용성이 있는 코드를 모아 놓은 것

- 장점 : 코드의 반복을 줄이고 재사용을 할 수 있게 한다, 프로그래밍 속도를 단축할 수 있다.

API (Application Programming Interface)

- Collection of Software Protocols : 인터페이스를 모아 놓은 것

- 진행중인 코드와 다른 진행중인 코드를 상호작용할 수 있게 해준다.
