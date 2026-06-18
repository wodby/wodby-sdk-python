#!/usr/bin/env bash

set -e

if [[ "${DEBUG}" ]]; then
    set -x
fi

function pkg_release() {
    local dir="${1}"
    local repository_url='https://upload.pypi.org/legacy/'
    local stored_dir=$(pwd)

    if [[ -n "${PYPI_TOKEN:-}" ]]; then
        export PYPI_USERNAME='__token__'
        export PYPI_PASSWORD="${PYPI_TOKEN}"
    fi

    if [[ -z "${PYPI_USERNAME:-}" || -z "${PYPI_PASSWORD:-}" ]]; then
        echo "ERROR: Set PYPI_TOKEN or PYPI_USERNAME/PYPI_PASSWORD before publishing." 1>&2
        exit 1
    fi

    if [[ -n "${TEST_PYPI:-}" ]]; then
        repository_url='https://test.pypi.org/legacy/'
    fi

    cd "${dir}"
    rm -rf dist build ./*.egg-info

    python setup.py sdist bdist_wheel

    # !!! Pay attention, there is no way to remove published package !!!
    echo "Releasing ${dir} to ${repository_url} ..."
    twine upload -u "${PYPI_USERNAME}" -p "${PYPI_PASSWORD}" --repository-url "${repository_url}" dist/*

    cd "${stored_dir}"
}

pkg_release ./src
