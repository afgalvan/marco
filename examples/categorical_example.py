from pandas.core.frame import DataFrame

from marco import categorical_table

table: DataFrame = categorical_table(["Coke Classic", "Sprite", "Pepsi", "Diet Coke",
          "Coke Classic", "Coke Classic", "Pepsi", "Diet Coke",
          "Coke Classic", "Diet Coke", "Coke Classic", "Coke Classic",
          "Coke Classic", "Diet Coke", "Pepsi", "Coke Classic",
          "Coke Classic", "Dr. Pepper", "Dr. Pepper", "Sprite", "Coke Classic",
          "Diet Coke", "Pepsi", "Diet Coke", "Pepsi", "Coke Classic", "Pepsi",
          "Pepsi", "Coke Classic", "Pepsi", "Coke Classic", "Coke Classic", 
          "Pepsi", "Dr. Pepper", "Pepsi", "Pepsi", "Sprite", "Coke Classic",
          "Coke Classic", "Coke Classic", "Sprite", "Dr. Pepper", "Diet Coke",
          "Dr. Pepper", "Pepsi", "Coke Classic", "Pepsi", "Sprite", 
          "Coke Classic", "Diet Coke"])

print(table)
