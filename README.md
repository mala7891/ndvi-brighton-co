# ndvi-brighton-co

# Introduction
This README file provides an overview of a capstone project focused on enhancing the historical and ecological understanding of environmentally sensitive areas within the City of Brighton, Colorado. The project aims to analyze satellite data and create custom NDVI (Normalized Difference Vegetation Index) maps for five specific areas in Brighton. These maps will assist decision-makers in making informed choices about managing and preserving these properties to withstand the immediate effects of climate change.

# In This Repository:
* README.md
* LICENSE.txt
* .gitignore file
* "notebooks" folder containing:
- ndvi_brighton_co.html
- ndvi_brighton_co.ipynb

# Project Objectives
The primary objectives of this project are as follows:

* Analyze satellite data: Collect and process satellite imagery to obtain relevant data for the selected areas in Brighton, Colorado.
* Generate custom NDVI maps: Utilize the Normalized Difference Vegetation Index (NDVI) to produce maps that depict vegetation density and health.
* Enhance historical and ecological understanding: Provide decision-makers with valuable insights into the historical and ecological conditions of the selected areas, aiding in informed decision-making and resource management.
* Support sustainable landscape management: Enable the prioritization of conservation practices, effective monitoring, and evaluation of progress towards sustainability and climate resilience goals within the city.

# Purpose
The purpose of this repository is to provide a workflow for custom NDVI mapping using Landsat imagery data. It includes code and instructions on how to process satellite data, calculate NDVI, classify land cover, and calculate the percent change of land cover between two time periods.

The goals and motivations for the project are to enhance the historical and ecological understanding of the landscape in the City of Brighton, Colorado. The project aims to enable decision-makers to make informed choices about how environmentally sensitive areas can withstand the immediate effects of climate change and promote sustainable landscape management.

One unique contribution of this project repository to data science and earth/environmental science is the integration of various free and open source Python packages, such as rioxarray, geopandas, earthpy, numpy, and matplotlib, to perform the entire workflow from loading publicly available datasets such as Landsat imagery to generating custom NDVI maps and land cover classifications.

Someone would want to use the code/workflow presented in this repository for several reasons:

* It provides a standardized and replicable approach for processing Landsat imagery and calculating NDVI, making it easier for researchers, horticulturists, and decision-makers to analyze vegetation dynamics.
* The workflow enables the classification of land cover based on NDVI values, allowing users to identify different vegetation types or land cover classes within the study area.
* The calculation of percent change of land cover between two time periods provides insights into vegetation changes over time, aiding in monitoring and assessing the effects of environmental changes and climate resilience.
* The workflow includes visualization capabilities, allowing users to generate maps and visual representations of NDVI, land cover classifications, and percent change of land cover, facilitating data interpretation and communication of findings.
* Overall, this code/workflow is valuable for professionals working in the field of environmental science, horticulture, land management, or anyone interested in analyzing and monitoring vegetation dynamics using Landsat imagery.

# Project Steps
To achieve the project objectives, the following steps will be undertaken:

# Data Collection: 
Gather satellite imagery data for the selected areas in Brighton, Colorado. This data should cover a sufficient historical time frame to observe changes in vegetation patterns.
# Preprocessing and Analysis: 
Process the collected satellite data to remove any noise or artifacts and calculate the NDVI values for each pixel within the imagery.
# NDVI Map Generation: 
Utilize GIS software (such as ArcGIS, QGIS, or similar) to generate custom NDVI maps based on the processed satellite data. These maps will visually represent the vegetation density and health across the selected areas.
# Interpretation and Analysis:
Interpret the NDVI maps and analyze the vegetation patterns, identifying areas with higher or lower vegetation density or potential ecological significance.
# Documentation and Reporting: 
Prepare a comprehensive report summarizing the findings, interpretations, and recommendations based on the NDVI analysis. Include relevant historical and ecological context to enhance decision-makers' understanding of the landscape conditions.
# Presentation and Discussion: 
Present the findings to the appropriate stakeholders, including municipality officials, urban planners, and environmental experts. Facilitate a discussion on the management strategies and practices that balance conservation and resource use while maintaining ecosystem services and resilience to environmental changes.
# Integration and Decision-making: 
Collaborate with decision-makers to integrate the acquired knowledge into municipal decision-making processes. Use the information gained to guide sustainable landscape management practices and prioritize initiatives that promote a healthier and more resilient city.

# Project Deliverables
The final deliverables for this project will include:

* Custom NDVI maps: Maps depicting the vegetation density and health for the selected areas in Brighton, Colorado.
* Comprehensive report: A detailed report summarizing the findings, interpretations, and recommendations based on the NDVI analysis. This report will also include historical and ecological context for the selected areas.
* Presentation materials: Presentation slides or visual aids to communicate the project's key findings and recommendations to stakeholders and decision-makers.

# Tools/Packages Required
To run the workflow, you will need the following tools/packages:
* Python (version 3.0 or higher)
* os
* rioxarray
* geopandas
* earthpy
* numpy
* matplotlib

# Data Formats and Types
To apply this workflow, you need Landsat imagery data in GeoTIFF format. The Landsat imagery should contain the necessary bands, specifically the red and near-infrared (NIR) bands.

The workflow expects the Landsat imagery to be organized in a specific folder structure, where the Landsat GeoTIFF files are stored in a folder named "landsat_data".

Make sure to select Landsat scenes that cover the study area and the desired time periods. The Landsat data should be available in GeoTIFF format and include the red and NIR bands necessary for NDVI calculation.

Ensure that the Landsat imagery data has sufficient spatial and temporal resolution for analysis. Additionally, consider the cloud cover percentage and select scenes with minimal cloud cover to obtain accurate results.

You can explore other reputable data sources or satellite data repositories that provide Landsat imagery data in GeoTIFF format suitable for NDVI analysis.

# Conclusion
This project aims to enhance the historical and ecological understanding of environmentally sensitive areas within the City of Brighton, Colorado. By analyzing satellite data and generating custom NDVI maps, decision-makers will gain valuable insights into vegetation density and health, promoting informed choices regarding sustainable landscape management and climate resilience. This project contributes to the broader goal of creating a healthier and more sustainable city by balancing conservation, resource use, and maintaining ecosystem services.

