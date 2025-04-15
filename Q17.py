def list_operations(lst):

    print("Fourth item:", lst[3] if len(lst) > 3 else "List too short")

    print("All except first two:", lst[2:])

    print("Reversed list:", lst[::-1])

    print("Sum:", sum(lst))

    print("Max:", max(lst))
    print("Min:", min(lst))

    zero_index = next((i for i, x in enumerate(lst) if x == 0), -1)
    print("First zero index:", zero_index)

    print("Ascending order:", sorted(lst))
    print("Descending order:", sorted(lst, reverse=True))


print("Testing list_operations:")
list_operations([10, 20, 30, 40, 50, 0, -10])
