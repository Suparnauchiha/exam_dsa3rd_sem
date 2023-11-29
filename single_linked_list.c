#include<stdio.h>
#include<stdlib.h>

struct Node
{
  int data;
  struct Node *next;
};

void insertStart (struct Node **head, int data)
{

  // dynamically create memory for this newNode
  struct Node *newNode = (struct Node *) malloc (sizeof (struct Node));

  // assign data value
  newNode->data = data;
  // change the next node of this newNode 
  // to current head of Linked List
  newNode->next = *head;

  //re-assign head to this newNode
  *head = newNode;
}

void insertEnd (struct Node **head, int data)
{

  struct Node *newNode = (struct Node *) malloc (sizeof (struct Node));

  newNode->data = data;
  // since this will be the last node so it will point to NULL
  newNode->next = NULL;

  // if the Linked List is empty this is the first node being entered
  if (*head == NULL)
    {
      *head = newNode;
      return;
    }

  // create another variable to traverse the LL
  // *head should not be used as we do not want to change head
  struct Node *temp = *head;

  // traverse to the last node of Linked List
  while (temp->next != NULL)
    temp = temp->next;

  // assign last node's next to this newNode
  temp->next = newNode;
}

int getCurrSize (struct Node *node)
{
  int size = 0;

  while (node != NULL)
    {
      node = node->next;
      size++;
    }
  return size;
}

void insertPosition (int pos, int data, struct Node **head)
{
  int size = getCurrSize (*head);

  // Can only insert after 1st position
  // Can't insert if position to insert is greater than size of Linked List
  if (pos < 1 || pos > size)
    printf ("Invalid position to insert");

  else
    {
      struct Node *newNode = (struct Node *) malloc (sizeof (struct Node));
      newNode->data = data;
      newNode->next = NULL;

      // temp used to traverse the Linked List
      struct Node *temp = *head;

      // traverse till the nth node
      while (--pos)
	temp = temp->next;

      // assign newNode's next to nth node's next
      newNode->next = temp->next;
      // assign nth node's next to this new node
      temp->next = newNode;
      // newNode inserted b/w 3rd and 4th node
    }
}


void deleteStart (struct Node **head)
{
  struct Node *temp = *head;

  // if there are no nodes in Linked List can't delete
  if (*head == NULL)
    {
      printf ("Linked List Empty, nothing to delete");
      return;
    }

  // move head to next node
  *head = (*head)->next;
  free (temp);
}

void deleteEnd (struct Node **head)
{
  struct Node *temp = *head;
  struct Node *previous;

  // if there are no nodes in Linked List can't delete
  if (*head == NULL)
    {
      printf ("Linked List Empty, nothing to delete");
      return;
    }

  // if Linked List has only 1 node
  if (temp->next == NULL)
    {
      *head = NULL;
      return;
    }

  // else traverse to the last node
  while (temp->next != NULL)
    {
      // store previous link node as we need to change its next val
      previous = temp;
      temp = temp->next;
    }
  // Curr assign 2nd last node's next to Null
  previous->next = NULL;
  // delete the last node
  free (temp);
  // 2nd last now becomes the last node
}

// to delete nth node
void deletePosition (struct Node **head, int pos)
{
  struct Node *temp = *head;
  struct Node *previous;

  //if the head node itself needs to be deleted
  int size = getCurrSize (*head);

  // not valid
  if (pos < 1 || pos > size)
    {
      printf ("Enter valid position\n");
      return;
    }

  // delete the first node
  if (pos == 1)
    {
      deleteStart (head);
      return;
    }

  // traverse to the nth node
  while (--pos)
    {
      // store previous link node as we need to change its next val
      previous = temp;
      temp = temp->next;
    }
  // change previous node's next node to nth node's next node
  previous->next = temp->next;
  // delete this nth node
  free (temp);
}

void display (struct Node *node)
{

  // as linked list will end when Node is Null
  while (node != NULL)
    {
      printf ("%d ", node->data);
      node = node->next;
    }
  printf ("\n");
}

int main ()
{
  struct Node *head = NULL;

// Need '&' i.e. address as we need to change head
  insertStart (&head, 3);
  insertStart (&head, 12);
  insertStart (&head, 111);

  // no need for '&' as head need not be changed
  // only doing traversal
  display (head);

  insertEnd (&head, 335);
  insertEnd (&head, 6);
  insertEnd (&head, 87);

  display (head);

  //Inserts data: 4 after 3rd position
  insertPosition (3, 9000, &head);
  display (head);
  
  deleteStart (&head);
  display (head);

  deleteEnd (&head);
  display (head);

  // delete 3rd node
  deletePosition (&head, 3);
  display (head);

  // delete 1st node
  deletePosition (&head, 1);
  display (head);

  return 0;
}
