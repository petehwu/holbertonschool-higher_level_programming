#include "lists.h"
/**
 * insert_node - inserts a node into sorted linked list
 * @head: pointer to pointer to head of list
 * @number: number to insert into list
 * Return: address of new node or NULL if ailed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *newnode;

	newnode = malloc(sizeof(listint_t));
	if (!newnode)
		return (NULL);
	newnode->n = number;
	newnode->next = NULL;
	if (!*head)
	{
		*head = newnode;
		return (newnode);
	}
	node = *head;
	do {
		if (number <= node->n)
		{
			newnode->next = node;
			*head = newnode;
			return (newnode);
		}
		else if (node->next && number <= node->next->n)
		{
			newnode->next = node->next;
			node->next = newnode;
			return (newnode);
		}
		node = node->next;
	} while (node);
	free(newnode);
	return (add_nodeint_end(head, number));

}
