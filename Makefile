.PHONY: setup
.DEFAULT_GOAL := setup

VENV_NAME?=venv
PYTHON=${VENV_NAME}/bin/python

$(VENV_NAME): requirements.txt
	test -d $(VENV_NAME) || virtualenv -p python3 $(VENV_NAME)
	${PYTHON} -m pip install -U pip
	${PYTHON} -m pip install -Ur requirements.txt
	touch $(VENV_NAME)

setup: $(VENV_NAME)