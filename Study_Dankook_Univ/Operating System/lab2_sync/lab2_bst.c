
/*

*    Operating System Lab

*        Lab2 (Synchronization)

*        Student id : 32151648 / 32155068

*        Student name : 박동학 / 홍승기

*

*   lab2_bst.c :

*       - thread-safe bst code.

*       - coarse-grained, fine-grained lock code

*

*   Implement thread-safe bst for coarse-grained version and fine-grained version.

*/

 

#include <stdio.h>

#include <stdlib.h>

#include <assert.h>

#include <pthread.h>

#include <string.h>

#include <errno.h>
 

#include "lab2_sync_types.h"

pthread_mutex_t mutex; //mutex variable
pthread_mutex_t mutex2;//mutex variable
lab2_node *global_root; //delete_fg에서 사용할 글로벌 root

/*


 *  Implement funtction which traverse BST in in-order

 * 

 *  @param lab2_tree *tree  : bst to print in-order.

 *  @return                 : status (success or fail)

 */

int lab2_node_print_inorder(lab2_tree *tree) {

    // You need to implement lab2_node_print_inorder function.

    if (tree->root == NULL)

    {

        return LAB2_SUCCESS; // root가 비어 있으면 이를 반환 (재귀함수에서 사용)
    }

 

    else

    {

        lab2_tree *Templeft = (lab2_tree*)malloc(sizeof(lab2_tree));

        Templeft->root = tree->root->left; // 임시 트리를 구성하여 재귀적 

        lab2_node_print_inorder(Templeft);

 

//        printf(" %d ", tree->root->key);

 

        lab2_tree *Tempright = (lab2_tree*)malloc(sizeof(lab2_tree));

        Tempright->root = tree->root->right;

        lab2_node_print_inorder(Tempright);

    }

}

 

/*


 *  Implement function which creates struct lab2_tree

 *  ( refer to the ./include/lab2_sync_types.h for structure lab2_tree )

 *

 *  @return                 : bst which you created in this function.

 */

lab2_tree *lab2_tree_create() {

    // You need to implement lab2_tree_create function.

    lab2_tree *NewTree = (lab2_tree*)malloc(sizeof(lab2_tree)); // 트리를 

    NewTree->root = NULL; //루트를 NULL로 

    return NewTree; // 반환
}

 

/*


 *  Implement function which creates struct lab2_node

 *  ( refer to the ./include/lab2_sync_types.h for structure lab2_node )

 *

 *  @param int key          : bst node's key to creates

 *  @return                 : bst node which you created in this function.

 */

lab2_node * lab2_node_create(int key) {

    // You need to implement lab2_node_create function.

    lab2_node *NewNode = (lab2_node*)malloc(sizeof(lab2_node)); // 노드를 동적할당 
    NewNode->key = key;

    NewNode->left = NULL;

    NewNode->right = NULL;

    pthread_mutex_init(&NewNode->mutex, NULL); //구조체안에 있는 변수들 초기화 

    return NewNode;

}

 

/*


 *  Implement a function which insert nodes from the BST.

 * 

 *  @param lab2_tree *tree      : bst which you need to insert new node.

 *  @param lab2_node *new_node  : bst node which you need to insert.

 *  @return                 : satus (success or fail)

 */

int lab2_node_insert(lab2_tree *tree, lab2_node *new_node){

    // You need to implement lab2_node_insert function.

    lab2_node *pp = NULL; //부모의 부모 노드 

    lab2_node *p = tree->root; // 부모노드를 루트로 초기화 

 

    if (p == NULL)

    {

        tree->root = new_node; // 루트노드가 비어있으면 루트에 삽입 

        return LAB2_SUCCESS;

    }

 

    else

    {

        while (p) 

        {

            pp = p;

            if (new_node->key < p->key)

            {

                p = p->left;

            }

            else if (new_node->key == p->key)

            {

                return LAB2_ERROR;

            }

            else

            {

                p = p->right;

            }

        } // 조건 검사를 통해서 삽입해야할 위치를 

 

        if (new_node->key < pp->key)

        {

            pp->left = new_node;

        }

        else

        {

            pp->right = new_node;

        } // 큰것은 오른쪽으로 작은 것은 왼쪽으로 삽입 

    }

}

 

