#!/usr/bin/env bash

set -e

if [[ "${DEBUG}" ]]; then
    set -x
fi

function pkg_release() {
    local dir="${1}"
    local test="${2}"
    local stored_dir=$(pwd)

    cd "${dir}"

    if [[ "${TRAVIS}" ]]; then
        python setup.py sdist bdist_wheel
    fi

    if [[ "${test}" ]]; then
        echo "Releasing ${dir} (test) ..."
        twine upload -u "${PYPI_USERNAME}" -p "${PYPI_PASSWORD}" --repository-url https://test.pypi.org/legacy/ dist/*
    else
        # !!! Pay attention, there is no way to remove published package !!!
        echo "Releasing ${dir} ..."
        twine upload -u "${PYPI_USERNAME}" -p "${PYPI_PASSWORD}" --repository-url https://upload.pypi.org/legacy/ dist/*
    fi

    cd "${stored_dir}"
}

if [[ "${TRAVIS}" ]]; then
    if [[ ! "$(python --version | grep "Python ${RELEASE_ON_VER}")" ]]; then
        echo 'Exit because of Python version'
        exit 0
    fi

    if [[ "${TRAVIS_PULL_REQUEST}" != "false"  ]]; then
        echo 'Ignore pull request'
        exit 0
    fi

    if [[ "${TRAVIS_BRANCH}" == "master"  ]]; then
        pkg_release ./src-master
    fi

    if [[ "${TRAVIS_TAG}"  ]]; then
        pkg_release ./src-tag
    fi
else
    pkg_release ./src test
fi