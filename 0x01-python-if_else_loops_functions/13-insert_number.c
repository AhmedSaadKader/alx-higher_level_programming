#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - inserts node at specific position
 * @head: the node to insert
 * @number: the n of the node
 *
 * Return: the address of the new node, or NULL if failed
*/

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	else
	{
		while (current->next != NULL && current->next->n < number)
		{
			current = current->next;
		}
		new->next = current->next;
		current->next = new;
	}
	return (new);
}
