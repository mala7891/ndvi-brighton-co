#!/usr/bin/env python
# coding: utf-8

# # Visualizing Percent Change in NDVI Land Cover to Measure Vegetation Health in Brighton, Colorado
# 
# ## Introduction
# An unhealthy environment vulnerable to flash floods, wildfires, and droughts can worsen the impacts of climate change by reducing the landscape's ability to absorb and retain water, increasing erosion and soil degradation. This can lead to a loss of vegetation, biodiversity, and wildlife habitats, which can further degrade the ecosystem and exacerbate the impacts of climate change.
# 
# Understanding past conditions is crucial for a municipality’s informed decision-making and effective resource management, such as which practices to prioritize, and how to effectively monitor and evaluate progress towards sustainability and climate resilience goals. This knowledge can enhance our understanding of management strategies that balance conservation and resource use, while maintaining ecosystem services and resilience to environmental changes, ultimately promoting a healthier and more sustainable city.
# 
# My aim as a horticulturist working for the City of Brighton, Colorado is to enhance the historical and ecological understanding of the landscape by analyzing a curated list of environmentally sensitive areas found throughout the city. This will enable decision-makers to make informed choices about how these properties can withstand the immediate effects of climate change.
# 
# Other similarly related examples of efforts on this topic area include a paper on using NDVI for greenness exposure assessments and policy interventions in urban greening:
# https://www.sciencedirect.com/science/article/pii/S0013935122024823#cebib0010
# 
# In addition, a link is provided for NASA Scientific Visualization System’s article on NDVI anomalies revealing areas of likely drought in Colorado: 
# https://svs.gsfc.nasa.gov/2939
# 

# ## Study Area
# Brighton, Colorado is a city located in Adams County, situated approximately 20 miles northeast of downtown Denver and covers an area of approximately 21 square miles. The area has experienced a significant population boom in recent years, with a current population of around 41,000 people. This growth has been driven by a combination of factors, including its proximity to Denver, a strong local economy, and affordable housing. 
# 
# Despite the rapid urbanization and development of Brighton, the area has managed to preserve its agricultural roots. The region boasts numerous farms and ranches, which contribute to the local economy while maintaining the connection to the city's rich agricultural heritage. With a semi-arid climate characterized by hot summers and cold winters, the area has long been an ideal location for growing crops such as corn, wheat, and alfalfa.
# 
# However, the rapid growth and development of the area have put significant pressure on the local ecosystem. The natural habitats of prairie grasslands, wetlands, and riparian areas have been threatened by the expansion of urban areas and agricultural lands, leading to a decline in biodiversity and ecological health. To counteract this trend, the city has taken steps to protect these ecological features, including the establishment of conservation easements and other preservation measures.
# 
# To ensure the long-term sustainability of the region, it is important to implement sustainable land use management practices. Research into best practices for ecological, social, and economic sustainability can provide valuable insights to guide decision-making and resource management. Through the integration of sustainable practices, Brighton can continue to thrive as a vibrant community while maintaining its connection to its agricultural heritage and natural surroundings.
# 

# ## Methods
# The purpose of this project is to collect and analyze data to visualize and measure drought indicators from 1990 to present in order to promote future conservation efforts and focus time and resources to the most sensitive areas of the city.
# 
# Five areas within the city have been selected to be designated as “priority conservation areas.” A PCA will be defined as "an area desirable to maintain or enhance through protection, restoration, or sustainable stewardship", such as an area with:
# 
# * Land that provides essential ecosystem services (Erger’s Pond)
#  							
# * Critical habitat for vulnerable species (Ken Mitchell Open Space)
# 				 					
# * Protected Wildlife habitat (beavers, prairie dogs, raptors, owls, etc) (Morgan Smith Nature Area)
# 
# * Significant biodiversity, pocket prairies (Mattive Open Space)
#  					 				
# * Land with historical agriculture use (Wagner-Mayhew)
#  						
# 
# By analyzing the data, any significant changes in vegetation land cover, such as deforestation, agricultural conversion, or changes in plant species can be identified. These changes can then be compared against historical data, identifying the important biotic and abiotic structures within each PCA's boundaries, such as rivers, streams, and wetlands. These structures play a critical role in the ecosystem and can provide insight into potential threats to the area.

