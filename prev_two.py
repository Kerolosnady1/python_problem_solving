# Enter numbers separated by space: -1 2 5 -3 5 7
# ==================================================
# positive even numbers = 2
# Number of positive even = 1
# Max positive even number = 2
# Min positive even number = 2
# Product of positive even numbers = 2
# Total number of positive even = 2
# Average number of positive even = 2.0
# ==================================================
# negative even numbers =
# Number of negative even = 0
# Max negative even number = 0
# Min negative even number = 0
# Product of negative even numbers = 0
# Total number of negative even = 0
# Average: Can't divide over zero!
# ==================================================
# positive odd numbers = 5 5 7
# Number of positive odd = 3
# Max positive odd number = 7
# Min positive odd number = 5
# Product of positive odd numbers = 175
# Total number of positive odd = 17
# Average number of positive odd = 5.666666666666667
# ==================================================
# negative odd numbers = -1 -3
# Number of negative odd = 2
# Max negative odd number = -1
# Min negative odd number = -3
# Product of negative odd numbers = 3
# Total number of negative odd = -4
# Average number of negative odd = -2.0
# ==================================================
# Zeros =
# Number of zeros = 0
# ==================================================
# Total of your numbers = 15
# ==================================================
# Average of your numbers = 2.5
# ==================================================
# Top 3 numbers = [7, 5, 5]
# ==================================================
# Less 3 numbers = [-3, -1, 2]
# ==================================================
# Frequencies = {-3: 1, -1: 1, 2: 1, 5: 2, 7: 1}
# ==================================================
# Mode = [5] appears 2 times.
# ==================================================
# Range = 10
# ==================================================
# Absolute values = [3, 1, 2, 5, 5, 7]
# ==================================================
# Ascending order = [-3, -1, 2, 5, 5, 7]
# ==================================================
# Median = (2, 5)
# ==================================================
# Standard deviation = 3.8858718455450894
# ==================================================
# Variance = 15.1
# ==================================================
# Percentage for every number = [-20, -6, 13, 33, 33, 46]
# ==================================================
# Normalized every number = [0.0, 0.2, 0.5, 0.8, 0.8, 1.0] 

from collections import Counter
import statistics
import math

def separator():
    print("".center(50, "="))

def max_min_prod_sum_avg(name: str, list_of_numbers: list):
    separator()
    print(f"{name} numbers =", *list_of_numbers)
    print(f"Number of {name} = {len(list_of_numbers)}")

    if list_of_numbers:
        print(f"Max {name} number = {max(list_of_numbers)}")
        print(f"Min {name} number = {min(list_of_numbers)}")
        print(f"Product of {name} numbers = {math.prod(list_of_numbers)}")
        print(f"Total number of {name} = {sum(list_of_numbers)}")
        print(f"Average number of {name} = {sum(list_of_numbers) / len(list_of_numbers)}")
    else:
        print(f"Max {name} number = {0}")
        print(f"Min {name} number = {0}")
        print(f"Product of {name} numbers = {0}")
        print(f"Total number of {name} = {sum(list_of_numbers)}")
        print(f"Average: Can't divide over zero!")

while True:
    
    numbers  = input("Enter numbers separated by space: ").strip().split()

    try:

        converted = [int(number) for number in numbers]

        pos_evens = [pos_even for pos_even in converted if pos_even % 2 == 0 and pos_even > 0]
        neg_evens = [neg_even for neg_even in converted if neg_even % 2 == 0 and neg_even < 0]

        pos_odds = [pos_odd for pos_odd in converted if pos_odd % 2 != 0 and pos_odd > 0]
        neg_odds = [neg_odd for neg_odd in converted if neg_odd % 2 != 0 and neg_odd < 0]

        zeros = [zero for zero in converted if zero == 0]

        max_min_prod_sum_avg("positive even", pos_evens)
        max_min_prod_sum_avg("negative even", neg_evens)
        max_min_prod_sum_avg("positive odd", pos_odds)
        max_min_prod_sum_avg("negative odd", neg_odds)
        separator()
        print("Zeros =", *zeros)
        print(f"Number of zeros = {len(zeros)}")
        separator()
        print(f"Total of your numbers = {sum(converted)}")
        separator()
        if converted:
            print(f"Average of your numbers = {sum(converted) / len(converted)}")
            separator()
            converted.sort(reverse=True)
            print(f"Top 3 numbers = {converted[:3]}")
            separator()
            converted.sort()
            print(f"Less 3 numbers = {converted[:3]}")
            separator()
            freq = Counter(converted)
            print(f"Frequencies = {dict(freq)}")
            separator()
            mode = [num for num, count in freq.items() if count == max(freq.values())]
            print(f"Mode = {mode} appears {max(freq.values())} times.")
            separator()
            print(f"Range = {max(converted) - min(converted)}")
            separator()
            print(f"Absolute values = {[abs(x) for x in converted]}")
            separator()
            print(f"Ascending order = {converted}")
            separator()
            median = len(converted) / 2
            if len(converted) % 2 != 0:
                print(f"Median = {converted[int(median)]}")
            else:
                print(f"Median = {converted[int(median) - 1], converted[int(median)]}")
            separator()
            print(f"Standard deviation = {statistics.stdev(converted)}")
            separator()
            print(f"Variance = {statistics.variance(converted)}")
            separator()
            if sum(converted) != 0:
                percentages = [int(x / sum(converted) * 100) for x in converted]
                print(f"Percentage for every number = {percentages}")
            else:
                print(f"Percentage for every number = {0}")
            
            separator()
            if max(converted) != min(converted):
                norm_list = [(x - min(converted)) / (max(converted) - min(converted)) for x in converted]
                print(f"Normalized every number = {norm_list}")
            else:
                print(f"Normalized every number = {0}")
            
        else:
            print("Avergae: Can't divide over zero!")
            separator()
            print(f"Top 3 numbers = {0}")
            separator()
            print(f"Less 3 numbers = {0}")
            separator()
            print(f"Frequencies = {0}")
            separator()
            print(f"Mode = {0} appears {0} times.")
            separator()
            print(f"Range = {0}")
            separator()
            print(f"Absolute values = {0}")
            separator()
            print(f"Ascending order = {converted}")
            separator()
            print(f"Median = {0}")
            separator()
            print(f"Standard deviation = {0}")
            separator()
            print(f"Variance = {0}")
            
        break
    except ValueError:
        print("Please enter only numbers separated by spaces.")


