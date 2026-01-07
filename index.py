python
import requests
import matplotlib.pyplot as plt

# Constants
TRANSPORT_API_URL = 'https://api.transport.abudhabi/realtime'
AQI_API_URL = 'https://api.airquality.abudhabi/current'

# Fetch real-time transport data
def get_transport_data():
    response = requests.get(TRANSPORT_API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception('Failed to fetch transport data')

# Fetch real-time AQI data
def get_aqi_data():
    response = requests.get(AQI_API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception('Failed to fetch AQI data')

# Display transport and AQI data
def display_data(transport_data, aqi_data):
    # Example: Plotting bus locations and AQI on a map
    plt.figure(figsize=(10, 5))
    
    # Plot transport data
    for bus in transport_data['buses']:
        plt.scatter(bus['lng'], bus['lat'], color='blue', label='Bus')
    
    # Plot AQI data
    for station in aqi_data['stations']:
        plt.scatter(station['lng'], station['lat'], color='red', label=f'AQI: {station['aqi']}')
    
    plt.title('Real-Time Public Transport and Air Quality in Abu Dhabi')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    plt.legend()
    plt.show()

# Main function
if __name__ == '__main__':
    transport_data = get_transport_data()
    aqi_data = get_aqi_data()
    display_data(transport_data, aqi_data)
