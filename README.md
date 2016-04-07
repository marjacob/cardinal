# python-template
A template for new Python 3 projects.

## Requirements
- `make`
- `pip`
- `python3`
- `virtualenv`

## Setup
At this point I assume you do not have root access to the machine, but you do have the `make`, `python3` and `pip` commands available in your `${PATH}`.

### Special notes for users at the University of Oslo
Add the following to your`.bashrc` file if you do not have the aforementioned commands.

	PATH=~/.local/bin:/snacks/bin:${PATH}
	
Restart your terminal or issue `source ~/.bashrc` after editing.

### Installing virtualenv
You may skip this step if you have `virtualenv` available already. Otherwise, issue the following command.

	pip install --user virtualenv

## Using the template
The simplest way to use the template is to just fork this repository on GitHub, rename it and clone it to your local machine.

### Using the Makefile

#### Installing dependencies
If have just cloned this repository or a project using this `Makefile`, the first thing you want to do is to download and install all the dependencies locally in a virtual environment. You can do this by just issuing `make` inside the project directory. To add additional dependencies, add them to the `requirements-to-freeze.txt` file and issue `make` once more.

	make

#### Pinning package versions	
Under some circumstances (such as deploying to a production environment), you may want or need to deploy with specific versions of some or all project dependencies. Issuing `make freeze` writes a list of all currently installed packages and their versions to a `requirements.txt` file. This is used by `make restore` to recreate that specific environment.
	
	make freeze

#### Installing pinned packages
Destroy the virtual environment and rebuild it using the packages and versions specified in the `requirements.txt` file.
	
	make unfreeze

#### Upgrading dependencies
To update all packages installed in the virtual environment, issue `make upgrade`. Don't worry, you can revert to the previously installed package versions by issuing `make freeze` before doing the upgrade, and `make restore` after the upgrade.
	
	make upgrade

#### Linting your code
It is recommended to use tools to verify that your code meets the preferred coding standards of the Python community. See [PEP8](http://pep8.org) and [The Hitchhiker’s Guide to Python](http://docs.python-guide.org/en/latest/) for more information about that. This `Makefile` uses `pylint` by default to generate a report based on your code. You may use any tool you prefer, however.
	
	make lint

#### Executing the Python REPL
You can launch the interactive Python interpreter from inside the virtual environment.
	
	make repl

#### Executing your code
To execute your code inside the virtual environent, issue `make run`. Unfortunately, this command does not support any arguments (yet).
	
	make run

#### You made a mess of it
Destroy the virtual environment and all cache files.
	
	make clean

## More information
To read more about `requirements.txt` versus `requirements-to-freeze.txt`, refer to [this article](http://www.kennethreitz.org/essays/a-better-pip-workflow) by Kenneth Reitz.
