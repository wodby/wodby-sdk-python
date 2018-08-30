#!/usr/bin/env bash

set -e

if [[ "${DEBUG}" ]]; then
    set -x
fi

function pkg_codegen() {
    local out="${1}"
    local pkg_ver="${2}"

    if [[ ! -f ./codegen.jar ]]; then
        wget -nv "${CODEGEN_URL}" -O ./codegen.jar
    fi

    docker run -it --rm \
        -v "${PWD}":/gen \
        -w /gen \
        ${CODEGEN_USER} \
        maven:"${CODEGEN_MAVEN_VER}" java ${CODEGEN_JAVA_OPTS} -jar ./codegen.jar generate \
            -i ./swagger.json \
            -l python \
            -o "${out}" \
            -D packageName=wodby \
            -D packageUrl=https://github.com/wodby/wodby-sdk-python \
            -D packageVersion="${pkg_ver}"

    if [[ "${TRAVIS}" ]]; then
        sudo chown -R ${UID} "${out}"
    fi

    rm -f "${out}"/.travis.yml \
        "${out}"/git_push.sh \
        "${out}"/.gitignore \
        "${out}"/tox.ini \
        "${out}"/test-requirements.txt
}

dir="${1}"

if [[ ! "${dir}" ]]; then
    echo "ERROR: Package dir have to be specified" 1>&2
    exit 1
fi

CODEGEN_MAVEN_VER='3-jdk-7-alpine'
CODEGEN_VER=2.3.1
CODEGEN_URL=http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/${CODEGEN_VER}/swagger-codegen-cli-${CODEGEN_VER}.jar
CODEGEN_JAVA_OPTS='-Xmx1024M -DapiTests=false -DmodelTests=false'

if [[ ! "${TRAVIS}" ]]; then
    CODEGEN_USER="-u ${UID}"
fi

if [[ "${TRAVIS}" ]]; then
    if [[ "${TRAVIS_BUILD_NUMBER}" ]]; then
        build="${TRAVIS_BUILD_NUMBER}"
    else
        echo 'ERROR: TRAVIS_BUILD_NUMBER env var have to be defined' 1>&2
        exit 1
    fi
else
    # For local dev and tests.
    build=0
fi

schema_ver=$(cat ./swagger.json | yq '.info.version' | cut -d '"' -f 2)
schema_ver_pattern='^([0-9]+).([0-9]+)(.([0-9]+))?$'

if [[ ! ${schema_ver} =~ ${schema_ver_pattern} ]]; then
    echo "ERROR: Expected schema version format ${schema_ver_pattern}, got ${schema_ver}" 1>&2
    exit 1
fi

schema_ver_minor="${BASH_REMATCH[1]}.${BASH_REMATCH[2]}"
schema_ver_dev="${schema_ver_minor}d${build}"

rm -rf "${dir}"
mkdir -p "${dir}"
pkg_codegen "./src" "${schema_ver_dev}"