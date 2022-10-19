import pandas as pd
import geopandas as gpd
import matplotlib
import matplotlib.pyplot as plt
import json
import jsonschema
import streamlit as st
from streamlit_folium import folium_static

# regions location
# Swiss Kantons for this example, but can be any region list (for later display as shapes on map)
shapeFilename = "SHAPEFILE_LV95_LN02/swissBOUNDARIES3D_1_3_TLM_KANTONSGEBIET.shp"

# schema filename
schemaFilename = "AvailabilityMapSchema.json"
# availability filename
availabilityFilename = "AvailabilityMapProvider3.json"

# color map for availability states
regionColormap = matplotlib.colors.ListedColormap(['#333333','#dddddd'])

st.title('Region Availability Dashboard')
st.markdown('Proof of concept to visualize regional availability information on a map.')


st.sidebar.title('Dashboard Parameters')

st.sidebar.write('Loading region data')
shape_regions = gpd.read_file(shapeFilename)

st.sidebar.write('Loading availability data')

# Load availabilities from JSON file
f1 = open(availabilityFilename)
regionAvailabilities = json.load(f1)
f1.close()

# Load JSON schema of availability data for validation
f2 = open(schemaFilename)
availabilitiesSchema = json.load(f2)
f2.close()

st.sidebar.write('Schema validation errors:', jsonschema.validate(regionAvailabilities, availabilitiesSchema))

# availability period parameters
noOfPeriods = regionAvailabilities['regionPeriods']['noOfPeriods']
startDate = regionAvailabilities['regionPeriods']['startDate']
intervalHours = regionAvailabilities['regionPeriods']['intervalHours']

st.sidebar.write('Number of periods:', noOfPeriods)
st.sidebar.write('Start date:', startDate)
st.sidebar.write('Interval duration [hours]:', intervalHours)

mapview = st.sidebar.radio('Map view', ('static', 'interactive'))
current_period = st.sidebar.slider('Availability period', 0, noOfPeriods-1, 0, 1)

regionPeriodValues = regionAvailabilities['regionPeriods']['regionPeriodValues']

r_current = []
for r in regionPeriodValues:
    r_current.append([r['region']['regionId'], r['periodValues'][current_period]])

r_current_df = pd.DataFrame(r_current, columns=['KANTONSNUM', 'Availability'])
current_regions = shape_regions.merge(r_current_df, on='KANTONSNUM')

if mapview == 'static':
    st.subheader(mapview)
    fig, ax = plt.subplots()
    ax = current_regions.plot(ax=ax, figsize=(20,20), edgecolor='white', column='Availability', cmap=regionColormap)
    ax.axis('off')
    st.pyplot(fig)
elif mapview == 'interactive':
    st.subheader(mapview)
    fm = current_regions.explore(column='Availability', cmap=regionColormap)
    folium_static(fm)
else:
    st.write('unexpected')
