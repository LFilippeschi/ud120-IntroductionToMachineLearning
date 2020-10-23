#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    support_list = []
    count = 0
    for x in predictions:
        support_list.append((abs(x-net_worths[count]), ages[count], net_worths[count]))
        count += 1

    #print support_list
    support_list.sort()
    #print support_list

    for x in range(81):
        value = support_list[x]
        cleaned_data.append((value[1], value[2], value[0]))

    #print cleaned_data

    return cleaned_data
