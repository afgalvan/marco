import os
import sys
import matplotlib.pyplot as plt

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from marco import QuantitativeFrame, quantitative_table

data = [170, 172, 183, 164 ,166, 164, 160, 168, 173, 176,
184, 190, 163, 151, 158, 166 ,166, 172, 170, 186,
170, 166, 169, 160, 158, 155 ,160, 157, 163, 165,
170, 172, 178, 183, 170, 166 ,165, 172, 168, 158,
158, 168, 166, 159, 154, 166 ,172, 168, 163, 172]


data2 = [4, 5, 6, 7, 4, 5, 7, 7, 5, 7, 1, 3, 4, 5, 6, 3, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 6]
quantitative_frame: QuantitativeFrame = quantitative_table(data2)

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
