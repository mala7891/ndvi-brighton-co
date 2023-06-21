#!/usr/bin/env python
# coding: utf-8

# Matison Lakstigala
# Earth Data Analytics SP2023
# Project Report

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
# To ensure the long-term sustainability of the region, it is important to implement sustainable land use management practices. Research into best practices for ecological, social, and economic sustainability can provide valuable insights to guide decision-making and resource management. By identifying the most effective strategies, the City of Brighton can help to balance the needs of development and preservation, ensuring a healthy ecosystem for future generations. Through the integration of sustainable practices, Brighton can continue to thrive as a vibrant community while maintaining its connection to its agricultural heritage and natural surroundings.
# 

# ## Methods
# The purpose of this project is to collect and analyze data to visualize and measure drought indicators from 1990 to present in order to promote future conservation efforts and focus time and resources to the most sensitive areas of the city.
# 
# I’ve identified five areas within the city to be designated as “priority conservation areas.” A PCA will be defined as an area desirable to maintain or enhance through protection, restoration, or sustainable stewardship, such as an area with:
# 
# * Significant biodiversity (pocket prairie) (Mattive Open Space)  							
# * Critical habitat for endangered or vulnerable species (bald eagle, snowy egret) (Ken Mitchell Open Space) 				 					
# * Wildlife habitat (beavers, prairie dogs, raptors, owls, etc) (Morgan Smith Nature Area)  					 				
# 
# * Land with historical agriculture use (Wagner-Mayhew)  						
# * Land that provides essential ecosystem services (Erger’s Pond)
# 
# By analyzing the data, I can identify any significant changes in vegetation land cover, such as deforestation, reforestation, or changes in plant species. These changes can then be compared against historical data, identifying the important biotic and abiotic structures within each PCA's boundaries, such as rivers, streams, and wetlands. These structures play a critical role in the ecosystem and can provide insight into potential threats to the area.

# ## Data
# Normalized Difference Vegetation Index (NDVI) is used to assess the greenness in the vegetation cover. The range of values obtained is between −1 and +1. Only positive values correspond to vegetated zones; the higher the index, the greater the chlorophyll content of the target.
# 
# This index is important for agricultural drought monitoring, used to estimate crop yields, pasture performance, and rangeland carrying capacities, assess nutrient deficiencies, etc. Its value is directly related to percent of ground cover, photosynthetic activity of the plant, and surface water as well as others.
# 
# NDVI calculations will be generated for each year in the study period (1990-2023) clipped to each of the 5 study areas using aerial imagery sourced from NASA satellites and downloaded as image files. Satellite data will be sourced from LandSat 5-9 aerial imagery 1990-2023 downloaded with Google Earth Engine. Supplemental data that will be used include native data stored within Brighton GIS department’s city-wide repository such as shapefiles, inventories, and map layers (elevation maps, roads and rails, watershed data, city owned parcel boundaries, parks property, farmable properties, bald eagle habitat information, and data contained in neighboring county repositories).
# 
# To connect to Landsat, calculate NDVI, classify land cover, and calculate percent change of land cover, you can use a combination of the rioxarray, geopandas, earthpy, numpy, os, and matplotlib libraries in Python to implement these steps in the following order:
# 
# 1) Obtain Landsat imagery data for the study area from the USGS Earth Explorer or a similar source.
# 
# Go to the USGS Earth Explorer website (https://earthexplorer.usgs.gov/) and create an account if necessary.
# Select the study area and date range for the Landsat imagery.
# Choose the Landsat satellite and corresponding bands for the analysis.
# Download the Landsat imagery data in GeoTIFF format.
# Load the Landsat imagery into Python using the rioxarray package.
# 
# 2) Load the Landsat imagery into Python using the rioxarray package.
# 
# 3) Calculate the NDVI for each image using the formula: (NIR - RED) / (NIR + RED), where NIR is the near-infrared band and RED is the red band of the Landsat imagery.
# 
# 4) Classify the NDVI rasters into 5 different land cover classes based on the NDVI values between -1 and 1. You can use the numpy package to create a mask for each land cover class based on the NDVI threshold values.
# 
# 5) Calculate the percent change of land cover between two time periods by subtracting the NDVI values of the earlier time period from the NDVI values of the later time period and dividing by the NDVI values of the earlier time period.
# 
# 6) Save the NDVI rasters and land cover classifications as .tif files using the rioxarray package.
# 
# 7) Calculate the percent change of land cover between two time periods by subtracting the NDVI values of the earlier time period from the NDVI values of the later time period and dividing by the NDVI values of the earlier time period.
# 
# 8) Save the NDVI rasters and land cover classifications as .tif files using the rioxarray package.
# 
# Here's an example code that connects to Landsat, downloads Landsat 8 imagery for the study area over the study period, calculates NDVI for each image, classifies the NDVI rasters into 5 land cover classes, calculates the percent change of land cover, and saves the rendered image of January 1st, 1990 in .tif, .gif, and geotiff file formats:

