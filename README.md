
# Data Profiling and Anomaly Detection Assignment

## Problem Description

In this assignment, you will practice data profiling to understand the characteristics of a dataset and implement a simple anomaly detection technique. Identifying anomalies is crucial for data quality and fraud detection.

## Instructions

1.  Open the `assignment.py` file.
2.  You will find two function definitions: `profile_data(df)` and `detect_anomalies(df, column)`.
3.  Your task is to implement these functions:
    *   `profile_data`: Return a dictionary containing the number of unique values and missing values for each column in the input DataFrame `df`.
    *   `detect_anomalies`: Identify anomalies in a specified `column` of the DataFrame `df` using the Z-score method (values with a Z-score greater than 3 are considered anomalies).

## Further Exploration (Optional)

*   Explore more advanced data profiling libraries like `Pandas Profiling`.
*   Investigate other anomaly detection algorithms, such as Isolation Forest or One-Class SVM.
*   How can you visualize the anomalies in your data?
