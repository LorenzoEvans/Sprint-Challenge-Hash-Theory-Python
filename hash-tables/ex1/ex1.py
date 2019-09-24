#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
  ht = HashTable(16)

  new_weights = []

  result = ()

  for x in weights:

    hash_table_insert(ht, x, weights.index(x))
    new_weights.append(x)

  if len(weights) == 1:
    return None
  if limit not in new_weights:

    new_weights.append(limit)

  elif limit in new_weights:
    result = result + (new_weights.index(0), new_weights.index(limit))
    # print('Found it.', 'limit: ',limit)
    # result = result + ()
    print('result is: ',result)
    return result

  new_weights.sort()
  sum = new_weights[len(new_weights) - 1]
  print('new_weights: ',new_weights)
  for x in reversed(range(len(new_weights))):
    if x is 0:
      print('Done.')
    elif sum % new_weights[x] in new_weights:
      items = ()
      items = items + (sum % new_weights[x], new_weights[x])
      print(items)
      val = new_weights.index(sum % new_weights[x])
      print('val is: ',val)
      print('x is: ',x)
      val1 = new_weights[val]
      val2 = new_weights.index(limit - new_weights[val])
      result = result + (val2, val)
      # print('limit - val: ',limit - new_weights[val])
      # print(new_weights.index(limit - new_weights[val]))
      # print(new_weights[val])
      print("is",result)
      return result
      # result_2 = result + (new_weights.index([new_weights.index(sum % new_weights[x])])[0], new_weights[x])
      # print(result_2)
    elif sum % new_weights[x] not in new_weights:
      if new_weights[x] + new_weights[x - 1] == limit:
        result = (new_weights.index(new_weights[x]))

        print('is',result)
        x_count = new_weights.count(new_weights[x])
        if x_count > 1:
          new_weights[x] = None
          # new_weights.remove(new_weights[x])
          print(new_weights)
          result = (x, result)
          print("result is", result)
        print("x count is",x_count)
        print("x is:", x, "new_weights[x]", new_weights[x])
        return result
      print(x)

    # else:
    #   print(f"new_weights[x]: {new_weights[x]} + new_weights[x - 1]: {new_weights[x - 1]}")
    #   print(f"sum: {(new_weights[x] + new_weights[x - 1])}")


  # Given the list [4, 6, 10, 15, 16], what can we say?

  # answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
  #         self.assertTrue(answer_3[0] == 3) => (weights)list[3] => 15
  #         self.assertTrue(answer_3[1] == 1) => (weights)list[1] => 6

  # 6 + 15 = 21 = limit = 6 + 15 = 21 = limit =...

  # If we sort the list, what can we reason about the list,
  # and the values it contains, and the relationships that,
  # those values have to the other values it shares membership with?

  # Could we binary sort, then binary search for it?

  # Sorted, it looks like [4, 6, 10, 15, 16].

  # 1. The limit has to be equal to or lower than the last,
  #    two elements of the sorted list, otherwise no two elements in the list will add up to it.

  # 2. If the limit is in the list, the items are the element at the index with a value,
  #    matching the limit, and whatever other element has a value of 0.
  #    A number plus anything other than 0 can not equal itself, and the limit has to be
  #   the result of adding two numbers.

  # What properties does the list get if we add the limit to it?

  # Can we get list[1], 6, and list[3] = 15?

  # list_with_limit = [4, 6, 10, 15, 16, 21]

  # 15 + 16 = 31. So the next two elements aren't it.

  # 21 % 15 = 6. Can we take this value and search for it by index via value?


  # Can we rely on this assumption? Let's try a bigger set.

  #        weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
  #         answer_4 = get_indices_of_item_weights(weights_4, 9, 7)
  #         self.assertTrue(answer_4[0] == 6)
  #         self.assertTrue(ans
  #         wer_4[1] == 2)

  # sorted = [0, 3, 6, 7, 12, 14, 19, 25, 40.] limit = 7

  # 7 % 7 gives us 0, and if we search for that value, we find it.

  # sorted = [0, 3, 6, 9, 12, 14, 19, 25, 40.] limit = 9

  # The limit is in the list, but is also the result of adding two numbers to the list.

  # Does the test check for this edge case? No, but we know about it now.
  # The limit is the result of a two set, 3, and 6, which will catch it.
  # sorted = [0, 3, 6, 9, 12, 14, 19, 25, 40.] limit = 9

  # If we add the limit to the sorted list, we can remove every element to the right of it.


  # Any number greater than the limit can not be added to the limit to derive it.

  # Can we assume, that for every sorted list with the limit added, the limit modulo some element in the list,

  # WILL GIVE BACK THE REMAINDER BECAUSE THAT'S WHAT MODULO DOES, WHICH HAS TO BE THE VALUE WE NEED TO ADD,

  # TO CREATE THE NUMBER, AND THAT ELEMENT HAS TO BE IN THE LIST DUE TO THE NATURE OF THE PROBLEM.


  # So, add value to list.

  # Sort list, remove every element from the right of the list.



  # Obviously,

  # """
	# YOUR CODE HERE
	# """

  # return element_list

print(get_indices_of_item_weights([4, 4], 2, 8))
# def print_answer(answer):
#     if answer is not None:
#         print(str(answer[0] + " " + answer[1]))
#     else:
#         print("None")
