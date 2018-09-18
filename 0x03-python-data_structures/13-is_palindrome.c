#include "lists.h"

/**
 * is_palindrome - determines if a singly linked list is a palindrome
 * @head: pointer to pointer of head of the list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	size_t numnodes = 0, i = 0, j = 0;
	int vals[1024];

	if (!temp || !temp->next)
		return (1);
	while (temp)
	{
		vals[numnodes] = temp->n;
		numnodes++;
		temp = temp->next;
	}
	numnodes--;
	for (i = 0, j = numnodes; i < j; i++, j--)
	{
		if (vals[i] != vals[j])
			return (0);
	}
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


