#include <stdio.h>
#include <stdlib.h>
#include "plusminus.h"

void addNode(NODE **head, double coef, int exp)
{
   NODE *p = *head;
   NODE *temp = (NODE*)malloc(sizeof(NODE));

   temp->coef = coef;
   temp->exp = exp;
   temp->link = NULL;

   if (*head == NULL)
   {
      *head = temp;
      return;
   }

   while (p->link)
      p = p->link;

   p->link = temp;
}

NODE * SumPoly(NODE *a, NODE *b)
{
   NODE *c = NULL;

   while (a || b)
   {
      if (a->exp > b->exp)
      {
         addNode(&c, a->coef, a->exp);

         a = a->link;
      }

      else if (a->exp == b->exp)
      {
         addNode(&c, a->coef + b->coef, a->exp);

         a = a->link;
         b = b->link;
      }

      else
      {
         addNode(&c, b->coef, b->exp);

         b = b->link;
      }
   }
   return c;
}

NODE * DiffPoly(NODE *a, NODE *b)
{
   NODE *c = NULL;

   while (a || b)
   {
      if (a->exp > b->exp)
      {
         addNode(&c, a->coef, a->exp);

         a = a->link;
      }

      else if (a->exp == b->exp)
      {
         addNode(&c, a->coef - b->coef, a->exp);

         a = a->link;
         b = b->link;
      }

      else
      {
         addNode(&c, -(b->coef), b->exp);

         b = b->link;
      }
   }
   return c;
}
void showList(NODE *head)
{
   NODE *p = head;

   while (p)
   {
      if (p->exp == -1)
      {
         break;
      }

      printf("%s%.2lfx^%d", p->coef >= 0 ? "+" : "", p->coef, p->exp);

      p = p->link;
   }
   printf("\n");
}