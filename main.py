 from road_sub1_class import OSMRoadDataDownloader

     geojson_path = "/home/evangelos/json/GeoJSON/swe.json"
     #future version will make it dynamic
     crs_project = 3006  # SWEREF99 TM, for Sweden
     crs_global = 4326   # Global geographic CRS

     downloader = OSMRoadDataDownloader(geojson_path)
     downloader.download_data()


 if __name__ == "__main__":
     main()
#
#



