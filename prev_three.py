import math, statistics, numpy
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
        print(f"Max {name} number = {0}")
        print(f"Min {name} number = {0}")
        print(f"Product of {name} numbers = {0}")
        print(f"Total number of {name} = {0}")
        print(f"Average: Can't divide over zero!")

while True:

    numbers = input("Enter numbers separated by space: ").strip().split()

    try:
        converted = [int(number) for number in numbers]

        pos_evens = [pos_even for pos_even in converted if pos_even % 2 == 0 and pos_even > 0]
        neg_evens = [neg_even for neg_even in converted if neg_even % 2 == 0 and neg_even < 0]

        pos_odds = [pos_odd for pos_odd in converted if pos_odd % 2 != 0 and pos_odd > 0]
        neg_odds = [neg_odd for neg_odd in converted if neg_odd % 2 != 0 and neg_odd < 0]

        zeros = [zero for zero in converted if zero == 0]

        sep()
        all_in("positive even", pos_evens)
        sep()
        all_in("negative even", neg_evens)
        sep()
        all_in("positive odd", pos_odds)
        sep()
        all_in("negative odds", neg_odds)
        sep()
        print("Zeros =", *zeros)
        print(f"Number of zeros = {len(zeros)}")
        sep()
        if converted:
            print(f"Total of your numbers = {sum(converted)}")
            sep()
            print(f"Average of your numbers = {sum(converted) / len(converted):.2f}")
            sep()
            converted.sort(reverse=True)
            print(f"Top 3 numbers = {converted[:3]}")
            sep()
            converted.sort()
            print(f"Less 3 numbers = {converted[:3]}")
            sep()
            print(f"Frequencies = {dict(Counter(converted))}")
            sep()
            max_freq = max(Counter(converted).values())
            modes = [x for x, count in Counter(converted).items() if count == max_freq]
            print(f"Modes = {modes} appears {max_freq} times.")
            sep()
            print(f"Range = {max(converted) - min(converted)}")
            sep()
            abs_vals = [abs(x) for x in converted]
            print(f"Absolute values = {abs_vals}")
            sep()
            print(f"Ascending order = {converted}")
            sep()
            print(f"Median = {statistics.median(converted)}")
            sep()
            print(f"Standard deviation = {statistics.stdev(converted)}")
            sep()
            print(f"Variance = {statistics.variance(converted)}")
            sep()
            if sum(converted) != 0:
                percentage = [int(x / sum(converted) * 100) for x in converted]
                print(f"Percentage for every number = {percentage}")
            else:
                print(f"Percentage for every number = {0}")
            sep()
            if max(converted) != min(converted):
                norm_nums = [((x - min(converted)) / (max(converted) - min(converted))) for x in converted]
                print(f"Normalized for every number = {norm_nums}")
            else:
                print(f"Normalized for every number = {0}")
            sep()
            Q1, Q2, Q3 = numpy.percentile(converted, [25, 50, 75])
            print(f"Quartiles => Q1 = {Q1}, Q2 = {Q2}, Q3 = {Q3}")
            sep()
            IQR = Q3 - Q1
            print(f"Interquartile Range (IQR) = {IQR}")
            sep()
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = [x for x in converted if x < lower_bound or x > upper_bound]
            print(f"Lower bound = {lower_bound}, Upper bound = {upper_bound}")
            print(f"Outliers = {outliers if outliers else 'No outliers found'}")

        else:
            print(f"Total of your numbers = {0}")
            sep()
            print(f"Average: Can't divide over zero!")
            sep()
            print(f"Top 3 numbers = {0}")
            sep()
            print(f"Less 3 numbers = {0}")
            sep()
            print(f"Frequencies = {0}")
            sep()
            print(f"Modes = {0} appears {0} times.")
            sep()
            print(f"Range = {0}")
            sep()
            print(f"Absolute values = {0}")
            sep()
            print(f"Ascending order = {0}")
            sep()
            print(f"Median = {0}")
            sep()
            print(f"Standard deviation = {0}")
            sep()
            print(f"Variance = {0}")
            sep()
            print(f"Quartiles => Q1 = {0}")
            sep()
            print(f"Interquartile Range (IQR) = {0}")
            sep()
            print(f"Interquartile Range (IQR) = {0}")

        break

    
    except ValueError:
        print("Please enter only numbers separated by spaces.")


#           OR          #
# Manual solution:
# 
# def sep() -> None:
#     print("".center(55, "="))

# def all_in(name: str, list_of_nums: list):
#     print(f"{name} numbers =".capitalize(), *list_of_nums)
#     print(f"Number of {name} = {len(list_of_nums)}")
#     if list_of_nums:
#         max_num = min_num = prod = total = list_of_nums[0]
#         for x in range(1, len(list_of_nums)):
#             if max_num < list_of_nums[x]:
#                 max_num = list_of_nums[x]
#             if min_num > list_of_nums[x]:
#                 min_num = list_of_nums[x]
#             prod *= list_of_nums[x]
#             total += list_of_nums[x]

