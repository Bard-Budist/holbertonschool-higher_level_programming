#include "lists.h"
/**
 * is_palindrome - ...
 * @head: ..
 * Return: ..
*/
int is_palindrome(listint_t **head)
{
        int len = 0, i;

        if (head == NULL)
                return (0);

        if  (*head == NULL || (*head)->next == NULL)
                return (1);
        
        while (head[len] != NULL)
                len++;

        for (i = 0; i < len; i++)
        {
                if ((*head[i]).n != (*head[len - 1 - i]).n)
                {
                        return (0);
                }
        }
        return (1);
}
