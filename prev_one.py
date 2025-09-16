# Enter numbers separated by space: -1 2 5 -3 5 7
# positive even numbers = 2
# Number of positive even = 1
# Max positive even number = 2
# Min positive even number = 2
# Product positive even number = 2
# Total number of positive even = 2
# Average number of positive even = 2.0
# ==================================================
# negative even numbers =
# Number of negative even = 0
# Max negative even number = 0
# Min negative even number = 0
# Product negative even number = 0
# Total number of negative even = 0
# Can't divide over zero!
# ==================================================
# positive odd numbers = 5 5 7
# Number of positive odd = 3
# Max positive odd number = 7
# Min positive odd number = 5
# Product positive odd number = 175
# Total number of positive odd = 17
# Average number of positive odd = 5.666666666666667
# ==================================================
# negative odd numbers = -1 -3
# Number of negative odd = 2
# Max negative odd number = -1
# Min negative odd number = -3
# Product negative odd number = 3
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
# Mode = 5 appears 2 times
# ==================================================
# Range: 10
# ==================================================
# Absolute values = [3, 1, 2, 5, 5, 7]
# ==================================================
# List the numbers ascending order = [-3, -1, 2, 5, 5, 7]    
# Median = (2, 5)
from collections import Counter
import math

def separator() -> None:
    print("".center(50, "="))

def all_in(name: str, lists: list):
    if lists:
        print(f"{name} numbers =",*lists)
        print(f"Number of {name} = {len(lists)}")
        print(f"Max {name} number = {max(lists)}")
        print(f"Min {name} number = {min(lists)}")
        print(f"Product {name} number = {math.prod(lists)}")
        print(f"Total number of {name} = {sum(lists)}")
    else:
        print(f"{name} numbers =",*lists)
        print(f"Number of {name} = {0}")
        print(f"Max {name} number = {0}")
        print(f"Min {name} number = {0}")
        print(f"Product {name} number = {0}")
        print(f"Total number of {name} = {sum(lists)}")
    if lists:
        print(f"Average number of {name} = {sum(lists) / len(lists)}")
    else:
        print("Can't divide over zero!")

while True:

    numbers = input("Enter numbers separated by space: ").strip().split()

    try:

        converted = [int(number) for number in numbers]

        pos_evens = [pos_even for pos_even in converted if pos_even % 2 == 0 and pos_even > 0]
        neg_evens = [neg_even for neg_even in converted if neg_even % 2 == 0 and neg_even < 0]

        pos_odds = [pos_odd for pos_odd in converted if pos_odd % 2 != 0 and pos_odd > 0]
        neg_odds = [neg_odd for neg_odd in converted if neg_odd % 2 != 0 and neg_odd < 0]

        zeros = [zero for zero in converted if zero == 0]

        all_in("positive even", pos_evens)
        separator()
        all_in("negative even", neg_evens)
        separator()
        all_in("positive odd", pos_odds)
        separator()
        all_in("negative odd", neg_odds)
        separator()
        print("Zeros =", *zeros)
        print(f"Number of zeros = {len(zeros)}")
        separator()
        print(f"Total of your numbers = {sum(converted)}")
        separator()
        if converted:
            print(f"Average of your numbers = {sum(converted) / len(converted)}")
        else:
            print("Can't divide over zero!")
        separator()
        if converted:
            converted.sort(reverse=True)
            print(f"Top 3 numbers = {converted[:3]}")
            separator()
            converted.sort()
            print(f"Less 3 numbers = {converted[:3]}")
            separator()
            count = Counter(converted)
            print(f"Frequencies = {dict(count)}")
            separator()
            most_common_num, freq = count.most_common(1)[0]
            print(f"Mode = {most_common_num} appears {freq} times")
            separator()
            print(f"Range: {max(converted) - min(converted)}")
            separator()
            print(f"Absolute values = {[abs(num) for num in converted]}")
            separator()
            print(f"List the numbers ascending order = {converted}")
            median = len(converted) / 2
            if len(converted) % 2 != 0:
                print(f"Median = {converted[int(median)]}")

            else:
                print(f"Median = {converted[int(median) - 1], converted[int(median)]}")
        else:
            print("Empty or even zero.")
        

        break


    
    except ValueError:
        print("Please enter only numbers separated by spaces.")


#           OR          #
# Manual solution:
# from collections import Counter

# def separator() -> None:
#     print("".center(50, "="))

# def min_and_max(name: str, list_of_numbers: list):
#     print(f"{name} numbers = ", *list_of_numbers)
#     print(f"Number of {name} numbers = {len(list_of_numbers)}")
#     if list_of_numbers:
#         min_num = max_num = list_of_numbers[0]

