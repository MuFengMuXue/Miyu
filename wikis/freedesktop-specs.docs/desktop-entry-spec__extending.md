## 12 Extending the format

If the standard is to be amended with a new `{key,value}` pair which should be applicable to all supporting parties, a group discussion will take place. This is the preferred method for introducing changes. If one particular party wishes to add a field for personal use, they should prefix the key with the string `X-`*`PRODUCT`*, e.g. `X-NewDesktop-Foo`, following the precedent set by other IETF and RFC standards.

Alternatively, fields can be placed in their own group, where they may then have arbitrary key names. If this is the case, the group should follow the scheme outlined above, i.e. `[X-`*`PRODUCT`*` `*`GROUPNAME`*`]` or something similar. These steps will avoid namespace clashes between different yet similar environments.
