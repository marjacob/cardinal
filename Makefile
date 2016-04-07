SHELL := /bin/sh

##### Variables
##############################################################################

# Python
python_bin    := $(shell which python3)

# Requirements
req_floating  := requirements-to-freeze.txt
req_pinned    := requirements.txt

# Virtual environment (do not change the ordering).
venv_path     := .venv
venv_bin_path := $(venv_path)/bin
venv_activate := $(venv_bin_path)/activate
venv_exec     := source $(venv_activate) && PS1="venv $$ " exec

# Virtual environment tools.
venv_pip      := $(venv_exec) pip
venv_pylint   := $(venv_exec) pylint
venv_python   := $(venv_exec) python

# Application
app_root      := cardinal

##### Rules
##############################################################################

# Build the virtual environment.
$(venv_path): $(venv_activate)
$(venv_activate): Makefile $(req_floating)
	@test -d $(venv_path) || virtualenv -p $(python_bin) $(venv_path)
	@$(venv_pip) install -Ur $(req_floating)
	@touch $(venv_activate)

# Destroy the virtual environment and cache files.
.PHONY: clean
clean:
	@$(RM) -r $(venv_path)
	@find $(app_root) \
		-name __pycache__ \
		-type d \
		-prune \
		-exec $(RM) -rf {} \;

# Save a list of all currently installed packages with pinned version numbers.
.PHONY: freeze
freeze: $(venv_path)
	@$(venv_pip) freeze > $(req_pinned)

# Generate linting report.
.PHONY: lint
lint: $(venv_path)
	@$(venv_pylint) --rcfile=pylintrc --output-format=text $(app_root)

# Recreate the virtual environment with pinned package versions.
.PHONY: unfreeze
unfreeze: clean
	@test -d $(venv_path) || virtualenv -p $(python_bin) $(venv_path)
	$(venv_pip) install -Ur $(req_pinned)
	@touch $(venv_activate)

# Install the latest version of all non-pinned packages.
.PHONY: upgrade
upgrade: $(venv_path)
	$(venv_pip) install -Ur $(req_floating)
	@touch $(venv_activate)

# Execute a REPL within the virtual environment.
.PHONY: repl
repl: $(venv_path)
	@$(venv_python)

# Execute the code within the virtual environment.
.PHONY: run
run: $(venv_path)
	@$(venv_python) -tt $(app_root)/main.py

# Execute a shell within the virtual environment.
.PHONY: shell
shell: $(venv_path)
	@$(venv_exec) $(SHELL)

# Perform unit tests.
.PHONY: test
test: $(venv_path)
	@$(venv_exec) green --processes 1 --run-coverage -v $(app_root)
