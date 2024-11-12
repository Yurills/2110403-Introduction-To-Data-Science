import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
import numpy as np
import warnings
from sklearn.exceptions import ConvergenceWarning
warnings.filterwarnings("ignore", category=ConvergenceWarning)
class BankLogistic:
    def __init__(self, data_path): # DO NOT modify this line
        self.data_path = data_path
        self.df = pd.read_csv(data_path, sep=',')
    def Q1(self): # DO NOT modify this line
        """
        Problem 1:
        Load ‘bank-st.csv’ data from the “Attachment”
        How many rows of data are there in total?
        """
        return self.df.shape[0]
    def Q2(self): # DO NOT modify this line
        """
        Problem 2:
        How many numeric variables are there ?
        """
        return self.df.select_dtypes(include=[np.number]).shape[1]

    def Q3(self): # DO NOT modify this line
        """
        Problem 3:
        How many categorical variables are there?
        """
        return self.df.select_dtypes(include=[object]).shape[1]


    def Q4(self): # DO NOT modify this line
        """
        Problem 4:
        What is the distribution of the target variable for the 'NO' class?
        """
        return self.df['y'].value_counts()['no']/self.df['y'].value_counts().sum()
        

    def Q5(self): # DO NOT modify this line
        """
        Problem 5:
        Drop duplication of the data
        What are the shapes of the data?
        """
        self.df.drop_duplicates(inplace=True)
        return self.df.shape


    def Q6(self):
        """
        Problem 6:
        How many null values are there in the job and education columns?
        For numeric variables, fill missing values with the mean, and for
        categorical variables, fill missing values with the mode.
        Hint: replace unknown with null
        """
        self.Q5();
        
        self.df = self.df.replace('unknown', np.nan)
        
        job = self.df['job'].isna().sum()
        education = self.df['education'].isna().sum()
        
    
        
        self.df.fillna(self.df.mean(numeric_only=True) ,inplace=True)
        self.df.fillna(self.df.mode().iloc[0], inplace=True)
        
        return (int(job),int(education))
        
        
        
    def Q7(self):
        """
        Problem 7:
        Split train/test for 70%:30% with random_state=0 & stratify option
        What are the shapes of X_train and X_test?
        Hint: Don't forget to encode categorical data using pd.get_dummies before
        splitting the data.
        """
        self.Q6();
        
        
        y = self.df.pop("y")
        df = pd.get_dummies(self.df, drop_first=True)
        X = df
        
        
        X_train, X_test, y_train, y_test = train_test_split(X,y,stratify=y,test_size=0.3, random_state=0)
        return X_train.shape, X_test.shape

    def Q8(self):
        """
        Problem 8:
        How much data does the test set contain for the class 'No'?
        """
        self.Q6();
        
        
        y = self.df.pop("y")
        df = pd.get_dummies(self.df, drop_first=True)
        X = df
        
        
        X_train, X_test, y_train, y_test = train_test_split(X,y,stratify=y,test_size=0.3, random_state=0)
        return y_test.value_counts()['no']
    
        
    def Q9(self):
        """
        Problem 9:
        Set the model to be used as Logistic Regression only with random_state=0
        and max_iter=5000
        Build a model that uses all variables.
        What is the macro F1 score for Model on the test data? (Answer with two
        decimal places).
        """
        self.Q6();
        
        
        y = self.df.pop("y")
        df = pd.get_dummies(self.df, drop_first=True)
        X = df
        
        
        X_train, X_test, y_train, y_test = train_test_split(X,y,stratify=y,test_size=0.3, random_state=0)
        
        logmodel = LogisticRegression(random_state=0, max_iter=5000)
        logmodel.fit(X_train,y_train)
        prediction = logmodel.predict(X_test)
        
        macro_f1 = f1_score(y_test, prediction, average='macro')
        
        

        return round(macro_f1,2)