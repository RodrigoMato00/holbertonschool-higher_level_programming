#include "lists.h"

/**
 *listint_t - ldkfjdkfjpdofkpdokdpokcsdpokcsdpokcsodpkcdopk
 *@head: sfldfkamdfamdfkadmzfkamdklmclddfadfdfad
 *@i: dlkfjadiofjaoidjfaiodjf
 *Return: pfkspodkspodkspdokspd
 */
listint_t *check_list(listint_t *head, listint_t *i)
{
	listint_t *j;

	if (i == NULL)
		return (head);

	else
	{
		j = check_list(head, i->next);

		if (j == NULL)
			return (NULL);

		if (j->n == i->n && j->next)
			return (i->next);

		else if (j->n == head->n)
			return (j);

		else
			return (NULL);
	}
	return (NULL);
}

/**
 *is_palindrome - dfjkdopfkpdfksdf
 *@head: odfjpdskfpodkfposdkf
 *Return: dfñksñdmfslkdmfslkmd
 */
int is_palindrome(listint_t **head)
{
	listint_t *i;

	if (head == NULL)
		return (0);
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	i = *head;
	if (check_list(*head, i))
		return (1);
	else
		return (0);
}
