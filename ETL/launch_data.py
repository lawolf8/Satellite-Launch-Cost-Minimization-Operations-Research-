import requests
import Optional
import pandas as pd

class LaunchAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_upcoming_launches(self) -> None:
        """Retrieve upcoming launches from the API."""
        response = requests.get(f"{self.base_url}/upcoming")
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()

    def parse_launches(self, data) -> Optional[pd.DataFrame]:
        """Parse the API data into a more convenient format."""
        raise NotImplementedError("This method should be overridden by subclasses.")

class NasaLaunch(LaunchAPI):
    def __init__(self) -> None:
        super().__init__("https://api.nasa.gov/launches")

    def parse_launches(self, data) -> Optional[pd.DataFrame]:
        """Parse specific data format from NASA's launch API."""
        return [{
            'name': launch['mission_name'],
            'date': launch['launch_date'],
            'aircraft_type': launch['rocket']['rocket_name'],
            'details': launch['details']
        } for launch in data['launches']]

class SpaceXLaunch(LaunchAPI):
    def __init__(self) -> None:
        super().__init__("https://api.spacexdata.com/v4/launches")

    def parse_launches(self, data) -> Optional[pd.DataFrame]:
        """Parse specific data format from SpaceX's launch API."""
        return [{
            'name': launch['name'],
            'date': launch['date_utc'],
            'aircraft_type': launch['rocket']['name'],
            'details': launch['details']
        } for launch in data]
    
class UlaLaunch(LaunchAPI):
    def __init__(self):
        super().__init__("https://api.ulalaunch.com/v1/launches")

    def parse_launches(self, data) -> Optional[pd.DataFrame]:
        """Parse specific data format from ULA's launch API."""
        return [{
            'name': launch['mission'],
            'date': launch['scheduled_launch_date'],
            'aircraft_type': launch['rocket']['configuration'],
            'details': launch['mission_description']
        } for launch in data['results']]

class BlueOriginLaunch(LaunchAPI):
    def __init__(self) -> None:
        super().__init__("https://api.blueorigin.com/v1/launches")

    def parse_launches(self, data) -> Optional[pd.DataFrame]:
        """Parse specific data format from Blue Origin's launch API."""
        # Assuming structure; adjust according to actual API response
        return [{
            'name': launch['mission_name'],
            'date': launch['launch_date_utc'],
            'aircraft_type': launch['vehicle'],
            'details': launch.get('details', 'No details available')
        } for launch in data]


class data_main:
    def __init__(self) -> None:
        pass
    def main() -> None:
        nasa = NasaLaunch()
        spacex = SpaceXLaunch()
        ula = UlaLaunch()
        blue_origin = BlueOriginLaunch()

        # Process each agency
        agencies = [nasa, spacex, ula, blue_origin]
        for agency in agencies:
            try:
                data = agency.get_upcoming_launches()
                launches = agency.parse_launches(data)
                print(f"{agency.__class__.__name__} Launches:", launches)
                return {{}} #Outer Hash map for company, data; inner hashmap for additional data
            except Exception as e:
                print(f"Failed to process data for {agency.__class__.__name__}: {str(e)}")

