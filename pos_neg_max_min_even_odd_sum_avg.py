# ==================================================
# Enter numbers separated by space: 0 1 2 -1 0 -2 6
# ==================================================
# Positive evens = 2 6
# Number of positive evens = 2
# Max positive even number = 6
# Min positive even number = 2
# Product number of positive evens = 12
# ==================================================
# Negative evens = -2
# Number of negative evens = 1
# Max negative even number = -2
# Min negative even number = -2
# Product number of negative evens = -2
# ==================================================
# Positive odds = 1
# Number of positive odds = 1
# Max positive odd number = 1
# Min positive odd number = 1
# Product number of odds = 1
# ==================================================
# Negative odds = -1
# Number of negative odds = 1
# Max negative odd number = -1
# Min negative odd number = -1
# Product number of negative odds = -1
# ==================================================
# Zeros = 0 0
# Number of zeros = 2
# ==================================================
# Sum of numbers = 6
# ==================================================
# Average number = 0.8571428571428571

import math
while True:

    def separator() -> None:
        print("".center(50, "="))

    separator()
    numbers = input("Enter numbers separated by space: ").strip().split()
    separator()

    try:
        converted = [int(number) for number in numbers]

        pos_evens = [pos_even for pos_even in converted if pos_even > 0 and pos_even % 2 == 0]
        neg_evens = [neg_even for neg_even in converted if neg_even < 0 and neg_even % 2 == 0]

        pos_odds = [pos_odd for pos_odd in converted if pos_odd > 0 and pos_odd % 2 != 0]
        neg_odds = [neg_odd for neg_odd in converted if neg_odd < 0 and neg_odd % 2 != 0]

        zeros = [zero for zero in converted if zero == 0]


        print("Positive evens =", *pos_evens)
        print(f"Number of positive evens = {len(pos_evens)}")
        if pos_evens:
            print(f"Max positive even number = {max(pos_evens)}")
            print(f"Min positive even number = {min(pos_evens)}")
            print(f"Product number of positive evens = {math.prod(pos_evens)}")
        else:
            print(f"Max positive even number = {0}")
            print(f"Min positive even number = {0}")
            print(f"Product number of positive evens = {0}")
        separator()
        print("Negative evens =", *neg_evens)
        print(f"Number of negative evens = {len(neg_evens)}")
        if neg_evens:
            print(f"Max negative even number = {max(neg_evens)}")
            print(f"Min negative even number = {min(neg_evens)}")
            print(f"Product number of negative evens = {math.prod(neg_evens)}")
        else:
            print(f"Max negative even number = {0}")
            print(f"Min negative even number = {0}")
            print(f"Product number of negative evens = {0}")
        separator()
        print("Positive odds =", *pos_odds)
        print(f"Number of positive odds = {len(pos_odds)}")
        if pos_odds:
            print(f"Max positive odd number = {max(pos_odds)}")
            print(f"Min positive odd number = {min(pos_odds)}")
            print(f"Product number of odds = {math.prod(pos_odds)}")
        else:
            print(f"Max positive odd number = {0}")
            print(f"Min positive odd number = {0}")
            print(f"Product number of odds = {0}")
        separator()
        print("Negative odds =", *neg_odds)
        print(f"Number of negative odds = {len(neg_odds)}")
        if neg_odds:
            print(f"Max negative odd number = {max(neg_odds)}")
            print(f"Min negative odd number = {min(neg_odds)}")
            print(f"Product number of negative odds = {math.prod(neg_odds)}")
        else:
            print(f"Max negative odd number = {0}")
            print(f"Min negative odd number = {0}")
            print(f"Product number of negative odds = {0}")
        separator()
        print("Zeros =", *zeros)
        print(f"Number of zeros = {len(zeros)}")
        separator()
        print(f"Sum of numbers = {sum(converted)}")
        separator()
        if converted:
            print(f"Average number = {sum(converted) / len(converted)}")
        else:
            print("Can't divide over zero.")

        break


    except ValueError:
        print("Please enter only numbers separated by spaces.")

#           OR          #
# Manual solution:
# while True:
#     def separator():
#         print("".center(50,"="))

#     separator()
#     numbers = input("Enter numbers separated by space: ").strip().split()
#     separator()

#     try:
#         converted = [int(number) for number in numbers]