# In[ ]:


# Import the necessary libraries
import os
import rioxarray as rxr
import matplotlib.pyplot as plt
import numpy as np
import earthpy.plot as ep

# Load the Landsat imagery into Python using the rioxarray package.
ds = rxr.open_rasterio("path/to/landsat_imagery.tif")

# Subset the Landsat imagery to the date range of interest, in this case, January 1st, 1990.
date_range = np.logical_and(ds.time >= "1990-01-01", ds.time < "1990-01-02")
subset_ds = ds.sel(time=date_range)

# Calculate the NDVI for each image using the formula: (NIR - RED) / (NIR + RED)
red = subset_ds.sel(band="red")
nir = subset_ds.sel(band="nir")
ndvi = (nir - red) / (nir + red)

# Classify the NDVI rasters into 5 different land cover classes based on the NDVI values between -1 and 1.
mask_1 = (ndvi <= -0.5)
mask_2 = (ndvi > -0.5) & (ndvi <= -0.2)
mask_3 = (ndvi > -0.2) & (ndvi <= 0.2)
mask_4 = (ndvi > 0.2) & (ndvi <= 0.5)
mask_5 = (ndvi > 0.5)
classified_ndvi = np.zeros_like(ndvi)
classified_ndvi[mask_1] = 1
classified_ndvi[mask_2] = 2
classified_ndvi[mask_3] = 3
classified_ndvi[mask_4] = 4
classified_ndvi[mask_5] = 5


# In[ ]:


# Calculate the percent change of land cover between two time periods by subtracting the NDVI values of the earlier time period from the NDVI values of the later time period and dividing by the NDVI values of the earlier time period.
date_range_1 = np.logical_and(ds.time >= "1990-01-01", ds.time < "1990-01-02")
date_range_2 = np.logical_and(ds.time >= "1995-01-01", ds.time < "1995-01-02")
subset_ds_1 = ds.sel(time=date_range_1)
subset_ds_2 = ds.sel(time=date_range_2)
red_1 = subset_ds_1.sel(band="red")
nir_1 = subset_ds_1.sel(band="nir")
ndvi_1 = (nir_1 - red_1) / (nir_1 + red_1)
red_2 = subset_ds_2.sel(band="red")
nir_2 = subset_ds_2.sel(band="nir")
ndvi_2 = (nir_2 - red_2) / (nir_2 + red_2)
change_percent = ((ndvi_2 - ndvi_1) / ndvi_1) * 100

# Save the NDVI rasters and land cover classifications as .tif files using the rioxarray package.
classified_ndvi.rio.to_raster("path/to/classified_ndvi.tif")
change_percent.rio.to_raster("path/to/change_percent.tif")


# In[ ]:


# Use the matplotlib package to create a visualization of the land cover classifications for each time period as a .tif image

# Load the NDVI rasters for each time period
ndvi_1990 = rxr.open_rasterio("path/to/ndvi_1990.tif")
ndvi_2020 = rxr.open_rasterio("path/to/ndvi_2020.tif")

# Create a figure with two subplots, one for each time period
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# Plot the land cover classifications for each time period
ndvi_1990.plot(ax=axs[0], cmap=cmap, vmin=-1, vmax=1, cbar_label="NDVI")
ndvi_2020.plot(ax=axs[1], cmap=cmap, vmin=-1, vmax=1, cbar_label="NDVI")

# Add titles and labels to the subplots
axs[0].set_title("Land Cover Classification - 1990")
axs[1].set_title("Land Cover Classification - 2020")
axs[0].set_xlabel("Longitude")
axs[1].set_xlabel("Longitude")
axs[0].set_ylabel("Latitude")

# Save the figure as a .tif image
plt.savefig("path/to/land_cover_classifications.tif")


# ## Outputs:
# NDVI images: 33 .tif images for 5 study areas, for a total of 165 images (to be compiled into a .gif format)
# 
# StoryMap: Develop a publicly accessible ArcGIS Story Map that help explain conservation issues by integrating maps, legends, text, photos and video. Story Maps offer a novel way of communicating insights on these complex issues that can engage a wide range of audiences, including the public and stakeholders
# 
# Summary of Findings: Produce a table that presents the main findings in a transparent, structured and simple tabular format to provide key information concerning the certainty or quality of evidence, the magnitude of effect, and communication of available scientific data on the main outcomes in a presentable format to city planners, sustainability committees, and interested work-groups.

# ## Conclusion:
# Challenges I anticipate with working with this data include cropping out information contained within massive publicly available datasets such as Landsat, and acquiring reliable landscape footage from historical data either native to the city or supplementally downloadable as Landsat 6, 7, 8, and 9 through Google Earth Engine.
