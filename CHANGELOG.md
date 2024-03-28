# Phonexia gRPC application interface

## 1.5.0 (2024-03-27)
### Added
- Interface for `gender identification` in `phonexia.grpc.technologies.gender_identification.v1`

## 1.4.0 (2024-02-29)
### Added
- `ExtractConfig.speech_length` parameter in `phonexia.grpc.technologies.speaker_identification.v1` to specify the maximum speech length from which the voiceprint will be extracted.

## 1.3.0 (2024-02-22)
### Added
- Interface for `speaker diarization` in `phonexia.grpc.technologies.speaker_diarization.v1`

## 1.2.0 (2024-02-19)
### Added
- `Audio.time_range` parameter in `phonexia.grpc.common` to specify `start`/`end` times from/to which to process the audio
- `TranscribeConfig.enable_language_switching` parameter in `phonexia.grpc.technologies.speech_to_text_whisper_enhanced.v1` to turn on automatic language switching approximately every 30 seconds

## 1.1.0 (2024-01-17)
### Added
- Interface for `speech to text whisper enhanced` in `phonexia.grpc.technologies.speech_to_text_whisper_enhanced.v1`

## 1.0.0 (2023-12-12)
### Added
- Common interface for microservices in `phonexia.grpc.common`
- Interface for `licensing` in `phonexia.grpc.common`
- Interface for `health_check` in `phonexia.grpc.common`
- Interface for `voiceprint extraction` and `comparison` in `phonexia.grpc.technologies.speaker_identification.v1`