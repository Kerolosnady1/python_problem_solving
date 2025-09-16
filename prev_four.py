import math, statistics, matplotlib.pyplot as plt, pandas as pd
from collections import Counter

def sep() -> None:
    print("".center(55, "="))

def all_in(name: str, list_of_nums: list):
    print(f"{name} numbers =".capitalize(), *list_of_nums)
    print(f"Number of {name} = {len(list_of_nums)}")

    if list_of_nums:
        print(f"Max {name} number = {max(list_of_nums)}")
        print(f"Min {name} number = {min(list_of_nums)}")
        print(f"Product of {name} numbers = {math.prod(list_of_nums)}")
        print(f"Total number of {name} = {sum(list_of_nums)}")
        print(f"Average number of {name} = {sum(list_of_nums) / len(list_of_nums):.2f}")

    else:
        print("No numbers found.")

while True:
    numbers = input("Enter numbers separated by space: ").strip().split()

    try:

        converted = [int(number) for number in numbers]

        pos_evens = [pos_even for pos_even in converted if pos_even > 0 and pos_even % 2 == 0]
        neg_evens = [neg_even for neg_even in converted if neg_even < 0 and neg_even % 2 == 0]

        pos_odds = [pos_odd for pos_odd in converted if pos_odd > 0 and pos_odd % 2 != 0]
        neg_odds = [neg_odd for neg_odd in converted if neg_odd < 0 and neg_odd % 2 != 0]

        zeros = [zero for zero in converted if zero == 0]

        sep(); all_in("positive even", pos_evens)
        sep(); all_in("negative even", neg_evens)
        sep(); all_in("positive odd", pos_odds)
        sep(); all_in("negative odd", neg_odds)
        sep()
        print("Zeros =", *zeros)
        print(f"Number of zeros = {len(zeros)}")
        if converted:
            sep(); print(f"Total of your numbers = {sum(converted)}")
            sep(); print(f"Average of your numbers = {sum(converted) / len(converted):.2f}")
            sep()
            converted.sort(reverse=True)
            print(f"Top 3 number = {converted[:3]}")
            sep()
            converted.sort()
            print(f"Less 3 numbers = {converted[:3]}")
            sep()
            freq = Counter(converted)
            print(f"Frequencies = {dict(freq)}")
            sep()
            max_val = max(freq.values())
            modes = [num for num, count in freq.items() if max_val == count]
            print(f"Modes = {modes} appears {max_val} times.")
            sep(); print(f"Range = {max(converted) - min(converted)}")
            sep()
            abs_vals = [abs(x) for x in converted]
            print(f"Absolute values = {abs_vals}")
            sep(); print(f"Ascending order = {converted}")
            sep(); print(f"Median = {statistics.median(converted)}")
            sep(); print(f"Standard deviation = {statistics.stdev(converted)}")
            sep(); print(f"Variance = {statistics.variance(converted)}")
            sep()
            if sum(converted) != 0:
                percentage = [(x / sum(converted)) * 100 for x in converted]
                print(f"Percentage for every number = {percentage}")
            else:
                print(f"The sum of numbers = {0}, and you can't divide over zero in the calculation.")
            sep()
            if max(converted) != min(converted):
                norm_nums = [(x - min(converted) / (max(converted) - min(converted))) for x in converted]
                print(f"Normalized for every number = {norm_nums}")
            else:
                print(f"The maximum and the minimum are equal.")
            sep()
            q1 = converted[len(converted) // 4] # 25th
            q2 = converted[len(converted) * 2 // 4] # 50th
            q3 = converted[len(converted) * 3 // 4] # 75th
            iqr = q3 - q1

            print(f"Q1 => {q1}, Q2 => {q2}, Q3 => {q3}")
            sep(); print(f"InterQuartile Range (IQR) = {iqr}")
            sep()
            lower_bond = q1 - 1.5 ** iqr
            upper_bond = q3 + 1.5 ** iqr

            outliers = [x for x in converted if x > lower_bond or x < upper_bond]

            print(f"Lower bond = {lower_bond}, upper bond = {upper_bond}")
            print(f"Outliers = {outliers if outliers else "No outliers found"}")
            sep()

            # Visualization part:

            plt.hist(converted, bins=10, edgecolor="black") # bins => for cm
            plt.title("Histogram of Numbers")
            plt.xlabel("Value")
            plt.ylabel("Frequency")
            plt.show()

            plt.boxplot(converted, vert=False) # vert => vertically = False
            plt.title("Boxplot of Numbers")
            plt.show()

            plt.pie(freq.values(), labels=freq.keys(), autopct="%1.1f%%") # autopct => for the number and the number after the . if 1 just 1 and 5 just 5
            plt.title("Pie Chart of Frequencies")
            plt.show()

            # Pandas summary statistics
            
            series = pd.Series(converted)
            print(series.describe())

        else:
            print(f"Empty list.")

        break

    
    except ValueError:
        print("Please enter only numbers separated by spaces.")