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
## Data Concatenation: 
Merges multiple geographic data frames into a single consolidated frame.
## Geometric Transformations and Analysis:
Projects data into a suitable CRS for distance measurements, generates buffers, and checks for intersections between geographic features.
## Exporting Results: 
Saves the final processed data to a CSV file, updating it with intersection results and additional geographic information.
This script is particularly useful for spatial analysis projects that require precise geographic manipulations and data integration between multiple sources.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your suggested changes.

## Contact
For any queries or further collaboration, feel free to contact Loc Nguyen nguyenloctkp@gmail.com.
