name = "3dequalizer"

version = "4.5.0"

authors = [
    "Science-D-Visions"
]

description = \
    """
    3DEqualizer is by no doubt the world's best 3D tracking solution for merging live action footage with digital
    visual effects. It represents a cornerstone of modern post production business and is used by virtually all of
    the major players around the globe who are working in this field.
    """

requires = [
    "cmake-3+",
    "license_manager"
]

variants = [
    ["platform-linux"]
]

tools = [
    "3DE4",
    "flcd4",
    "flcinfo4",
    "makeBCFile",
    "tde4mhpd",
    "warp4"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "3dequalizer-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.TDE4_ROOT.set("{root}")

    # We setup the license server.
    if "EQUALIZER_LICENSE_SERVER" in env.keys():
        env.LICENCE_SERVER_3DE4.set(str(env.EQUALIZER_LICENSE_SERVER))

    # Helper environment variables.
    env.EQUALIZER_BINARY_PATH.set("{root}/bin")