# In[1]:


pip install imageio


# In[2]:


# Import required libraries and modules
from glob import glob
from matplotlib.patches import Polygon
from shapely.geometry import Polygon as ShapelyPolygon
from time import time
import os
import earthpy as et
import geopandas as gpd
import imageio.v2 as imageio
import matplotlib.pyplot as plt
import numpy as np
import pathlib
import pandas as pd
import rioxarray as rxr
import xarray as xr
import seaborn as sns

# Set the default theme for Seaborn
sns.set_theme() #"dark"

# Set the working directory and output directory
os.chdir(os.path.join(et.io.HOME, 'earth-analytics', 'landsat-brighton'))
output_dir = os.path.join(et.io.HOME, 'earth-analytics', 'landsat-brighton', 'results')

# List of shapefiles for different study areas
shapefile = [
    "Brighton_Boundary.shp",
    "Ergers_Pond.shp",
    "Ken_Mitchell_Open_Space.shp",
    "Mattive_Open_Space.shp",
    "Morgan_Smith_Nature_Area.shp",
    "Wagner_Mayhew_Property.shp"
]

# Initialize dictionaries to store data
shapefile_completion_time = {}
shapefile_change_pct = {}
shapefile_graphs = {}

# Function to plot polygon outlines
def plot_outline(geometry, ax):
    if isinstance(geometry, ShapelyPolygon):
        ax.add_patch(Polygon(list(geometry.exterior.coords), facecolor="none", edgecolor="black", linewidth=1))
    elif geometry.geom_type == "MultiPolygon":
        for polygon in geometry.geoms:
            plot_outline(polygon, ax)

