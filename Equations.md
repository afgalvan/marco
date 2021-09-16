# Decentralized trend measures (Continuation)

## Quartiles or Quantiles

Quartiles are three values that divide a set of ordered data into four equal parts (of 25% each part). 

To solve a problem about quartiles we only have to find Q1; Q2 and Q3.

__________________________________________________________

#### How to find quartiles for ungrouped data?

1. Sort the data (Ascending order).
2. Apply the formula:

        k = Must be 1, 2 or 3.

        Pos(Qk) = k(n + 1) / 4

Example:

        Sorted data

            4   4   8   8   10  10  12  12  13
            16  16  20  20  22  26  
            n = 15

        Finding Q2

            Pos(Q2) = 2(15 + 1) / 4 => 8

It means that the value of **Q2** is the data located in the 8th position of the list.

In this case it is **12**.

Q2 will always be the median of the data.

__________________________________________________________

#### How to find quartiles for grouped data?

Where:
        
        Qk: The quartial to find.
        Li: Lower limit of the selected range.
         k: Must be 1, 2 or 3.
         n: Total number of data.
        fi: Absolute frequency of the selected interval.
      Fi_1: Previous Cumulative Absolute Frequency.
        ai: Interval width (Subtract the 2 values: L sup - L inf)

Assuming we have the table filled with all its values

1. Find the Quartile class:
        
        Quartile class = (k * n) / 4
Then in the Column of the accumulated frequency choose the first value higher than the quartile class found.

2. Apply the formula:

        Qk = Li + ai * ((Quartile class - Fi_1) / fi)

Example: Find the first quartile of the following table of frequencies that shows the worked years of some employees of the ABC Company.

| Worked years | fi     | Fi |
|:-------------|--------|---:|
| 1 - 8        | 9      |  9 |
| 8 - 15       | 7      | 16 |
| 15 - 22      | 12     | 28 |
| 15 - 22      | 12     | 28 |
| 22 - 29      | 16     | 44 |
| 29 - 36      | 8      | 52 |
| 36 - 43      | 3      | 55 |
| Total        | n = 55 |    |

1st Quartil 

        Quartil class = (1 * 55) / 4 => 13,75


        Q1 = 8 + 7 * ((13,75 - 9) / 7) => 12,7

It means that the 25% of the employees have worked 12,7 years or less.

__________________________________________________________

## Deciles

Deciles are nine values that divide a set of ordered data into ten equal parts (of 10% each part). 

To solve a problem about deciles we have to find D1; D2; D3; D4; ... D9.

__________________________________________________________

#### How to find deciles for ungrouped data?

The equation to resolve a decile problem is:

        Pos(Dk) = (K * (n + 1)) / 10

To explain the solution let's take the same ungrouped data from the previous exercise: 

        4   4   8   8   10  10  12  12  13
        16  16  20  20  22  26  
        n = 15

        Finding D4

                1. Pos(D4) = (4 * (15 + 1)) / 10 => 6,4 <- Decile class

In most cases the result will be a decimal number, to continue we must subtract **the approximate value higher than the decile class** with the **value of the data found in the integer part of the same** and multiply it by its decimal part.

In this case because the result is **6,4** ; The approximate higher value will be **7**, the integer part is **6**, and the decimal part is **0,4**.

So...

        (Pos(7) - Pos(6)) * 0,4

        Replacing values...

        1. (12 - 10) * 0,4 => 0,8 

As the last step, we have to add to the integer part (that is, 6 in this case) of the first result, the decimal result that we have just found.

        D4 = Pos(6) + 0,8
           = 10 + 0,8
           = 10,8

The value of the fourth decile of the data is **10,8**.

It means that the 40% of the data will be **10,8** or less.

__________________________________________________________

#### How to find deciles for grouped data?

Where:
        
        Dk: The decil to find.
        Li: Lower limit of the selected range.
         k: Must be 1, 2, 3, 4, ... , 9.
         n: Total number of data.
        fi: Absolute frequency of the selected interval.
      Fi_1: Previous Cumulative Absolute Frequency.
        ai: Interval width (Subtract the 2 values: L sup - L inf)

Assuming we have the table filled with all its values

1. Find the Decile class:

        Pos(Dk) = (K * (n + 1)) / 10

Then in the Column of the accumulated frequency choose the first value higher than the decile class found.

