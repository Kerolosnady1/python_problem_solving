import statistics, math, pandas as pd, matplotlib.pyplot as plt, numpy
from collections import Counter


class NumbersAnalyzer:

    def __init__(self, numbers: list):
        self.numbers = numbers

    def sep(self):
        print("".center(55, "="))

    def calculations(self):
        self.zeros = [zero for zero in self.numbers if zero == 0]
        if self.numbers:
            self.freq = Counter(self.numbers)
            self.abs_vals = [abs(num) for num in self.numbers]
            self.max_freq = max(self.freq.values())
            self.modes = [num for num, count in self.freq.items() if self.max_freq == count]
            if sum(self.numbers) != 0:
                self.percentage = [x / sum(self.numbers) * 100 for x in self.numbers]
            if min(self.numbers) != max(self.numbers):
                self.norm = [(num - min(self.numbers)) / (max(self.numbers) - min(self.numbers)) for num in self.numbers]
            self.q1 = numpy.percentile(self.numbers, 25)
            self.q2 = numpy.percentile(self.numbers, 50)
            self.q3 = numpy.percentile(self.numbers, 75)
            self.iqr = self.q3 - self.q1
            self.lower_bond = self.q1 - 1.5 ** self.iqr
            self.upper_bond = self.q3 + 1.5 ** self.iqr
            self.outliers = [x for x in self.numbers if x < self.lower_bond or x > self.upper_bond]

    
    def even_odd(self, name: str, list_of_nums):
        self.sep()
        print(f"{name} numbers =".capitalize(), *list_of_nums)
        print(f"Number of {name} = {len(list_of_nums)}")
        if list_of_nums:
            print(f"Max {name} number = {max(list_of_nums)}")
            print(f"Min {name} number = {min(list_of_nums)}")
            print(f"Product of {name} numbers = {math.prod(list_of_nums)}")
            print(f"Total number of {name} = {sum(list_of_nums)}")
            print(f"Average number of {name} = {sum(list_of_nums) / len(list_of_nums)}")
        
        else:
            print(f"Empty list.")
        self.sep()

    def stat(self):
        if self.numbers:
            self.numbers.sort(reverse=True)
            self.sep(); print(f"Top 3 numbers = {self.numbers[:3]}")
            self.numbers.sort()
            self.sep(); print(f"Less 3 numbers = {self.numbers[:3]}")
            self.sep(); print(f"Ascending order = {self.numbers}")
            self.sep(); print(f"Range = {max(self.numbers) - min(self.numbers)}")
            self.sep(); print(f"Median = {statistics.median(self.numbers)}")
            self.sep(); print(f"Standard Deviation = {statistics.stdev(self.numbers)}")
            self.sep(); print(f"Variance = {statistics.variance(self.numbers)}")
            self.sep(); print(f"Frequencies: {dict(self.freq)}")
            self.sep(); print(f"Absolute values: {self.abs_vals}")
            self.sep(); print(f"Modes = {self.modes} appears {self.max_freq} times.")
            self.sep(); print(f"Percentage = {self.percentage}")
            self.sep(); print(f"Normalized = {self.norm}")
            self.sep(); print(f"Q1 = {self.q1}, Q2 = {self.q2}, Q3 = {self.q3}")
            self.sep(); print(f"InterQuartile Range = {self.iqr}")
            self.sep(); print(f"Lower bond = {self.lower_bond}\nUpper bond = {self.upper_bond}")
            self.sep(); print(f"Outliers: {self.outliers if self.outliers else 'No outliers found.'}")
        else:
            print("Empty list.")


    def summary(self):
        self.sep()
        print("Zeros =", *self.zeros)
        print(f"Number of zeros = {len(self.zeros)}")
        self.sep()
        print(f"Total = {sum(self.numbers)}")
        if self.numbers:
            self.sep(); print(f"Average = {sum(self.numbers) / len(self.numbers)}")
        else:
            print("Average: Can't divide over zero!")
        self.sep(); print(f"Max: {max(self.numbers)}")
        self.sep(); print(f"Min: {min(self.numbers)}")

    def virtual(self):
        if self.numbers:
            plt.hist(self.numbers, bins = 10, edgecolor = "blue")
            plt.title("Histogram of Numbers")
            plt.xlabel("Values")
            plt.ylabel("Frecuencies")
            plt.show()

            plt.boxplot(self.numbers, vert = False)
            plt.title("Boxplot of Numbers")
            plt.show()

            plt.pie(self.freq.values(), labels = self.freq.keys(), autopct = "%1.1f%%")
            plt.title("Pie Chart of Frequencies")
            plt.show()

            # Pandas summary statistics:
            self.series = pd.Series(self.numbers)
            print(self.series.describe())
        else:
            print("No numbers found!")


    
while True:
    numbers = input("Enter numbers separated by space: ").strip().split()

    try:
        converted = [int(number) for number in numbers]

        pos_evens = [pos_even for pos_even in converted if pos_even > 0 and pos_even % 2 == 0]
        neg_evens = [neg_even for neg_even in converted if neg_even < 0 and neg_even % 2 == 0]
        pos_odds = [pos_odd for pos_odd in converted if pos_odd > 0 and pos_odd % 2 != 0]
        neg_odds = [neg_odd for neg_odd in converted if neg_odd < 0 and neg_odd % 2 != 0]

        if converted:
            number = NumbersAnalyzer(converted)
            number.calculations()
            number.even_odd("positive even", pos_evens)
            number.even_odd("negative even", neg_evens)
            number.even_odd("positive odd", pos_odds)
            number.even_odd("negative odd", neg_odds)
            number.summary()
            number.stat()
            number.virtual()
        
        else:
            print(f"No numbers found!")
        
        break

    except ValueError:
        print(f"Please enter only numbers separated by spaces.")