def linear_sort(self, data_collection):
    """Linear sort algorithm."""
    for j in range(1, len(data_collection)):
        current_item = data_collection[j]
        current_position = j

        while current_position > 0 and data_collection[current_position-1] > current_item:
            data_collection[current_position] = data_collection[current_position-1]
            current_position -= 1

        data_collection[current_position] = current_item

    return data_collection

