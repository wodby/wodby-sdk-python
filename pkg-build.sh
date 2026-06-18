#!/usr/bin/env bash

set -e

if [[ "${DEBUG}" ]]; then
    set -x
fi

function pkg_build() {
    local dir="${1}"
    local pkg_ver="${2}"
    local generator_ver='v7.10.0'
    local generator_image="openapitools/openapi-generator-cli:${generator_ver}"
    local codegen_user=''

    echo "Building ${pkg_ver} in ${dir} ..."

    local codegen_user="-u ${UID}"

    docker run --rm \
        -v "${PWD}":/gen \
        -w /gen \
        ${codegen_user} \
        "${generator_image}" generate \
            -i ./swagger.json \
            -g python \
            -o "${dir}" \
            --additional-properties=packageName=wodby,packageUrl=https://github.com/wodby/wodby-sdk-python,packageVersion="${pkg_ver}"

    rm -f "${dir}"/.travis.yml \
        "${dir}"/git_push.sh \
        "${dir}"/.gitignore \
        "${dir}"/.gitlab-ci.yml \
        "${dir}"/tox.ini \
        "${dir}"/test-requirements.txt
    rm -rf "${dir}"/.github

    cp ./patches/*.patch ./"${dir}"/
    ( cd "${dir}" && patch < ./setup.py.patch )
    rm -f "${dir}"/*.patch
    rm -f "${dir}"/setup.py.orig

    cat > "${dir}"/requirements.txt <<'EOF'
urllib3 >= 2.7.0, < 3.0.0
python-dateutil >= 2.9.0.post0
pydantic >= 2.13.4
typing-extensions >= 4.15.0
EOF

    perl -0pi -e '
        s/urllib3 >= 1\.25\.3, < 3\.0\.0/urllib3 >= 2.7.0, < 3.0.0/g;
        s/python-dateutil >= 2\.8\.2/python-dateutil >= 2.9.0.post0/g;
        s/pydantic >= 2(?![.\d])/pydantic >= 2.13.4/g;
        s/typing-extensions >= 4\.7\.1/typing-extensions >= 4.15.0/g;
        s/urllib3 = ">= 1\.25\.3 < 3\.0\.0"/urllib3 = ">= 2.7.0 < 3.0.0"/g;
        s/python-dateutil = ">= 2\.8\.2"/python-dateutil = ">= 2.9.0.post0"/g;
        s/pydantic = ">= 2"/pydantic = ">= 2.13.4"/g;
        s/typing-extensions = ">= 4\.7\.1"/typing-extensions = ">= 4.15.0"/g;
        s/^description = ".*?"/description = "Python SDK for the Wodby 2.0 Public API"/mg;
        s#^repository = ".*?"#repository = "https://github.com/wodby/wodby-sdk-python"#mg;
        s/^keywords = \[.*?\]/keywords = ["wodby", "sdk", "api", "cloud", "python"]/mg;
        s/^    description=".*?"/    description="Python SDK for the Wodby 2.0 Public API"/mg;
        s/^    keywords=\[.*?\]/    keywords=["wodby", "sdk", "api", "cloud", "python"]/mg;
    ' "${dir}"/setup.py "${dir}"/pyproject.toml
}

schema_ver="${PKG_VERSION:-$(python3 -c 'import json; print(json.load(open("swagger.json"))["info"]["version"])')}"
schema_ver_pattern='^([0-9]+).([0-9]+)(.([0-9]+))?$'

if [[ ! ${schema_ver} =~ ${schema_ver_pattern} ]]; then
    echo "ERROR: Expected schema version format ${schema_ver_pattern}, got ${schema_ver}" 1>&2
    exit 1
fi

schema_ver_minor="${BASH_REMATCH[1]}.${BASH_REMATCH[2]}"

pkg_build ./src "${schema_ver}"
