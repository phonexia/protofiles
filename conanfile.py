import os

from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout
from conan.tools.files import collect_libs, copy
from conan.tools.scm import Git


class PhonexiaGrpcProtobuf(ConanFile):
    name = "phonexia_grpc_public"
    description = "C++ library for definition of stubs and messages for communicating with phonexia microservices"
    url = "https://github.com/phonexia/protofiles"
    license = "Apache License 2.0"
    settings = "os", "compiler", "build_type", "arch"
    generators = ["CMakeDeps", "CMakeToolchain"]
    exports_sources = ["CmakeLists.txt", "src/**"]
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {
        "shared": False, 
        "fPIC": True,
        "grpc/*:with_libsystemd": False
        }
    package_type = "library"

    def layout(self):
        cmake_layout(self)

    @staticmethod
    def is_tag(git: Git) -> bool:
        try:
            git.run("describe --tags --exact-match")
            return True
        except:
            return False

    def get_latest_tag(self) -> str:
        git = Git(self)
        return git.run("describe --tags --abbrev=0 --always").strip()

    def set_version(self):
        self.version = self.get_latest_tag()
        build_num = os.getenv("CI_PIPELINE_ID")
        if build_num and not self.is_tag(Git(self)):
            self.version = "{}-{}".format(self.version, build_num)

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def requirements(self):
        self.requires("grpc/1.72.0")

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = collect_libs(self)
