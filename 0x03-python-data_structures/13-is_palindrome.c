#include "lists.h"
int is_palindrome(listint_t **head)
{
int len = 0, i, j, array[3000];
if (!head || !(*head) || (*head)->next == NULL)
{
return (1);
}
while (*head)
{
array[len] = (*head)->n;
*head = (*head)->next;
len++;
}
for (i = 0, j = len - 1; i < len / 2 + 1; i++, j--)
{
if (array[i] != array[j])
{
return (0);
}
}
return (1);
}
