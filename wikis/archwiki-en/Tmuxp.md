# Tmuxp

tmuxp is a session manager for the tmux terminal multiplexer. Compare to tmuxinator or teamocil.

## Installation
Install the  package.

## Configurations
tmuxp accepts both JSON and YAML configurations. The YAML markup is similar to tmuxinators.

You can put configurations in any directory to access them via 3 ways:

# Via absolute or relative file path ,
# tmuxp checks for files in  (usually ), and  path (default ). Files inside can be loaded via filename, e.g. . So  would be loadable via .
# Via  in a project or directory (so you can store configs in a VCS per-project / folder. And then

A sample YAML configuration with 4 panes:

 session_name: 4-pane-split
 windows:
 - window_name: dev window
   layout: tiled
   shell_command_before:
     - cd ~/                    # run as a first command in all panes
   panes:
     - shell_command:           # pane no. 1
         - cd /var/log          # run multiple commands in this pane
         - ls -al | grep \.log
     - echo second pane         # pane no. 2
     - echo third pane          # pane no. 3
     - echo forth pane          # pane no. 4

tmuxp is also capable of running arbitrary scripts before building tmux sessions via . In this example, from the tmuxp project itself, a bootstrap script runs which creates a virtualenv (python package environment) for the project and installs dependency packages. In addition, the session configures all panes to source the project's virtualenv:

 session_name: tmuxp
 start_directory: ./ # load session relative to config location (project root).
 before_script: ./bootstrap_env.py # ./ to load relative to project root.
 windows:
 - window_name: tmuxp
   focus: True
   layout: main-horizontal
   options:
     main-pane-height: 35
   shell_command_before:
     - '[ -d .venv -a -f .venv/bin/activate ] && source .venv/bin/activate'
   panes:
   - focus: true
   - pane
   - make watch_test
 - window_name: docs
   layout: main-horizontal
   options:
     main-pane-height: 35
   start_directory: doc/
   shell_command_before:
     - '[ -d ../.venv -a -f ../.venv/bin/activate ] && source ../.venv/bin/activate'
   panes:
   - focus: true
   - pane
   - make serve
   - make watch

More examples are available in the documentation showcasing YAML, as well as JSON configurations.
