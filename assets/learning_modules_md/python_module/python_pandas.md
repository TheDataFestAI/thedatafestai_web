## Pandas

### Series:
Ref: https://pandas.pydata.org/docs/reference/series.html


### Dataframe:
Ref: https://pandas.pydata.org/docs/reference/frame.html

```python
import pandas as pd

df = pd.DataFrame({
    'col_1': [1, 2, 3],
    'col_2': ['emp1', 'emp2', 'emp3'],
    'col_3': ['India', 'UK', 'USA']
})

df.head()
```

### Dataframe Basic Functionalities:

| ID   |Commands | Topic |
| :--- | :---- | :------- | 
| 1  | df.shape | Count of Rows, Columns of Dataframe | 
| 2  | | |

### Dataframe Rows and Columns level Operations:

| ID   | Commands | Details |
| :--- | :---- | :------- |
| 1    | **df.at[\<index\>, \<column\>]** | 1. Will return the data in a dataframe at the passed location.<br>2. Will return single value, hence it is faster than **df.loc()**.|

```python
import pandas as pd

df = pd.DataFrame({
    'col_1': [1, 2, 3],
    'col_2': ['emp1', 'emp2', 'emp3'],
    'col_3': ['India', 'UK', 'USA']
})
```
```python
df.at[2,'col_2']  # output: emp3
```

### Dataframe Joins & Concat with Other Dataframes:

| ID   | Commands | Details |
| :--- | :---- | :------- |
| 1  | pd.concat([df1, df2])           | Concat 2 Dataframes |

```python
import pandas as pd

df1 = pd.DataFrame({
    'col_1': [3],
    'col_2': ['emp3'],
    'col_3': ['India']
})

df2 = pd.DataFrame({
    'col_1': [4],
    'col_2': ['emp4'],
    'col_3': ['UK']
})

df3 = pd.DataFrame({
    'col_1': [5],
    'col_2': ['emp5'],
    'col_3': ['USA']
})
```
```python
df = pd.concat([df1, df2, df3])
```

### Dataframe Other Functionality Understanding:

| ID   | Commands | Comments  |
| :--- | :------- | :-------- |
| 1    | df1 = df.copy()                       | in Pandas, indexing a DataFrame returns a reference to the initial DataFrame. Thus, changing the subset will change the initial DataFrame.<br> Thus, you'd want to use the copy if you want to make sure the initial DataFrame shouldn't change |
| 2    |          |           | 
