Maintained by [Aric Stewart](@aricstewart)

If you find incorrect information here please contact me.

## About Fallback Fonts

Uniscribe will fallback to known good fonts for some scripts. Like the
native Microsoft usp10 Wine's will by default fall back to given fonts.
If you install these fonts on your system or setup font overrides you
will get this immediate benefit. I have also added another way to setup
an override. You can setup registry keys in
\[HKEY_CURRENT_USER\Software\Wine\Uniscribe\Fallback\]. The key will be
the scripts OpenType tag in hex and the value is the font face you want
to use as the fallback for that font.

for example to add a fallback for Arabic you would set
"0x62617261"="<my arabic font>"

Fallback fonts will only be used in programs and areas where the
[ScriptString](https://msdn.microsoft.com/en-us/library/windows/desktop/dd374124%28v=vs.85%29.aspx)
apis are used. Internally, in the near future, this will include the
Edit Control and RichEdit Control.

## Supported Scripts

as of 2011-12-16

| Script                            | Complex? | Default Fallback Font | Fallback registry key | Known Issues / Bugs |
|-----------------------------------|----------|-----------------------|-----------------------|---------------------|
| Latin                             |          | Microsoft Sans Serif  | 0x6e74616c            |                     |
| Numeric                           |          | Microsoft Sans Serif  |                       |                     |
| Control                           |          |                       |                       |                     |
| Punctuation                       |          | Microsoft Sans Serif  |                       |                     |
| Arabic                            | YES      | Microsoft Sans Serif  | 0x62617261            |                     |
| Hebrew                            | YES      | Microsoft Sans Serif  | 0x72626568            |                     |
| Syriac                            | YES      | Estrangelo Edessa     | 0x63727973            |                     |
| Persian                           | YES      | Estrangelo Edessa     | 0x63727973            |                     |
| Thaana                            | YES      | MV Boli               | 0x61616874            |                     |
| Greek                             |          | Microsoft Sans Serif  | 0x6b657267            |                     |
| Cyrillic                          |          | Microsoft Sans Serif  | 0x6c727963            |                     |
| Armenian                          |          | Sylfaen               | 0x6e6d7261            |                     |
| Georgian                          |          | Sylfaen               | 0x726f6567            |                     |
| Sinhala                           | YES      | Iskoola Pota          | 0x686e6973            |                     |
| Tibetan                           | YES      | Microsoft Himalaya    | 0x74626974            |                     |
| Phags_pa                          | YES      | Microsoft PhagsPa     | 0x67616870            |                     |
| Thai                              | YES      | Microsoft Sans Serif  | 0x69616874            |                     |
| Lao                               | YES      | DokChampa             | 0x206f616c            |                     |
| Devanagari                        | YES      | Mangal                | 0x61766564            | #27637              |
| Bengali                           | YES      | Vrinda                | 0x676e6562            | #27637              |
| Gurmukhi                          | YES      | Raavi                 | 0x75727567            | #27637              |
| Gujarati                          | YES      | Shruti                | 0x726a7567            | #27637              |
| Oriya                             | YES      | Kalinga               | 0x6179726f            | #27637              |
| Tamil                             | YES      | Latha                 | 0x6c6d6174            | #27637              |
| Telugu                            | YES      | Gautami               | 0x756c6574            | #27637              |
| Kannada                           | YES      | Tunga                 | 0x61646e6b            | #27637              |
| Malayalam                         | YES      | Kartika               | 0x6d796c6d            | #27637              |
| Diacritical                       |          |                       |                       |                     |
| Latin Punctuation                 |          | Microsoft Sans Serif  | 0x6e74616c            |                     |
| Numeric 2                         |          |                       |                       |                     |
| Myanmar                           | YES      |                       | 0x726d796d            |                     |
| Tai Le                            | YES      | Microsoft Tai Le      | 0x656c6174            |                     |
| New Tai Lue                       | YES      | Microsoft New Tai Lue | 0x756c6174            |                     |
| Khmer                             | YES      | DaunPenh              | 0x726d686b            |                     |
| CJK Unified Ideographs            |          |                       | 0x696e6168            |                     |
| Ideographic Description           |          |                       | 0x696e6168            |                     |
| Bopomofo                          |          |                       | 0x6f706f62            |                     |
| Kana                              |          |                       | 0x616e616b            |                     |
| Hangul                            | YES      |                       | 0x676e6168            |                     |
| Yi                                |          | Microsoft Yi Baiti    | 0x20206979            |                     |
| Ethiopic                          | YES      | Nyala                 | 0x69687465            |                     |
| Mongolian                         | YES      | Mongolian Baiti       | 0x676e6f6d            |                     |
| Tifinagh                          | YES      | Ebrima                | 0x676e6674            |                     |
| N’Ko                              | YES      | Ebrima                | 0x206f6b6e            |                     |
| Vai                               | YES      | Ebrima                | 0x20696176            |                     |
| Cherokee                          | YES      | Plantagenet Cherokee  | 0x72656863            |                     |
| Canadian Aboriginal Syllabics     | YES      | Euphemia              | 0x736e6163            |                     |
| Ogham                             | YES      | Segoe UI Symbol       | 0x6d61676f            |                     |
| Runic                             | YES      | Segoe UI Symbol       | 0x726e7572            |                     |
| Braille                           | YES      | Segoe UI Symbol       | 0x69617262            |                     |
| Surrogates Area                   |          |                       |                       |                     |
| Private-Use                       |          |                       |                       |                     |
| Deseret                           | YES      | Segoe UI Symbol       | 0x74727364            |                     |
| Osmanya                           | YES      | Ebrima                | 0x616d736f            |                     |
| Mathematical Alphanumeric Symbols | YES      | Cambria Math          | 0x6874616d            |                     |

## General Issues and Further Development

as of 2011-11-10

Uniscribe is used in the following areas within Wine:

- ExtTextOut: This partial support should allow Complex scripts to be
  displayed correctly in most Static controls, Menus and the like.
- Edit Control: as of version 1.3.32 the Wine edit controls is fully
  uniscribe based. This allows for the correct display and editing of
  complex scripts as well as the use of fallback fonts.

Other than the Dozens of random bugs and unimplemented features here are
specific issues that need to be kept in mind or worked on.

- Currently there is no specific support for GPOS tables. Relying
  completely on GDI/FreeType to process that.
- The RichEdit control should use the
  [ScriptString](https://msdn.microsoft.com/en-us/library/windows/desktop/dd374124%28v=vs.85%29.aspx)
  functions
- Wine's fallback to uniscribe in ExtTextOut is a bit hacky and only
  happens for BiDi strings and Indic ranges.
- most flags in the
  [SCRIPT_PROPERTIES](https://msdn.microsoft.com/en-us/library/windows/desktop/dd374042%28v=VS.85%29.aspx),
  [SCRIPT_ANALYSIS](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368797%28v=VS.85%29.aspx)
  and
  [SCRIPT_STATE](https://msdn.microsoft.com/en-us/library/windows/desktop/dd374043%28v=VS.85%29.aspx)
  structures are ignored.
