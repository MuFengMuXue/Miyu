# pkaction(1)

## Name
pkaction — Get details about a registered action

## Synopsis
```
pkaction --version --help
pkaction --verbose
pkaction --action-id action --verbose
```

## DESCRIPTION

`pkaction` is used to obtain information about registered polkit actions. If called without `--action-id` then all actions are displayed. Otherwise the action \<action\>. If called without the `--verbose` option only the name of the action is shown. Otherwise details about the actions are shown.

## RETURN VALUE

On success `pkaction` returns 0. Otherwise a non-zero value is returned and a diagnostic message is printed on standard error.

## SEE ALSO

[`polkit(8)`](#polkit.8), [`polkitd(8)`](#polkitd.8), [`pkcheck(1)`](#pkcheck.1), [`pkexec(1)`](#pkexec.1), [`pkttyagent(1)`](#pkttyagent.1)
