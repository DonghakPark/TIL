### 삼각형 만들기

#### 삼각형 만들기

OpenGL에서 모든 3D 물체는 삼각형으로 이루어진다. OpenGL에서 가장 기본되는 단위는 정점, 선, 삼각형으로 이를 통해서 우리가 보는 컴퓨터 그래픽을 구현한다. 따라서 이번 게시물에서는 삼각형 생성을 다룬다.

#### import

```
import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy
```

- opengl을 사용하기 위한 import 구문이다

  - glfw : Window를 생성하기 위해 사용

  - OpenGL.GL : OpenGL 사용을 위해 사용

  - OpenGL.GL.shaders : Shader 사용을 위해 사용

  - numpy : 형변환을 위해 사용

#### main()

코드에 대한 설명은 주석으로 대체한다.

```python

def main():

    # glfw 초기화
    if not glfw.init():
        return

    # 윈도우 생성 800x600 사이즈로 My OpenGL Window라는 창을 새로 생성
    window = glfw.create_window(800, 600, "My OpenGL window", None, None)

    # 윈도우 생성 실패시 glfw 종료
    if not window:
        glfw.terminate()
        return

    # context 생성
    glfw.make_context_current(window)

    #            위치            색상
    triangle = [-0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
                0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
                0.0, 0.5, 0.0, 0.0, 0.0, 1.0]

    # 타입 변환
    triangle = numpy.array(triangle, dtype=numpy.float32)
```

#### Shader

```python

    # Vertex Shader 정점 쉐이더
    vertex_shader = """
    #version 330        //version 정보를 표시
    in vec3 position;   //vec3의 position 변수 선언 (위치 정보를 입력받음)
    in vec3 color;      //vec3의 color 변수 선언 (색상 정보를 입력받음)

    out vec3 newColor;

    void main()
    {
        gl_Position = vec4(position, 1.0f);
        newColor = color;
    }
    """

    # Fragment Shader 프로그먼트 쉐이더
    fragment_shader = """
    #version 330

    in vec3 newColor;
    out vec4 outColor;

    void main()
    {
        outColor = vec4(newColor, 1.0f);
    }
    """

    # 쉐이더 선언
    shader = OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
                                              OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))

    # 버퍼 생성
    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, 72, triangle, GL_STATIC_DRAW)

    # position
    position = glGetAttribLocation(shader, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    # color
    color = glGetAttribLocation(shader, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)

    # Program Use
    glUseProgram(shader)

    # 배경색을 초기화
    glClearColor(0.2, 0.3, 0.2, 1.0)

    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT)

        glDrawArrays(GL_TRIANGLES, 0, 3)

        glfw.swap_buffers(window)

    glfw.terminate()


if __name__ == "__main__":
    main()

```

#### Appendix) 전체 코드

```python
import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy


def main():
    # glfw 초기화
    if not glfw.init():
        return
    # 윈도우 생성
    window = glfw.create_window(800, 600, "My OpenGL window", None, None)
    # 윈도우 생성 실패시 glfw 종료
    if not window:
        glfw.terminate()
        return
    # context 생성
    glfw.make_context_current(window)
    #            위치            색상
    triangle = [-0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
                0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
                0.0, 0.5, 0.0, 0.0, 0.0, 1.0]
    # 타입 변환
    triangle = numpy.array(triangle, dtype=numpy.float32)
    # Vertex Shader
    vertex_shader = """
    #version 330
    in vec3 position;
    in vec3 color;
    out vec3 newColor;
    void main()
    {
        gl_Position = vec4(position, 1.0f);
        newColor = color;
    }
    """
    # Fragment Shader
    fragment_shader = """
    #version 330
    in vec3 newColor;
    out vec4 outColor;
    void main()
    {
        outColor = vec4(newColor, 1.0f);
    }
    """

    shader = OpenGL.GL.shaders.compileProgram(OpenGL.GL.shaders.compileShader(vertex_shader, GL_VERTEX_SHADER),
                                              OpenGL.GL.shaders.compileShader(fragment_shader, GL_FRAGMENT_SHADER))

    VBO = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, VBO)
    glBufferData(GL_ARRAY_BUFFER, 72, triangle, GL_STATIC_DRAW)

    position = glGetAttribLocation(shader, "position")
    glVertexAttribPointer(position, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
    glEnableVertexAttribArray(position)

    color = glGetAttribLocation(shader, "color")
    glVertexAttribPointer(color, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))
    glEnableVertexAttribArray(color)

    glUseProgram(shader)

    glClearColor(0.2, 0.3, 0.2, 1.0)

    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT)

        glDrawArrays(GL_TRIANGLES, 0, 3)

        glfw.swap_buffers(window)

    glfw.terminate()


if __name__ == "__main__":
    main()

```
