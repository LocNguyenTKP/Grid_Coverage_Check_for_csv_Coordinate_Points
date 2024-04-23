#!/usr/bin/env python
# coding: utf-8

# In[55]:


# Install Geopandas and Shapely
get_ipython().system('pip install geopandas shapely')


# In[56]:


import geopandas as gpd
from shapely.geometry import box


# In[57]:


# Load the shapefiles
grid_gdf = gpd.read_file(r"D:\BONN HELP\ethiopia-electricity-transmission-network\grid.gpkg")
region_gdf = gpd.read_file(r"D:\BONN HELP\GPS\GPS\Uganda\gadm41_UGA_shp\gadm41_UGA_1.shp")



# In[58]:


# Ensure the CRS matches
region_gdf = region_gdf.to_crs(grid_gdf.crs)
# Clip the grid data
clipped_grid_gdf = gpd.clip(grid_gdf, region_gdf)
# Save the clipped data to a new file
clipped_grid_gdf.to_file(r"D:\BONN HELP\GPS\GPS\Uganda.gpkg", driver="GPKG")
import pandas as pd


# In[59]:


# Load another shapefile that need to combine with clipped_grid_gdf
another_gdf = gpd.read_file(r"D:\BONN HELP\GPS\GPS\Uganda\uganda-electricity-transmission-network\Uganda Electricity Transmission Network.shp")


# In[60]:


# Ensure the combined shapefile matches the CRS
another_gdf = another_gdf.to_crs(grid_gdf.crs)


# In[61]:


# Concatenate GeoDataFrames
combined_gdf = gpd.GeoDataFrame(pd.concat([clipped_grid_gdf, another_gdf], ignore_index=True))


# In[74]:


import geopandas as gpd
import pandas as pd
from shapely.geometry import Point

points_df = pd.read_csv(r"D:\BONN HELP\GPS\GPS\Uganda\Uganda_2011.csv")
print(points_df.columns)
geometry = [Point(xy) for xy in zip(points_df['long'], points_df['lat'])]
points_gdf = gpd.GeoDataFrame(points_df, geometry=geometry)
points_gdf.set_crs("EPSG:4326", inplace=True)


# In[75]:


# Project to a suitable projected CRS for distance measurements (e.g., World Mercator, EPSG:3395)
points_gdf_projected = points_gdf.to_crs(epsg=3395)
points_gdf_buffered = points_gdf_projected.buffer(5000)


# In[76]:


# Convert the buffered geometries into a GeoDataFrame
buffered_gdf = gpd.GeoDataFrame(geometry=points_gdf_buffered, crs='EPSG:3395')
grid_gdf = clipped_grid_gdf.to_crs(epsg=3395)


# In[77]:


# Check for intersections between the buffered points and the grid
buffered_gdf['intersects'] = buffered_gdf.apply(lambda x: grid_gdf.intersects(x.geometry).any(), axis=1)
# Map True/False to Yes/No for intersection results
buffered_gdf['Grid_Within_5km'] = buffered_gdf['intersects'].map({True: 'Yes', False: 'No'})


# In[78]:


# Merge the intersection results back to the original data
points_gdf['Grid_Within_5km'] = buffered_gdf['Grid_Within_5km'].values


# In[79]:


# Drop the geometry column to save as an Excel file
final_df = points_gdf.drop(columns=['geometry'])
#Export excel file
final_df.to_csv(r"D:\BONN HELP\GPS\GPS\Uganda\Uganda_2011_update.csv", index=False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




