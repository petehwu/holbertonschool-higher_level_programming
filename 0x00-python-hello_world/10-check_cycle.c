#include "lists.h"

/**
 * check_cycle - checks the list to see if there is circular link
 * @list: linked likst to check
 * Return: 0 if not circular 1 is circular
 */
int check_cycle(listint_t *list)
{
	listint_t *normal, *skipper;

	if (!list)
		return (0);
	normal = list;
	skipper = list;
	do {
		if (skipper->next && skipper->next->next)
			skipper = skipper->next->next;
		else
			break;
		if (normal == skipper)
			return (1);
		normal = normal->next;

	} while (normal && skipper);
	return (0);

}
