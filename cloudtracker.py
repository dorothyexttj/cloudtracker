import os
import ctypes
import time
from datetime import datetime, timedelta
from pathlib import Path
import json

class CloudTracker:
    def __init__(self, image_folder, schedule_file):
        self.image_folder = Path(image_folder)
        self.schedule_file = schedule_file
        self.current_image_index = 0
        self.load_schedule()

    def load_schedule(self):
        if os.path.exists(self.schedule_file):
            with open(self.schedule_file, 'r') as file:
                self.schedule = json.load(file)
        else:
            self.schedule = {"interval": 60}  # Default to 60 minutes
            self.save_schedule()

    def save_schedule(self):
        with open(self.schedule_file, 'w') as file:
            json.dump(self.schedule, file)

    def change_wallpaper(self):
        images = list(self.image_folder.glob('*.jpg')) + list(self.image_folder.glob('*.png'))
        if not images:
            print("No images found in the specified folder.")
            return

        self.current_image_index = (self.current_image_index + 1) % len(images)
        new_wallpaper = str(images[self.current_image_index])
        
        # Change desktop wallpaper
        ctypes.windll.user32.SystemParametersInfoW(20, 0, new_wallpaper, 3)
        print(f"Wallpaper changed to: {new_wallpaper}")

    def run(self):
        next_change = datetime.now()
        while True:
            if datetime.now() >= next_change:
                self.change_wallpaper()
                next_change = datetime.now() + timedelta(minutes=self.schedule["interval"])
            
            time.sleep(1)

if __name__ == "__main__":
    image_folder = "C:\\Path\\To\\Your\\ImageCollection"
    schedule_file = "schedule.json"
    tracker = CloudTracker(image_folder, schedule_file)
    tracker.run()