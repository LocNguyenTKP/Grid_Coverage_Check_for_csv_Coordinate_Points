![image](https://github.com/LocNguyenTKP/Grid_Extraction/assets/66542803/8ccea15e-dc5d-4cd0-b45b-477167c1658f)

# Grid_Extraction

This Python script provides a comprehensive solution for manipulating geographic data specific to grid and region shapefiles. It primarily uses the Geopandas library along with Shapely for geometric operations. Key functionalities include:
## Installation of Necessary Libraries:
Automates the setup by installing Geopandas and Shapely.
## Data Loading: 
Loads grid and region shapefiles from specified directories.
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
