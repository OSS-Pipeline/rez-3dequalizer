CMAKE_MINIMUM_REQUIRED(VERSION 3.0)

include(RezBuild)
include(RezRepository)
include(ExternalProject)

# We split the 3DEqualizer version string in multiple ones.
string(REPLACE "." ";" 3DEQUALIZER_VERSION_LIST ${REZ_BUILD_PROJECT_VERSION})
list(GET 3DEQUALIZER_VERSION_LIST 0 3DEQUALIZER_VERSION_MAJOR)
list(GET 3DEQUALIZER_VERSION_LIST 1 3DEQUALIZER_VERSION_MINOR)
list(GET 3DEQUALIZER_VERSION_LIST 2 3DEQUALIZER_VERSION_PATCH)

# 3DEqualizer
rez_set_archive(
    # This is a relative path from the ${REZ_REPO_PAYLOAD_DIR} environment variable,
    # that is pointing to the root directory where we can find all the archives of the package
    # we can build, using the following hierarchy:
    # "${REZ_REPO_PAYLOAD_DIR}/project_name/archive.what.ever"
    DELIGHT_URL 3dequalizer/3DE${3DEQUALIZER_VERSION_MAJOR}_linux64_r${3DEQUALIZER_VERSION_MINOR}.tar
    https://www.3dequalizer.com/?site=downloads&id=141205_01
)

configure_file(config/3dequalizer.in config/3dequalizer @ONLY)

# The environment variable REZ_TMP_PATH is meant to point to a location such as "/tmp/rez".
set(EXTRACT_DIR $ENV{REZ_TMP_PATH}/3dequalizer/${REZ_BUILD_PROJECT_VERSION})

# We configure/build/install 3DEqualizer through the ExternalProject_Add macro,
# using three different shell scripts for each of these steps.
# If necessary, it is possible to skip one of these steps by replacing the command
# by "", an empty string.
ExternalProject_Add(
    REZ_3DEQUALIZER
    URL ${DELIGHT_URL}
    PREFIX 3dequalizer
    SOURCE_DIR ${EXTRACT_DIR}
    PATCH_COMMAND ""
    UPDATE_COMMAND ""
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND bash ${CMAKE_SOURCE_DIR}/install.sh ${EXTRACT_DIR}
)

install(PROGRAMS
    ${CMAKE_CURRENT_BINARY_DIR}/config/3dequalizer
    DESTINATION bin
)

# We use a bogus CMake "install" step in order to be able to properly finish
# and get out of the CMake script.
install(
    CODE
    "execute_process(
        COMMAND echo \"\n[CMAKE] 3DEqualizer-${REZ_BUILD_PROJECT_VERSION} PACKAGE SETUP FINISHED!\n\"
    )"
)
