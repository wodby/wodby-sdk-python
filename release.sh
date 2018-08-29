#!/usr/bin/env bash

set -e

if [[ "${DEBUG}" ]]; then
    set -x
fi

if [[ ! "$(python --version | grep "Python ${RELEASE_ON_VER}")" ]]; then
    exit 0
fi

if [[ "${TRAVIS_PULL_REQUEST}" == "false" && ("${TRAVIS_BRANCH}" == "master"  || -n "${TRAVIS_TAG}") ]]; then
    cd ./src
    python setup.py sdist bdist_wheel
    twine upload -u "${PIPY_USERNAME}" -p "${PIPY_PASSWORD}" --repository-url https://upload.pypi.org/legacy/ dist/*
fi