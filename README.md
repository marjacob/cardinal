# Cardinal the IRC bot
Cardinal ensures the continued survival of the species at the Department of Informatics by locating viable food sources in close proximity.

## Requirements
- `make` 
- `pip`
- `python3`
- `virtualenv`

## Setup
At this point I assume you do not have root access to the machine, but you do have the `make`, `python3` and `pip` commands available in your `${PATH}`.

Ensure that `~/.local/bin` is in your `${PATH}`, e.g. by adding the following to your `~/.bashrc` file.

```bash
PATH=~/.local/bin:${PATH}
```

### Installing `virtualenv`
You may skip this step if you have `virtualenv` available already. Otherwise, issue the following command. `sudo` is not required for local installations.

```bash
pip install --user virtualenv
```

## Using the `Makefile`

#### Installing dependencies
```bash
make
```
If have just cloned this repository, the first thing you want to do is to download and install all the dependencies locally in a virtual environment. You can do this by just issuing `make` inside the project directory. To add additional dependencies, add them to the `requirements-to-freeze.txt` file and issue `make` once more.

#### Pinning package versions	
```bash
make freeze
```
Under some circumstances (such as deploying to a production environment), you may want or need to deploy with specific versions of some or all project dependencies. Issuing `make freeze` writes a list of all currently installed packages and their versions to a `requirements.txt` file. This file is used by `make unfreeze` to recreate that specific environment.

#### Installing pinned packages
```bash
make unfreeze
```
Destroy the current virtual environment and rebuild it using the packages and versions specified in the `requirements.txt` file.

#### Upgrading dependencies
```bash
make upgrade
```
Update all packages installed in the current virtual environment. Don't worry, you can revert to the previously installed package versions at any time by issuing `make freeze` before doing the upgrade, and `make unfreeze` after the upgrade.

#### Linting your code
```bash
make lint | less
```
It is widely considered to be good practice to verify that your code meets the preferred coding standards of the Python community by using automated tools. See [PEP8](http://pep8.org) and [The Hitchhiker’s Guide to Python](http://docs.python-guide.org/en/latest/) for more information about that. This `Makefile` uses `pylint` by default to generate a report based on your code. You may use any tool you prefer, however.

#### Executing the Python REPL
```bash
make repl
```
You can launch the interactive Python interpreter from inside the virtual environment. Your own code as well as packages installed in the virtual environment is available here.

#### Executing a shell

```bash
make shell
```

Launch a shell inside the virtual environment. This allows you to use e.g. `pip` and `python` directly.

#### Executing your code
```bash
make run
```
Executes your code inside the virtual environent. Unfortunately, this command does not support any arguments (and it never will, due to limitations in `make`).

#### Executing unit tests

Performs all of the non-existing unit tests in the project. They may be implemented one day in the near or distant future.

#### You made a mess of it
```bash
make clean
```
Destroy the virtual environment and all cache files.

## Configuring Cardinal
Cardinal is configured through the configuration file `~/.cardinal/config.json`. This configuration file is generated automatically the first time you launch Cardinal (stop it by issuing `CTRL`+`C`).

The following is an automatically generated example configuration file for the Freenode IRC network (not UiO).

```son
{
	"host": "chat.freenode.net",
	"port": 6697,
	"ssl": true,
	"nick": "cardinal",
	"realname": "cardinal",
	"autojoins": [
		"##cardinal-default"
	],
	"includes": [
		"irc3.plugins.log",
		"irc3.plugins.uptime",
		"plugins.sio_plugin",
		"plugins.termvakt_plugin"
	]
}
```

There are currently no actions to perform server-side.

## Extending Cardinal

Because Cardinal uses the `irc3` library, we have inherited its plugin system. Take a look at the files in `cardinal/plugins/` to see how the existing plugins have been developed. Please refer to the [`irc3` documentation](https://irc3.readthedocs.org/en/latest/) for more information.

You should be aware that the `irc3` library uses the [`docopt` library](http://docopt.org) extensively, and the plugin system depends on it. This is weird but also good. I am a bit confused myself.

To make Cardinal load new plugins, add them the to the `includes` section in your local configuration file.

New plugins may be submitted with pull requests!

## More information
To read more about `requirements.txt` versus `requirements-to-freeze.txt`, refer to [this article](http://www.kennethreitz.org/essays/a-better-pip-workflow) by Kenneth Reitz.

Information from SiO is fetched using the RESTful [API](https://github.com/VegarM/sio-todays-dinner) developed by [VegarM](https://github.com/VegarM). The official endpoint is available at `http://api.desperate.solutions/dagens/`.