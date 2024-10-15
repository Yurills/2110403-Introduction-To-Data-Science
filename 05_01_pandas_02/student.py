import pandas as pd
import json

"""
    ASSIGNMENT 1 (STUDENT VERSION):
    Using pandas to explore youtube trending data from GB (GBvideos.csv and GB_category_id.json) and answer the questions.
"""
dataframe = pd.read_csv('USvideos.csv')
def Q1():
    vdo_df = dataframe
    """
        1. How many rows are there in the GBvideos.csv after removing duplications?
        - To access 'GBvideos.csv', use the path '/data/GBvideos.csv'.
    """
    return vdo_df.drop_duplicates().shape[0]

def Q2(vdo_df):
    '''
        2. How many VDO that have "dislikes" more than "likes"? Make sure that you count only unique title!
            - GBvideos.csv has been loaded into memory and is ready to be utilized as vdo_df
            - The duplicate rows of vdo_df have been removed.
    '''
    cond = vdo_df["dislikes"] > vdo_df["likes"]
    return vdo_df[cond]["title"].nunique()

def Q3(vdo_df):
    '''
        3. How many VDO that are trending on 22 Jan 2018 with comments more than 10,000 comments?
            - GBvideos.csv has been loaded into memory and is ready to be utilized as vdo_df
            - The duplicate rows of vdo_df have been removed.
            - The trending date of vdo_df is represented as 'YY.DD.MM'. For example, January 22, 2018, is represented as '18.22.01'.
    '''
    cond = (vdo_df["trending_date"] == '18.22.01') & (vdo_df['comment_count'] > 10000)
    return vdo_df[cond]["video_id"].nunique()
def Q4(vdo_df):
    '''
        4. Which trending date that has the minimum average number of comments per VDO?
            - GBvideos.csv has been loaded into memory and is ready to be utilized as vdo_df
            - The duplicate rows of vdo_df have been removed.
    '''
    group = vdo_df.groupby("trending_date")["comment_count"].mean().sort_values()
    return group.index[0]

def Q5(vdo_df):
    '''
        5. Compare "Sports" and "Comedy", how many days that there are more total daily views of VDO in "Sports" category than in "Comedy" category?
            - GBvideos.csv has been loaded into memory and is ready to be utilized as vdo_df
            - The duplicate rows of vdo_df have been removed.
            - You must load the additional data from 'GB_category_id.json' into memory before executing any operations.
            - To access 'GB_category_id.json', use the path '/data/GB_category_id.json'.
    '''
    with open('US_category_id.json') as fd:
        js = json.load(fd)
    category = []
    for i in js['items']:
        category.append((int(i['id']), i['snippet']['title']))

    category_df = pd.DataFrame(category, columns = ["id", "category"])
    merged_df =  vdo_df.merge(category_df, left_on="category_id",right_on="id")

    cond = (merged_df["category"] == "Sports") | (merged_df["category"] == "Comedy")
    merged_df = merged_df[cond]

    group = merged_df.groupby(['trending_date','category'])['views'].sum().reset_index()

    pivot_df = group.pivot(index=["trending_date"], columns=['category'], values=['views'])
   
    cond = pivot_df["views"]["Comedy"] < pivot_df["views"]["Sports"]

    return pivot_df[cond].shape[0]
print(Q1())
print(Q2(dataframe))
print(Q3(dataframe))
print(Q4(dataframe))
print(Q5(dataframe))