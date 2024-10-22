import pandas as pd
from sklearn.model_selection import train_test_split

"""
    ASSIGNMENT 2 (STUDENT VERSION):
    Using pandas to explore Titanic data from Kaggle (titanic.csv) and answer the questions.
"""

def Q1(df: pd.DataFrame):
    """
        Problem 1:
            How many rows are there in the “titanic.csv?
            Hint: In this function, you must load your data into memory before executing any operations. To access titanic.csv, use the path /data/titanic.csv.
    """
    return df.shape[0]


def Q2(df: pd.DataFrame):
    '''
        Problem 2:
            Drop unqualified variables
            Drop variables with missing > 50%
            Drop categorical variables with flat values > 70% (variables with the same value in the same column)
            How many columns do we have left?
    '''
    drop_column = []
    for col in df.columns:
        if ((df[col].isna().sum())/len(df[col])) > 0.5: #missing > 50%
            drop_column.append(df[col].name)
        if (df[col].value_counts().max()/len(df[col])) > 0.7: #flat > 70%
            drop_column.append(df[col].name)
    df.drop(drop_column, axis=1, inplace=True)        
    return df.shape[1]


def Q3(df: pd.DataFrame):
    '''
       Problem 3:
            Remove all rows with missing targets (the variable "Survived")
            How many rows do we have left?
    '''
    df.dropna(subset=['Survived'], inplace=True)
    return df.shape[0]


def Q4(df: pd.DataFrame):
    '''
       Problem 4:
            Handle outliers
            For the variable “Fare”, replace outlier values with the boundary values
            If value < (Q1 - 1.5IQR), replace with (Q1 - 1.5IQR)
            If value > (Q3 + 1.5IQR), replace with (Q3 + 1.5IQR)
            What is the mean of “Fare” after replacing the outliers (round 2 decimal points)?
            Hint: Use function round(_, 2)
    '''
    Q1 = df['Fare'].quantile(0.25)
    Q3 = df['Fare'].quantile(0.75)
    IQR = Q3-Q1
    
    lower = Q1-1.5*IQR
    upper = Q3+1.5*IQR

    for i in range(0, len(df['Fare'])):
        if df.loc[i,'Fare'] > upper:
            df.loc[i,'Fare'] = upper
        elif df.loc[i,'Fare'] < lower:
            df.loc[i,'Fare'] = lower
    return round(df['Fare'].mean(), 2)

def Q5(df: pd.DataFrame):
    '''
       Problem 5:
            Impute missing value
            For number type column, impute missing values with mean
            What is the average (mean) of “Age” after imputing the missing values (round 2 decimal points)?
            Hint: Use function round(_, 2)
    '''
    df.fillna(df.mean(numeric_only=True), inplace=True)
    df.fillna(df.mode().iloc[0], inplace=True)
    return round(df["Age"].mean(),2)


def Q6(df: pd.DataFrame):
    '''
        Problem 6:
            Convert categorical to numeric values
            For the variable “Embarked”, perform the dummy coding.
            What is the average (mean) of “Embarked_Q” after performing dummy coding (round 2 decimal points)?
            Hint: Use function round(_, 2)
    '''
    df_dummies = pd.get_dummies(df, columns=['Embarked'], prefix='Embarked')
    df = pd.concat([df, df_dummies], axis=1)
    df = df.drop("Embarked", axis=1)
    return round(df["Embarked_Q"].mean(),2)


def Q7(df: pd.DataFrame):
    '''
        Problem 7:
            Split train/test split with stratification using 70%:30% and random seed with 123
            Show a proportion between survived (1) and died (0) in all data sets (total data, train, test)
            What is the proportion of survivors (survived = 1) in the training data (round 2 decimal points)?
            Hint: Use function round(_, 2), and train_test_split() from sklearn.model_selection
    '''
    X = df
    y = df.pop("Survived")
    
    X_train, X_test, y_train, y_test = train_test_split(X,y,stratify=y,test_size=0.3,random_state=123)
    return round(len(y_train[y_train == 1])/len(y_train),2)
