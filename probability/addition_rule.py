def prob_a_or_b(a, b, all_posible_outcomes):
    # probability of event a
    prob_a = len(a)/len(all_posible_outcomes)

    # probability of event b
    prob_b = len(b)/len(all_posible_outcomes)

    # intersection of events a and b
    inter = a.intersection(b)

    # probability of intersection of events a and b
    prob_inter = len(inter)/len(all_posible_outcomes)

    # probability of a or b (Addition rule)
    add_rule_formula = prob_a + prob_b - prob_inter

    # add return statement here
    return add_rule_formula

# rolling a die once and getting an even number or an odd number
evens = {2, 4, 6}
odds = {1, 3, 5}
all_possible_rolls = {1, 2, 3, 4, 5, 6}

# call function here first
print(prob_a_or_b(evens, odds, all_possible_rolls))

# rolling a die once and getting an odd number or a number greater than 2
odds = {1, 3, 5}
greater_than_two = {3, 4, 5, 6}
all_possible_rolls = {1, 2, 3, 4, 5, 6}

# call function here second 
print(prob_a_or_b(odds, greater_than_two, all_possible_rolls))