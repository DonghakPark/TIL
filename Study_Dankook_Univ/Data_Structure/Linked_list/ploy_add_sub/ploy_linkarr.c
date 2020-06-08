#include <stdio.h>
#include <stdlib.h>
#include "plusminus.h"
#pragma warning (disable:4996)

int main()
{
	double coef;
	int exp;
	NODE *a = NULL;
	NODE *b = NULL;
	NODE *c = NULL;

	printf("A 다항식의 계수(coef)와 지수(exp)를 입력하세요. expon이 -1이 되면 종료합니다.\n");

	while (1)
	{
		printf("coef: "); scanf("%lf", &coef);
		printf("exp: "); scanf("%d", &exp);

		addNode(&a, coef, exp);

		if (exp == -1)
			break;
	}

	printf("B 다항식의 계수(coef)와 지수(exp)를 입력하세요. expon이 -1이 되면 종료합니다.\n");

	while (1)
	{
		printf("coef: "); scanf("%lf", &coef);
		printf("exp: "); scanf("%d", &exp);

		addNode(&b, coef, exp);

		if (exp == -1)
			break;
	}
	printf("\nA 다항식\n");
	showList(a);
	printf("\nB 다항식\n");
	showList(b);
	c = SumPoly(a, b);
	printf("\nA+B의 결과 다항식\n");
	showList(c);
	c = DiffPoly(a, b);
	printf("\nA-B의 결과 다항식\n");
	showList(c);
	free(a);
	free(b);
	free(c);
	return 0;
}