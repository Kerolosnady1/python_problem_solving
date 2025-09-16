# Enter numbers separated by space: 1 2 3 4 5
# Positive numbers: 1 2 3 4 5
# Number of positives: 5
# Negative numbers:
# Number of negatives: 0
# Zero numbers:
# Number of zeros: 0
# Sum: 15
# Average: 3.0


while True:

    numbers = input("Enter numbers separated by space: ").strip().split()

    try:

        converted = [int(number) for number in numbers]
        pos_nums= [pos for pos in converted if pos > 0]
        neg_nums= [neg for neg in converted if neg < 0]
        zeros = [zero for zero in converted if zero == 0]

        print(f"Positive numbers:", *pos_nums)
        print(f"Number of positives: {len(pos_nums)}")
        print(f"Negative numbers:", *neg_nums)
        print(f"Number of negatives: {len(neg_nums)}")
        print("Zero numbers:", *zeros)
        print(f"Number of zeros: {len(zeros)}")
        print(f"Sum: {sum(converted)}")
        if len(converted) != 0:
            print(f"Average: {sum(converted) / len(converted)}")
        else:
            print("You cann't divide any number over zero.")
        break

    except ValueError:
        print("Please enter only numbers separated by spaces.")


#           OR          #
# Manual solution:

# while True:

#     numbers = input("Enter numbers separated by space: ").strip().split()

#     try:

#         converted = [int(number) for number in numbers]

#         pos_nums = [pos for pos in converted if pos > 0]
#         neg_nums = [neg for neg in converted if neg < 0]
#         zeros = [zero for zero in converted if zero == 0]
#         if len(converted) != 0:
#             total = converted[0]
#         else:
#             total = 0

#         for x in range(1, len(converted)):
#             total += converted[x]

#         print("Positive numbers:", *pos_nums)
#         print(f"number of positives: {len(pos_nums)}")
#         print("".center(50, "="))
#         print("Negative numbers:", *neg_nums)
#         print(f"Number of negatives: {len(neg_nums)}")
#         print("".center(50, "="))
#         print("Zero numbers:", *zeros)
#         print(f"Number of zeros: {len(zeros)}")
#         print("".center(50, "="))
#         print(f"Sum: {total}")
#         print("".center(50, "="))
#         if len(converted) != 0:
#             print(f"Average: {total / len(converted)}")
#         else:
#             print("Cann't divide over zero.")

#         break


#     except ValueError:
#         print("Please enter only numbers separated by spaces.")