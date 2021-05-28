# homeassistant-timebox-mini
Divoom Timebox Mini custom service component for Home Assistant.
Based on [ScR4tCh/timebox](https://github.com/ScR4tCh/timebox) converted to Python3 and fixed.

The Divoom Timebox Mini is a Bluetooth speaker with a 11x11 RGB LED matrix.

![Timebox Mini](res/timebox-mini.jpg)

This component allow to run the following actions on your Timebox Mini from a HomeAssistant service:
- Set the clock automatically from your system clock
- Display the clock
- Set the audio volume level
- Set the LED brightness level
- Display a picture from predefined choices (see [matrices](timebox_mini/matrices) folder)
- Display the weather information (you have to use Divoom phone app to send weather info to your timebox)

## Setup instructions
### Copying into custom_components folder
Create a directory `custom_components` in your Home-Assistant configuration directory.
Copy the whole [timebox_mini](timebox_mini) folder from this project into the newly created directory `custom_components`.

The result of your copy action(s) should yield a directory structure like so:

```
.homeassistant/
|-- custom_components/
|   |-- timebox_mini/
|       |-- matrices/*.png
|       |-- __init__.py
|       |-- manifest.json
|       |-- services.yaml
```

### Enabling the custom_component
In order to enable this custom device_tracker component, add this code snippet to your Home-Assistant `configuration.yaml` file:

```yaml
timebox_mini:
```
After restart, the `timebox_mini.action` service will be available. You only need the MAC address of your Timebox.
![Timebox Mini Service](res/service.png)

When you run an action that changes what is displayed on the Timebox, an entity will be created to save the current displayed state.

![Timebox Mini entity](res/entity.png)

Please note that if you change the content on your Timebox without using the service (i.e. mobile app) this entity will not be updated.

## Troubleshooting
If the actions are not applied to your Timebox, you may need to pair manually with your device first using your OS Bluetooth settings.

## TODO
- Weather info setting
- Display animation
- [Moving text](https://github.com/DaveDavenport/timebox/blob/master/examples/movingtext.py)
