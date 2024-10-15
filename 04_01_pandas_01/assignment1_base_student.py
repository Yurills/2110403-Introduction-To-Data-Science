import pandas as pd

def main():
    file = input()
    func = input()
    
    df = pd.read_csv(file)


    if func == 'Q1':
        return df.shape
    elif func == 'Q2':
        return df["score"].max()
    elif func == 'Q3':
        cond = df["score"] >= 80
        return df[cond]["id"].count()
    else:
        return "No Output"

if __name__ == "__main__":
    print(main())