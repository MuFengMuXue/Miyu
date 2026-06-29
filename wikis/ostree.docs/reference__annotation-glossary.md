|  |  |  |  |  |
|:---|----|----|----|----|
| [A](#glsA)  \|  [E](#glsE)  \|  [N](#glsN)  \|  [O](#glsO)  \|  [S](#glsS)  \|  [T](#glsT)  \|  [U](#glsU) | [](reference__index.md) |  | [](reference__ostree-ostree-version.md) |  |

# Annotation Glossary

### A

allow-none

NULL is OK, both for passing and for returning.

array

Parameter points to an array of items.

### E

element-type

Generics and defining elements of containers and arrays.

### N

not nullable

NULL must not be passed as the value in, out, in-out; or as a return value.

nullable

NULL may be passed as the value in, out, in-out; or as a return value.

### O

optional

NULL may be passed instead of a pointer to a location.

out

Parameter for returning results. Default is transfer full.

out caller-allocates

Out parameter, where caller must allocate storage.

### S

skip

Exposed in C code, not necessarily available in other languages.

### T

transfer container

The caller owns the data container, but not the data inside it.

transfer floating

Alias for transfer none, used for objects with floating refs.

transfer full

The caller owns the data, and is responsible for free it.

transfer none

The data is owned by the callee, which is responsible of freeing it.

type

Override the parsed C type with given type.

### U

Unstable

Unstable interfaces are experimental or transitional. They are typically used to give outside developers early access to new or rapidly changing technology, or to provide an interim solution to a problem where a more general solution is anticipated. No claims are made about either source or binary compatibility from one minor release to the next. The Unstable interface level is a warning that these interfaces are subject to change without warning and should not be used in unbundled products. Given such caveats, customer impact need not be a factor when considering incompatible changes to an Unstable interface in a major or minor release. Nonetheless, when such changes are introduced, the changes should still be mentioned in the release notes for the affected release.
