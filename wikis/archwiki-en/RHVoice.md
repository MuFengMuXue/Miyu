# RHVoice

RHVoice is a multilingual speech synthesizer. It uses statistical parametric synthesis and relies on existing open-source speech technologies (mainly HTS and related software).

## Installation
Install the  package. Also install necessary #Languages and #Voices.

## Languages
Initially, RHVoice could speak only Russian. But now it supports many other languages.

Available languages list you can get by command:

 $ pacman -Ss rhvoice-lang

{| class="wikitable"
|-
! Package name !! Language
|-
|  || Albanian
|-
|  || Portuguese
|-
|  || English
|-
|  || Esperanto
|-
|  || Georgian
|-
|  || Kyrgyz
|-
|  || Macedonian
|-
|  || Polish
|-
|  || Russian
|-
|  || Tatar
|-
|  || Ukrainian
|}

## Voices
Voices are built from recordings of natural speech. They have small footprints, because only statistical models are stored on users' computers. And though the voices lack the naturalness of the synthesizers which generate speech by combining segments of the recordings themselves, they are still very intelligible and resemble the speakers who recorded the source material.

Available voices list you can get by command:

 $ pacman -Ss rhvoice-voice

{| class="wikitable"
|-
! Package name !! Language !! Note
|-
| style="white-space:nowrap" |  || Albanian ||
|-
| style="white-space:nowrap" |  || Portuguese ||
|-
| style="white-space:nowrap" |
| rowspan=6 | English || Scottish English
|-
| style="white-space:nowrap" |  ||
|-
| style="white-space:nowrap" |  ||
|-
| style="white-space:nowrap" |  || Evgeniy Chebatkov (StandUp comedian, voice actor)
|-
| style="white-space:nowrap" |  || Lyubov Sablina (teacher at the language center "Lingua Belle")
|-
| style="white-space:nowrap" |  ||
|-
| style="white-space:nowrap" |  || Esperanto ||
|-
| style="white-space:nowrap" |  || Georgian ||
|-
| style="white-space:nowrap" |
| rowspan=2 | Kyrgyz ||
|-
| style="white-space:nowrap" |  ||
|-
| style="white-space:nowrap" |
| rowspan=2 | Macedonian || Developed by LouderPages
|-
| style="white-space:nowrap" |  || Developed by Branislav Gerazov
|-
| style="white-space:nowrap" |
| rowspan=2 | Polish ||
|-
| style="white-space:nowrap" |  ||
|-
| style="white-space:nowrap" |
| rowspan=14 | Russian
| rowspan=2 | Aleksandr Karlov (TV and radio host, audiobook reader).The current version of the HQ voice has a higher quality than the previous version, their sound is different, so the new version is temporarily separated into a separate voice to collect feedback. This version may contain issues that are not present in the original voice. Since the speech base is open, we will be happy for your participation in improving the voice.
|-
| style="white-space:nowrap" |
|-
| style="white-space:nowrap" |  ||
|-
| style="white-space:nowrap" |  || Arina Syukkya (event organizer, designer)
|-
| style="white-space:nowrap" |  || Artemiy Lebedev (designer, blogger, traveler)
|-
| style="white-space:nowrap" |  ||
|-
| style="white-space:nowrap" |  || Evgeniy Chebatkov (StandUp comedian, voice actor)
|-
| style="white-space:nowrap" |  ||
|-
| style="white-space:nowrap" |  || Mikhail Sokolov (news anchor on Autoradio)
|-
| style="white-space:nowrap" |  || Pavel Klyachenko (psychologist, tiflopsychologist)
|-
| style="white-space:nowrap" |  || Tatiana Kruk (host of broadcasts on «Tiflo Info»)
|-
| style="white-space:nowrap" |  || Natalya Arsenyeva (radio host and author of the travel blog "I was there")
|-
| style="white-space:nowrap" |  || Vitaliy Chuvaev (brand voice of Russia Today TV channel)
|-
| style="white-space:nowrap" |  || Yuriy Zaborovsky (Soviet and Russian actor, audiobook reader)
|-
| style="white-space:nowrap" |  || Tatar
|-
| style="white-space:nowrap" |
| rowspan=4 | Ukrainian ||
|-
| style="white-space:nowrap" |  || Marianna Firtka (radio presenter)
|-
| style="white-space:nowrap" |  ||
|-
| style="white-space:nowrap" |  || Volodymyr Beglov (journalist, radio host, lecturer)
|}

## Synthesis example
You can listen to examples of speech synthesis for different voices here and here.

## Configuration
Configuration file located at: .

File format and available settings are detail described in official documentation.

## Speech-dispatcher
RHVoice includes module for .

Everything should work out of the box without additional settings. But if you want to set RHVoice as the default synthesizer for speech-dispatcher, use the  utility or change the configuration file manually (if you want to change per-user configuration, edit  instead):

## Usage
If configuration you made is correct, the following commands will allow you to start the synthesis (for voice ):

 $ echo "test" | RHVoice-test -p "bdl"
 $ spd-say -o rhvoice -y bdl "test"

## Dictionaries
User dictionaries must be created in the  directory, for example, for the English language: .
