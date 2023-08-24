# ndvi-brighton-co

## CU Boulder Earth Data Analytics Professional Graduate Certificate
### Summer 2023 Capstone Project:

# NDVI Analysis as a Tool for Evaluating Vegetation Health and Land Management in Brighton, CO
[![DOI](https://zenodo.org/badge/637627095.svg)](https://zenodo.org/badge/latestdoi/637627095)

Details of these findings are documented in an ArcGIS StoryMap available here: https://storymaps.arcgis.com/stories/9410607d90ff40b782a55d9f2a0f7a0c

Author: Matison Lakstigala

# Introduction
This README file provides an overview of a capstone project focused on enhancing the historical and ecological understanding of environmentally sensitive areas within the City of Brighton, Colorado. The project aims to analyze satellite data and create custom NDVI (Normalized Difference Vegetation Index) maps for five specific areas in Brighton. These maps will assist decision-makers in making informed choices about managing and preserving these properties to withstand the immediate effects of climate change.

# In This Repository:
* README.md
* LICENSE.txt
* .gitignore file
* environment.yml
* oryx-build-commands.txt
* "notebooks" folder containing:
  - ndvi_brighton_co.html
  - ndvi_brighton_co.ipynb
  - ndvi_brighton_co.py
* "shapefiles" folder containing:
  - Brighton_Boundary_Current Shapefile
  - Ken_Mitchell_Open_Space Shapefile
  - Mattive_Open_Space Shapefile
  - Ergers_Pond Shapefile
  - Morgan_Smith Shapefile
  - Wagner_Mayhew_Property Shapefile
* "inputs" folder
  - an .html to link you to a Google Drive folder containing raw Landsat data downloaded from USGS EarthExplorer
* "outputs" folder
  - brighton_boundary
  - ergers_pond
  - ken_mitchell_open_space
  - mattive_open_space
  - morgan_smith_nature_area
  - wagner_mayhew_property
    * inside each folder:
    - "AREA_NAME"_ndvi_1990.tif
    - "AREA_NAME"_ndvi_2000.tif
    - "AREA_NAME"_ndvi_2010.tif
    - "AREA_NAME"_ndvi_2020.tif
    - "AREA_NAME"_ndvi_decades.tif
    - "AREA_NAME"_ndvi_yearly.gif
    - "AREA_NAME" KDE.png"

# Project Objectives
The primary objectives of this project are as follows:

* Analyze satellite data: Collect and process satellite imagery to obtain relevant data for the selected areas in Brighton, Colorado.
* Generate custom NDVI maps: Utilize the Normalized Difference Vegetation Index (NDVI) to produce maps that depict vegetation density and health.
* Enhance historical and ecological understanding: Provide decision-makers with valuable insights into the historical and ecological conditions of the selected areas, aiding in informed decision-making and resource management.
* Support sustainable landscape management: Enable the prioritization of conservation practices, effective monitoring, and evaluation of progress towards sustainability and climate resilience goals within the city.

# Purpose
The purpose of this repository is to provide a workflow for custom NDVI mapping using Landsat imagery data. It includes code and instructions on how to process satellite data, calculate NDVI, classify land cover, and calculate the percent change of land cover between two time periods.

The goals and motivations for the project are to enhance the historical and ecological understanding of the landscape in the City of Brighton, Colorado. The project aims to enable decision-makers to make informed choices about how environmentally sensitive areas can withstand the immediate effects of climate change and promote sustainable landscape management.

One unique contribution of this project repository to data science and earth/environmental science is the integration of various free and open source Python packages to perform the entire workflow from loading publicly available datasets such as Landsat imagery to generating custom NDVI maps and land cover classifications.

Someone would want to use the code/workflow presented in this repository for several reasons:

* It provides a standardized and replicable approach for processing Landsat imagery and calculating NDVI, making it easier for city decision-makers to analyze vegetation dynamics.
* The workflow enables the classification of land cover based on NDVI values, allowing users to identify different vegetation types or land cover classes within the study area.
* The calculation of percent change of land cover for each decade provides insights into vegetation changes over time, aiding in monitoring and assessing the effects of environmental changes and climate resilience.
* The workflow includes visualization capabilities, allowing users to generate maps, charts, and calculations of NDVI land cover classifications, and percent change of land cover, facilitating data interpretation and communication of findings.
* Overall, this code/workflow is valuable for professionals working in the field of environmental science, horticulture, land management, or anyone interested in analyzing and monitoring vegetation dynamics using Landsat imagery.

# Project Steps
To achieve the project objectives, the following steps will be undertaken:

# Data Collection: 
Gather satellite imagery data for the selected areas in Brighton, Colorado. This data should cover a sufficient historical time frame to observe changes in vegetation patterns.
# Preprocessing and Analysis: 
Process the collected satellite data to remove any noise or artifacts and calculate the NDVI values for each pixel within the imagery.
# NDVI Map Generation: 
Utilize ArcGIS Pro to generate custom NDVI maps based on the processed satellite data. These maps will visually represent the vegetation density and health across the selected areas.
# Interpretation and Analysis:
Interpret the NDVI maps and analyze the vegetation patterns, identifying areas with higher or lower vegetation density or potential ecological significance.
# Documentation and Reporting: 
Summarize the findings, interpretations, and recommendations based on the NDVI analysis. Include relevant historical and ecological context to enhance decision-makers' understanding of the landscape conditions.
# Presentation and Discussion: 
Present the findings to the appropriate stakeholders, including municipality officials, urban planners, and environmental experts. Facilitate a discussion on the management strategies and practices that balance conservation and resource use while maintaining ecosystem services and resilience to environmental changes.
# Integration and Decision-making: 
Collaborate with decision-makers to integrate the acquired knowledge into municipal decision-making processes. Use the information gained to guide sustainable landscape management practices and prioritize initiatives that promote a healthier and more resilient city.

# Project Deliverables
The final deliverables for this project will include:

* Custom NDVI/maps: Maps depicting each study area and its features, and mapping positive or negative changes in vegetation density and health (Normalized Difference Vegetation Index) for the selected areas in Brighton, Colorado.
* Summary Table: In a tabular format, presenting the findings, interpretations, and recommendations based on the NDVI analysis. 
* Presentation materials: ArcGIS StoryMap will include historical and ecological context for the each of the selected areas to communicate the project's key findings and recommendations to a general audience.

# Tools/Packages Required
To run the workflow, you will need the following tools/packages:
* Python (version 3.0 or higher)
* os
* earthpy
* glob
* geopandas
* imageio
* matplotlib
* numpy
* pandas
* pathlib
* rioxarray
* seaborn
* shapely
* time
* xarray


# Install the Earth Analytics Python Conda Environment
To install the earth-analytics-python environment, you will need to follow these steps:

Fork and clone a GitHub repository from https://github.com/earthlab/earth-analytics-python-env to your own directory (such as "earth-analytics-python-env").
This repository also contains instructions to install the environment, as well as on the Earth Data Science textbook website: https://www.earthdatascience.org/workshops/setup-earth-analytics-python/

1. In the Terminal, set your directory to the cloned earth-analytics-python-env dir using "cd" to change directories (e.g. "cd earth-analytics-python-env)".

2. Once you are in the earth-analytics-python-env directory, you can create your environment. 
To do this run: "conda env create -f environment.yml"

3. When the environment is installed you can activate it using: "conda activate earth-analytics-python"

Note that it takes time to install of the packages found in the earth-analytics-python environment as it needs to download and install each library. Also, you need to have internet access for this to run!

# Inputs
To apply this particular workflow, download the Landsat imagery folder using the link either located under the "inputs" or at: https://drive.google.com/file/d/1AlZ2P_mSEjlP0k6AHfXPzT4AAtmDqhHA/view?usp=drive_link

To replicate the download process, go to the USGS Earth Explorer website (https://earthexplorer.usgs.gov/) and create an account if necessary. Select the appropriate Landsat tiles and date range (May 1st, 1990 to August 31st, 2023) for the Landsat imagery. Filter imagery with less than 10 percent cloud cover, and choose the Landsat satellite (Tier 2, Collection 2) for the analysis. This downloads the Landsat imagery data and all of its bands in .TIF format. 

The workflow expects the Landsat imagery to be organized in a specific folder structure, where the Landsat .TIF files AND shapefiles are stored in a folder inside "users/YOUR_NAME_HERE/earth-analytics/landsat_brighton". You can find the shapefiles for this code stored in this repository as .zip files. Make sure that the shapefiles and their metadata are located inside the same folder as your home directory.

# Outputs
Values:
* Decadal Average Percent of Change in NDVI: 6 study areas (5 PCA's + Brighton) and across 3 decades for a total of 24 percentage values, printed as in-line table.

Figures:
* KDE Frequency of NDVI Values by Decade: 5 kinetic depth effect (KDE) figures for each study area across 4 decades + and 1 for all decades, for a total of 6 in-line figures, downloadable as .png images (if desired).
* Annual Change in NDVI: A .gif is generated for each study area (6) cycling through 34 images (at most) for a total of 6 .gif files.
* Decadal Average NDVI Subplots: Average NDVI for 4 decades displayed as four-figure subplots clipped to each clipped to 5 study areas + Brighton for a total of 6 .tif subplot figures.

Raster Images:
* Decadal Average NDVI Composites:  A mean composited NDVI image using the supplied RED and NIR bands calculated for each decade (4) for 6 study areas for a total of 24 .tif images.

# Next Steps
For additional research, imagery can be substituted with different Landsat data downloaded with EarthExplorer covering different areas. Just upload the shapefiles within your area you wish to analyze during the import process accordingly and the same outputs will be created! Runtime usually takes about 10-15 minutes, depending on your device's processing power.

# Conclusion
This project aims to enhance the historical and ecological understanding of environmentally sensitive areas within the City of Brighton, Colorado. By analyzing satellite data and generating custom NDVI maps, decision-makers will gain valuable insights into vegetation density and health, promoting informed choices regarding sustainable landscape management and climate resilience. This project contributes to the broader goal of creating a healthier and more sustainable city by balancing conservation, resource use, and maintaining ecosystem services.
