# Enter numbers separated by space: -1 2 0 0 2 3 4 5 -2
# ==================================================
# Positive evens = 2 2 4
# Number of positive evens = 3
# Max positive even number = 4
# Min positive even number = 2
# ==================================================
# Negative evens = -2
# Number of negative evens = 1
# Max negative even number = -2
# Min negative even number = -2
# ==================================================
# Positive odds = 3 5
# Number of positive odds = 2
# Max positive odd number = 5
# Min positive odd number = 3
# ==================================================
# Negative odds = -1
# number of negative odds = 1
# Max negative odd number = -1
# Min negative odd number = -1
# ==================================================
# Zeros = 0 0
# Number of zeros = 2
# ==================================================
# Sum of numbers = 13
# ==================================================
# Average number = 1.4444444444444444

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
        if len(pos_evens) != 0:
            print(f"Max positive even number = {max(pos_evens)}")
            print(f"Min positive even number = {min(pos_evens)}")
        else:
            print(f"Max positive even number = {0}")
            print(f"Min positive even number = {0}")

        separator()
        print("Negative evens =", *neg_evens)
        print(f"Number of negative evens = {len(neg_evens)}")
        if len(neg_evens) != 0:
            print(f"Max negative even number = {max(neg_evens)}")
            print(f"Min negative even number = {min(neg_evens)}")
        else:
            print(f"Max negative even number = {0}")
            print(f"Min negative even number = {0}")

        separator()
        print("Positive odds =", *pos_odds)
        print(f"Number of positive odds = {len(pos_odds)}")
        if len(pos_odds) != 0:
            print(f"Max positive odd number = {max(pos_odds)}")
            print(f"Min positive odd number = {min(pos_odds)}")
        else:
            print(f"Max positive odd number = {0}")
            print(f"Min positive odd number = {0}")

        separator()
        print("Negative odds =", *neg_odds)
        print(f"number of negative odds = {len(neg_odds)}")
        if len(neg_odds) != 0:
            print(f"Max negative odd number = {max(neg_odds)}")
            print(f"Min negative odd number = {min(neg_odds)}")
        else:
            print(f"Max negative odd number = {0}")
            print(f"Min negative odd number = {0}")

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
        separator()


#           OR          #
# Manual solution:

# while True:
    
#     def separator() -> None:
#         print("".center(50, "="))

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
#             total = converted[0]
#         else:
#             total = 0

#         for x in range(1, len(converted)):
#             total += converted[x]

#         if pos_evens:
#             max_pos_even = min_pos_even = pos_evens[0]
#         else:
#             max_pos_even = min_pos_even = 0

#         for x in range(1, len(pos_evens)):
#             if max_pos_even < pos_evens[x]:
#                 max_pos_even = pos_evens[x]

#             if min_pos_even > pos_evens[x]:
#                 min_pos_even = pos_evens[x]

#         if neg_evens:
#             max_neg_even = min_neg_even = neg_evens[0]
#         else:
#             max_neg_even = min_neg_even = 0

#         for x in range(1, len(neg_evens)):
#             if max_neg_even < neg_evens[x]:
#                 max_neg_even = neg_evens[x]

#             if min_neg_even > neg_evens[x]:
#                 min_neg_even = neg_evens[x]
#         if pos_odds:
#             max_pos_odd = min_pos_odd = pos_odds[0]
#         else:
#             max_pos_odd = min_pos_odd = 0

#         for x in range(1, len(pos_odds)):
#             if max_pos_odd < pos_odds[x]:
#                 max_pos_odd = pos_odds[x]

#             if min_pos_odd > pos_odds[x]:
#                 min_pos_odd = pos_odds[x]
#         if neg_odds:
#             max_neg_odd = min_neg_odd = neg_odds[0]
#         else:
#             max_neg_odd = min_neg_odd = 0

#         for x in range(1, len(neg_odds)):
#             if max_neg_odd < neg_odds[x]:
#                 max_neg_odd = neg_odds[x]
            
#             if min_neg_odd > neg_odds[x]:
#                 min_neg_odd = neg_odds[x]

#         print("Positive evens =", *pos_evens)
#         print(f"Number of positive evens = {len(pos_evens)}")
#         print(f"Max positive even number = {max_pos_even}")
#         print(f"Min positive even number = {min_pos_even}")
#         separator()
#         print("Negative evens =", *neg_evens)
#         print(f"Number of negative evens = {len(neg_evens)}")
#         print(f"Max negative even number = {max_neg_even}")
#         print(f"Min negative even number = {min_neg_even}")
#         separator()
#         print("Positive odds =", *pos_odds)
#         print(f"Number of positive odds = {len(pos_odds)}")
#         print(f"Max positive odd number = {max_pos_odd}")
#         print(f"Min positive odd number = {min_pos_odd}")
#         separator()
#         print("Negative odds =", *neg_odds)
#         print(f"Number of negative odds = {len(neg_odds)}")
#         print(f"Max negative odd number = {max_neg_odd}")
#         print(f"Min negative odd number = {min_neg_odd}")
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
#         separator()