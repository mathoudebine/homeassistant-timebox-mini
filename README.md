# homeassistant-timebox-mini
Divoom Timebox Mini custom service component for Home Assistant.

This component allow to run the following actions on your Timebox Mini from a HomeAssistant service:
- Set the clock
- Display the clock
- Set the volume level
- Display a picture from predefined choices (see [matrices](./timebox-mini/matrices) folder)
- Display the weather information (you have to use Divoom phone app to send weather info to your timebox)

## Setup instructions
### Copying into custom_components folder
Create a directory `custom_components` in your Home-Assistant configuration directory.
Copy the whole [timebox-mini](./timebox-mini) folder from this project into the newly created directory `custom_components`.

The result of your copy action(s) should yield a directory structure like so:

```
.homeassistant/
|-- custom_components/
|   |-- timebox-mini/
|       |-- __init__.py
|       |-- manifest.json
|       |-- services.yaml
```

### Enabling the custom_component
In order to enable this custom device_tracker component, add this code snippet to your Home-Assistant `configuration.yaml` file:

```yaml
timebox-mini:
```
After restart, the `timebox-mini.action` service will be available. You only need the MAC address of your Timebox.

## Troubleshooting
If the actions are not applied to your Timebox, you may need to pair manually with your device first using your OS Bluetooth settings.
