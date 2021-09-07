#include "lists.h"

/**
 *check_cycle -  checks if a singly linked list has a cycle in it
 *@list: linked list
 *Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tortuga;
	listint_t *liebre;

	/*if (list == NULL || list->next == NULL)
		return (0);*\

	tortuga = list->next;
	liebre = list->next->next;

	while (tortuga && liebre && liebre->next)
	{
		if (tortuga == liebre)
			return (1);

		tortuga = tortuga->next;
		liebre = liebre->next->next;
	}
	return (0);
}
