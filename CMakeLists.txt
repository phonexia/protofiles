cmake_minimum_required(VERSION 3.4)

project(phonexia_grpc_public)

set(CMAKE_EXPORT_COMPILE_COMMANDS TRUE)
set(PHX_GRPC_BUILD_NUMBER $ENV{CI_PIPELINE_ID})
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

list(APPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/tools/cmake/include")

message(STATUS "Bin dir: ${CMAKE_CURRENT_BINARY_DIR}")

add_subdirectory(src)
