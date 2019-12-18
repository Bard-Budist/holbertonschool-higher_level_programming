#include "lists.h"
/**
 * is_palindrome - ...
 * @head: ..
 * Return: ..
*/
int is_palindrome(listint_t **head)
{
        int len = 0, i;
        listint_t *tem2 = *head, *tem1 = *head;
        if (head == NULL)
                return (0);
        if (*head == NULL || (*head)->next == NULL)
                return (1);

        while (tem2->next != NULL)
        {
                tem2 = tem2->next;
                len++;
        }
        if (len == 0)
                return (1);
        for (i = 0; i < len / 2; i++)
        {       
                if (tem1->n != tem2->n)
                {
                        return (0);
                }
                tem1++;
                --tem2;
        }
        return (1);
}
