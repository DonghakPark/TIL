#include "vgl.h"
#include "LoadShader.h"

enum VAO_IDs
{
    Triangles,
    NumVAOs
};
enum Buffer_IDs
{
    ArrayBuffer,
    NumBuffers
};
enum Attrib_IDs
{
    vPosition = 0
};

GLuint VAOs[NumVAOs];
GLuint Buffers[NumBuffers];

const GLuint NumVertices = 6;

void init()
{
    glGenVertexArrays(NumVAOs, VAOs);
    glBindVertexArray(VAOs[Triangles]);

    GLfloat vertices[NumVertices][2] = {
        {-0.90f, -0.90f}, {0.85f, -0.90f}, {-0.90f, 0.85f}, // Triangle 1
        {0.90f, -0.85f},
        {0.90f, 0.90f},
        {-0.85f, 0.90f} // Triangle 2
    };

    glCreateBuffers(NumBuffers, Buffers);
    glBindBuffer(GL_ARRAY_BUFFER, Buffers[ArrayBuffer]);
    glBufferStorage(GL_ARRAY_BUFFER, sizeof(vertices), vertices, 0);

    ShaderInfo shaders[] =
        {
            {GL_VERTEX_SHADER, "media/shaders/triangles/triangles.vert"},
            {GL_FRAGMENT_SHADER, "media/shaders/triangles/triangles.frag"},
            {GL_NONE, NULL}};

    GLuint program = LoadShaders(shaders);
    glUseProgram(program);

    glVertexAttrivPointer(vPosition, 2, GL_FLOAT,
                          GL_FALSE, 0, BUFFER_OFFSET(0));
    glEnableVertexAttribArray(vPosition);
}

void display()
{
    static const float black[] = {0.0f, 0.0f, 0.0f, 0.0f};

    glClearBufferfv(GL_COLOR, 0, black);

    glBindVertexArray(VAOs[Triangles]);
    glDrawArrays(GL_TRIANGLES, 0, NumVertices);
}

#ifdef _WIND32
int CALLBACK WinMain(
    _In_ HINSTANCE gInstace,
    _In_ HINSTANCE hPrevInstance,
    _In_ LPSTR IpCmdLine,
    _In_ int nCmdShow)

#else
int main(int argc, char **argv)
#endif
{
    glfwInit();

    GLFWwindow *window = glfwCreateWindow(800, 600, "Triangles", NULL, NULL);

    glfwMakeContextCurrent(window);
    gl3wInit();

    init();

    while (!glfwWindowShouldClose(window))
    {
        display();
        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    glfwDestroyWindow(window);

    glfwTerminate();
}