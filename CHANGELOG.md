# Phonexia gRPC application interface

## 2.12.0 (2025-02-26)
### Added
- Interface for `KeywordSpotting` in `phonexia.grpc.technologies.keyword_spotting.v1`

## 2.11.0 (2025-01-22)
### Added
- Support for audio processing in `phonexia.grpc.technologies.gender_identification.v1`
### Changed
- `IdentifyResult.score_male` and `IdentifyResult.score_female` are optional in `phonexia.grpc.technologies.gender_identification.v1` 
  (they are not set for empty/short audio or voiceprint created from empty/short audio)

## 2.10.0 (2025-01-20)
### Added
- `Word` message that represents detailed per-word segmentation of segment in `phonexia.grpc.technologies.enhanced_speech_to_text_built_on_whisper.v1`

## 2.9.0 (2025-01-08)
### Added
- Interface for `DeepfakeDetection` in `phonexia.grpc.technologies.deepfake_detection.experimental`

## 2.8.0 (2024-12-09)
### Added
- Interface for `Denoiser` in `phonexia.grpc.technologies.denoiser.v1`

## 2.7.0 (2024-10-23)
### Added
- `Extract` method for languageprint extraction in `phonexia.grpc.technologies.language_identification.v1.LanguageIdentification`
- Languageprint support in `Identify` method in `phonexia.grpc.technologies.language_identification.v1.LanguageIdentification`
- `Adapt` method for adaptation profile creation in `phonexia.grpc.technologies.language_identification.v1.LanguageIdentification`
- Support for using adaptation profile in `Identify` and `ListSupportedLanguages` in `phonexia.grpc.technologies.language_identification.v1.LanguageIdentification`

## 2.6.0 (2024-10-14)
### Added
- Interface for `Emotion Recognition` in `phonexia.grpc.technologies.emotion_recognition.v1`

## 2.5.0 (2024-09-16)
### Added
- `probability` field in `phonexia.grpc.technologies.gender_identification.v1.Score`

## 2.4.0 (2024-09-11)
### Added
- Interface for `Voice Activity Detection` in `phonexia.grpc.technologies.voice_activity_detection.v1`

## 2.3.1 (2024-08-20)
### Changed
- `max_speakers` argument is made optional in `phonexia.grpc.technologies.speaker_diarization.v1.DiarizeConfig` message

## 2.3.0 (2024-07-09)
### Changed
- `score` field to `probability` in `phonexia.grpc.technologies.language_identification.v1.LanguageIdentificationScore`
- `individual_languages` field to `languages` in `phonexia.grpc.technologies.language_identification.v1.LanguageIdentificationScore`
### Added
- `IdentifierType` enum and `identifier_type` field in `phonexia.grpc.technologies.language_identification.v1.LanguageIdentificationScore`
- Support for raw audio streaming using the `raw_audio_config` field in `phonexia.grpc.common.Audio`

## 2.2.0 (2024-06-19)
### Added
- `individual_languages` field in `phonexia.grpc.technologies.language_identification.v1.LanguageIdentificationScore` for languages belonging to a group

## 2.1.0 (2024-05-30)
### Added
- Interface for `language identification` in `phonexia.grpc.technologies.language_identification.v1`

## 2.0.0 (2024-04-25)
### Changed
- Renamed `speech_to_text_whisper_enhanced` to `enhanced_speech_to_text_built_on_whisper`
### Added
- `SpeechToText.Translate` rpc for machine translation
- `SpeechToText.ListSupportedLanguages` now also lists languages for translation

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
