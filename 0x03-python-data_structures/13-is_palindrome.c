#include "lists.h"

/**
 * is_palindrome - determines if a singly linked list is a palindrome
 * @head: pointer to pointer of head of the list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *rev = NULL, *temp2, *temp = *head;
	size_t numnodes = 0, i = 0;

	if (!temp || !temp->next)
		return (1);
	while (temp)
	{
		add_nodeint(&rev, temp->n);
		temp = temp->next;
		numnodes++;
	}
	if (numnodes % 2)
		numnodes /= 2;
	else
		numnodes = (numnodes / 2) + 1;
	temp = *head;
	temp2 = rev;
	for (i = 0; i < numnodes; i++)
	{
		if (temp->n != temp2->n)
		{
			free_listint(rev);
			return (0);
		}
		temp = temp->next;
		temp2 = temp2->next;
	}
	free_listint(rev);
	return (1);
}
/**
 * add_nodeint - adds a node to the head of a list
 * @head: pointer to pointer of head of list
 * @n: value to add
 * Return: address of new node
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);
	new->n = n;
	if (!*head)
		new->next = NULL;
	else
		new->next = *head;
	*head = new;
	return (new);
}


