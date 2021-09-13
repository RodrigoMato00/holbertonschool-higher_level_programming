#include "lists.h"

/**
 *is_palindrome - checks if a singly linked list is a palindrome
 *@head: head of a linked list
 *Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	unsigned int num;
	listint_t *i;

	if (!head || !*head)
		return (1);

	i = *head;
	num = 1;

	while (i)
	{
		i = i->next;
		num++;
	}
	return (0);
}
