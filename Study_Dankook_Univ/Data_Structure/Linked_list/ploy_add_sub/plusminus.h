#ifndef _PLUSMINUS_
#define _PLUSMINUS_
typedef struct node {
	double coef;
	int exp;
	struct node*link;
}NODE;

void addNode(NODE **head, double coef, int exp);

NODE * SumPoly(NODE *a, NODE *b);

NODE * DiffPoly(NODE *a, NODE *b);

void showList(NODE *head);


#endif