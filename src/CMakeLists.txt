find_package(protobuf CONFIG REQUIRED)
find_package(gRPC CONFIG REQUIRED)

#
# Protobuf/gRPC source files
#
file(GLOB_RECURSE PROTO_FILES
    "phonexia/grpc/*.proto"
)

message("PROTO_FILES = ${PROTO_FILES}")

#
# Add Library target with protobuf sources
#
add_library(phonexia_grpc_public ${PROTO_FILES})
target_link_libraries(
    phonexia_grpc_public PUBLIC protobuf::libprotobuf gRPC::grpc++_unsecure
)

set(PROTO_INCLUDE_DIR "${CMAKE_CURRENT_BINARY_DIR}/generated")
set(PROTO_IMPORT_DIRS "${CMAKE_CURRENT_LIST_DIR}")

file(MAKE_DIRECTORY "${PROTO_INCLUDE_DIR}")

#
# Compile protobuf and grpc files in phonexia_grpc_public target to cpp
#
protobuf_generate(
    TARGET
    phonexia_grpc_public
    OUT_VAR
    PROTO_GENERATED_FILES
    IMPORT_DIRS
    ${PROTO_IMPORT_DIRS}
    PROTOC_OUT_DIR
    "${PROTO_INCLUDE_DIR}"
)
set_source_files_properties(
    ${PROTO_GENERATED_FILES} PROPERTIES SKIP_UNITY_BUILD_INCLUSION on
)
message("PROTO_GENERATED_FILES = ${PROTO_GENERATED_FILES}")

protobuf_generate(
    TARGET
    phonexia_grpc_public
    OUT_VAR
    PROTO_GENERATED_FILES
    LANGUAGE
    grpc
    GENERATE_EXTENSIONS
    .grpc.pb.h
    .grpc.pb.cc
    PLUGIN
    "protoc-gen-grpc=\$<TARGET_FILE:gRPC::grpc_cpp_plugin>"
    # PLUGIN_OPTIONS "generate_mock_code=true"
    IMPORT_DIRS
    ${PROTO_IMPORT_DIRS}
    PROTOC_OUT_DIR
    "${PROTO_INCLUDE_DIR}"
)
set_source_files_properties(
    ${PROTO_GENERATED_FILES} PROPERTIES SKIP_UNITY_BUILD_INCLUSION on
)
message("PROTO_GENERATED_FILES = ${PROTO_GENERATED_FILES}")
message("PROTO_INCLUDE_DIR = ${PROTO_INCLUDE_DIR}")

target_include_directories(
    phonexia_grpc_public PUBLIC "${PROTO_INCLUDE_DIR}"
)
target_sources(
    phonexia_grpc_public
    PUBLIC
    ${PROTO_GENERATED_FILES}
)

install(TARGETS phonexia_grpc_public DESTINATION lib)
install(DIRECTORY ${PROTO_INCLUDE_DIR}/ DESTINATION include FILES_MATCHING PATTERN "*.h")