/*


 *  Implement a function which insert nodes from the BST in fine-garined manner.

 *

 *  @param lab2_tree *tree      : bst which you need to insert new node in fine-grained manner.

 *  @param lab2_node *new_node  : bst node which you need to insert.

 *  @return                     : status (success or fail)

 */

int lab2_node_insert_fg(lab2_tree *tree, lab2_node *new_node){

      // You need to implement lab2_node_insert_fg function.

    pthread_mutex_lock(&mutex); // 초기화 부분을 lock
    lab2_node *pp = NULL;
    lab2_node *p = tree->root;
    pthread_mutex_unlock(&mutex);
 

    if (p == NULL)

    {
        pthread_mutex_lock(&mutex);// 초기화 부분을 lock
        tree->root = new_node;
        pthread_mutex_unlock(&mutex);
        return LAB2_SUCCESS;

    }

 

    else

    {

        while (p)

        {

            pp = p;

            if (new_node->key < p->key)

            {
                pthread_mutex_lock(&mutex);
                p = p->left;
                pthread_mutex_unlock(&mutex);
            }

            else if (new_node->key == p->key)

            {
                pthread_mutex_lock(&mutex);
                pthread_mutex_unlock(&mutex);
                return LAB2_ERROR;

            }

            else

            {
                pthread_mutex_lock(&mutex);
                p = p->right;
                pthread_mutex_unlock(&mutex);
            }

        } //노드를 찾아가는 과정에서 발생하는 오류를 막기위해서 이동마다 lock

 

        if (new_node->key < pp->key)

        {
            pthread_mutex_lock(&mutex);
            pp->left = new_node;
            pthread_mutex_unlock(&mutex);
        }

        else

        {
            pthread_mutex_lock(&mutex);
            pp->right = new_node;
            pthread_mutex_unlock(&mutex);
        }

    } // 삽입하는 부분에서 다른 노드가 잘 못 삽입되지 않도록 lock

}

 

/*


 *  Implement a function which insert nodes from the BST in coarse-garined manner.

 *

 *  @param lab2_tree *tree      : bst which you need to insert new node in coarse-grained manner.

 *  @param lab2_node *new_node  : bst node which you need to insert.

 *  @return                     : status (success or fail)

 */

int lab2_node_insert_cg(lab2_tree *tree, lab2_node *new_node){

    // You need to implement lab2_node_insert_cg function.
    pthread_mutex_lock(&mutex); // 삽입 함수 전체에 대해서 lock  
    lab2_node *pp = NULL;
    lab2_node *p = tree->root;
     
    
    
    if (p == NULL)

    {
        tree->root = new_node;
        pthread_mutex_unlock(&mutex); //반환에 따라 unlock
        return LAB2_SUCCESS;
    }

    else
    {
           
   
        while (p)

        {

            pp = p;

            if (new_node->key < p->key)

            {

                p = p->left;
               
               

            }

            else if (new_node->key == p->key)

            {
               
                pthread_mutex_unlock(&mutex);//반환에 따라 unlock
                return LAB2_ERROR;
            }   

            else

            {

                p = p->right;
               
               
           
            }

        }
       
 
       
        
        if (new_node->key < pp->key)

        {

            pp->left = new_node;
           
            pthread_mutex_unlock(&mutex);//반환에 따라 unlock
	    return LAB2_SUCCESS;
        }

        else

        {

            pp->right = new_node;
            pthread_mutex_unlock(&mutex);//반환에 따라 unlock
	    return LAB2_SUCCESS;

        }
       
       
    }
    pthread_mutex_unlock(&mutex);//함수 종료에 따라 unlock
}

 

/*

 *

 *  Implement a function which remove nodes from the BST.

 *

 *  @param lab2_tree *tree  : bst tha you need to remove node from bst which contains key.

 *  @param int key          : key value that you want to delete.

 *  @return                 : status (success or fail)

 */

