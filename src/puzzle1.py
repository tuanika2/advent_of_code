"""Advent of code 2021
   Problem 1
"""
import pandas as pd


def calculating():
    inp = pd.read_csv(r"D:\advent_of_code\tasks1_input.csv", header=None)

    i = []
    c = 0

    results = inp.copy()

    for k in list(results.loc[:, 0]):
        if c == 0:
            results["yesno"] = False
            i.append(k)
            c = c + 1
        else:
            # print(c)
            if k > i[c - 1]:
                # print(k,i[c-1])
                results.loc[
                    c, "yesno"
                ] = True  # .iat[c, results.columns.get_loc("yesno")] = True
                i.append(k)
                c = c + 1
            else:
                # print(k,i[c-1])
                results.loc[
                    c, "yesno"
                ] = False  # .iat[c, results.columns.get_loc("yesno")] = False
                i.append(k)
                c = c + 1

    count = results.value_counts(subset="yesno")
    result = count[1]

    # print(f"number of increasing values is {result}")

    return result
