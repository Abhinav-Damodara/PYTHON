#include<stdlib.h>

#include<stdio.h>

struct Node {
  int data;
  struct Node * next;
};
void deletion(struct Node ** head) {
  struct Node * temp = * head;
  if (* head == NULL) {
    printf("Not Possible");
    return;
  }
  * head = ( * head) -> next;
  printf("Done Deleting:  %d\n", temp -> data);
  free(temp);
}
void insertion(struct Node ** head, int data) {
  struct Node * newNode = (struct Node * ) malloc(sizeof(struct Node));
  newNode -> data = data;
  newNode -> next = * head;
  * head = newNode;
  printf("Inserted: %d\n", newNode -> data);
}
void disp(struct Node * node) {
  printf("\nLinked List: ");
  while (node != NULL) {
    printf("%d ", node -> data);
    node = node -> next;
  }
  printf("\n");
}
int main() {
  struct Node * head = NULL;
  insertion(& head, 500);
  insertion(& head, 450);
  insertion(& head, 400);
  insertion(& head, 350);
  insertion(& head, 300);
  disp(head);
  deletion(& head);
  deletion(& head);
  disp(head);
  return 0;
}