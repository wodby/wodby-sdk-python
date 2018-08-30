#!/usr/bin/env bash

set -e

if [[ "${DEBUG}" ]]; then
    set -x
fi

function pkg_test() {
    local dir="${1}"

    echo "Testing ${dir} ..."

    cp ./tests/test.py "${dir}"/
    cd "${dir}"

    if [[ "${TRAVIS}" ]]; then
        pip install -r ./requirements.txt
    fi

    python test.py
    rm -f test.py
}

if [[ "${TRAVIS}" ]]; then
    pkg_test ./src-master

    if [[ "${TRAVIS_TAG}" ]]; then
        pkg_test ./src-tag
    fi
else
    pkg_test ./src
fi