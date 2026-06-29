# Tab completion

Starting with snapd 2.30, commands and aliases packaged in snaps are able to perform tab-completion in the bash shell, and in the future that same mechanism may be enabled in other shells as well.

For this to work, a `completer` key must be specified under the application scope in snap.yaml or snapcraft.yaml, pointing to a bash completion snippet (that would in traditional packaging be dropped in `/usr/share/bash-completion/completions`). With that, `snapd` will create the necessary system setup to run the completer script confined. The completer must be for the full app name (`<snap>.<app>`), without considering aliases.

Two sample snaps that implement this are the `http` and `test-snapd-complexion` (edge) snaps.

Snapcraft has had support for the `completer` attribute of snap apps since version 2.33.

Debugging tab completion of a strict snap can be hard, so we [wrote a guide for it](https://forum.snapcraft.io/t/debugging-tab-completion/4198).

Extending this tab completion mechanism to other shells (zsh for example) is relatively simple. All that is needed is a marshaller of the completion request. See [`complete.sh` in the snapd source](https://github.com/canonical/snapd/blob/master/data/completion/bash/complete.sh) for details.
