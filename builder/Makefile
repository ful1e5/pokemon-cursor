all: setup build
.PHONY: all

.ONESHELL:
SHELL:=/bin/bash

bitmaps_dir = "../bitmaps"

X_SIZES ?=22 24 28 32 40 48 56 64 72 80 88 96
WIN_CANVAS_SIZE ?= 32
WIN_SIZE ?= 24

setup:
	@python3 -m pip install clickgen --user

build:
	@python3 build.py -p "$(bitmaps_dir)/Pokemon" --xsizes $(X_SIZES) --win-size $(WIN_SIZE) --win-canvas-size $(WIN_CANVAS_SIZE)

build_unix:
	@python3 build.py unix -p "$(bitmaps_dir)/Pokemon" --xsizes $(X_SIZES)

build_windows:
	@python3 build.py windows -p "$(bitmaps_dir)/Pokemon" --win-size $(WIN_SIZE) --win-canvas-size $(WIN_CANVAS_SIZE)
