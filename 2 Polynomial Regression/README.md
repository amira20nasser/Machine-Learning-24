# Polynomial Regression
implement polynomial feature from scratch

## Preprocessing

- **Nulls:** There were no null values in the dataset.
- **Duplicated data:** A total of 127 rows containing duplicated data were removed.
- **Label Encoding:** The column `Extracurricular Activities` was encoded using label encoding for categorical data.

## Feature Selection Process

The Correlation Method was applied to analyze the relationship between columns and prioritize the most significant features.

- **Four Most Important Features Selected:**
  - “Previous Score”
  - “Hours Studied”
  - “Sleep Hours”
  - “Papers Practiced”

- **Mean square error for train:** 4.2
- **Mean square error for test data:** 4.4

- **Two Most Important Features Selected:**
  - “Previous Score”
  - “Hours Studied”

- **Mean square error for train:** 5.15
- **Mean square error for test data:** 5.56

## Conclusion

After comprehensive analysis and evaluation, the decision to prioritize features based on mean square error (MSE) led to the selection of "Previous Score," "Hours Studied," "Sleep Hours," and "Papers Practiced" as the four most important features for our predictive model.
