# Dependencies and their handling in Home Assistant

As a lot of other Open Source project, Home Assistant is using third party
Python libraries to perform certain tasks. For serving the frontend we
use `aiohttp`. The `luftdaten` sensor platform is using `python-luftdaten`.
This leads to a long list of dependencies currently we are talking about 150.

To avoid requiring users to install every dependency for every integration when
they install Home Assistant, we decided to go for an on-demand approach:

- The core dependencies are installed as normal when Home Assistant is
  installed with `pip3 install homeassistant`
- Dependencies for platforms are installed when a platform is loaded
- Dependencies for platforms are installed in `<config>/deps` using 
  `pip --target <config>/deps`
- `pkg_resources` is used to check if a dependency exists in `<config>/deps`
  and current Python environment
- The folder `<config>/dep`s is cleared when Home Assistant is upgraded
  (e.g., 0.60 -> 0.61)
- Package installation code lives in `util/package.py^
- Although there are many different permutations of requirements and some of
  these combinations require conflicting versions to be installed, we don't get
  reports of broken systems.

## 0.38 and the broken package system

aiohttp 1.3.0 introduced a bug that would break our websocket connections.
This was quickly discovered and they put a fix out in 1.3.1. Home Assistant
0.38 shipped with aiohttp 1.3.1.

Our brand new AppleTV integration is built on top of the library pyatv. In 0.38
we shipped version 0.1.3 which depended on aiohttp 1.3.0.

When Home Assistant loads the AppleTV platform (either via config or via
discovery), it will install pyatv 0.1.3 and it's dependency aiohttp 1.3.0
into `<config>/deps`. When you restart Home Assistant, the packages contained
in the `<config>/deps` folder have higher priority than the system environment,
thus aiohttp 1.3.0 will get loaded and breaking peoples installation.

The issue is caused by the following behavior:

When invoking `pip --target`, `pip` does not verify if a dependency already
exists in the current active Python environment.

While researching the issue, this answer on StackOverflow talks about changing
`PYTHONUSERBASE` instead of using `--target`. This is something we should
explore.

Research results PYTHONUSERBASE:

It works as long as the libraries specify a range for their dependencies. If
the version is pinned to a different version than our core dependency (as was
the case with atv in 0.38), it will go ahead and install the wrong dependency
in the target directory.

On OS X using `--user` will also result in a conflict with the prefix
configuration of Homebrew.

With aiohttp 1.3.0 installed in Python environment:

```bash
› PYTHONUSERBASE=/Users/paulus/dev/python/home-assistant/target-test python3 -m pip install pyatv==0.1.3 --user
Collecting pyatv==0.1.3
  Using cached pyatv-0.1.3-py3-none-any.whl
Requirement already satisfied: aiohttp==1.3.0 in /Users/paulus/.pyenv/versions/3.5.2/lib/python3.5/site-packages (from pyatv==0.1.3)
With aiohttp 1.3.1 installed in Python environment:

› PYTHONUSERBASE=/Users/paulus/dev/python/home-assistant/target-test python3 -m pip install pyatv==0.1.3 --user
```

