### 삼각형 만들기

#### import
```
import glfw
from OpenGL.GL import *
import OpenGL.GL.shaders
import numpy
```

``` python
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