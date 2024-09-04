# National Park Search Engine
This project hosts a single-page web application that allows users to search, filter, and display national parks data derived from https://data.gov/. The webpage is hosted on Render, accessible at https://parks-data.onrender.com and synced with this repository.

Author: **Kalea Ramsey**

For inquiries or further information, feel free to contact me:

- **Email:** [kalear01@gmail.com](mailto:kalear01@gmail.com)
- **LinkedIn:** [Visit my LinkedIn](https://www.linkedin.com/in/kramsey-rs1803)

## Data Overview
The available data from the source are listed on the left panel of the webpage and are as follows:
- **Category:** 40 categories (Arts and Culture, Astronomy ...)
- **Category ID:** 40 unique ID for each category (01D717BC-18BB-4FE4-95BA-6B13AD702038 ...)
- **Park Name:** 463 parks (Acadia, White Sands ...)
- **Park Code:** 464 park codes (not 463 due to 'Natchez Trace' having two Park Codes 'natr' and 'natt')
- **Park Designation:** 48 designations (Memorial, National Park, Wild River ...)
- **Park Full Name:** 464 parks (not 463 due to 'Natchez Trace' being shortened from two full names 'Natchez Trace National Scenic Trail' and 'Natchez Trace Parkway')
- **Park URL:** 464 urls to park website on https://www.nps.gov/
- **States:** 110 state(s), including single states (CT) and combinations (CT,GA,MA,MD,ME,NC). 

## For Users
### Feature:
1. Toggle checkboxes to choose data for display from all available data, click 'Update Table' to generate table
2. Use 'Count' to retrieve counts of categories or parks based on the selected data columns
3. Search globally or by specific columns to explore the data in more detail
4. Click on header to order a column by ascending or descending order

### Examples to Try:
1. **Count parks by category:** 

Select 'Category' and 'Count' to see the number of parks in each category. Sort 'Count' in order to see that the most popular category among parks is 'Junior Ranger Program' (379) and the least is 'Team Sports' (2). 
<img width="1350" alt="ex-1" src="https://github.com/user-attachments/assets/4c8fdc93-4564-4bb7-8b7a-fb2679892ffb">


2. **Count categories by parks:** 

Select 'Park Name' and 'Count' to see the number of categories in each park. Sort 'Count' in order to see that the park with the most different types of categories is 'Yosemite' (26) and the least is tied among multiple parks such as 'African American Civil War Memorial' (1) and 'Baltimore-Washington' (1). 

3. **Find all the Biking parks in New Mexico:**

Select 'Category', 'Park Name', and 'State', click 'Update Table', then under Biking under the 'Category' heading and NM under the 'States' heading. The result should be 3 entries (Capulin Volcano, Valles Caldera, and White Sands) filtered from 4,016 total entries. 

## For Developers:
### Code Structure:
Backend:
1. `parse.py`: pulls data from an url, contains mapping from raw data to display data which are checkboxes that can be added, removed, or renamed from the webpage. 
2. `server.py`: built with Flask to host the webpage. It receives user-selected columns from the frontend, fetches data from `parse.py` and populates the data table.
3. `function.py`: contains the `count_now` function that calculates Count of Parks and Count of Categories depending on user-selected columns

Frontend:
1. `templates/index.html`: organizes the frontend layout of title, checkboxes, and table. It retrieves a list of user-selected columns and flexibly populates the table using for loops.
2. `static/styles/style.css`: defines the color scheme and fonts of webpage elements
3. `static/js/search.js`: initalizes DataTable and search functionalities. 

### Setting Up the Webpage Locally
To run this webpage on your local machine, enter these lines in your terminal:

```bash
git clone https://github.com/aelak/parks-data.git
cd parks-data
pip3 install -r requirements.txt
python3 server.py
```
Last line will start the server and the webpage can be accessed on http://localhost:8000, please go into server.py to switch `serve(app, host="0.0.0.0", port=8000)` to `app.run(host="0.0.0.0", port=8000)` for development server. 

## Acknowledgments
**Background image:** The background image used in this application is provided by Vecteezy (Vecteezy.com) under their Free License.

### License Notice for DataTables
DataTables is licensed under the MIT License. Copyright (C) 2008-2024 by SpryMedia Ltd. For more information on the license, please see the LICENSE file in this repository.

