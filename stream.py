def live_input(stream=False):
    if stream:
        print("Streaming real-time geospatial data...")
        return [{"lat": 40.7128, "lon": -74.0060, "info": "sample"}]
    else:
        print("Returning static sample data.")
        return [{"lat": 40.7128, "lon": -74.0060, "info": "sample"}]