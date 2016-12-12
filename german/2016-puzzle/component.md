# Komponente

- Zusammenfassung von Einzelteilen
- Vereinfachung der Konfiguration
- Discovery

## Immer das gleiche...

Konfiguration für binären Sensor, Sensor und Schalter.

```bash
sensor:
  - platform: awesome_weather
    host: 10.100.0.200

binary_sensor:
  - platform: awesome_weather
    host: 10.100.0.200

switch:
  - platform: awesome_weather
    host: 10.100.0.200
```

## Mini-Komponente

```python
DOMAIN = 'mini_component'

def setup(hass, config):
    hass.states.set('mini.component', 'Yeah!')
    return True
```

Konfigurationseintrag in `configuration.yaml`:

```bash
mini_component:
```

Genau, das sieht wie `awesome_service` aus...

## hass bei Komponenten

- `hass.config`
  - Basis-Konfiguration vom Home Assistant inkl. Standort, Koordinaten, Temperatur-Einheit und Pfad des Konfigurations-Verzeichnis ([Details](https://github.com/home-assistant/home-assistant/blob/dev/homeassistant/core.py#L687))
- `hass.states`
  - Die StateMachine erlaubt das Zuordnen von Zuständen und Verfolgung deren Veränderungen ([Details](https://github.com/home-assistant/home-assistant/blob/dev/homeassistant/core.py#L434)) 
- `hass.bus`
  - Der EventBus hört auf Events und kann diese auslösen ([siehe auch verfügbare Methoden](https://github.com/home-assistant/home-assistant/blob/dev/homeassistant/core.py#L229))
- `hass.services   `
  - Die ServiceRegistry ist für die Verwaltung der Services zuständig ([siehe auch verfügbare Methoden](https://github.com/home-assistant/home-assistant/blob/dev/homeassistant/core.py#L568))

## Konfiguration

- siehe auch Platform-Konfiguration
- Unterschied: kompletter Inhalt von `config`

```bash
mini_component:
  name: hugo
  location: stockholm
```

Inhalt `config` (-> `config[DOMAIN]['name']`):

```bash
OrderedDict([
('homeassistant', OrderedDict([('latitude', 46.94807602611714), ('longitude', ...,
('sun', {}),
('mini_component', OrderedDict([('name', 'hugo'), ('location', 'stockholm')])),
])
```

## awesome_station-Komponente

```python
import logging
from datetime import timedelta

import voluptuous as vol

import homeassistant.helpers.config_validation as cv
from homeassistant.const import CONF_HOST, CONF_PORT
from homeassistant.util import Throttle

_LOGGER = logging.getLogger(__name__)

AWESOME = None
AWESOME_PLATFORMS = ['sensor', 'binary_sensor']

DOMAIN = 'awesome_station'

MIN_TIME_BETWEEN_UPDATES = timedelta(seconds=10)

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Required(CONF_HOST): cv.string,
        vol.Optional(CONF_PORT, default=5000): cv.port,
    }),
}, extra=vol.ALLOW_EXTRA)


def setup(hass, config):
    """Set up of the Awesome Weather Station component."""
    host = config[DOMAIN][CONF_HOST]
    port = config[DOMAIN][CONF_PORT]

    global AWESOME
    if AWESOME is None:
        AWESOME = AwesomeStationData(host, port)

    return True


class AwesomeStationData(object):
    """Get the latest data and update the states."""

    def __init__(self, host, port):
        """Initialize the data object."""
        self.host = host
        self.port = port

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    def update(self):
        """Get the latest data from the Awesome Weather station."""
        import requests
        url = '{}{}:{}/{}'.format('http://', self.host, self.port, 'weather')
        self.data = requests.get(url).json()
```

### Binärer Sensor

```python
import logging

from homeassistant.components.binary_sensor import BinarySensorDevice
from homeassistant.loader import get_component

_LOGGER = logging.getLogger(__name__)

DEPENDENCIES = ['awesome_station']


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Set up the Awesome Weather Station binary sensor platform."""
    awesome = get_component('awesome_station')
    add_devices([
        AwesomeStationBinarySensor(awesome.AWESOME)
    ])

class AwesomeStationBinarySensor(BinarySensorDevice):
    """Representation of an Awesome Weather Station binary sensor."""

    def __init__(self, aw):
        """Initialize the sensor."""
        self._awesome = aw
        self._data = False
        self.update()

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Awesome Station Binary sensor'

    @property
    def is_on(self):
        """Return the state of the sensor."""
        return bool(int(self._data))

    @property
    def sensor_class(self):
        """Return the class of this sensor."""
        return 'light'

    def update(self):
        """Get the latest data and updates the state."""
        self._awesome.update()
        self._data = self._awesome.data['sun']

```

### Einrichtung

Verschieben nach `<config_dir>/custom_components/awesome_station.py`

Konfigurationseintrag in `configuration.yaml`:

```bash
awesome_station:
    host: 10.100.0.200
binary_sensor:
  - platform: awesome_station
```

## Automatisches Laden von Platformen

- Konfiguration für Benutzer sehr simple
- Benutzer kriegt alles, auch Platformen, welcher er gar nicht hat oder will

Konfiguration nur in `configuration.yaml` nur noch:

```bash
awesome_station1:
    host: 10.100.0.200
```

### Komponente

```python
import logging
from datetime import timedelta

import voluptuous as vol

from homeassistant.components.discovery import load_platform
import homeassistant.helpers.config_validation as cv
from homeassistant.const import CONF_HOST, CONF_PORT
from homeassistant.util import Throttle

_LOGGER = logging.getLogger(__name__)

AWESOME = None
AWESOME_PLATFORMS = ['binary_sensor', 'sensor']

DOMAIN = 'awesome_station1'

MIN_TIME_BETWEEN_UPDATES = timedelta(seconds=10)

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Required(CONF_HOST): cv.string,
        vol.Optional(CONF_PORT, default=5000): cv.port,
    }),
}, extra=vol.ALLOW_EXTRA)


def setup(hass, config):
    """Set up of the Awesome Weather Station component."""
    host = config[DOMAIN][CONF_HOST]
    port = config[DOMAIN][CONF_PORT]

    global AWESOME
    if AWESOME is None:
        AWESOME = AwesomeStationData(host, port)
        AWESOME.update()

    for platform in AWESOME_PLATFORMS:
        load_platform(hass, platform, DOMAIN, {}, config)

    return True


class AwesomeStationData(object):
    """Get the latest data and update the states."""

    def __init__(self, host, port):
        """Initialize the data object."""
        self.host = host
        self.port = port

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    def update(self):
        """Get the latest data from the Awesome Weather station."""
        import requests
        url = '{}{}:{}/{}'.format('http://', self.host, self.port, 'weather')
        self.data = requests.get(url).json()

```

### Binärer Sensor

```python
from homeassistant.components.binary_sensor import BinarySensorDevice
import homeassistant.components.awesome_station1 as awesome

def setup_platform(hass, config, add_devices, discovery_info=None):
    """Set up the Awesome Weather Station binary sensor platform."""
    add_devices([
        AwesomeStationBinarySensor(awesome.AWESOME)
    ])

class AwesomeStationBinarySensor(BinarySensorDevice):
    """Representation of an Awesome Weather Station binary sensor."""

    def __init__(self, aw):
        """Initialize the sensor."""
        self._awesome = aw
        self._data = False
        self.update()

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Awesome Station Binary sensor'

    @property
    def is_on(self):
        """Return the state of the sensor."""
        return bool(int(self._data))

    @property
    def sensor_class(self):
        """Return the class of this sensor."""
        return 'light'

    def update(self):
        """Get the latest data and updates the state."""
        self._data = self._awesome.data['sun']
```

### Sensor

```python
import homeassistant.components.awesome_station1 as awesome
from homeassistant.const import ATTR_LONGITUDE, ATTR_LATITUDE, TEMP_CELSIUS
from homeassistant.helpers.entity import Entity

def setup_platform(hass, config, add_devices, discovery_info=None):
    """Set up the Awesome Weather Station sensor platform."""
    add_devices([
        AwesomeStationSensor(awesome.AWESOME)
    ])

class AwesomeStationSensor(Entity):
    """Representation of an Awesome Weather Station sensor."""

    def __init__(self, aw):
        """Initialize the sensor."""
        self._awesome = aw
        self._data = False
        self.update()

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Awesome Weather sensor'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._data['temp']

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return TEMP_CELSIUS

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        if self._data is not None:
            return {
                'led': self._data['led'],
                'humitidy': self._data['hum'],
                'sun': self._data['sun'],
                ATTR_LONGITUDE: self._data['details']['long'],
                ATTR_LATITUDE: self._data['details']['lat'],
            }

    def update(self):
        """Get the latest data and updates the state."""
        self._data = self._awesome.data
```

### Einrichtung

Verschieben nach `<config_dir>/custom_components/awesome_station1.py`

Konfigurationseintrag in `configuration.yaml`:

```bash
awesome_station:
    host: 10.100.0.200
```

### Dateien

```bash
Komponente:       awesome_station1.py
Binärer Sensor:  /binary_sensor/awesome_station1.py
Sensor:          /sensor/awesome_station1.py
```

## Dicovery

- Suchen nach uPnP und zeroconf/mDNS-Diensten
- Über `discovery`-Komponent mit [netdisco](https://github.com/home-assistant/netdisco)
- Warten auf `SERVICE_DISCOVERED`-Events
- Automatisches Einrichtung (z. B. chromecast)

Details [Discovery](https://home-assistant.io/developers/component_discovery/)

## Eigene Ideen umsetzen

### Weitere Punkte

- Setup der Platform/Komponente fehlschlagen lassen, wenn Problem vorhanden
- Robustheit
- Docstrings
- Nutzen von [Asynchronous Programming](https://home-assistant.io/developers/asyncio/)
- [Frontend](https://home-assistant.io/developers/frontend/) erweitern


### Pull request eröffnen

- [Development-Umgebung](https://home-assistant.io/developers/development_environment/) einrichten inkl. Fork
- Neuer Branch erzeugen: `git checkout -b some-feature`
- Etwas machen (Ergänzungen, Änderungen, etc)...
  - Neue Abhängigkeiten als `REQUIREMENTS` hinzufügen
  - [Testen](https://home-assistant.io/developers/development_testing/) des Codes (Stil und Syntax)
- Dokumentation für home-assistant.io machen
- Aktualisieren von `requirements_all.txt` mit `script/gen_requirements_all.py`
- Tests hinzufügen oder neue Platform/Komponente in `.coveragerc` eintragen
- [Pull request](https://github.com/home-assistant/home-assistant/compare) eröffnen mit allen Dateien
