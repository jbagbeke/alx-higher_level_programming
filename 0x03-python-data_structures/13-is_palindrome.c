#include "lists.h"
/**
 * is_palindrome - checks if a list is a palindrome
 * @head: Pointer to first node of the list
 * Return: 1 if a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast = *head, *slow = *head, *current, *next, *prev = NULL;
	listint_t *prev_list = NULL, *current1 = *head, *current2;

	if (*head == NULL || *head->next == NULL)
		return (1);
	while (fast != NULL && fast->next != NULL)
	{
		prev_list = slow;
		slow = slow->next;
		fast = fast->next->next;
	}
	if (fast != NULL)
		slow = slow->next;

	prev_list->next = NULL;
	current = slow;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	current2 = prev;
	while (current1 != NULL && current2 != NULL)
	{
		if (current1->n != current2->n)
			return (0);

		current1 = current1->next;
		current2 = current2->next;
	}
	return (1);
}
