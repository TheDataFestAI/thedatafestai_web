## Pandas

### Series:
Ref: https://pandas.pydata.org/docs/reference/series.html


### Dataframe:
Ref: https://pandas.pydata.org/docs/reference/frame.html

```python
import pandas as pd

df = 
```

### Dataframe Basic Functionalities:

| ID   | Topic | Commands |
| :--- | :---- | :------- | 
| 1  | Count of Rows, Columns of Dataframe | df.shape | 
| 2  | | |

### Dataframe Rows and Columns level Operations:

| ID   | Topic | Commands |
| :--- | :---- | :------- |
| 1    | 

### Dataframe Joins & Concat with Other Dataframes:

| ID   | Topic | Commands |
| :--- | :---- | :------- |
| 1  | Union/Concat 2 Dataframes           | pd.concat([df1, df2]) |


### Dataframe Other Functionality Understanding:

| ID   | Topic | Commands | Comments  |
| :--- | :---- | :------- | :-------: |
| 1    | copy()            | df1 = df.copy()                       | in Pandas, indexing a DataFrame returns a reference to the initial DataFrame. Thus, changing the subset will change the initial DataFrame. Thus, you'd want to use the copy if you want to make sure the initial DataFrame shouldn't change |
| 2    |       |          |           | 
