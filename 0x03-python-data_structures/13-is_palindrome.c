#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if linked list is palindrome or not.
 * @head: pointer to head of list
 *
 * Return: 0 if not a palindrome, and 1 if it's palindrome.
 */
int is_palindrome(listint_t **head)
{
listint_t *current;
int len_of_list = 0, i = 0;

if (*head == NULL)
{
return (1);
}

current = *head;
while (current != NULL)
{
current = current->next;
len_of_list++;
}

if (len_of_list % 2 != 0)
{
return (0);
}
else
{
half_list = len_of_list / 2;
}
}
