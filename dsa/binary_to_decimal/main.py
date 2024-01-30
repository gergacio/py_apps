def binary_to_decimal(self):
    # 1. Initialize a variable 'num' to 0. This will be used to accumulate the
    # decimal value as we traverse the linked list.
    num = 0

    # 2. Start at the head of the linked list.
    current = self.head

    # 3. Traverse through the linked list.
    while current:
        # 3.1. For each node, left shift the accumulated value by 1 position.
        # This is the same as multiplying by 2. This step ensures that we are
        # moving to the next binary position.
        #
        # Example: If num is '10' (binary for 2) and next node value is '1',
        # left shifting '10' results in '100' (binary for 4).
        # Now, adding the next node value gives '101' (binary for 5).
        num = num * 2

        # 3.2. Add the current node's value (which should be either 0 or 1)
        # to the accumulated value 'num'.
        num = num + current.value

        # OR both the above steps can be combined as:
        # num = num * 2 + current.value

        # 3.3. Move to the next node in the list.
        current = current.next

    # 4. Return the accumulated decimal value.
    return num


