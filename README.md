# National Park Search Engine
This project hosts a single-page web application that allows users to search, filter, and display national parks data derived from https://data.gov/

## Data Overview

## For Users
### Feature:
1. Toggle checkboxes to choose data for display from all available data, click 'Update Table' to generate table
2. Use 'Count' to retrieve counts of categories or parks based on the selected data columns
3. Search globally or by specific columns to explore the data in more detail
4. Click on header to order a column by ascending or descending order

### Examples to Try:
1. **Count parks by category:** 

Select 'Category' and 'Count' to see the number of parks in each category. Sort 'Count' in order to see that the most popular category among parks is 'Junior Ranger Program' (379) and the least is 'Team Sports' (2). 

2. **Count categories by parks:** 

Select 'Park Name' and 'Count' to see the number of categories in each park. Sort 'Count' in order to see that the park with the most different types of categories is 'Yosemite' (26) and the least is tied among multiple parks such as 'African American Civil War Memorial' (1) and 'Baltimore-Washington' (1). 

3. **Find all the Biking parks in New Mexico:**

Select 'Category', 'Park Name', and 'State', click 'Update Table', then under Biking under the 'Category' heading and NM under the 'States' heading. The result should be 3 entries (Capulin Volcano, Valles Caldera, and White Sands) filtered from 4,016 total entries. 

## For Developers:
### Code Structure:
Backend:
1. `parse.py`
2. `server.py`
3. `function.py`

Frontend:
1. `index.html`
2. `style.css`

### To set up this webpage locally:

## Acknowledgments
**Background image:** The background image used in this application is provided by Vecteezy (Vecteezy.com) under their Free License.

**DataTables:** an open-source software for creating HTML tables. More details and documentation can be found at [DataTables official website](https://datatables.net/). DataTables is licensed under the MIT License. Copyright (C) 2008-2024 by SpryMedia Ltd.

