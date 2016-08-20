CURRENT_DIR = $(shell pwd)

all:
	( \
       source $(CURRENT_DIR)/.venv/bin/activate; \
       pip install -r requirements.txt; \
       deactivate; \
  )

run:
	( \
       source $(CURRENT_DIR)/.venv/bin/activate; \
       python spiffy; \
       deactivate; \
  )

.PHONY: all clean 