int lab2_node_remove(lab2_tree *tree, int key) {

    // You need to implement lab2_node_remove function.

 
   
    lab2_node *pp = NULL; //부모의 부모 

    lab2_node *p = tree->root; //부모노드를 루트노드로 초기화 

    if (p == NULL)

    {

        return LAB2_ERROR;//p가 비어있으면 에러 리턴

    }

    while (p != '\0' && p->key != key) //삭제 위치를 찾아가는 과정

    {

        pp = p; //pp에 p의 위치를 넣어줌

        if (p->key < key) //찾는 값이 노드의 값보다 클경우

        {

            p = p->right;

        }

        else if (p->key > key) //반대경우

        {

            p = p->left;

        }

    }

    if (p == NULL) //p가 비어있는지 한번더 검사

    {

        return LAB2_ERROR;

    }

    if (p->left != '\0' && p->right != '\0') //2개의 자식이 있을 경우

    {

        lab2_node *s = p->left; //왼쪽 자식을 줌

        lab2_node *ps = p; //ps에 p를 대입해줌

 

        while (s->right != '\0') //왼쪽 서브트리의 최대값을 찾는 과정

        {

            ps = s;

            s = s->right;

        }

 

        p->key = s->key;

        p = s;

        pp = ps;

    }

 

    lab2_node *temp = (lab2_node*)malloc(sizeof(lab2_node)); //템프 노드를 동적 생성

    if (p->left == '\0') //p의 왼쪽 자식이 없는 경우

    {

        temp = p->right; //temp에 오른쪽 자식을 줌

    }

    else//반대경우

    {

        temp = p->left;

    }

 

    if (p == tree->root) //p가 루트 노드일때
        {
                tree->root = temp;
                lab2_node_delete(p);
        }
    else //반대 경우

    {

        if (p == pp->left)

        {

            pp->left = temp;
                        lab2_node_delete(p);
 

        }

        else
                {
                      pp->right = temp;
                      lab2_node_delete(p);
                }
    }
}

 

/*


 *  Implement a function which remove nodes from the BST in fine-grained manner.

 *

 *  @param lab2_tree *tree  : bst tha you need to remove node in fine-grained manner from bst which contains key.

 *  @param int key          : key value that you want to delete.

 *  @return                 : status (success or fail)

 */
lab2_node *del_search(int key, lab2_node* root) // 삭제할 위치를 찾는 함수 

{

	if (key == root->key)

	{

		return root;

	}

	else if (key < root->key)

	{

		if (root->left == NULL)

		{

			pthread_mutex_unlock(&root->mutex);

			return NULL;

		}

		else

		{

			pthread_mutex_lock(&root->left->mutex);

			if (key == root->left->key)

			{

				return root->left;

			}

			else

			{

				pthread_mutex_unlock(&root->mutex);

				return del_search(key, root->left);

			}

		}

	}

 

	else {

		if (root->right == NULL)

		{

			/*

			* Could not find the node, unlock current root and return

			*/

			pthread_mutex_unlock(&root->mutex);

			return NULL;

		}

		else

		{

			pthread_mutex_lock(&root->right->mutex);

			if (key == root->right->key)

			{

				return root->right;

			}

			else

			{

				pthread_mutex_unlock(&root->mutex);

				return del_search(key, root->right);

			}

		}

	}

	return NULL;

}


int lab2_node_remove_fg(lab2_tree *tree, int key)

 

