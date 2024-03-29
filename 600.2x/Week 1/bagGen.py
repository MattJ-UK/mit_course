def yieldAllCombos(items):
    """
      Generates all combinations of N items into two bags, whereby each
      item is in one or zero bags.

      Yields a tuple, (bag1, bag2), where each bag is represented as
      a list of which item(s) are in each bag.
    """
    # generate all combinations of N items

    N = len(items)
    # enumerate the 3**N possible combinations
    for i in range(3 ** N):
        bag_1 = []
        bag_2 = []
        for j in range(N):
            # test bit jth of integer i
            if (i >> j) % 3 == 1:
                bag_1.append(items[j])
            elif (i >> j) % 3 == 0:
                bag_2.append(items[j])
        yield (bag_1, bag_2)


test_list = ['apple', 'orange', 'banana']

x = yieldAllCombos(test_list)