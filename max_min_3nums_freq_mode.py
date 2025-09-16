from collections import Counter

while True:
    numbers = input("Enter numbers separated by space: ").strip().split()

    try:
        converted = [int(number) for number in numbers]

        # أكبر 3 أرقام
        top3_max = sorted(converted, reverse=True)[:3]
        print(f"Top 3 max numbers = {top3_max}")

        # أصغر 3 أرقام
        top3_min = sorted(converted)[:3]
        print(f"Top 3 min numbers = {top3_min}")

        # عدد الأرقام المكررة (frequency لكل رقم)
        counter = Counter(converted)
        print(f"Frequencies: {dict(counter)}")

        # الرقم الأكثر تكرارًا (mode)
        most_common_num, freq = counter.most_common(1)[0]
        print(f"Most common number (mode) = {most_common_num} (appears {freq} times)")

        break

    except ValueError:
        print("Please enter only numbers separated by spaces.")
