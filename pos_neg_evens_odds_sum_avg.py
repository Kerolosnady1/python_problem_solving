# Enter numbers separated by space: -1 2 0 -2 0 1 3 5
# ==================================================
# Positive evens = 2
# Number of positive evens: 1
# ==================================================
# Negative evens = -2
# Number of negative evens = 1
# ==================================================
# Positive odds = 1 3 5
# Number of positive odds = 3
# ==================================================
# Negative odds = -1
# Number of negative odds = 1
# ==================================================
# Zeros = 0 0
# Number of zeros = 2
# ==================================================
# Sum = 8
# ==================================================
# Average = 1.0

while True:

    numbers = input("Enter numbers separated by space: ").strip().split()
    print("".center(50, "="))

    try:
        converted = [int(number) for number in numbers]

        # pos_nums = [pos for pos in converted if pos > 0]
        # neg_nums = [neg for neg in converted if neg < 0]
        pos_evens = [pos_even for pos_even in converted if pos_even > 0 and pos_even % 2 == 0]
        neg_evens = [neg_even for neg_even in converted if neg_even < 0 and neg_even % 2 == 0]

        pos_odds = [pos_odd for pos_odd in converted if pos_odd > 0 and pos_odd % 2 != 0]
        neg_odds = [neg_odd for neg_odd in converted if neg_odd < 0 and neg_odd % 2 != 0]
        zeros = [zero for zero in converted if zero == 0]

        print("Positive evens =", *pos_evens)
        print(f"Number of positive evens: {len(pos_evens)}")
        print("".center(50, "="))
        print("Negative evens =", *neg_evens)
        print(f"Number of negative evens = {len(neg_evens)}")
        print("".center(50, "="))
        print("Positive odds =", *pos_odds)
        print(f"Number of positive odds = {len(pos_odds)}")
        print("".center(50, "="))
        print("Negative odds =", *neg_odds)
        print(f"Number of negative odds = {len(neg_odds)}")
        print("".center(50, "="))
        print("Zeros =", *zeros)
        print(f"Number of zeros = {len(zeros)}")
        print("".center(50, "="))
        print(f"Sum = {sum(converted)}")
        print("".center(50, "="))
        if len(converted) != 0:
            print(f"Average = {sum(converted) / len(converted)}")
        else:
            print("Cann't divide over zero.")

        break


    except ValueError:
        print("Please enter only numbers separated by spaces.")


#           OR          #
# Manual solution:

# while True:
#     def separator() -> None:
#         print("".center(50, "="))

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

#         for num in range(1, len(converted)):
#             total += converted[num]

#         print("Positive even numbers =", *pos_evens)
#         print(f"Number of positive evens = {len(pos_evens)}")
#         separator()
#         print("Negative even numbers =", *neg_evens)
#         print(f"Number of negative evens = {len(neg_evens)}")
#         separator()
#         print("Positive odd numbers =", *pos_odds)
#         print(f"Number of positive odds = {len(pos_odds)}")
#         separator()
#         print("Negative odd numbers =", *neg_odds)
#         print(f"Number of negative odds = {len(neg_odds)}")
#         separator()
#         print("Zeros =", *zeros)
#         print(f"Number of zeros = {len(zeros)}")
#         separator()
#         print(f"Sum of numbers = {total}")
#         separator()
#         if converted:
#             print(f"Average numbers = {total / len(converted)}")
#         else:
#             print("Cann't divide over zero.")

#         break



#     except ValueError:
#         print("Please enter only numbers separated by spaces.")