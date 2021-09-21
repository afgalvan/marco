# import os
# import sys

# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from marco import GroupedFrame, QuantitativeFrame, quantitative_table
from matplotlib.pyplot import show

# Grouped data ----------------------------------------------------------
grouped_data = [
    170, 172, 183, 164, 166, 164, 160, 168, 173,
    176, 184, 190, 163, 151, 158, 166, 166, 172,
    170, 186, 170, 166, 169, 160, 158, 155, 160,
    157, 163, 165, 170, 172, 178, 183, 170, 166,
    165, 172, 168, 158, 158, 168, 166, 159, 154,
    166, 172, 168, 163, 172,
]

quantitative_frame: GroupedFrame = quantitative_table(grouped_data)
dataframe = quantitative_frame.dataframe
print(dataframe)
axe = dataframe["hi"].plot.hist(grid=True, bins=len(dataframe), rwidth=quantitative_frame.interval)
for bar in axe.containers:
    axe.bar_label(bar)
show()

print(quantitative_frame.quantile())
print("\nDecile")
print(quantitative_frame.decile([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print("\nPercentile")
print(quantitative_frame.percentile([99]))
print(quantitative_frame.dataframe)
print("\n\nmedia aritmética: ", quantitative_frame.arithmetic_mean())
print("moda: {:.2f}".format(quantitative_frame.trend()))
print("fila: ")
print(quantitative_frame.trend_row())
print("mediana: {:.2f}".format(quantitative_frame.median()))
print("fila: ")
print(quantitative_frame.median_row())

# Ungrouped --------------------------------------------------------------
ungrouped_data = [4, 4, 8, 8, 10, 10, 12, 12, 13, 16, 16, 20, 20, 22, 2]
quantitative_frame: QuantitativeFrame = quantitative_table(ungrouped_data)
print(quantitative_frame.quantile())
print(quantitative_frame.decile([6, 4]))
print(quantitative_frame.percentile([99]))
print("Ta bli ta")
print(quantitative_frame.dataframe)
print("\nMedia arigmedica")
print(quantitative_frame.arithmetic_mean())
print("\nMediana")
print(quantitative_frame.median())
print("Fila: ")
print(quantitative_frame.median_row())
print("\nModa")
print(quantitative_frame.trend())
print("Fila: ")
print(quantitative_frame.trend_row())
