#include "lists.h"
int is_palindrome(listint_t **head)
{
        listint_t *temp = *head;
        int len = 0, i;

        if (head == NULL || *head == NULL)
                return (0);
        
        while (*head[len] != NULL)
                len++;

        for (i = 0; i < len; i++)
        {
                if (temp[i]->n != temp[i - len - 1]->n)
                {
                        return (0);
                }
        }

        return (1);
}
