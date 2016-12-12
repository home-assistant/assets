# Home Assistant Workshop @ [Puzzle ITC](https://www.puzzle.ch/de/), Bern - 12.12.2016

## Unterlagen

- Slides: [2016-puzzle-slides.html](2016-puzzle-slides.html)
- Handout: [2016-puzzle-web.html](2016-puzzle-web.html)

## Test-Sensor

- IP-Adresse: http://192.168.0.209:5000
- Awesome Weather Station: `/weather`
- Weitere Endpunkte:
  - `/binary_sensor`
  - `/binary_sensor1`
  - `/sensor`
  - `/sensor1`
  - `/sensor2` inklusive Untersützung für POST requests
  - `/auth_basic` HTTP Basic Auth (`ha1`/`test1` oder `ha2`/`test2`
  - `/auth_digest` HTTP Digest Auth (`ha1`/`test1` oder `ha2`/`test2`)

Alternativen (online):

- https://www.ipify.org
- https://freegeoip.net


Details: [ha-rest.py](https://github.com/home-assistant/home-assistant-dev-helper/blob/master/ha-rest.py)

