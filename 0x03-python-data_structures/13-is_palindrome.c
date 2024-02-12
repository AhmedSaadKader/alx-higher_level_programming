#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: the singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
*/

int is_palindrome(listint_t **head)
{
	listint_t *first;
	listint_t *mid = *head;
	listint_t *last = *head;
	int total_len = 0, i = 0, l = 0, f = 0, half_point;

	while (last != NULL)
	{
		last = last->next;
		total_len++;
	}
	if (total_len % 2 == 0)
		half_point = total_len / 2;
	else
		half_point = (total_len + 1) / 2;
	while (i != half_point)
	{
		mid = mid->next;
		i++;
	}
	i = 0;
	while (i != total_len - half_point)
	{
		last = mid;
		first = *head;
		l = 0;
		f = 0;
		while ((l != ((total_len - half_point) - (i + 1))) && (last->next != NULL))
		{
			last = last->next;
			l++;
		}
		while (f != i)
		{
			first = first->next;
			f++;
		}
		if (first->n != last->n)
			return (0);
		i++;
	}
	return (1);
}
