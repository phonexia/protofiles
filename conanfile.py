import os
import re

from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps
from conans.tools import collect_libs, load, Git


class PhonexiaGrpcProtobuf(ConanFile):
    name = "phonexia_grpc_public"
    description = "C++ library for definition of stubs and messages for communicating with phonexia microservices"
    url = "https://github.com/phonexia/protofiles"
    license = "Apache License 2.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = ["CMakeDeps", "CMakeToolchain"]
    exports_sources = ["CmakeLists.txt", "src/**"]
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}

    def set_version(self):
        self.version = get_latest_tag()
        build_num = os.getenv("CI_PIPELINE_ID")
        if build_num and not Git().get_tag():
            self.version = "{}-{}".format(self.version, build_num)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.verbose = True
        cmake.configure()
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def requirements(self):
        self.requires("grpc/1.54.3")

    def package(self):
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = collect_libs(self)


def get_latest_tag() -> str:
    git = Git()
    return git.run("describe --tags --abbrev=0 --always").strip()
