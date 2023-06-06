#include "lists.h"

/**
 * check_cycle - check if singly linked list has a cycle
 * @list: pointer to the head
 * Return: 0 no cycle, 1 if cycle exists
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = NULL, *fast = NULL;

	/* Check for base cases */
	if (list == NULL || list->next == NULL)
		return (0);

	/* Initialize the two pointers */
	slow = list;
	fast = list->next;

	/* Loop until 'fast' pointer reaches end or becomes NULL */
	while (fast && fast->next)
	{
		/* If slow and fast meet, cycle is detected */
		if (slow == fast)
			return (1);
		slow = slow->next; /* One step forward */
		fast = fast->next->next; /* Two steps forward */
	}
	return (0); /* No cycle */
}
