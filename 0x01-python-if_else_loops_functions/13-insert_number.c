#include "lists.h"
/**
 * insert_node - Insert node
 * @head: Head
 * @number: Number of node
 * Return: New node
*/
listint_t * insert_node (listint_t ** head, int number)
{
  listint_t *temporal = *head, *new_node;
  if (head == NULL)
    return (NULL);

  new_node = malloc(sizeof(listint_t));
  if (new_node == NULL)
    return (NULL);
  if (temporal->n >= number)
  {
    new_node->n = number;
    new_node->next = temporal;
    *head = new_node;
    return (new_node);
  }
  while (temporal != NULL)
  {
    if (temporal->next == NULL)
    {
      new_node->n = number;
      new_node->next = NULL;
      temporal->next = new_node;
      return (new_node);
    }
    if (temporal->next != NULL && temporal->next->n >= number)
    {
      new_node->n = number;
      new_node->next = temporal->next;
      temporal->next = new_node;
      return (new_node);
    }
    temporal = temporal->next;
  }
  free(new_node);
  return (NULL);
}
