import geopandas as gpd

def convert_shapefile_to_geojson(shapefile_path, output_geojson_path):
    # Read the shapefile using geopandas
    gdf = gpd.read_file(shapefile_path)
    
    # Convert the geodataframe to a GeoJSON file
    gdf.to_file(output_geojson_path, driver='GeoJSON')

# Define the file paths for the input shapefile and output GeoJSON file
shapefile_path = 'shapefile_path'
output_geojson_path = 'output_geojson_path`'

# Call the conversion function
convert_shapefile_to_geojson(shapefile_path, output_geojson_path)

print('Shapefile has been successfully converted to GeoJSON!')
