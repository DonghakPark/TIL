/*
*	DKU Operating System Lab
*	    Lab2 (Synchronization)
*	    Student id : 32151648 / 32155068
*	    Student name : 박동학 / 홍승기
*
*/


#ifndef _LAB2_HEADER_H
#define _LAB2_HEADER_H

#include <pthread.h>

#define LAB2_SUCCESS                0
#define LAB2_ERROR                 -1

/*
 * lab2_node
 *
 *  struct lab2_node *left  : left child link
 *  struct lab2_node *right : right child link
 *  int key                 : node key value 
 */
typedef struct lab2_node {

    pthread_mutex_t mutex;
    struct lab2_node *left;
    struct lab2_node *right;
    struct lab2_node *parent; //delete fg 에서 사용한 node
    int key;

} lab2_node;

/*
 * lab2_tree
 *
 *  struct lab2_node *root  : root node of bst.
 */
typedef struct lab2_tree {
    struct lab2_node *root;
} lab2_tree;

/* 
 * lab2_bst_test.c related structure.  
 */
typedef struct thread_arg{
    pthread_t thread;
    lab2_tree *tree;
    int node_count;
    int num_iterations;
    int is_sync;
    int *data_set;
    int start;
    int end;
}thread_arg;

/* 
 * lab2_bst.c related functions 
 *
 *  You need to implement these functions. 
 */
int lab2_node_print_inorder(lab2_tree *tree);
lab2_tree *lab2_tree_create();
lab2_node *lab2_node_create(int key);
int lab2_node_insert(lab2_tree *tree, lab2_node *new_node);
int lab2_node_insert_fg(lab2_tree *tree, lab2_node *new_node);
int lab2_node_insert_cg(lab2_tree *tree, lab2_node *new_node);
int lab2_node_remove(lab2_tree *tree, int key);
int lab2_node_remove_fg(lab2_tree *tree, int key);
int lab2_node_remove_cg(lab2_tree *tree, int key);
void lab2_tree_delete(lab2_tree *tree);
void lab2_node_delete(lab2_node *node);
//아래 부분은 delete를 구현하는데 사용되는 함수이다.
lab2_node *del_search(int key, lab2_node* root);
lab2_node *get_inorder_predecessor(lab2_node *node);
lab2_node *get_inorder_successor(lab2_node *node);
/* lab2_timeval.c related function */
double get_timeval(struct timeval *tv, struct timeval *tv_end);

#endif /* LAB2_HEADER_H*/
