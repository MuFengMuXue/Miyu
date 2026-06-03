# Object Lifetimes Validation

The object tracking validation object tracks all Vulkan objects. Object lifetimes are validated
along with issues related to unknown objects and object destruction and cleanup.

All Vulkan dispatchable and non-dispatchable objects are tracked by this module.

This layer validates that:

- only known objects are referenced and destroyed
- lookups are performed only on objects being tracked
- objects are correctly freed/destroyed

Validation will print errors if validation checks are not correctly met and warnings if improper
reference of objects is detected.
