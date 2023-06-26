#include "lists.h"

/**
 * is_palindrome - determine if singly linked list is palindrome
 * @head: pointer to head of singly linked list
 *
 * Description: This implementation uses the "runner technique"
 * The space complexity O(1)
 * Return: 0 if not, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head;
	listint_t *fast = *head;
	listint_t *prev = NULL;
	listint_t *next = NULL;

	if (head == NULL || *head == NULL)
		return (1); /* Empty list or single node list is palindrome */
	/* Find the middle of the linked list */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
	}
	/* If linked list odd number of nodes, move slow pointer one step */
	if (fast != NULL)
		slow = slow->next;
	/* Reverse the second half of the linked list */
	while (slow != NULL)
	{
		next = slow->next;
		slow->next = prev;
		prev = slow;
		slow = next;
	}
	/* Compare the first half and reversed second half of the linked list */
	slow = prev;
	fast = *head;
	while (slow != NULL)
	{
		if (fast->n != slow->n)
			return (0); /* Not a palindrome */
		fast = fast->next;
		slow = slow->next;
	}
	return (1); /* Palindrome */
}
