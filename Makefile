testenv:
	docker build -t wodby-sdk-python-test-env ./
	docker run --rm -v$(PWD):/opt/sdk -it wodby-sdk-python-test-env bash
.PHONY: testenv