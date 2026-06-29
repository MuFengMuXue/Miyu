## Introduction

Writing cmd tests is a bit different than writing standard wine tests.

The tests are not written in C, but directly in the form of batch files,
which are processed by wine cmd, then compared line by line to the
associated expected result files.

Currently, we do the equivalent of

`cmd /c test_file.cmd == test_file.cmd.exp`

for each test file.

## Adding tests

- Edit the appropriate test file
- Find the relevant test section (\`--- Testing foo ---\`), or create it
  if necessary.
- Enter the batch code to be processed in the \`.cmd\` file, and the
  expected result in the associated \`.exp\` file.

Note you might have to use some special keywords as explained below.

## Dealing with missing or extra lines

If a test outputs a different number of lines in Wine than on Windows
the actual output will get out of sync with the expected file, causing
all the tests that follow to fail. To avoid that the test environment
treats all lines that start with `---` as resynchronization points. That
is, if it encounters a line starting with `---` in the output, it will
read lines from the expected file until it finds the matching `---`
line, and vice versa.

For this reason all section and subsection headers should start with
three dashes in order to cut short the cascade of failures when this
unexpectedly happens.

Also if you know that Wine is buggy and outputs an extra line (for
instance), you can have it output a `---` line right after that test and
match it with `@todo_wine@---`. This will mark the forced
resynchronization as expected and the tests that follow will not be
impacted. For instance:

| Command        | Windows Output | Wine Output   | Matched by     |
|----------------|----------------|---------------|----------------|
| buggy_command  | result         | result        | result         |
| \<#ffffff\>    | \<#ffffff\>    | error message | @todo_wine@--- |
| echo ---       | ---            | ---           |                |
| echo next test | next test      | next test     | next test      |

## Keywords Handling

Both the .cmd and .exp files can contain some keywords, that are
expanded or treated specially at runtime.

Only `@space@` and `@tab@` are usable in .cmd files.

### Whitespace Characters

These keywords can be used in both the `.cmd` and `.exp` files:

| Keyword   | Substituted by          | Comments                                                                           |
|-----------|-------------------------|------------------------------------------------------------------------------------|
| `@space@` | space character (`' '`) | Should only be used for trailing spaces, where they can be difficult to spot       |
| `@tab@`   | tab character (`'\t'`)  | Should *always* be used instead of regular tab characters, for improved visibility |

### Environment

The following keywords are relevant to the test environment in general:

| Keyword       | Substituted by                              | Examples                         |       |
|---------------|---------------------------------------------|----------------------------------|-------|
| `@drive@`     | initial drive letter                        | `C:\`                            | `Z:`  |
| `@pwd@`       | initial working directory (no trailing `\`) | `C:\Documents and Settings\wine` | `Z:\` |
| `@path@`      | initial path (without drive)                | `\Documents and Settings\wine\`  | `\`   |
| `@shortpath@` | initial path with short names               | `\DOCUME~1\wine\`                | `\`   |

### Test Helpers

The following keywords are not really substituted, but act as
markers/indicators

| Keyword       | Usage                                                                                                                                                                                                                                                   |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `@todo_wine@` | Used at the start of an expected line to indicate a current failure on wine, so the test suite can run successfully. To be removed when the test eventually succeeds.                                                                                   |
| `@or_broken@` | Used to specify broken (invalid) values returned by different windows versions, which shouldn't be emulated by Wine. Test runner ignores the remainder of the line following the first @or_broken@ (keyword included). Can be specified multiple times. |

See the [testing
section](Wine-Developer's-Guide/Writing-Conformance-Tests) of the
[Wine Developer's Guide](Wine-Developer's-Guide) for more information

### Usage Example

`@todo_wine@expected val@space@@or_broken@foo @tab@bar@or_broken@baz`

specifies

- a failure on wine (`@todo_wine@`)
- normal value is `expected val `
- other windows versions can return `foo \tbar`
- still other windows versions can return `baz`

## Remarks / Tips & Tricks

### Error Messages

Don't try to match error messages: they are language/locale specific and
won't work on all (multilingual) windows versions.

e.g. don't use

`echo foo_expr -> foo_val@or_broken@Echo is OFF`

but use

`echo 'foo_expr' -> 'foo_val'@or_broken@''`

instead.

### Temporary Files

If you need temporary batch/data files, don't add them to git, but
create them at runtime, e.g. using `echo foo >>tmpFile`, and delete
them afterwards.

The best way is generally to use names like `foo`, `bar` or `baz`,
or even better a `mkdir foobar & cd foobar` at the start and `cd .. &
rd /s/q foobar` at the end of your test section, if appropriate.

### Processed File

The result file (processed `.cmd` file) and error file are deleted
after usage. If you want to check their contents (e.g. for debugging
tests), you can temporarily comment/delete the lines

```c
DeleteFileA("test.out");
DeleteFileA("test.err");
```

in `programs/cmd/tests/batch.c`.