#         for x in range(1, len(list_of_numbers)):
#             if min_num > list_of_numbers[x]:
#                 min_num = list_of_numbers[x]

#             if max_num < list_of_numbers[x]:
#                 max_num = list_of_numbers[x]

#         print(f"Max {name} number = {max_num}")
#         print(f"Min {name} number = {min_num}")
#     else:
#         print(f"Max {name} number = {0}")
#         print(f"Min {name} number = {0}")
    

# def prod_and_sum(name: str,list_of_numbers: list):
#     if list_of_numbers:
#         prod_num = total = list_of_numbers[0]
#         for x in range(1, len(list_of_numbers)):
#             prod_num *= list_of_numbers[x]

#             total += list_of_numbers[x]

#         print(f"Product of {name} numbers = {prod_num}")
#         print(f"Total number of {name} = {total}")
    
#     else:
#         print(f"Product {name} number = {0}")
#         print(f"Total number of {name} = {0}")



# while True:

#     numbers = input("Enter numbers separated by space: ").strip().split()


#     try:
#         converted = [int(number) for number in numbers]

#         pos_evens = [pos_even for pos_even in converted if pos_even % 2 == 0 and pos_even > 0]
#         neg_evens = [neg_even for neg_even in converted if neg_even % 2 == 0 and neg_even < 0]

#         pos_odds = [pos_odd for pos_odd in converted if pos_odd % 2 != 0 and pos_odd > 0]
#         neg_odds = [neg_odd for neg_odd in converted if neg_odd % 2 != 0 and neg_odd < 0]

#         zeros = [zero for zero in converted if zero == 0]

#         separator()
#         min_and_max("positive even", pos_evens)
#         prod_and_sum("positive even", pos_evens)
#         separator()
#         min_and_max("negative even", neg_evens)
#         prod_and_sum("negative even", neg_evens)
#         separator()
#         min_and_max("positive odd", pos_odds)
#         prod_and_sum("positive odd", pos_odds)
#         separator()
#         min_and_max("negative odd", neg_odds)
#         prod_and_sum("negative odd", neg_odds)
#         separator()
#         if converted:
#             print("Zeros =", *zeros)
#             print(f"Number of zeros = {len(zeros)}")
#             separator()
#             total = max_converted = min_converted = converted[0]
#             for x in range(1, len(converted)):
#                 total += converted[x]
#                 if max_converted < converted[x]:
#                     max_converted = converted[x]
                
#                 if min_converted > converted[x]:
#                     min_converted = converted[x]
            
#             print(f"Total of your numbers = {total}")
#             separator()
#             print(f"Average of your numbers = {total / len(converted)}")
#             separator()
#             converted.sort(reverse=True)
#             print(f"Top 3 numbers = {converted[:3]}")
#             separator()
#             converted.sort()
#             print(f"Less 3 numbers = {converted[:3]}")
#             separator()
#             counter = Counter(converted)
#             print(f"Frequencies = {dict(counter)}")
#             separator()
#             mode = max(counter, key=counter.get)
#             print(f"Most common number = {mode} appears {counter[mode]} times.")
#             separator()
#             print(f"Range = {max_converted - min_converted}")
#             separator()
#             new_converted = []
#             for x in range(len(converted)):
#                 if converted[x] < 0:
#                     new_converted.append(converted[x] * -1)
                
#                 else:
#                     new_converted.append(converted[x] * 1)

#             print(f"Absolute values = {new_converted}")
#             separator()
#             median = len(converted) / 2
#             if len(converted) % 2 != 0:
#                 print(f"Median = {converted[int(median)]}")

#             else:
#                 print(f"Median = {converted[int(median) - 1], converted[int(median)]}")
        
#         else:
#             print("Zeros =", *zeros)
#             print(f"Number of zeros = {len(zeros)}")
#             separator()
#             print(f"Total of your numbers = {0}")
#             separator()
#             print(f"Can't divide over zero!")
#             separator()
#             converted.sort(reverse=True)
#             print(f"Top 3 numbers = {0}")
#             separator()
#             converted.sort()
#             print(f"Less 3 numbers = {0}")
#             separator()
#             counter = Counter(converted)
#             print(f"Frequencies = {0}")
#             separator()
#             print(f"Most common number = {0} appears {0} times.")
#             separator()
#             print(f"Range = {0}")
#             separator()
#             new_converted = []
#             print(f"Absolute values = {0}")
#             separator()
#             print(f"Median = {0}")

#         break

#     except ValueError:
#         print("Please enter only numbers separated by spaces.")