import math
from datetime import datetime
import argparse

def dms_to_decimal(degree, minute, direction):
    decimal = degree + minute / 60
    if direction in ['S', 'W']:
        decimal = -decimal
    return decimal

def parse_position(input_str):
    date_str, coord_str = input_str.split('@')
    # Parse date and time
    timestamp = datetime.strptime(date_str, "%Y-%m-%dT%H:%M")
    
    # Parse coordinates
    lat_str, lon_str = coord_str.split(',')
    # Latitude
    lat_degree = int(lat_str[:2])
    lat_minute = int(lat_str[3:5])
    lat_direction = lat_str[-1]
    latitude = dms_to_decimal(lat_degree, lat_minute, lat_direction)
    
    # Longitude
    lon_degree = int(lon_str[:3])
    lon_minute = int(lon_str[4:6])
    lon_direction = lon_str[-1]
    longitude = dms_to_decimal(lon_degree, lon_minute, lon_direction)
    
    return timestamp, latitude, longitude

def haversine(lat1, lon1, lat2, lon2):
    R = 3440.1  # Earth's radius in nautical miles
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance_nm = R * c
    return distance_nm

def initial_bearing(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dlon = lon2 - lon1
    
    x = math.sin(dlon) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dlon)
    
    bearing = math.atan2(x, y)
    bearing = math.degrees(bearing)
    initial_bearing = (bearing + 360) % 360
    return initial_bearing

def calculate_course_distance_speed(positions):
    results = []
    for i in range(1, len(positions)):
        timestamp1, lat1, lon1 = parse_position(positions[i - 1])
        timestamp2, lat2, lon2 = parse_position(positions[i])
        
        # Calculate distance and course
        distance = haversine(lat1, lon1, lat2, lon2)
        course = initial_bearing(lat1, lon1, lat2, lon2)
        
        # Calculate time difference in hours
        time_diff = (timestamp2 - timestamp1).total_seconds() / 3600.0
        speed = distance / time_diff if time_diff > 0 else 0
        
        results.append({
            "start_position": positions[i - 1],
            "end_position": positions[i],
            "course": course,
            "distance_nm": distance,
            "speed_knots": speed
        })
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate course, distance, and speed between multiple positions.")
    parser.add_argument(
        "positions",
        metavar="POSITION",
        type=str,
        nargs="+",
        help="Position in the format YYYY-MM-DDTHH:MM@00°00'N,000°00'E"
    )
    
    args = parser.parse_args()
    
    # Process the positions provided via CLI
    results = calculate_course_distance_speed(args.positions)
    
    # Output the results
    for result in results:
        print(f"From {result['start_position']} to {result['end_position']}:")
        print(f"  Course: {result['course']:.2f}°")
        print(f"  Distance: {result['distance_nm']:.2f} nm")
        print(f"  Speed: {result['speed_knots']:.2f} knots\n")
