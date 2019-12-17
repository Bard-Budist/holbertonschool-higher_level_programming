#include "lists.h"
/**
 * is_palindrome - ...
 * @head: ..
 * Return: ..
*/
int is_palindrome(listint_t **head)
{
        int len = 0, i;

        if (head == NULL || *head == NULL)
                return (0);
        
        while (head[len] != NULL)
                len++;

        for (i = 0; i < len; i++)
        {
                if ((*head[i]).n != (*head[i - len]).n)
                {
                        return (0);
                }
        }
        return (1);
}
