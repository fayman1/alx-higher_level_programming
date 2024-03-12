#include<stdlib.h>
#include "lists.h"

/**
 * insert_node - function to insert a node in a sorted linked list
 * @h: pointer to pointer to the head of the list
 * @num: integer value to insert
 * Return: address of the new node or NULL on failure
 */
listint_t *insert_node(listint_t **h, int num)
{
	listint_t *new_node;
	listint_t *current_node = *h;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = num;

	if (current_node == NULL || current_node->n >= num)
	{
		new_node->next = current_node;
		*h = new_node;
		return (new_node);
	}

	while (current_node && current_node->next && current_node->next->n < num)
		current_node = current_node->next;

	new_node->next = current_node->next;
	current_node->next = new_node;

	return (new_node);
}

