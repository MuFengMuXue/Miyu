# Font configuration/Examples/No anti-aliasing

The following is a comprehensive fontconfig for turning off anti-aliasing under certain conditions.

Most contemporary fonts are not very readable when anti-aliasing is turned off. Hence, the following fontconfig disables anti-aliasing only for certain fonts — mostly  Microsoft fonts — that are designed to look well without anti-aliasing.

It also re-enable anti-aliasing above a certain size.

Finally, it sets preferred fonts that look well without anti-aliasing. This is useful for web browsing, as many websites specify font family names such as "serif", "sans-serif", and "monospace". In these situations fontconfig will choose nice fonts without anti-aliasing.
