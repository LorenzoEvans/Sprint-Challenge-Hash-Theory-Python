#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    # {limit: limit, weights: [1,2,3...n]}
    for x in weights:
      hash_table_insert(ht, x, weights.index(x))

    flag = False
    i = 0
    for x in ht.elements:
      cur_val = ht.elements[i]
      if x.key + x.next.key is not limit
    # element_list = []
    # for x in ht.storage:
    #   if x is None:
    #     # element_list.append(x)
    #     continue
    #   elif x is not None:
    #
    #     element_list.append([x.key, x.value])
    print('ele_list: ', element_list)

    """
    YOUR CODE HERE
    """

    return element_list

get_indices_of_item_weights([4, 6, 10, 15, 16], 5, 21)
# def print_answer(answer):
#     if answer is not None:
#         print(str(answer[0] + " " + answer[1]))
#     else:
#         print("None")
