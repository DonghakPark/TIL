#include "stdafx.h"
#include<gl/freeglut.h>
#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<time.h>
#include<float.h>
#pragma warning(disable : 4996) 
#define Degree_to_Rad 3.141592f / 180

typedef struct vector_struct
{
	GLfloat x;
	GLfloat y;
	GLfloat z;
}vector_struct;
typedef struct point_struct
{
	GLfloat x;
	GLfloat y;
	GLfloat z;
	GLint count;
	vector_struct normal_vector_struct;
}point_struct;
typedef struct indextable
{
	unsigned int first;
	unsigned int second;
	unsigned int third;
}indextable;
GLfloat light0_pos[] = { 10.0, 10.0, 10.0, 1.0 };
GLfloat ambient0[] = { 0.5f, 0.5f, 0.5f, 1.0f };
GLfloat diffuse0[] = { 0.8f, 0.8f,0.8f, 1.0f };
GLfloat specular0[] = { 0.4f, 0.4f, 0.4f, 1.0f };
GLfloat mat_ambient[] = { 0.7f, 0.7f, 0.7f, 1.0f };
GLfloat mat_diffuse[] = { 0.7f, 0.7f, 0.7f, 1.0f };
GLfloat mat_specular[] = { 0.2f,0.2f,0.2f,1.0f };
GLfloat degree_x, degree_y;
GLfloat radius = 3;
point_struct * p;
vector_struct temp;
indextable * index;
GLfloat max_len;
GLfloat max_x = -FLT_MAX;
GLfloat min_x = FLT_MAX;
GLfloat max_y = -FLT_MAX;
GLfloat min_y = FLT_MAX;
GLfloat max_z = -FLT_MAX;
GLfloat min_z = FLT_MAX;
GLfloat default_ortho = 0.5f;
GLfloat default_fovy = 20.0f;
int mouse_state = 0;
int origin_x, origin_y;
int pointerNumber;
int facenum;
int dim;
int ww = 500, wh = 500;
vector_struct face_vector_struct(int i)
{
	vector_struct temp1;
	vector_struct temp2;
	vector_struct re;
	temp1.x = p[index[i].second].x - p[index[i].first].x;
	temp1.y = p[index[i].second].y - p[index[i].first].y;
	temp1.z = p[index[i].second].z - p[index[i].first].z;
	temp2.x = p[index[i].third].x - p[index[i].first].x;
	temp2.y = p[index[i].third].y - p[index[i].first].y;
	temp2.z = p[index[i].third].z - p[index[i].first].z;
	re.x = temp1.y*temp2.z - temp1.z*temp2.y;
	re.y = temp1.z*temp2.x - temp1.x*temp2.z;
	re.z = temp1.x*temp2.y - temp1.y*temp2.x;
	return re;
}

void mousewheel(int button, int dir, int x, int y);
void set_light();
void set_material(void);
void rendering(void);
void display();
void myReshape(int w, int h);
void Load_file(const char*filename);
void normalize();
void init();
void mouse(int button, int state, int x, int y);
void mousewheel(int button, int dir, int x, int y);
void mouse_move(int x, int y);

int main(int argc, char **argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH);
	glutInitWindowSize(ww, wh);
	glutInitWindowPosition(0, 0);
	glutCreateWindow("3D Model Viewer");
	init();
	glutDisplayFunc(display);
	glutMouseFunc(mouse);
	glutMotionFunc(mouse_move);
	glutMouseWheelFunc(mousewheel);
	glutReshapeFunc(myReshape);

	glutMainLoop();

}
void set_light()
{
	glLightfv(GL_LIGHT0, GL_AMBIENT, ambient0);
	glLightfv(GL_LIGHT0, GL_DIFFUSE, diffuse0);
	glLightfv(GL_LIGHT0, GL_SPECULAR, specular0);
	glLightfv(GL_LIGHT0, GL_POSITION, light0_pos);
	glEnable(GL_LIGHT0);
}
void set_material(void)
{
	glMaterialfv(GL_FRONT, GL_DIFFUSE, mat_diffuse);
	glMaterialfv(GL_FRONT, GL_AMBIENT, mat_ambient);
	glMaterialfv(GL_FRONT, GL_SPECULAR, mat_specular);
	glMaterialf(GL_FRONT, GL_SHININESS, 20);
}

void rendering(void)
{
	set_material();
	glPushMatrix();
	glTranslatef((max_x + min_x) / -2, (max_y + min_y) / -2, (max_z + min_z) / -2);

	for (int i = 0; i < facenum; i++)
	{
		glBegin(GL_TRIANGLES);

		glNormal3f(p[index[i].first].normal_vector_struct.x, p[index[i].first].normal_vector_struct.y, p[index[i].first].normal_vector_struct.z);
		glVertex3f(p[index[i].first].x, p[index[i].first].y, p[index[i].first].z);

		glNormal3f(p[index[i].second].normal_vector_struct.x, p[index[i].second].normal_vector_struct.y, p[index[i].second].normal_vector_struct.z);
		glVertex3f(p[index[i].second].x, p[index[i].second].y, p[index[i].second].z);
		glNormal3f(p[index[i].third].normal_vector_struct.x, p[index[i].third].normal_vector_struct.y, p[index[i].third].normal_vector_struct.z);
		glVertex3f(p[index[i].third].x, p[index[i].third].y, p[index[i].third].z);
		glEnd();
	}
	glPopMatrix();
}

