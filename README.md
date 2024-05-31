# Yet-another-i3-blocks-weather-block

Simple script that utilizes the AccuWeather API for displaying the current weather status.

![alt text](https://i.imgur.com/fr5TKwL.png)

## Dependencies
```
python3
```

## Installation

- Clone this repo into your i3blocks/scripts directory
- Create an account and get your api key https://developer.accuweather.com/
- Run the script once to create config.json
- Put your API key in config.json

## Note
The free tier of accuweather is limited to 50 calls/day and 1 key/developer. This is why the script executes every 1728 seconds (28.8 minutes)

## Usage
Add these lines to your i3blocks config file

```bash
[WEATHER]
command=$SCRIPT_DIR/yet-another-i3-blocks-weather-block/yaibwb
interval=1728
```
