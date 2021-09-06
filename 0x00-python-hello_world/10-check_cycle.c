#include "lists.h"

/**
 *check_cycle -  checks if a singly linked list has a cycle in it
 *@list: linked list
 *Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tortuga = list->next;
	listint_t *liebre = list->next->next;

	while (tortuga != NULL && liebre != NULL)
	{
		tortuga = tortuga->next;
		if (tortuga == NULL)
			return (0);
		tortuga = tortuga->next;
		liebre = liebre->next->next;
		if (tortuga == liebre)
			return (1);
	}
	return (0);
}
