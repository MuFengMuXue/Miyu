# Stateless Parameter Validation

The stateless parameter validation object checks the input parameters to API calls for validity.
This layer performs the following tasks:

- validation of structures; structures are recursed if necessary
- validation of enumerated type values
- null pointer conditions
- stateless valid usage checks
- checks requiring only static state such as properties or limits

The Stateless Validation is run before [Core Validation Checks](core_checks.md). If there is a
validation error found in Stateless Validation, it will return and not call Core Validation nor call down the layer chain.