{

 

	lab2_node *to_be_deleted, *parent, *successor_parent, *successor; //탐색을 위한 노드들 

 

	lab2_node *predecessor, *predecessor_parent;

 

 

 

	pthread_mutex_lock(&mutex);

 

	if (global_root == NULL) {

 

		pthread_mutex_unlock(&mutex);

 

		return LAB2_ERROR;

 

	}

 

 

 

	tree->root = global_root;

 

	pthread_mutex_lock(&tree->root->mutex);

 

 

 

	if (key == tree->root->key && tree->root->left == NULL && tree->root->right == NULL) {

 

 

 

		free(tree->root);

 

		global_root = NULL;

 

		pthread_mutex_unlock(&mutex);

 

		return 0;

 

	}

 

 

 

	to_be_deleted = del_search(key, tree->root);

 

	if (to_be_deleted == NULL) {

 

 

 

		pthread_mutex_unlock(&mutex);

 

		return 0;

 

	}

 

 

 

	parent = to_be_deleted->parent;

 

 

 

	if (to_be_deleted->left == NULL && to_be_deleted->right == NULL && parent == NULL)

 

	{

 

		free(to_be_deleted);

 

		global_root = NULL;

 

		pthread_mutex_unlock(&mutex);

 

		return 0;

 

	}

 

 

 

	pthread_mutex_unlock(&mutex);

 

	if (to_be_deleted->left == NULL && to_be_deleted->right == NULL) {

 

		if (to_be_deleted->key < parent->key) {

 

 

 

			free(to_be_deleted);

 

			parent->left = NULL;

 

			pthread_mutex_unlock(&parent->mutex);

 

			return 0;

 

		}

		else {

 

 

 

			free(to_be_deleted);

 

			parent->right = NULL;

 

			pthread_mutex_unlock(&parent->mutex);

 

			return 0;

 

		}

 

	}

 

 

 

 

 

	if (parent != NULL) {

 

		pthread_mutex_unlock(&parent->mutex);

 

	}

 

 

 

	if (to_be_deleted->right != NULL) {

 

		pthread_mutex_lock(&to_be_deleted->right->mutex);

 

		if (to_be_deleted->right->left == NULL) {

 

 

 

			successor = to_be_deleted->right;

 

 

 

			if (successor->right != NULL) {

 

				pthread_mutex_lock(&successor->right->mutex);

 

				to_be_deleted->key = successor->key;

 

				to_be_deleted->right = successor->right;

 

				successor->right->parent = to_be_deleted;

 

				pthread_mutex_unlock(&successor->right->mutex);

 

			}

			else {

 

				to_be_deleted->key = successor->key;

 

				to_be_deleted->right = NULL;

 

			}

 

			free(successor);

 

			pthread_mutex_unlock(&to_be_deleted->mutex);

 

			return 0;

 

		}

 

 

 

		successor = get_inorder_successor(to_be_deleted);

 

		successor_parent = successor->parent;

 

 

 

		if (successor->right != NULL) {

 

			pthread_mutex_lock(&successor->right->mutex);

 

			successor_parent->left = successor->right;

 

			successor->right->parent = successor_parent;

 

			to_be_deleted->key = successor->key;

 

			pthread_mutex_unlock(&successor->right->mutex);

 

		}

		else {

 

			to_be_deleted->key = successor->key;

 

			successor_parent->left = NULL;

 

		}

 

 

 

		free(successor);

 

		pthread_mutex_unlock(&successor_parent->mutex);

 

		pthread_mutex_unlock(&to_be_deleted->mutex);

 

		return 0;

 

	}

 

 

 

	if (to_be_deleted->left != NULL) {

 

		pthread_mutex_lock(&to_be_deleted->left->mutex);

 

 

 

		if (to_be_deleted->left->right == NULL) {

 

 

 

			predecessor = to_be_deleted->left;

 

 

 

			if (predecessor->left != NULL) {

 

				pthread_mutex_lock(&predecessor->left->mutex);

 

				to_be_deleted->key = predecessor->key;

 

				to_be_deleted->left = predecessor->left;

 

				predecessor->left->parent = to_be_deleted;

 

				pthread_mutex_unlock(&predecessor->left->mutex);

 

			}

			else {

 

				to_be_deleted->key = predecessor->key;

 

				to_be_deleted->left = NULL;

 

			}

 

 

 

			free(predecessor);

 

			pthread_mutex_unlock(&to_be_deleted->mutex);

 

			return 0;

 

		}

 

 

 

		predecessor = get_inorder_predecessor(to_be_deleted);

 

		predecessor_parent = predecessor->parent;

 

 

 

		if (predecessor->left != NULL) {

 

			pthread_mutex_lock(&predecessor->left->mutex);

 

			predecessor_parent->right = predecessor->left;

 

			predecessor->left->parent = predecessor_parent;

 

			to_be_deleted->key = predecessor->key;

 

			pthread_mutex_unlock(&predecessor->left->mutex);

 

		}

		else {

 

			to_be_deleted->key = predecessor->key;

 

			predecessor_parent->right = NULL;

 

		}

 

		free(predecessor);

 

		pthread_mutex_unlock(&predecessor_parent->mutex);

 

		pthread_mutex_unlock(&to_be_deleted->mutex);

 

		return 0;

 

	}

 

 

 

	return LAB2_ERROR;

 

}


