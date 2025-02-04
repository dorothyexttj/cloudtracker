# CloudTracker

CloudTracker is a simple Python program that rotates your desktop wallpaper based on a user-defined schedule and a collection of images stored on your Windows machine.

## Features

- Change desktop wallpaper at specified intervals.
- Supports JPG and PNG image formats.
- Easy configuration through a JSON file.

## Requirements

- Windows OS
- Python 3.x

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/cloudtracker.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd cloudtracker
   ```

3. **Prepare your image folder:**

   Add JPG and/or PNG images to a directory on your computer that you want to use as your wallpapers.

4. **Edit the script:**

   Update the `image_folder` variable in `cloudtracker.py` with the path to your image collection folder.

5. **Configure the schedule:**

   Edit `schedule.json` to set the interval (in minutes) for changing the wallpaper. The default is set to 60 minutes.

## Usage

Run the script using Python:

```bash
python cloudtracker.py
```

The program will rotate your wallpapers based on the specified schedule.

## License

This project is licensed under the MIT License.

## Contributing

Feel free to submit issues or pull requests for improvements or new features.

## Acknowledgements

- Inspired by the desire to keep desktop environments fresh and personalized.