#!/usr/bin/env bash

set -e

if [[ "${DEBUG}" ]]; then
    set -x
fi

dir="${1}"

if [[ ! "${dir}" ]]; then
    echo "ERROR: Package dir have to be specified" 1>&2
    exit 1
fi

if [[ "${TRAVIS}" ]]; then
    if [[ ! "$(python --version | grep "Python ${RELEASE_ON_VER}")" ]]; then
        echo 'Exit because of Python version'
        exit 0
    fi
else
    only_test_release='true'
    echo 'Test release only due to empty TRAVIS env var'
fi

# Debug.
only_test_release='true'

if [[ "${TRAVIS_PULL_REQUEST}" == "false" && ("${TRAVIS_BRANCH}" == "master"  || -n "${TRAVIS_TAG}") ]]; then
    cd "${dir}"
    python setup.py sdist bdist_wheel

    if [[ "${only_test_release}" ]]; then
        echo 'Releasing test package'
        twine upload -u "${PYPI_USERNAME}" -p "${PYPI_PASSWORD}" --skip-existing \
            --repository-url https://test.pypi.org/legacy/ dist/*
    else
        echo '!!! Releasing package !!!'
        twine upload -u "${PYPI_USERNAME}" -p "${PYPI_PASSWORD}" --skip-existing \
            --repository-url https://upload.pypi.org/legacy/ dist/*
    fi
fi