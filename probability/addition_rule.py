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
