.PHONY: setup build clean

setup:
	direnv allow
	pip install -r requirements.txt

build:
	buildozer android debug

clean:
	rm -rf build bin .buildozer *.apk

