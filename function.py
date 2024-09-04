import pandas as pd

def count_now(table, headers):
    group_col = None
    label = ""
    
    cat = {'Category', 'Category ID'}
    category_cols = list(set(headers) & cat)
    park_cols = list(set(headers) - cat)
    
    if category_cols:
        group_col = category_cols[0]
        label = "Count of Parks"
    elif park_cols:
        group_col = park_cols[0]
        label = "Count of Categories"

    if group_col:
        count_df = table.groupby(group_col).size().reset_index(name='count')
        table = pd.merge(table.drop_duplicates(), count_df, on=group_col, how='left')
    
    return table, label
