# Setup/Installation

## Standard-Methode

- Anforderungen: Python 3, `pip3`, und eventuell `gcc`

```bash
$ pip3 install homeassistant
```

Ein [`venv`](https://docs.python.org/3/library/venv.html) schützt vor Überraschungen.

## Development

```bash
$ git clone https://github.com/<FORK>/home-assistant.git
$ cd home-assistant
$ git remote add upstream https://github.com/home-assistant/home-assistant.git
$ git pull --rebase upstream master
$ script/setup
```

## Python Virtual Environment

Fedora:

```bash
$ git clone https://github.com/home-assistant/home-assistant.git
$ cd home-assistant
$ pyvenv-3.5 .
$ source bin/activate
$ script/setup
```

[Guide für Debian](https://home-assistant.io/getting-started/installation-virtualenv)

Details: [Python venv](https://docs.python.org/3/library/venv.html)

## Docker/Vagrant/LXC

- Docker:

```bash
$ docker run -d --name="home-assistant" -v /path/to/your/config:/config \
    -v /etc/localtime:/etc/localtime:ro --net=host homeassistant/home-assistant
```

- Vagrant: siehe [installation Vagrant](https://home-assistant.io/getting-started/installation-vagrant/)
- LXC/rkt/nspawn: siehe oben 

