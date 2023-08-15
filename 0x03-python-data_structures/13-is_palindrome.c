#include <lists.h>

/**
 * is_palindrome - Tests if a single linked list is a palindrome
 * @head: Pointer to the first node of the list
 * Return: 1 if is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast, *slow, *current, *next, *prev, *head, *prev_list, *mid_node, *current1, *current2;
	int palindrome;

	if (*head == NULL)
		return (1);

	palindrome = 1;
	fast = *head;
	slow = *head;

	while (fast != NULL && fast->next != NULL)
	{
		prev_list = slow;
		slow = slow->next;
		fast = fast->next->next;
	}

	if (fast != NULL)
	{
		mid_node = slow;
		slow = slow->next;
	}

	prev_list->next = NULL;

	current = slow;
	prev = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	current1 = *head;
	current2 = prev;

	while (current1 != NULL && current2 != NULL)
	{
		if (current1->n != current2->n)
		{
			palindrome = 0;
			break;
		}
		current1 = current1->next;
		current2 = current2->next;
	}

	return (palindrome);
}
