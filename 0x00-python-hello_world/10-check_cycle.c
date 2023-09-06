#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * check_cycle - Checks if give list has cycle in it or not
 * @list: The list to be checked
 *
 * Return: 0 if there is no cycle, and 1 otherwise
 */
int check_cycle(listint_t *list)
{
int temp = list->n;

while (list->next != NULL)
{
if (list->next->n == temp)
{
return (1);
}
}
return (0);
}
