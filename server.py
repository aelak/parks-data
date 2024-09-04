from flask import Flask, render_template, request
from parse import get_data, displaying_col
import pandas as pd
from waitress import serve
from function import count_now

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])

def index(): 
    '''
    index() generates tables for display 
        1) Retrieve: requests from frontend (index.html), data from source (parse.py), and column mapping (parse.py)
        2) Populate: cascade down the data structure to create rows and one by one and only fill in columns that are selected by the user
        3) Count: if 'Count' is requested then the values will be calculated (function.py) and merged to table
        4) Remove Duplicates: tables are optimized to not have duplicated rows
    '''

    # 1) Retrieve
    selected_cols = request.args.getlist('cols')
    data_list = get_data()
    col_map = displaying_col()

    # 2) Populate
    rows = []
    for d in data_list:
        for park in d['parks']: 
            row = {} 
            for col in selected_cols:
                if col == 'Category' or col == 'Category ID':
                    row[col] = d[col_map[col]]
                elif col == 'Park Name':
                    row[col] = park[col_map[col]]
                elif col in col_map:
                    row[col] = park.get(col_map[col], None)
            rows.append(row)
    table = pd.DataFrame(rows)
    
    # 3) Count and 4) Remove Duplicates
    headers = selected_cols.copy()
    if 'count' in headers:
        count_idx = headers.index('count')
        table, label = count_now(table, headers)
        headers[count_idx] = label
    else: 
        if selected_cols:
            table = table.drop_duplicates(subset=selected_cols)

    park_stats = table.to_dict(orient='records')
    return render_template('index.html', stats=park_stats, columns=selected_cols, headers=headers, col_map=col_map)

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
    #app.run(host="0.0.0.0", port=8000) #for running in development server
