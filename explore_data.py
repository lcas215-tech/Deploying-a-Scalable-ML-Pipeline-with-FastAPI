import pandas as pd

df = pd.read_csv('data/census.csv')


def investigate(name):
    # query shape of file
    print("This is the amount of rows and columns", )
    print(name.shape, end="\n\n")

    # query file info
    print("This is the column name, amount of rows, and data type", end="\n\n")
    print(name.info(), end="\n\n")

    # Query data for null values
    print("This is how many null rows there are in each column")
    print(name.isnull().sum(), end="\n\n")

    # review descriptive statistics
    print("This is descriptive statistics of each column", end="\n\n")
    print(name.describe())

investigate(df)