from pathlib import Path
import json, os
from typing import Optional


class Settings:
    base_url = 'https://www.metaweather.com'
    default_location = 'nairobi'
    location_url = f'{base_url}/api/location/search/'
    weather_url = f'{base_url}/api/location'
    home_path = Path.home()
    folder_name = '.weatherTool'
    app_path = f'{home_path}/{folder_name}'
    file_name = f'{app_path}/app_data.json'

    def create_app_folder(self):
        path = Path(self.app_path)
        path.mkdir(mode=0o777, exist_ok=True)

    def persist_local_data(self, *, data: dict):
        assert isinstance(data, dict), "The data must be a dictionary"
        path = Path(self.app_path)
        if not path.exists():
            self.create_app_folder()
        with open(self.file_name, 'w') as obj_in:
            try:
                json.dump(data, obj_in)
            except IOError as e:
                print(f"The following error occurred while creating the file :{e}")

    def read_local_data(self) -> Optional[dict]:
        path = Path(self.file_name)
        if path.exists():
            if os.path.getsize(self.file_name) > 0:
                with open(self.file_name, 'r') as obj_out:
                    try:
                        data = json.load(obj_out)
                        if data:
                            return data
                        else:
                            return None
                    except IOError as e:
                        print(e)
                        return None
            else:
                return None
        else:
            return None



settings = Settings()
