defailt: build

build:
	./pkg-build.sh
.PHONY: build

test:
	./pkg-test.sh
.PHONY: test

release:
	./pkg-release.sh
.PHONY: release

testenv:
	docker build -t wodby-sdk-python-test-env ./
	docker run --rm -v$(PWD):/opt/sdk -it wodby-sdk-python-test-env bash
.PHONY: testenv