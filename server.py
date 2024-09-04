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
    try:
        # 1) Retrieve
        selected_cols = request.args.getlist('cols')
        data_list = get_data()
        col_map = displaying_col()

        # 2) Populate
        rows = []
        #There is a data dictionary, containing a list of parks which uses a park dictionary
        for d in data_list:
            for park in d['parks']: 
                row = {} 
                for col in selected_cols: #For only user-selected columns
                    #These two are items in the data dictionary
                    if col in {'Category', 'Category ID'}: 
                        row[col] = d[col_map[col]]
                    
                    #'Category' and 'Park Name' are both 'name' in raw data, here it is specified that 'Park Name' is the name in the park dictionary
                    elif col == 'Park Name': 
                        row[col] = park[col_map[col]]
                    
                    #The rest all belongs in the park dictionary
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
    
    except Exception as e:
        app.logger.error(f"Error occured: {e}")
        return render_template('index.html', error="An error occured while processing request, please retry and try again.", stats=[], columns=[], headers=[], col_map={})

@app.errorhandler(500)
def internal_error(error):
    app.logger.error(f"500 error: {error}")
    return render_template('index.html', error="Internal Server Error", stats=[], columns=[], headers=[], col_map={})

if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000) # production server
    #app.run(host="0.0.0.0", port=8000) #for running in development server
