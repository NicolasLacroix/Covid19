from folium import Map
from folium.plugins import HeatMap

# import html to png

import os

default_location = [0, 0]
default_zoom_start = 1.5

def generateHeatmaps(df_date_list, date_columns):
    for date_values, date_col in zip(df_date_list, date_columns):
        base_map = Map(location=default_location, control_scale=True,
                       zoom_start=default_zoom_start)
        heatmap = HeatMap(
            data=date_values,
            name='Confirmed cases',
            min_opacity=0.6,
            radius=10,
            max_zoom=13
        )
        heatmap.add_to(base_map)
        base_map.save(f"./heatmaps/heatmap_{date_col.replace('/', '_')}.html")
        
def saveHeatmapsToPNG(path):
    heatmaps_files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    for file in heatmaps_files:
        # SAVE TO PNG
        pass