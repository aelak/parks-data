import pandas as pd

def count_now(table, headers):
    '''
    count_now performs two kinds of counting based on the selected columns:
            1) if 'Category' or 'Category ID' is selected, then the count will be of Parks
            2) for any other columns selected, the count will be of Categories
        
        The table undergoes groupby() - groups the data by the specified column then counts the occurrences (rows) for each group.
        The result is merged back into the original table, and the corresponding table and label (by Parks or Categories) are returned.
    '''
    group_col = None
    label = ""
    no_count_headers = list(set(headers) - {'count'})
    
    cat = {'Category', 'Category ID'}
    category_cols = list(set(no_count_headers) & cat)
    park_cols = list(set(no_count_headers) - cat)
    
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