# Iterate over each shapefile
for shapefile_name in shapefile:
    landsat_ds_red = []
    landsat_ds_nir = []

    # Extract property name and output directory from shapefile name
    shapefile_noext = shapefile_name.split('.')[0]
    property_name = shapefile_noext.replace('_', ' ')
    property_output_dir = f"{output_dir}/{shapefile_noext.lower()}"
    
    # Create the output directory if it doesn't exist
    os.makedirs(property_output_dir, exist_ok=True)
    
    # Record the start time for processing
    tic = time()
    
    # Read the GeoDataFrame from the shapefile
    current_bounds_gdf = gpd.read_file(shapefile_name)
    
    # Iterate over sorted Landsat data files using glob
    for file_name in sorted(glob("*_L2SP_*_*_*_02_T1_SR_B*.TIF")):
        try:
            product = int(file_name[3])
        except:
            continue

        try: 
            band = int(file_name[-5])
        except:
            continue
        
        # Determine band and product for Landsat data
        if product < 8: 
            if band == 3:
                band_name = "red"
            elif band == 4:
                band_name = "nir"
            else:
                os.remove(file_name)
                continue
        else:
            if band == 4:
                band_name = "red"
            elif band == 5:
                band_name = "nir"
            else:
                os.remove(file_name)
                continue
        
        try:
            date = pd.to_datetime(file_name[17:25])
        except:
            continue
        
        # Read and preprocess the raster data using rioxarray
        ds = rxr.open_rasterio(file_name, masked=True).squeeze()
        if ds.isnull().sum() / ds.count() < 0.1:
            continue
        ds = ds.assign_coords(date=date)
        ds = ds.expand_dims("date")
        current_bounds_crs = current_bounds_gdf.to_crs(ds.rio.crs)
        ds = ds.rio.clip_box(*current_bounds_crs.total_bounds)
        
        # Separate data by red and near-infrared bands
        if band_name == "red":
            landsat_ds_red.append(ds)
        if band_name == "nir":
            landsat_ds_nir.append(ds)
    
    # Concatenate the Landsat data by bands
    red_landsat_ds = xr.concat(landsat_ds_red, dim=("date")).sortby("date")
    nir_landsat_ds = xr.concat(landsat_ds_nir, dim=("date")).sortby("date")

    # Calculate NDVI for each image
    ndvi = (nir_landsat_ds - red_landsat_ds) / (nir_landsat_ds + red_landsat_ds)

    # Define class bins for categorizing NDVI values
    class_bins = [-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1]

    # Calculate mean NDVI for each decade
    ndvi_decade = ndvi.resample(date="10AS").mean("date")
    ndvi_decade = ndvi_decade.assign_coords(date=ndvi_decade.date.dt.year)
    ndvi_decade_class = xr.apply_ufunc(np.digitize, ndvi_decade, class_bins)
    
    # Create a dataframe for storing NDVI values
    ndvi_decade_dataframe = ndvi_decade.to_dataframe(name="NDVI").reset_index().pivot(columns="date", values="NDVI", index=["x","y"])
    
    # Create and plot KDE for NDVI values
    ndvi_decade_dataframe.plot(kind="kde", colormap="copper_r", title=f"Frequency of NDVI Values for {property_name} Study Area")

    # Designate 4 distinct time periods for NDVI (Normalized Difference Vegetation Index) calculation
    ndvi_1 = ndvi_decade_class.sel(date=1990).mean()
    ndvi_2 = ndvi_decade_class.sel(date=2000).mean()
    ndvi_3 = ndvi_decade_class.sel(date=2010).mean()
    ndvi_4 = ndvi_decade_class.sel(date=2020).mean()

    # Calculate the percent change in NDVI for each time period and store in the shapefile_change_pct dictionary
    shapefile_change_pct[property_name] = {
        "2000's-1990's": ((ndvi_2 - ndvi_1) / ndvi_1) * 100,
        "2010's-2000's": ((ndvi_3 - ndvi_2) / ndvi_2) * 100,
        "2020's-2010's": ((ndvi_4 - ndvi_3) / ndvi_3) * 100,
    }

    # Save each decadal average figure of NDVI as a tif image to the specified directory
    for decade, NDVI_1_decade in ndvi_decade.groupby("date"):
        NDVI_1_decade.rio.to_raster(f"{property_output_dir}/{shapefile_noext}_ndvi_{decade}.tif")

    # Load the NDVI rasters for each time period
    ndvi_1990 = rxr.open_rasterio(f"{property_output_dir}/{shapefile_noext}_ndvi_1990.tif")
    ndvi_2000 = rxr.open_rasterio(f"{property_output_dir}/{shapefile_noext}_ndvi_2000.tif")
    ndvi_2010 = rxr.open_rasterio(f"{property_output_dir}/{shapefile_noext}_ndvi_2010.tif")
    ndvi_2020 = rxr.open_rasterio(f"{property_output_dir}/{shapefile_noext}_ndvi_2020.tif")

    # Create a 2x2 subplot figure for displaying NDVI maps for each time period
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(8, 8))
    fig.subplots_adjust(hspace=0.5, wspace=0.5)
    fig.suptitle(f"{property_name} Change in NDVI by Decade")

   # Prepare the axes for plotting
    axes_decades = [ax1, ax2]
    axes_yearly = [ax3, ax4]

    # Set aspect ratio for all axes
    for ax in axes_decades + axes_yearly:
        ax.set_aspect("equal")

    # Plot the NDVI maps for each time period using the specified colormap and limits
    cmap = "RdYlGn"
    ndvi_1990.plot(ax=ax1, cmap=cmap, vmin=-1, vmax=1,)
    ndvi_2000.plot(ax=ax2, cmap=cmap, vmin=-1, vmax=1,)
    ndvi_2010.plot(ax=ax3, cmap=cmap, vmin=-1, vmax=1,)
    ndvi_2020.plot(ax=ax4, cmap=cmap, vmin=-1, vmax=1,)

    # Convert the longitude and latitude values from meters to degrees for labeling
    shapefile_centroid = current_bounds_gdf.geometry.centroid.iloc[0]
    lon_degrees = 1 / (111320 * np.cos(shapefile_centroid.y * np.pi / 180))
    lat_degrees = 1 / 111320

    # Add titles, labels, and boundaries to the subplots
    ax1.set_title("1990 - 2000")
    ax2.set_title("2000 - 2010")
    ax3.set_title("2010 - 2020")
    ax4.set_title("2020 - 2023")
    for ax in [ax1, ax2, ax3, ax4]:
        ax.set_xlabel("Longitude")
        ax.set_ylabel("Latitude")
        ax.set_xticklabels((ax.get_xticks() * lon_degrees).round(3))
        ax.set_yticklabels((ax.get_yticks() * lat_degrees).round(3))
        for geometry in current_bounds_crs["geometry"]:
            plot_outline(geometry, ax)

    # Save the figure as a tif image
    plt.savefig(f"{property_output_dir}/{shapefile_noext}_ndvi_decades.tif")
    plt.close(fig)

    # Store the generated graphs for later use in the shapefile_graphs dictionary
    shapefile_graphs[property_name] = {
        "DecadeHistogram": ndvi_decade_dataframe,
    }

    # Create a GIF animation using the NDVI variable with one image for each year in the dataset
    with imageio.get_writer(f"{property_output_dir}/{shapefile_noext}_ndvi_yearly.gif", mode="I") as writer:
        for year, NDVI_1_year in ndvi.groupby("date"):
            yyyymmdd = str(year).split('T')[0]
            temp_image_path = f"{shapefile_noext}_ndvi_yearly_{yyyymmdd}.png"
            year_fig, year_ax = plt.subplots()
            year_ax.set_aspect("equal")
            # Design the plot features for the yearly NDVI maps
            NDVI_1_year.plot(cmap=cmap, vmin=-1, vmax=1, ax=year_ax)
            for geometry in current_bounds_crs["geometry"]:
                plot_outline(geometry, year_ax)
            plt.suptitle(f"{property_name} Annual Change in NDVI")
            plt.title(f"{yyyymmdd}")
            plt.axis("off")
            plt.savefig(temp_image_path, dpi=300)
            plt.close(year_fig)
            # Append the generated images to the GIF animation
            writer.append_data(imageio.imread(temp_image_path))
            os.remove(temp_image_path)

    # Calculate the time taken for the processing and store it in the shapefile_completion_time dictionary
    shapefile_completion_time[property_name] = time() - tic

    # Export a table displaying percent change data for each study area
    percent_change_dfs = []
    for prop_name, time_periods in shapefile_change_pct.items():
        percent_change_df = pd.DataFrame(data=time_periods, index=[prop_name])
        percent_change_dfs.append(percent_change_df)
    percent_change_concat = pd.concat(percent_change_dfs, axis=0)  # Use axis=0 to concatenate along rows

