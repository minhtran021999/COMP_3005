
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import geopandas as gpd
import matplotlib.pyplot as plt
import requests

base_url = " https://data.colorado.gov/resource/3qth-7k3v.json"  # data source

fields = "Date_Recor, the_geom, Subdivisio, SITUS_AD_1, SITUS_ZIP, Abbrev_Rac"  # column headers

url = f"{base_url}?$select={fields}"  # from the api documentation


# PROMPT 1. create a function with a get request to url and return the response as a JSON object.

def fetch_data(url):
    response = requests.get(url)
    data = response.json()
    return data

# PROMPT 2: identify the unique keys in data

data = fetch_data(url)
unique_keys = set()
for record in data:
    unique_keys.update(record.keys())
print("Unique keys in the data:", unique_keys)

# PROMPT 3. Rename the keys in the raw data to the following:
#  'Date_Recor' -> 'Year', 
# 'SITUS_AD_1' -> 'Address', 
# 'SITUS_ZIP' -> 'Zip Code', 
# 'Subdivisio' -> 'Subdivision', 
# 'Abbrev_Rac' -> 'Racial_Statement'

def rename_keys(data):
    renamed_data = []
    for record in data:
        renamed_record = {
            'Year': record.get('Date_Recor', '').strip(),
            'Address': record.get('SITUS_AD_1', '').strip(),
            'Zip Code': record.get('SITUS_ZIP', '').strip(),
            'Subdivision': record.get('Subdivisio', '').strip(),
            'Racial_Statement': record.get('Abbrev_Rac', '').strip(),
            'the_geom': record.get('the_geom', {})
        }
        renamed_data.append(renamed_record)
    return renamed_data

# PROMPT.4 Write a function to extract the 'latitude' and 'longitude' from the 'the_geom' key and add them as separate keys 
# in the dictionary. Remove the original 'the_geom' key.

def extract_lat_long(renamed_data):
    for record in renamed_data:
        geom = record.pop('the_geom', {})
        coordinates = geom.get('coordinates', [None, None])
        record['Longitude'] = coordinates[0]
        record['Latitude'] = coordinates[1]
    return renamed_data

# PROMPT 5. Create a data cleaning function to clean the remaining data to remove extra spaces and characters. 
# Then create and populate a 'Year' column, create and populate a 'Zip Code' column, and clean the 'Subdivision' column to 
# replace "AND A" with "".

def clean_data(renamed_data):
    for record in renamed_data:
        # Clean 'Year' column
        record['Year'] = record['Year'].split('-')[0].strip() if record['Year'] else ''
        
        # Clean 'Zip Code' column
        record['Zip Code'] = record['Zip Code'].strip() if record['Zip Code'] else ''
        
        # Clean 'Subdivision' column
        if record['Subdivision']:
            record['Subdivision'] = record['Subdivision'].replace("AND A", "").strip()
        else:
            record['Subdivision'] = ''
    return renamed_data

# PROMPT 6. Create a function that returns the percentage of records missing from each of the fields:
#  'Year', 'Address', 'Zip Code', 'Subdivision', 'Racial_Statement', 'Latitude', 'Longitude'. 
# Report percentages in whole numbers followed by percent sign.

def calculate_missing_percentages(renamed_data):
    total_records = len(renamed_data)
    missing_counts = {
        'Year': 0,
        'Address': 0,
        'Zip Code': 0,
        'Subdivision': 0,
        'Racial_Statement': 0,
        'Latitude': 0,
        'Longitude': 0
    }
    
    for record in renamed_data:
        for key in missing_counts.keys():
            if not record.get(key):
                missing_counts[key] += 1
                
    missing_percentages = {key: f"{(count / total_records) * 100:.0f}%" for key, count in missing_counts.items()}
    return missing_percentages

# PROMPT 7. Create a function to extract and print the 'number of unique entries' from the 'Racial_Statement' field.

def unique_racial_statements(renamed_data):
    unique_statements = set()
    for record in renamed_data:
        statement = record.get('Racial_Statement', '')
        # print(statement)
        if statement:
            unique_statements.add(statement)
    print("Number of unique Racial Statements:", len(unique_statements))
    return unique_statements

# PROMPT 8. Create a function to individually extract longitude and latitude values from renamed_data and store each in separate lists.

def extract_coordinates(renamed_data):
    longitudes = []
    latitudes = []
    for record in renamed_data:
        # Check if the values are not None and attempt to convert them to float
        try:
            if record.get('Longitude') is not None:
                longitudes.append(float(record['Longitude']))
            if record.get('Latitude') is not None:
                latitudes.append(float(record['Latitude']))
        except ValueError:
            # Handle cases where the coordinate is not a valid number (e.g., an empty string)
            pass 
    return longitudes, latitudes
# PROMPT 9. load the denver geojson neighborhood data from the project workspace and save in a neighborhoods variable.

neighborhoods = gpd.read_file("denver_neighborhoods.geojson")

# PROMPT 10. Filter NBHD_NAME in neighborhoods to exclude: "DIA","Central Park","Montbello","Gateway - Green Valley Ranch"

excluded_neighborhoods = ["DIA", "Central Park", "Montbello", "Gateway - Green Valley Ranch"]
filtered_neighborhoods = neighborhoods[~neighborhoods['NBHD_NAME'].isin(excluded_neighborhoods)]

"""
PROMPT 11.
Create a function to plot the filtered neightorhoods and overlay the longitude and latitude points from renamed_data on top of the neighborhood map.
Use Cartopy for the mapping.
Use the following specifications:
The plot size should be 15 x!5
The projection should be ccrs.PlateCarree()
The extent should be [-105.15, -104.83, 39.6, 39.8]
Add borders to the map in black, use linestyle = ":"
Add neighborhood bordors in black with a linewidth of 1
Add neighborhood names as labels on the map in the center of each neighborhood polygon.
Add points for the longitude and latitude values in blue with a marker size of 5.
Add a title to the map, "Racialized Deed Restrictions in Denver in 1931")
Plot the map
"""

def plot_map(neighborhoods, longitudes, latitudes):
    fig, ax = plt.subplots(figsize=(15, 15), subplot_kw={'projection': ccrs.PlateCarree()})
    ax.set_extent([-105.15, -104.83, 39.6, 39.8], crs=ccrs.PlateCarree())
    
    # Add borders
    ax.add_feature(cfeature.BORDERS, edgecolor='black', linestyle=':')
    
    # Plot neighborhood borders
    neighborhoods.boundary.plot(ax=ax, edgecolor='black', linewidth=1)
    
    # Add neighborhood names
    for idx, row in neighborhoods.iterrows():
        plt.text(row['geometry'].centroid.x, row['geometry'].centroid.y, row['NBHD_NAME'],
                 horizontalalignment='center', fontsize=8, transform=ccrs.PlateCarree())
    
    # Plot points
    ax.scatter(longitudes, latitudes, color='blue', s=5, transform=ccrs.PlateCarree())
    
    # Add title
    plt.title("Racialized Deed Restrictions in Denver in 1931")
    
    plt.show()


# Execution
data = fetch_data(url)
renamed_data = rename_keys(data)
renamed_data = extract_lat_long(renamed_data)
cleaned_data = clean_data(renamed_data)
missing_percentages = calculate_missing_percentages(cleaned_data)
print("Missing Data Percentages:", missing_percentages)
unique_statements = unique_racial_statements(cleaned_data)
longitudes, latitudes = extract_coordinates(cleaned_data)

plot_map(filtered_neighborhoods, longitudes, latitudes)


# At the bottom of your .py script, please include and answer the following questions:
'''
1. What percentage of Colorado’s black population lived in Denver during this period
the data was collected? (hint: refer to the1929 Negro Report)

- Approximately 2.4% of the total population in Denver

2. In what neighborhoods were they most concentrated?

- Five Points, Whittier

3. How many unique racialized comments did you print out? Describe in a few
sentences the focus & variation of the comments that are included on these deeds.

- 98 unique racialized comments. Below are a few descriptions:
    + "The residence erected thereon shall be a single detached dwelling house, which shall be occupied by white householders only."
    + "It is understood and agreed that, as a part of the consideration, these premises shall never be occupied by, sold, leased or rented to a negro."
    + "No intoxicating liquors of any kind shall be kept for sale or sold thereon; nor shall said premises be occupied by sold, leased, or rented a negro."
    + "In order to establish a high grade residence (354) no garage or outbuilding on any plot shall be used as a residence or living quarters except by servants engaged on the premises (357)  11. Ownership or Occupancy by Anyone Other Than the White Race: None"
    + "The said premises shall not be occupied, sold, lease or rented to a negro."

4. In what neighborhood(s) do you see the greatest number of discriminatory deed
restrictions?

- Banum West, Banum, Cherry Creek, Villa Park, Belcaro, Country Club, Washington Park, East Colfax, Chaffe Park, Globeville,
  South Park Hill, Monclair, Cory-Merrill

5. What other data could you collect to further understand the spatial patterns that
you see in your map? For example, what data might you collect that would enable
you to predict what neighborhoods are likely to manifest discriminatory housing
practices during this period?

- Data on new housing being built -> most likely to have more racial restrictions for newly built units
- Data on property values -> white-occupied neighborhoods likely to have higher prices
- Data on lending & mortgage -> non-white neighborhoods would highly likely be labeled as "high risk"
- Data on property owners associations -> these are the most enthusiastic legal enforcers of the leases,
  plotting their presence would point out where discrimatory restrictions were strongest
  
'''
