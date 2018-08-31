#!/usr/bin/env bash

set -e

if [[ "${DEBUG}" ]]; then
    set -x
fi

function pkg_build() {
    local dir="${1}"
    local pkg_ver="${2}"
    local codegen_ver='2.3.1'
    local codegen_url="http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/${codegen_ver}/swagger-codegen-cli-${codegen_ver}.jar"
    local codegen_java_ops='-Xmx1024M -DapiTests=false -DmodelTests=false'
    local codegen_user=''
    local maven_ver='3-jdk-7-alpine'

    echo "Building ${pkg_ver} in ${dir} ..."

    if [[ ! "${TRAVIS}" ]]; then
        local codegen_user="-u ${UID}"
    fi

    if [[ ! -f ./codegen.jar ]]; then
        wget -nv "${codegen_url}" -O ./codegen.jar
    fi

    docker run -it --rm \
        -v "${PWD}":/gen \
        -w /gen \
        ${codegen_user} \
        maven:"${maven_ver}" java ${codegen_java_ops} -jar ./codegen.jar generate \
            -i ./swagger.json \
            -l python \
            -o "${dir}" \
            -D packageName=wodby \
            -D packageUrl=https://github.com/wodby/wodby-sdk-python \
            -D packageVersion="${pkg_ver}"

    if [[ "${TRAVIS}" ]]; then
        sudo chown -R ${UID} "${dir}"
    fi

    rm -f "${dir}"/.travis.yml \
        "${dir}"/git_push.sh \
        "${dir}"/.gitignore \
        "${dir}"/tox.ini \
        "${dir}"/test-requirements.txt
}

schema_ver=$(cat ./swagger.json | yq '.info.version' | cut -d '"' -f 2)
schema_ver_pattern='^([0-9]+).([0-9]+)(.([0-9]+))?$'

if [[ ! ${schema_ver} =~ ${schema_ver_pattern} ]]; then
    echo "ERROR: Expected schema version format ${schema_ver_pattern}, got ${schema_ver}" 1>&2
    exit 1
fi

schema_ver_minor="${BASH_REMATCH[1]}.${BASH_REMATCH[2]}"
schema_ver_dev="${schema_ver_minor}.dev${TRAVIS_BUILD_NUMBER:=0}"

if [[ "${TRAVIS}" ]]; then
    pkg_build ./src-master "${schema_ver_dev}"

    if [[ "${TRAVIS_TAG}" ]]; then
        if [[ "${schema_ver}" != "${TRAVIS_TAG}" ]]; then
            echo "ERROR: Schema version (${schema_ver}) mismatch git tag (${TRAVIS_TAG})" 1>&2
            exit 1
        fi

        pkg_build ./src-tag "${schema_ver}"
    fi
else
    pkg_build ./src "${schema_ver}"
fi