lab2_node *get_inorder_successor(lab2_node *node)

{

	lab2_node *parent, *successor;

 

	parent = node->right;

	successor = parent->left;

 

	pthread_mutex_lock(&successor->mutex);

 

	while (successor->left != NULL) {

		successor = successor->left;

		pthread_mutex_unlock(&parent->mutex);

		pthread_mutex_lock(&successor->mutex);

		parent = successor->parent;

	}

 

	return successor;

}

 

 

lab2_node *get_inorder_predecessor(lab2_node *node)

{

	lab2_node *parent, *predecessor;

 

	parent = node->left;

	predecessor = parent->right;

 

	pthread_mutex_lock(&predecessor->mutex);

 

	while (predecessor->right != NULL) {

		predecessor = predecessor->right;

		pthread_mutex_unlock(&parent->mutex);

		pthread_mutex_lock(&predecessor->mutex);

		parent = predecessor->parent;

	}

 

	return predecessor;

}



 

 

/*

 *

 *  Implement a function which remove nodes from the BST in coarse-grained manner.

 *

 *  @param lab2_tree *tree  : bst tha you need to remove node in coarse-grained manner from bst which contains key.

 *  @param int key          : key value that you want to delete.

 *  @return                 : status (success or fail)

 */

int lab2_node_remove_cg(lab2_tree *tree, int key) {

    // You need to implement lab2_node_remove_cg function.

    pthread_mutex_lock(&mutex); // 전체적으로 lock을 걸어 구현한다.
    lab2_node *pp = NULL;

    lab2_node *p = tree->root;
   

    if (p == NULL)

    {
   
       
        pthread_mutex_unlock(&mutex);   
        return LAB2_ERROR;
       
    }

    while (p != '\0' && p->key != key)

    {
       
        pp = p;

        if (p->key < key)

        {

            p = p->right;

        }

        else if (p->key > key)

        {

            p = p->left;

        }
       
    }
   

    if (p == NULL)

    {
        pthread_mutex_unlock(&mutex);   

        return LAB2_ERROR;

    }
   
    if (p->left != '\0' && p->right != '\0')

    {
       
        lab2_node *s = p->left;

        lab2_node *ps = p;

 

        while (s->right != '\0')

        {

            ps = s;

            s = s->right;

        }

 

        p->key = s->key;

        p = s;

        pp = ps;
       
    }
   
 

    lab2_node *temp = (lab2_node*)malloc(sizeof(lab2_node));
   
    if (p->left == '\0')

    {

        temp = p->right;

    }

    else
        {

        temp = p->left;

    }

 

    if (p == tree->root)
        {
        tree->root = temp;
        }
    else
        {

        if (p == pp->left)

        {

            pp->left = temp;

 

        }

        else pp->right = temp;

    }
    lab2_node_delete(p);
    pthread_mutex_unlock(&mutex);   
}

 

 

/*

 *

 *  Implement function which delete struct lab2_tree

 *  ( refer to the ./include/lab2_sync_types.h for structure lab2_node )

 *

 *  @param lab2_tree *tree  : bst which you want to delete.

 *  @return                 : status(success or fail)

 */

void lab2_tree_delete(lab2_tree *tree) {

    // You need to implement lab2_tree_delete function.

    free(tree);
    tree->root = NULL;
    // tree의 동적할당을 해제한다.
}

 

/*

 *

 *  Implement function which delete struct lab2_node

 *  ( refer to the ./include/lab2_sync_types.h for structure lab2_node )

 *

 *  @param lab2_tree *tree  : bst node which you want to remove.

 *  @return                 : status(success or fail)

 */

void lab2_node_delete(lab2_node *node) {
        free(node); //동적할당을 free해준다.
        node=NULL;
}