#         pos_evens = [pos_even for pos_even in converted if pos_even > 0 and pos_even % 2 == 0]
#         neg_evens = [neg_even for neg_even in converted if neg_even < 0 and neg_even % 2 == 0]

#         pos_odds = [pos_odd for pos_odd in converted if pos_odd > 0 and pos_odd % 2 != 0]
#         neg_odds = [neg_odd for neg_odd in converted if neg_odd < 0 and neg_odd % 2 != 0]

#         zeros = [zero for zero in converted if zero == 0]

#         if converted:
#             total =  converted[0]
#             if pos_evens:
#                 max_pos_even = min_pos_even = pos_even_prod = pos_evens[0]

#             else:
#                 max_pos_even = min_pos_even = pos_even_prod = 0
            
#             if neg_evens:
#                 max_neg_even = min_neg_even = neg_even_prod = neg_evens[0]
#             else:
#                 max_neg_even = min_neg_even = neg_even_prod = 0

#             if pos_odds:
#                 max_pos_odd = min_pos_odd = pos_odd_prod = pos_odds[0]
#             else:
#                 max_pos_odd = min_pos_odd = pos_odd_prod = 0
            
#             if neg_odds:
#                 max_neg_odd = min_neg_odd = neg_odd_prod = neg_odds[0]
#             else:
#                 max_neg_odd = min_neg_odd = neg_odd_prod = 0

#         else:
#             total =  0

#         for x in range(1, len(pos_evens)):
#             if max_pos_even < pos_evens[x]:
#                 max_pos_even = pos_evens[x]

#             if min_pos_even > pos_evens[x]:
#                 min_pos_even = pos_evens[x]
            
#             pos_even_prod *= pos_evens[x]

#         for x in range(1, len(neg_evens)):
#             if max_neg_even < neg_evens[x]:
#                 max_neg_even = neg_evens[x]

#             if min_neg_even > neg_evens[x]:
#                 min_neg_even = neg_evens[x]
            
#             neg_even_prod *= neg_evens[x]

#         for x in range(1, len(pos_odds)):
#             if max_pos_odd < pos_odds[x]:
#                 max_pos_odd = pos_odds[x]

#             if min_pos_odd > pos_odds[x]:
#                 min_pos_odd = pos_odds[x]
            
#             pos_odd_prod *= pos_odds[x]

#         for x in range(1, len(neg_odds)):
#             if max_neg_odd < neg_odds[x]:
#                 max_neg_odd = neg_odds[x]

#             if min_neg_odd > neg_odds[x]:
#                 min_neg_odd = neg_odds[x]
            
#             neg_odd_prod *= neg_odds[x]

#         for x in range(1, len(converted)):
#             total += converted[x]

#         print("Positive evens =", *pos_evens)
#         print(f"Number of positive evens = {len(pos_evens)}")
#         print(f"Max positive even number = {max_pos_even}")
#         print(f"Min positive even number = {min_pos_even}")
#         print(f"Product number of positive evens = {pos_even_prod}")
#         separator()
#         print("Negative evens =", *neg_evens)
#         print(f"Number of negative evens = {len(neg_evens)}")
#         print(f"Max negative even number = {max_neg_even}")
#         print(f"Min negative even number = {min_neg_even}")
#         print(f"Product number of negative evens = {neg_even_prod}")
#         separator()
#         print("Positive odds =", *pos_odds)
#         print(f"Number of positive odds = {len(pos_odds)}")
#         print(f"Max positive odd number = {max_pos_odd}")
#         print(f"Min positive odd number = {min_pos_odd}")
#         print(f"Product number of positive odds = {pos_odd_prod}")
#         separator()
#         print("Negative odds =", *neg_odds)
#         print(f"Number of negative odds = {len(neg_odds)}")
#         print(f"Max negative odd number = {max_neg_odd}")
#         print(f"Min negative odd number = {min_neg_odd}")
#         print(f"Product number of negative odds = {neg_odd_prod}")
#         separator()
#         print("Zeros =", *zeros)
#         print(f"Number of zeros = {len(zeros)}")
#         separator()
#         print(f"Sum of numbers = {total}")
#         separator()
#         if converted:
#             print(f"Average number = {total / len(converted)}")
#         else:
#             print("Can't divide over zero.")

#         break


#     except ValueError:
#         print("Please enter only numbers separated by spaces.")