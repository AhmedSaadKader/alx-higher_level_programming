#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: singly linked list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
*/

int check_cycle(listint_t *list)
{

	listint_t *current, *first;

	first = list;
	current = first->next;
	while (current != NULL)
	{
		current = current->next;
		if (current == first)
		{
			return (1);
		}
	}
	return (0);
}
