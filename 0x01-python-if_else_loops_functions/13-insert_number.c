#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 *insert_node - inserts a number into a sorted singly linked list
 *@head: head of the linked list
 *@number: number to insert
 *Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *nodo;
	listint_t *nuevo_nodo;

	nodo = *head;

	nuevo_nodo = malloc(sizeof(listint_t));

	if (nuevo_nodo == NULL)
		return (NULL);

	nuevo_nodo->n = number;

	if (nodo == NULL || nodo->n >= number)
	{
		nuevo_nodo->next = nodo;
		*head = nuevo_nodo;
		return (nuevo_nodo);
	}

	while (nodo && nodo->next && nodo->next->n < number)
		nodo = nodo->next;

	nuevo_nodo->next = nodo->next;
	nodo->next = nuevo_nodo;

	return (nuevo_nodo);
}
