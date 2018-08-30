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

if [[ ! "${TRAVIS}" ]]; then
    while true; do
        read -p 'Do you wish to proceed with non-travis environment (Python packages will be installed)? ' yn
        case ${yn} in
            [Yy]* ) break;;
            [Nn]* ) exit;;
            * ) echo "Please answer yes or no.";;
        esac
    done
fi

cp tests/test.py "${dir}"/
cd "${dir}"
pip install -r ./requirements.txt
python ./test.py