# Region Availability Interactive
Region availability interactive - visualizing forecasted availability regions on a map.

## About our «Availability Initiative»
Welcome to our «regional availability forecast» initiative!

This initiative was triggered by the European energy crisis, caused by the Ukraine war. The idea is to inform energy consumers - both individual and commercial - in a timely manner about scheduled power unavailabilities (outages). Power can be mainly electricity and natural gas. Unavailabilities are forecasted by region. A region can be a municipality, but also any specific service area as defined by the energy provider.
## About this prototype
This forecasting prototype aims to visualize availability information on a map by region. Availabilities are predicted in periods from a given start date and by region. Although the prototype was initially triggered by the energy crisis, it is implemented in a generic way where availabilities of any type can be visualized or otherwise made available by region.
* The prototype is implemented in Python (obviously)
* Visualization on maps is achieved through [geopandas](https://geopandas.org/), with regions represented by «shapes»
* For demonstration purposees, Swiss Kantons are used as regions, with region information from [view swissBOUNDARIES3D](https://www.swisstopo.admin.ch/en/geodata/landscape/boundaries3d.html) - but any region information can be used
* Interactive functionalities and cloud deployment are provided through the [Streamlit](https://streamlit.io) framework
* A (json) schema is defined for providers to report availability information in a standardized way

## Standardized data delivery

To avoid data mappings and conversions from multiple data sources, a standardized data delivery format is provided through a schema, according to [jsonschema specifications](https://json-schema.org):

- Availability provider with identifier and name
- List of regions
    - Heading information with number of availability periods, start date and availability period duration
    - Every region with its identifier and name, followed by its periods with availability values

Currently availabilities can take two values (`true` or `false` as boolean) - integers or enumerations can be implemented in case more values are required.

The actual availability information is provided in `json` format, according to the specified schema. Received availability information is checked against the schema.

## Interactive vap visualization

Try the [interactive prototype](https://janesp-region-availability-interactive-rg-avail-inter-81cxrc.streamlitapp.com)!

Regions are represented on the map as geopandas shapes. Availability is visualized on the map for one specific period as specified by an index in the availabilities values list, interactively controlled by a slider.

As mentioned, for this prototype Swiss Kantons are used a regions. However, the prototype can easily be adopted for other types of regions, such as service areas.

In a simple form, a static map with its availabilities is plotted.

In a more advanced form, the map with its availabilities is interactive and supports functionalities such as zooming and panning.

## Data generation utility

For the purpose of this prototype, a utility is provided to generate the availability information file with random values for the availability periods of the regions. The availability data file is generated in the required `json` format according to the schema.

## Prototype code

The code, schema and data files are mostly self explanatory, with comments for additional clarity.

The code is simple by purpose, but nevertheless as structured as possible for best possible flexibility. Exception handling is currently very limited.