#           OR          #
# Semi-manual solution:

# from collections import Counter
# import statistics


# def sep() -> None:
#     print("".center(50,"="))

# def max_min_prod_sum_avg(name: str, list_of_numbers: list):
#     print(f"{name} numbers =", *list_of_numbers)
#     print(f"Number of {name} = {len(list_of_numbers)}")

#     if list_of_numbers:
#         max_num = min_num = total = prod = list_of_numbers[0]
#         for x in range(1, len(list_of_numbers)):
#             if max_num < list_of_numbers[x]:
#                 max_num = list_of_numbers[x]

#             if min_num > list_of_numbers[x]:
#                 min_num = list_of_numbers[x]

#             total += list_of_numbers[x]
#             prod *= list_of_numbers[x]
        
#         print(f"Max {name} number = {max_num}")
#         print(f"Min {name} number = {min_num}")
#         print(f"Product of {name} numbers = {prod}")
#         print(f"Total number of {name} = {total}")
#         print(f"Average number of {name} = {total / len(list_of_numbers)}")

#     else:
#         print(f"Max {name} number = {0}")
#         print(f"Min {name} number = {0}")
#         print(f"Product of {name} numbers = {0}")
#         print(f"Total number of {name} = {0}")
#         print(f"Average: Can't divide over zero!")



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
#         max_min_prod_sum_avg("positive even", pos_evens)
#         sep()
#         max_min_prod_sum_avg("negative even", neg_evens)
#         sep()
#         max_min_prod_sum_avg("positive odd", pos_odds)
#         sep()
#         max_min_prod_sum_avg("negative odd", neg_odds)
#         sep()
#         print("Zeros =", *zeros)
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
#             print(f"Average of your numbers = {total / len(converted)}")
#             sep()
#             converted.sort(reverse=True)
#             print(f"Top 3 numbers = {converted[:3]}")
#             sep()
#             converted.sort()
#             print(f"Less 3 numbers = {converted[:3]}")
#             sep()
#             freq = Counter(converted)
#             print(f"Frequencies = {dict(freq)}")
#             sep()
#             max_freq = max(freq.values())
#             mode = [num for num, counter in freq.items() if counter == max_freq]
#             print(f"Modes = {mode} appears {max_freq} times.")
#             sep()
#             print(f"Range = {max_num - min_num}")
#             sep()
#             abs_values = []
#             for x in converted:
#                 if x < 0:
#                     abs_values.append(x * -1)
                
#                 if x >= 0:
#                     abs_values.append(x)

#             print(f"Absolute values = {abs_values}")
#             sep()
#             print(f"Ascending order = {converted}")
#             sep()
#             median = len(converted) / 2
#             if len(converted) % 2 != 0:
#                 print(f"Median = {converted[int(median)]}")

#             else:
#                 print(f"Median = {converted[int(median) - 1], converted[int(median)]}")

#             sep()
#             print(f"Standard deviation = {statistics.stdev(converted)}")
#             sep()
#             print(f"Variance = {statistics.variance(converted)}")
#             sep()
#             if total != 0:
#                 percentage = [int((x / total) * 100) for x in converted]
#                 print(f"Percentage for every number = {percentage}")
#             else:
#                 print(f"Percentage for every number = {0}")
#             sep()
#             if max_num != min_num:
#                 norm_nums = [(x - min_num) / (max_num - min_num) for x in converted]
#                 print(f"Normalized every number = {norm_nums}")
#             else:
#                 print(f"Normalized every number = {0}")
                
        
#         else:
#             print(f"Total of your numbers = {0}")
#             sep()
#             print(f"Average: Can't divide over zero!")
#             sep()            
#             print(f"Top 3 numbers = {0}")
#             sep()
#             print(f"Less 3 numbers = {0}")
#             sep()
#             print(f"Frequencies = {0}")
#             sep()
#             print(f"Modes = {0} appears {0} times.")
#             sep()
#             print(f"Range = {0}")
#             sep()
#             print(f"Absolute values = {0}")
#             sep()
#             print(f"Ascending order = {0}")
#             sep()
#             print(f"Median = {0}")
#             sep()
#             print(f"Standard deviation = {0}")
#             sep()
#             print(f"Variance = {0}")

#         break



#     except ValueError:
#         print("Please enter only numbers separated by spaces.")
