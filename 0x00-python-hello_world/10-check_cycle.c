#include "lists.h"
/** 
 * check_cycle -  Check if loop in linked list
 * @list: List
 * Return - int
*/
int check_cycle(listint_t *list)
{

    listint_t *temp1, *temp2;
    if (list == NULL)
        return (0);
    temp1 = list;
    temp2 = list;
 
    while (temp1 != NULL && temp2->next != NULL && temp2)
    {
        temp1 = temp1->next;
        if (temp2->next->next != NULL)
            temp2 = temp2->next->next;
        else
            temp2 = temp2->next;
        if (temp1 == temp2)
        {
            return (1);                                  
        }                                     
    }
    return (0);
}
