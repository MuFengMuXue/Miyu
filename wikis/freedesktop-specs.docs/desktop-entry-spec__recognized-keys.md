## 6 Recognized desktop entry keys

Keys are either OPTIONAL or REQUIRED. If a key is OPTIONAL it may or may not be present in the file. However, if it isn't, the implementation of the standard should not blow up, it must provide some sane defaults.

Some keys only make sense in the context when another particular key is also present and set to a specific value. Those keys should not be used if the particular key is not present or not set to the specific value. For example, the `Terminal` key can only be used when the value of the `Type` key is `Application`.

If a REQUIRED key is only valid in the context of another key set to a specific value, then it has to be present only if the other key is set to the specific value. For example, the `URL` key has to be present when and only when when the value of the `Type` key is `Link`.

Some example keys: `Name[C]`, `Comment[it]`.

###### Table 2: Standard Keys

[TABLE]