#         print(f"Max {name} number = {max_num}")
#         print(f"Min {name} number = {min_num}")
#         print(f"Product of {name} numbers = {prod}")
#         print(f"Total number of {name} = {total}")
#         print(f"Average number of {name} = {total / len(list_of_nums):.2f}")
#     else:
#         print("N/A the list is empty.")

# while True:

#     numbers = input("Enter numbers separated by space: ").strip().split()

#     try:
#         converted = [int(number) for number in numbers]

#         pos_evens = [pos_even for pos_even in converted if pos_even % 2 == 0 and pos_even > 0]
#         neg_evens = [neg_even for neg_even in converted if neg_even % 2 == 0 and neg_even < 0]

#         pos_odds = [pos_odd for pos_odd in converted if pos_odd % 2 != 0 and pos_odd > 0]
#         neg_odds = [neg_odd for neg_odd in converted if neg_odd % 2 != 0 and neg_odd < 0]

#         zeros = [zero for zero in converted if zero == 0]
        
#         sep()
#         all_in("positive even", pos_evens)
#         sep()
#         all_in("negative even", neg_evens)
#         sep()
#         all_in("positive odd", pos_odds)
#         sep()
#         all_in("negative odd", neg_odds)
#         sep()
#         print(f"Zeros =", *zeros)
#         print(f"Number of zeros = {len(zeros)}")
#         sep()
#         if converted:
#             total = max_num = min_num = converted[0]
#             for x in range(1, len(converted)):
#                 if max_num < converted[x]:
#                     max_num = converted[x]
#                 if min_num > converted[x]:
#                     min_num = converted[x]
#                 total += converted[x]
#             print(f"Total of your numbers = {total}")
#             sep()
#             print(f"Average of your numbers = {total / len(converted):.2f}")
#             sep()
#             conv_len = len(converted)
#             for x in range(conv_len - 1):
#                 for y in range(conv_len - x - 1):
#                     if converted[y] < converted[y + 1]:
#                         converted[y], converted[y + 1] = converted[y + 1], converted[y]
#             print(f"Top 3 numbers = {converted[:3]}")
#             sep()
#             for x in range(conv_len - 1):
#                 for y in range(conv_len - x - 1):
#                     if converted[y] > converted[y + 1]:
#                         converted[y], converted[y + 1] = converted[y + 1], converted[y]
#             print(f"Less 3 numbers = {converted[:3]}")
#             sep()
#             # Initialize an empty dictionary
#             freq = {}

#             # Iterate through the list
#             for item in converted:
#                 # Increment the count if the item exists, otherwise set it to 1
#                 freq[item] = freq.get(item, 0) + 1

#             # Print the frequency dictionary
#             print(f"Frequencies = {freq}")
#             sep()
#             max_freq = max(freq.values())
#             modes = [x for x, count in freq.items() if count == max_freq]
#             print(f"Modes = {modes} appears {max_freq} times.")
#             sep()
#             print(f"Range {max_num - min_num}")
#             sep()
#             abs_vals = [abs(x) for x in converted]
#             print(f"Absolute values = {abs_vals}")
#             sep()
#             print(f"Ascending order = {converted}")
#             sep()
#             median = len(converted) / 2
#             if len(converted) % 2 != 0:
#                 print(f"Median = {converted[int(median)]}")
#             else:
#                 print(f"Median = {converted[int(median - 1)], converted[int(median)]}")
#             sep()
#             mean = total / len(converted)
#             variance = sum((x - mean) ** 2 for x in converted) / (len(converted) - 1)
#             stdev = variance ** 0.5
#             print(f"Standard deviation = {stdev:.2f}")
#             sep()
#             print(f"Variance = {variance:.2f}")
#             sep()
#             if total != 0:
#                 percentage = [(x / total) * 100  for x in converted]
#                 print(f"Percentage for every number = {percentage}")
#             else:
#                 print(f"Percentage for every number = {0}")
#             sep()
#             if max_num != min_num:
#                 norm_nums = [(x - min_num) / (max_num - min_num) for x in converted]
#                 print(f"Normalized for every number = {norm_nums}")
#             else:
#                 print(f"Normailzed for every number = {0}")
#             sep()
#             con_len = len(converted)
#             q1 = converted[conv_len // 4] # 25th
#             q2 = converted[conv_len * 2 // 4] # 50th
#             q3 = converted[conv_len * 3 // 4] # 75th
#             iqr = q3 - q1
#             print(f"Q1 => {q1}, Q2 => {q2}, Q3 => {q3}")
#             sep()
#             print(f"IQR = {iqr}")
#             sep()
#             lower_bond = q1 - 1.5 * iqr
#             upper_bond = q3 - 1.5 * iqr
#             outliers = [x for x in converted if x < lower_bond or x > upper_bond]
#             print(f"Lower bond = {lower_bond:.2f}\nUpper bond = {upper_bond:.2f}")
#             print(f"Outliers = {outliers if outliers else "No outliers found"}")

#         else:
#             print("N/A the list is empty.")

#         break


#     except ValueError:
#         print("Please enter only numbers separated by spaces.")