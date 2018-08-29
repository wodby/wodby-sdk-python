-include .env version

UID = $(shell id -u)
GID = $(shell id -g)

SWAGGER_CODEGEN_VER = 2.3.1
SWAGGER_CODEGEN_URL = http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/$(SWAGGER_CODEGEN_VER)/swagger-codegen-cli-$(SWAGGER_CODEGEN_VER).jar
SWAGGER_CODEGEN_JAVA_OPTS = -Xmx1024M -DapiTests=false -DmodelTests=false

ifndef ($(TRAVIS))
SWAGGER_CODEGEN_USER = -u $(UID):$(GID)
endif

MAVEN_VER = 3-jdk-7-alpine

default: build

build: clean codegen
.PHONY: build

codegen:
	[ -f ./codegen.jar ] || wget -nv "$(SWAGGER_CODEGEN_URL)" -O ./codegen.jar
	docker run -it --rm \
		-v "$(PWD)":/gen \
		-w /gen \
		$(SWAGGER_CODEGEN_USER) \
		maven:"$(MAVEN_VER)" java $(SWAGGER_CODEGEN_JAVA_OPTS) -jar ./codegen.jar generate \
			-i ./swagger.json \
			-l python \
			-o ./src \
			-D packageName=wodby_sdk \
			-D infoEmail='hello@wodby.com' \
			-D packageUrl='https://wodby.com/dev'

	[ -z "$(TRAVIS)" ] || sudo chown -R $(UID) ./

	rm -f ./src/.travis.yml \
		./src/git_push.sh \
		./src/.gitignore \
		./src/test-requirements.txt
.PHONY: codegen

clean:
	mv ./src/.swagger-codegen-ignore ./
	rm -rf ./codegen.jar ./src/*
	mv ./.swagger-codegen-ignore ./src/
.PHONY: clean

testenv:
	docker build -t wodby-sdk-python-test-env ./
	docker run --rm -v$(PWD):/opt/sdk -it wodby-sdk-python-test-env bash
.PHONY: testenv