# Print the resulting DataFrame
print(percent_change_concat)
    
# Display the plots
plt.show()

# Print completion message for each study area and its corresponding processing time
for prop_name, time_taken in shapefile_completion_time.items():
    print(f"Completed {prop_name} in {time_taken:.2f}")


# ## Outputs
# 
# ### Values:
# 1. Decadal Average Percent of Change in NDVI: 6 study areas (5 PCA's + Brighton) and across 3 decades for a total of 24 percentage values, printed as in-line table.
# 
# ### Figures:
# 2. KDE Frequency of NDVI Values by Decade: 5 kinetic depth effect (KDE) figures for each study area across 4 decades + and 1 for all decades, for a total of 6 in-line figures, downloadable as .png images (if desired).
# 
# 3. Annual Change in NDVI GIFs: A .gif is generated for each study area (6) cycling through 34 images (at most) for a total of 6 .gif files.
# 
# 4. Decadal Average NDVI Subplots: Average NDVI for 4 decades displayed as four-figure subplots clipped to each clipped to 5 study areas + Brighton for a total of 6 .tif subplot figures.
# 
# ### Raster Images:
# 5. Decadal Average NDVI Composites:  A mean composited NDVI image using the supplied RED and NIR bands calculated for each decade (4) for 6 study areas for a total of 24 .tif images.

# In[ ]:




