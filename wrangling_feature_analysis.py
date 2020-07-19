"""
Data wrangling with some wine data from UCI
"""

# %%

import pandas as pd

df = pd.read_csv('data/uci/20091017 wine-quality/winequality-white.csv', sep=';')
df = df.rename(columns=lambda s: s.replace(' ', '_'))
df.head()


def rank_feature(df, feature):
    r"""

    Parameters
    ----------
    df : DataFrame
    feature: str

    Returns
    -------
    DataFrameGroupBy

    """
    rank = feature + '_rank'
    median = df[feature].median()
    for i, f in enumerate(df[feature]):
        if f >= median:
            df.loc[i, rank] = 'high'
        else:
            df.loc[i, rank] = 'low'
    return df.groupby(rank)


for feature in df.columns[:-1]:
    print(rank_feature(df, feature)['quality'].mean(), '\n')
