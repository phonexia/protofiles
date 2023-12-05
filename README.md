![](https://www.phonexia.com/wp-content/uploads/phonexia-logo-transparent-500px.png)

# Phonexia gRPC protofiles repository

This repository contains defined interfaces for [microservices](https://docs.cloud.phonexia.com/docs/category/technologies) developed by [Phonexia](https://phonexia.com). 

* Maintained by [Phonexia](https://phonexia.com)
* Contact us via [e-mail](mailto:info@phonexia.com), or open a ticket at the [Phonexia Service Desk](https://phonexia.atlassian.net/servicedesk/customer/portal/15/group/20/create/40)
* See the [terms of use](https://www.phonexia.com/terms-and-conditions/)

For communication, Phonexia microservices use the [gRPC](https://grpc.io/) API, which is a high-performance, open-source Remote Procedure Call (`RPC`) framework that enables efficient communication between distributed systems using a variety of programming languages. When using `RPC`, we use an Interface Definition Language (`IDL`) to specify a common interface and contracts between components. We can specify methods with return types and arguments.

For the definition of microservice interfaces, we use the standard way of [protocol buffers](https://protobuf.dev/overview/). The `services`, together with the `procedures` and `messages` that they expose, are defined in the so-called `proto` files. In the `src/phonexia/grpc/technologies/` directory, you can find a subdirectory with `.proto` files for each microservice that Phonexia offers. Additionally, common interfaces for the API like *health_check* and *licensing* can be found in `src/phonexia/grpc/common/`.

The automatically generated *gRPC API* documentation can be found [here](https://docs.cloud.phonexia.com/docs/grpc/phonexia/grpc/technologies).

## Versioning

It is our high priority to not introduce breaking changes to the API. In practice this means that adding new features to our microservices or modifying existing ones will not result in deletion or modification of the existing API. Adding a feature is reflected by adding messages or procedures to the API, which does not break the existing API. Theoretically, newer versions of the `gRPC` library can be used with older versions of our microservices, as long as only the supported subset of features is used. Vice versa, older versions of the `gRPC` library can be used with newer versions of the microservices.

If a breaking change of the API would have to be made, a completely new version of the microservice API would be released instead. Generally, this should only happen with a new generation of the respective speech technology. For example, let's assume the current API for the Speaker Identification microservice can be found in "src/phonexia/grpc/technologies/speaker_identification/**v1**/". If a new generation of the Speaker Identification technology is introduced in the future, a new API will be found in "src/phonexia/grpc/technologies/speaker_identification/**v2**/".

This allows our customers to integrate the API with a clear visibility of future support for new versions.

# Generating the library

The `.proto` files can be used to generate client libraries in many programming languages. Take a look at [protobuf tutorials](https://protobuf.dev/getting-started/) for how to get started with generating the library in the languages of your choice using the `protoc` tool.

## Python package

If you use *Python* as your programming language, you can use our official [gRPC Python package](https://pypi.org/project/phonexia-grpc).

To install the package using `pip`, run:

```bash
pip install phonexia-grpc
```

You can then import:

- specific libraries for each microservice that provide the message wrappers
- [stubs](https://grpc.io/docs/languages/python/basics/#creating-a-stub) for the `gRPC` clients.

For example, [voiceprint extraction and comparison](https://docs.cloud.phonexia.com/docs/common/technologies/speaker-identification) libraries can be imported using the following lines of code:

```python
# phx_core contains classes common for multiple microservices like `Audio` or `Voiceprint`.
import phonexia.grpc.common.core_pb2 as phx_core
# speaker_identification_pb2 contains the request and response classes like `ExtractRequest` or `ExtractResponse`.
import phonexia.grpc.technologies.speaker_identification.v1.speaker_identification_pb2 as sid
# speaker_identification_pb2_grpc contains the stubs like `VoiceprintExtractionStub` needed to make the request.
import phonexia.grpc.technologies.speaker_identification.v1.speaker_identification_pb2_grpc as sid_grpc
```
