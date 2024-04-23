![image](https://github.com/LocNguyenTKP/Grid_Extraction/assets/66542803/8ccea15e-dc5d-4cd0-b45b-477167c1658f)

# Grid_Extraction

This Python script utilizes Geopandas and Shapely to perform spatial analysis on point data from a CSV file and grid data from shapefiles. The goal is to determine which points lie within a 5km radius of a grid (e.g., an electricity grid). Maps the intersection results back to the original points data, labeling each point with 'Yes' if it has grid within 5km, or 'No' if it does not.

## Installation of Necessary Libraries:
Automates the setup by installing Geopandas and Shapely.
![image](https://github.com/LocNguyenTKP/Grid_Extraction/assets/66542803/2f9f4606-0260-4482-b84a-a745fe9a2ab6)

## Data Loading: 
Loads grid and region shapefiles from specified directories.
![image](https://github.com/LocNguyenTKP/Grid_Extraction/assets/66542803/cdc0ea73-e749-4e5c-8df5-18f263969a2e)
![image](https://github.com/LocNguyenTKP/Grid_Extraction/assets/66542803/a3e3eff4-0712-457a-81d7-70f8baf6e8b2)

## Data Clipping and CRS Alignment: 
Ensures that Coordinate Reference Systems (CRS) match across datasets, and clips grid data based on regional boundaries.
![image](https://github.com/LocNguyenTKP/Grid_Extraction/assets/66542803/539233dc-69a8-43af-bcc4-08d5ff558109)

## Data Concatenation: 
Merges multiple geographic data frames into a single consolidated frame.
![image](https://github.com/LocNguyenTKP/Grid_Extraction/assets/66542803/0f46ea48-dde1-4691-ac2f-31b6f605d67b)

## Geometric Transformations and Analysis:
Projects data into a suitable CRS for distance measurements, generates buffers, and checks for intersections between geographic features.
![image](https://github.com/LocNguyenTKP/Grid_Extraction/assets/66542803/b50500b5-8f4c-49a6-8711-c5e1c5529651)
![image](https://github.com/LocNguyenTKP/Grid_Extraction/assets/66542803/a4a3814e-106e-4d26-8ae4-536d1da975d8)
![image](https://github.com/LocNguyenTKP/Grid_Extraction/assets/66542803/339e55ea-08c6-4a27-941e-bb7bb0e90cb6)

## Exporting Results: 
Saves the final processed data to a CSV file, updating it with intersection results and additional geographic information.
This script is particularly useful for spatial analysis projects that require precise geographic manipulations and data integration between multiple sources.
![image](https://github.com/LocNguyenTKP/Grid_Extraction/assets/66542803/378d9ea5-047f-40f9-9b8c-7b2641e7eab2)
![image](https://github.com/LocNguyenTKP/Grid_Extraction/assets/66542803/8fc83077-f5b9-4091-a3aa-2fb5652de1e4)

## Utility of the Script
This script is invaluable for projects where understanding the accessibility of infrastructure (like electricity grids) relative to specific locations is crucial. It can be used in urban planning, resource management, or any field requiring detailed spatial analysis of infrastructure coverage.
By using this script, analysts and planners can identify areas with sufficient infrastructure coverage and prioritize areas that need development or intervention, thereby aiding in efficient resource allocation and planning.

## Contact
For any queries or further collaboration, feel free to contact Loc Nguyen nguyenloctkp@gmail.com.
