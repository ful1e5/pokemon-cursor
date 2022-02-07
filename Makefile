all: clean render build

.PHONY: all

# Default
clean:
	@rm -rf bitmaps themes

render: bitmapper svg
	@cd bitmapper && make install render

build: bitmaps
	@cd builder && make setup build


# Specific platform build
unix: clean render bitmaps
	@cd builder && make setup build_unix

windows: clean render bitmaps
	@cd builder && make setup build_windows

# Installation
.ONESHELL:
SHELL:=/bin/bash

src := ./themes
theme = Pokemon

local := ~/.icons
local_dest := $(local)/$(theme)

root := /usr/share/icons
root_dest := $(root)/$(theme)


install: $(src)
	@if [[ $EUID -ne 0 ]]; then
		@echo "> Installing '$(theme)' cursors inside $(local)/..."
		@mkdir -p $(local)
		@cp -r $(src)/$(theme) $(local_dest)
	@else
		@echo "> Installing '$(theme)' cursors inside $(root)/..."
		@mkdir -p $(root)
		@cp -r $(src)/$(theme) $(root_dest)
	@fi

uninstall:
	@if [[ $EUID -ne 0 ]]; then
		@echo "> Removing '$(theme)' from '$(local)'..."
		@rm -rf $(local_dest)
	@else
		@echo "> Removing '$(theme)' from '$(root)'..."
		@rm -rf $(root_dest)
	@fi

reinstall: uninstall install


# generates binaries
BIN_DIR = ../bin

prepare: bitmaps themes
	@rm -rf bin
	@mkdir -p bin
	@cd bitmaps
	@zip -r $(BIN_DIR)/bitmaps.zip $(theme)/*
	@cd ..
	@cd themes
	@tar -czvf $(BIN_DIR)/$(theme).tar.gz $(theme)
	@zip -r $(BIN_DIR)/$(theme)-Windows.zip $(theme)-Windows
	@cd ..
