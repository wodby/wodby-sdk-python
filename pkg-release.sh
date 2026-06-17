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

    python setup.py sdist bdist_wheel

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

pkg_release ./src test
