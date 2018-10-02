build:
	python3 compile.py

.PHONY: clean test

clean:
	rm -rf build

test: build
	cd build; python -m http.server