void display()
{
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	set_light();
	rendering();
	glFlush();
	glutSwapBuffers();
}
void myReshape(int w, int h)
{
	ww = w;
	wh = h;

	GLfloat camX = radius * cosf(Degree_to_Rad*degree_y)*sinf(Degree_to_Rad*degree_x);
	GLfloat camY = radius * sinf(Degree_to_Rad*degree_y);
	GLfloat camZ = radius * cosf(Degree_to_Rad*degree_y)*cosf(Degree_to_Rad*degree_x);

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	glViewport(0, 0, w, h);
	gluPerspective(default_fovy, w / h, 1, -1);

	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	gluLookAt(camX, camY, camZ, 0, 0, 0, 0, 1, 0);

	glutPostRedisplay();
}
void Load_file(const char*filename)
{
	FILE*fp;
	int i;
	temp.x = temp.y = temp.z = 0;
	fp = fopen(filename, "rt");
	if (fp == NULL)
	{
		printf("Read Error\n");
		exit(0);
	}
	else
	{
		fscanf_s(fp, "%d %d\n", &pointerNumber, &facenum);

		p = new point_struct[pointerNumber];
		for (i = 0; i<pointerNumber; i++)
		{
			p[i].count = 0;
			p[i].normal_vector_struct.x = p[i].normal_vector_struct.y = p[i].normal_vector_struct.z = 0;
		}
		index = new indextable[facenum];

		float start, end;

		start = (float)clock();
		for (i = 0; i < pointerNumber; i++)
		{
			fscanf_s(fp, "%f %f %f\n", &p[i].x, &p[i].y, &p[i].z);

			if (p[i].x > max_x)
				max_x = p[i].x;
			else if (p[i].x < min_x)
				min_x = p[i].x;

			if (p[i].y > max_y)
				max_y = p[i].y;
			else if (p[i].y < min_y)
				min_y = p[i].y;

			if (p[i].z > max_z)
				max_z = p[i].z;
			else if (p[i].z < min_z)
				min_z = p[i].z;
		}
		end = (float)clock();
		printf("point_struct load %f ms\n", end - start);
		if (max_x - min_x > max_y - min_y)
		{
			if (max_x - min_x > max_z - min_z)
				max_len = max_x - min_x;
			else
				max_len = max_z - min_z;
		}
		else
		{
			if (max_y - min_y > max_z - min_z)
				max_len = max_y - min_y;
			else
				max_len = max_z - min_z;
		}

		start = (float)clock();
		for (i = 0; i < facenum; i++)
		{
			fscanf_s(fp, "%d", &dim);
			if (dim == 3)
			{
				fscanf_s(fp, "%d %d %d\n", &index[i].first, &index[i].second, &index[i].third);
				p[index[i].first].count++;
				p[index[i].second].count++;
				p[index[i].third].count++;

				temp = face_vector_struct(i);

				p[index[i].first].normal_vector_struct.x += temp.x;
				p[index[i].first].normal_vector_struct.y += temp.y;
				p[index[i].first].normal_vector_struct.z += temp.z;

				p[index[i].second].normal_vector_struct.x += temp.x;
				p[index[i].second].normal_vector_struct.y += temp.y;
				p[index[i].second].normal_vector_struct.z += temp.z;

				p[index[i].third].normal_vector_struct.x += temp.x;
				p[index[i].third].normal_vector_struct.y += temp.y;
				p[index[i].third].normal_vector_struct.z += temp.z;
			}
		}
		end = (float)clock();
		printf("face load %f ms\n", end - start);
		printf("Load Complete \n", pointerNumber, facenum);
	}
}
void normalize()
{
	for (int i = 0; i < pointerNumber; i++)
	{
		p[i].x /= max_len;
		p[i].y /= max_len;
		p[i].z /= max_len;

		p[i].normal_vector_struct.x /= p[i].count;
		p[i].normal_vector_struct.y /= p[i].count;
		p[i].normal_vector_struct.z /= p[i].count;
	}
	max_x /= max_len;
	max_y /= max_len;
	max_z /= max_len;
	min_x /= max_len;
	min_y /= max_len;
	min_z /= max_len;
}
void init()
{
	Load_file("cow.txt");
	normalize();
	glEnable(GL_NORMALIZE);
	glEnable(GL_DEPTH_TEST);
	glEnable(GL_LIGHTING);
}
void mouse(int button, int state, int x, int y)
{
	if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN)
	{
		if (x < ww&&y < wh)
		{
			origin_x = x;
			origin_y = y;
			mouse_state = 1;
		}
	}
	else if (state == GLUT_UP)
	{
		mouse_state = 0;
	}
}
void mouse_move(int x, int y)
{
	if (mouse_state == 1)
	{
		degree_x += (GLfloat)((origin_x - x) * 360 / wh);
		degree_y -= (GLfloat)((origin_y - y) * 360 / ww);

		if (degree_x > 360 || degree_x < -360)
			degree_x = 0;
		if (degree_y > 360 || degree_y < -360)
			degree_y = 0;
		origin_x = x;
		origin_y = y;
		myReshape(ww, wh);
	}
}
void mousewheel(int button, int dir, int x, int y)
{
	if (dir > 0)
	{
		default_ortho *= 0.9f;
		default_fovy *= 0.9f;
		myReshape(ww, wh);
	}
	else
	{
		default_ortho *= 1.1f;
		default_fovy *= 1.1f;
		myReshape(ww, wh);
	}
}