2. Apply the formula:

        Dk = Li + ai * ((Decile class - Fi_1) / fi)

**To find the decile is exactly the same as how the quartile is found in grouped data.**

__________________________________________________________

## Percentiles

ercentiles are the 99 values ​​of the variable that divide a data set ordered into 100 equal parts (of 1% each part). 

So to solve a problem about percentiles we have to find P1; P2; P3; P4; ...; P99

To find the Percentiles we follow the same procedure as the Quartiles and Deciles.

__________________________________________________________

#### How to find percentiles for grouped data?

1. Find the Percentile class:

        Pos(Pk) = (K * (n + 1)) / 100

2. Apply the formula:

        Pk = Li + ai * (Percentile class - Fi_1) / fi)

__________________________________________________________

# Dispersion measures

These measurements are very useful because they give us an idea of ​​how close or far the data is from an average value. If the result is close to zero (0) it is said that there is no dispersion or variability of the data but if it is far from zero (0), it is said that there is a lot of dispersion in the data.

Some of the equations used are:

### Range

        R = Vmax - Vmin

__________________________________________________________

### Interquartile range

        IQr = Q3 - Q1

__________________________________________________________

### Deviations

        D = |Xi - mean|
                or
        D = |mi - mean|

        Note: "Xi" and "mi" are the same, it depends in what do you prefer and use.

__________________________________________________________

### Quadratic deviation

        D = (Xi - mean) ^ 2
                or
        D = (mi - mean) ^ 2

__________________________________________________________

### Variance

It is defined as the mean of the squares of the differences between the values ​​that the variable takes, with respect to its arithmetic mean. The results are given in squared units.

There are two types:

- Statistic sample (s2)

For non grouped data: 

        s2 = Σ(Quadratic deviation) / n-1

For grouped data: 

        s2 = (Σ(Quadratic deviation) * ni) / n-1


- Statistical population (v2)

        v2 = (Σ(Xi - u)^2) / N

__________________________________________________________

### Standard deviation

It is the square root of the variance. It is the measure that is used the most because its result is given in the original units when obtaining the square root.

- Statistic sample (s2)

        S = sqrt(variance)

                or

        S = sqtr(s2)

- Statistical population (v2)

        V = sqrt(v2)

__________________________________________________________

### Variation coefficient

It is defined as the quotient of dividing the standard deviation by its respective arithmetic mean. It is very useful when comparing groups that have different units of measurement

        Cv = (S / mean) * 100

__________________________________________________________

# Dispersion measures(variability)

### Standard score

It is expressed as deviations with respect to the sample mean, in units of standard deviation. It is used in the transformation of values ​​of a given variable on a certain scale to Z scores. They also serve to indicate the relative position of an element of the distribution with respect to the measure in units of standard deviation.

        where "u" is the total amount of data given, 
        and "S" is the variance.

        Z = (mean - u) / S

It is usually used when comparing two samples, to draw conclusions from the results.

__________________________________________________________

### Chebyshev's theorem

Chebyshev's inequality is a theorem used in statistics that provides a conservative estimate (confidence interval) of the probability that a random variable with finite variance will be at a certain distance from its mathematical expectation or its mean.

Equation:

        (1 - (1 / Z^2)) * 100

Example:

        Where Z = 2, Then

        1 - (1 / 2^2) * 100 => 75% 

__________________________________________________________

# 5 Points summary

| Vmin  | Q1    | Q2     | Q3    |  Vmax |
|:------|-------|--------|-------|------:|
| 149.5 | 161,7 | 167,07 | 171,5 | 191.5 |

        Interquartile range ()

        IQr = Q3 - Q1
            = 171,5 - 161,7
            = 9.8

__________________________________________________________

### Moderate outliers

        Dam = 1.5 * IQr
            = 1.5 * 9.8 => 14,7

To get the intervals

        data < Q1 - Dam
             < 161,7 - 14,7 => 147

        data > Q3 + Dam
             > 171,5 + 14,7 => 186,2

**Interval (147 - 186,2)**

__________________________________________________________

### Extreme outliers

        Dae = 3 * IQr
            = 3 * 9.8 => 29,4

To get the intervals

        data < Q1 - Dam
             < 161,7 - 29,4 => 132,3

        data > Q3 + Dam
             > 171,5 + 29,4 => 200,9
