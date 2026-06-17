#!/usr/bin/env bash

set -e

if [[ "${DEBUG}" ]]; then
    set -x
fi

function pkg_test() {
    local dir="${1}"
    local stored_dir=$(pwd)

    cp ./tests/test.py "${dir}"/
    cd "${dir}"

    python test.py
    rm -f test.py

    cd "${stored_dir}"
}

pkg_test ./src
