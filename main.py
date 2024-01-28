from binary_tree import Tree

if __name__ == "__main__":
    tree = Tree()
    tree.insert_items([1, 5, 13, 22, 10, 110, 11, 67, 44])

    max_value_node = tree.max_value_node()
    min_value_node = tree.min_value_node()
    total_sum = tree.total_sum()

    if max_value_node is not None:
        print(f'Max value is {max_value_node.val}')
    else:
        print('Max value is not available')

    if min_value_node is not None:
        print(f'Max value is {min_value_node.val}')
    else:
        print('Min value is not available')

    print(f'Total sum is {total_sum}')
