[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Taskwarrior&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://taskwarrior.org/)

[[]][Official documentation](https://taskwarrior.org/docs/)

[[]][Package information](https://packages.gentoo.org/packages/app-misc/task)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Taskwarrior "wikipedia:Taskwarrior")

[[]][GitHub](https://github.com/GothenburgBitFactory/taskwarrior)

[[]][[#taskwarrior](ircs://irc.libera.chat/#taskwarrior)] ([[webchat](https://web.libera.chat/#taskwarrior)])

[[]][Blog](https://taskwarrior.org/news/)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/taskwarrior)

**Taskwarrior** (**[task]**) is a to-do list manager for the command line written in [C++](https://wiki.gentoo.org/wiki/C%2B%2B "C++"). It uses a simple human readable text file format to store to-do list items and associated metadata. Taskwarrior isn\'t tied to a specific school of thought on task organization. It\'s designed to be simple yet flexible and scalable. As such, Taskwarrior has a syntax that is simple and intuitive.

Notable features include:

-   Data is stored locally in [JSON](https://en.wikipedia.org/wiki/JSON "wikipedia:JSON") files, easing migration to and from Taskwarror.
-   Interactions can be scripted via Taskwarrior\'s Hooks API.
-   Multiple UI options are available as part of the Taskwarrior ecosystem.
-   When paired with [[[app-misc/taskd]](https://packages.gentoo.org/packages/app-misc/taskd)[]], tasks can be shared with multiple remote client applications.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Environment variables]](#Environment_variables)
    -   [[2.2] [Files]](#Files)
    -   [[2.3] [Service]](#Service)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
-   [[4] [Tips]](#Tips)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Taskwarrior is not respecting the XDG Base Directory Specification]](#Taskwarrior_is_not_respecting_the_XDG_Base_Directory_Specification)
-   [[6] [Removal]](#Removal)
    -   [[6.1] [Unmerge]](#Unmerge)
-   [[7] [See Also]](#See_Also)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask app-misc/task`

## [Configuration]

### [Environment variables]

-   `$TASKRC` allows the user to relocate the [.taskrc] configuration file to a desired directory.
-   `$TASKDATA` allows the user to relocate the [.task] data file to a desired directory.

Modifying these variables is **not** required to enforce XDG Base Directory Support. If you\'ve installed task warrior and it\'s ignoring you XDG preferences see the troubleshooting section.

### [Files]

-   [\~/.config/task/taskrc] --- XDG local (per user) configuration file.
-   [\~/.local/share/task/\*] --- XDG task list directory with tasks spread across multiple files.
-   [\~/.taskrc] --- legacy local (per user) configuration file.
-   [\~/.task/\*] --- legacy local (per user) task list directory with tasks spread across multiple files.

### [Service]

By itself, Taskwarrior is a single device application allowing all users on the device to have their own personal tasks lists.

## [Usage]

Basic usage is fairly intuitive, to list your existing to-do items:

`user `[`$`]`task`

    ID Age  Project         Tag       Due      Description                                Urg
    ¯¯ ¯¯¯  ¯¯¯¯¯¯¯¯¯¯¯     ¯¯¯¯¯¯    ¯¯¯¯¯¯   ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
    1  2w   gentoo-wiki               ~1mo     Add basic usage to ledger article          2.6
    2  1w   friends                    5d      Buy sam_ and ris a beer                    1.4
    3  3d   home                               Clean out the garage.                      0.2

To add a new task, simply type [task add \<task description\>] setting a due date and a project are optional but common for task organization purposes. Due dates do not necessarily require exact numeric dates. Taskwarrior has several human readable aliases such as `eom` for \"end of month\" and days of the week from which Taskwarrior can work out the date.

`user `[`$`]`task add Pay the utility bills due:eom project:home`

To complete a task you need to reference its task number:

`user `[`$`]`task 1 done`

Task completion and task deletion aren\'t the same thing. In the former case, the task is moved a \"completed\" state but a record of it remains. If a task is deleted it is removed from the database. To delete an erroneously created task:

`user `[`$`]`task 3 del`

To generate a simple report for all tasks associated with a specific project [task project:\ list]. So, if you have an existing project called `home` and you want a list of all the associated tasks the command and its output should look something like this:

`user `[`$`]`task project:home list`

    ID Age  Project     Tag       Due          Description                                Urg
    ¯¯ ¯¯¯  ¯¯¯¯¯¯¯¯¯¯¯ ¯¯¯¯¯¯    ¯¯¯¯¯¯¯¯¯¯   ¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯
    3  3d   home                               Clean out the garage                       0.2
    4  1h   home                  2023-04-30   Pay the utility bills                      0.1

Taskwarrior has many features burred below the surface. Numerous potential workflows are supported. The official Taskwarrior documentation is full of detail rich examples on how to get the most out of it.

### [Invocation]

`user `[`$`]`task help`

    Usage: task                                Runs rc.default.command, if
                                               specified.
           task <filter> active                Active tasks
           task          add <mods>            Adds a new task
           task <filter> all                   All tasks
           task <filter> annotate <mods>       Adds an annotation to an existing
                                               task
           task <filter> append <mods>         Appends text to an existing task
                                               description
           task <filter> blocked               Blocked tasks
           task <filter> blocking              Blocking tasks
           task <filter> burndown.daily        Shows a graphical burndown chart, by
                                               day
           task <filter> burndown.monthly      Shows a graphical burndown chart, by
                                               month
           task <filter> burndown.weekly       Shows a graphical burndown chart, by
                                               week
           task          calc <expression>     Calculator
           task          calendar [due|<month> Shows a calendar, with due tasks
           <year>|<year>] [y]                  marked
           task          colors [sample |      All colors, a sample, or a legend
           legend]
           task          columns [substring]   All supported columns and formatting
                                               styles
           task          commands              Generates a list of all commands,
                                               with behavior details
           task <filter> completed             Completed tasks
           task          config [name [value | Change settings in the task
           '']]                                configuration
           task          context [<name> |     Set and define contexts (default
           <subcommand>]                       filters / modifications)
           task <filter> count                 Counts matching tasks
           task <filter> delete <mods>         Deletes the specified task
           task <filter> denotate     Deletes an annotation
           task          diagnostics           Platform, build and environment
                                               details
           task <filter> done <mods>           Marks the specified task as completed
           task <filter> duplicate <mods>      Duplicates the specified tasks
           task <filter> edit                  Launches an editor to modify a task
                                               directly
           task          execute <external     Executes external commands and
           command>                            scripts
           task <filter> export [<report>]     Exports tasks in JSON format
           task <filter> ghistory.annual       Shows a graphical report of task
                                               history, by year
           task <filter> ghistory.daily        Shows a graphical report of task
                                               history, by day
           task <filter> ghistory.monthly      Shows a graphical report of task
                                               history, by month
           task <filter> ghistory.weekly       Shows a graphical report of task
                                               history, by week
           task          help ['usage']        Displays this usage help text
           task <filter> history.annual        Shows a report of task history, by
                                               year
           task <filter> history.daily         Shows a report of task history, by
                                               day
           task <filter> history.monthly       Shows a report of task history, by
                                               month
           task <filter> history.weekly        Shows a report of task history, by
                                               week
           task <filter> ids                   Shows the IDs of matching tasks, as a
                                               range
           task          import [<file> ...]   Imports JSON files
           task <filter> information           Shows all data and metadata
           task <filter> list                  Most details of tasks
           task          log <mods>            Adds a new task that is already
                                               completed
           task          logo                  Displays the Taskwarrior logo
           task <filter> long                  All details of tasks
           task <filter> ls                    Few details of tasks
           task <filter> minimal               Minimal details of tasks
           task <filter> modify <mods>         Modifies the existing task with
                                               provided arguments.
           task <filter> newest                Newest tasks
           task          news                  Displays news about the recent
                                               releases
           task <filter> next                  Most urgent tasks
           task <filter> oldest                Oldest tasks
           task <filter> overdue               Overdue tasks
           task <filter> prepend <mods>        Prepends text to an existing task
                                               description
           task <filter> projects              Shows all project names used
           task <filter> purge                 Removes the specified tasks from the
                                               data files. Causes permanent loss of
                                               data.
           task <filter> ready                 Most urgent actionable tasks
           task <filter> recurring             Recurring Tasks
           task          reports               Lists all supported reports
           task          show [all |           Shows all configuration variables or
           substring]                          subset
           task <filter> start <mods>          Marks specified task as started
           task <filter> stats                 Shows task database statistics
           task <filter> stop <mods>           Removes the 'start' time from a task
           task <filter> summary               Shows a report of task status by
                                               project
           task          synchronize           Synchronizes data with the Taskserver
           [initialize]
           task <filter> tags                  Shows a list of all tags used
           task [filter] timesheet             Summary of completed and started
                                               tasks
           task          udas                  Shows all the defined UDA details
           task <filter> unblocked             Unblocked tasks
           task          undo                  Reverts the most recent change to a
                                               task
           task <filter> uuids                 Shows the UUIDs of matching tasks, as
                                               a space-separated list
           task          version               Shows the Taskwarrior version number
           task <filter> waiting               Waiting (hidden) tasks
           task          _aliases              Generates a list of all aliases, for
                                               autocompletion purposes
           task          _columns              Displays only a list of supported
                                               columns
           task          _commands             Generates a list of all commands, for
                                               autocompletion purposes
           task          _config               Lists all supported configuration
                                               variables, for completion purposes
           task          _context              Lists all supported contexts, for
                                               completion purposes
           task          _get <DOM> [<DOM>     DOM Accessor
           ...]
           task <filter> _ids                  Shows the IDs of matching tasks, in
                                               the form of a list
           task <filter> _projects             Shows only a list of all project
                                               names used
           task          _show                 Shows all configuration settings in a
                                               machine-readable format
           task <filter> _tags                 Shows only a list of all tags used,
                                               for autocompletion purposes
           task          _udas                 Shows the defined UDAs for completion
                                               purposes
           task <filter> _unique <attribute>   Generates lists of unique attribute
                                               values
           task <filter> _urgency              Displays the urgency measure of a
                                               task
           task <filter> _uuids                Shows the UUIDs of matching tasks, as
                                               a list
           task          _version              Shows only the Taskwarrior version
                                               number
           task          _zshattributes        Generates a list of all attributes,
                                               for zsh autocompletion purposes
           task          _zshcommands          Generates a list of all commands, for
                                               zsh autocompletion purposes
           task <filter> _zshids               Shows the IDs and descriptions of
                                               matching tasks
           task <filter> _zshuuids             Shows the UUIDs and descriptions of
                                               matching tasks

           burndown                            Aliased to 'burndown.weekly'
           ghistory                            Aliased to 'ghistory.monthly'
           history                             Aliased to 'history.monthly'
           rm                                  Aliased to 'delete'

    Documentation for Taskwarrior can be found using 'man task', 'man taskrc', 'man task-color', 'man task-sync' or at https://taskwarrior.org

    The general form of commands is:
      task [<filter>] <command> [<mods>]

    The <filter> consists of zero or more restrictions on which tasks to select, such as:
      task                                      <command> <mods>
      task 28                                   <command> <mods>
      task +weekend                             <command> <mods>
      task project:Home due.before:today        <command> <mods>
      task ebeeab00-ccf8-464b-8b58-f7f2d606edfb <command> <mods>

    By default, filter elements are combined with an implicit 'and' operator, but 'or' and 'xor' may also be used, provided parentheses are included:
      task '(/[Cc]at|[Dd]og/ or /[0-9]+/)'      <command> <mods>

    A filter may target specific tasks using ID or UUID numbers.  To specify multiple tasks use one of these forms:
      task 1,2,3                                    delete
      task 1-3                                      info
      task 1,2-5,19                                 modify pri:H
      task 4-7 ebeeab00-ccf8-464b-8b58-f7f2d606edfb info

    The <mods> consist of zero or more changes to apply to the selected tasks, such as:
      task <filter> <command> project:Home
      task <filter> <command> +weekend +garden due:tomorrow
      task <filter> <command> Description/annotation text
      task <filter> <command> /from/to/     <- replace first match
      task <filter> <command> /from/to/g    <- replace all matches

    Tags are arbitrary words, any quantity:
      +tag       The + means add the tag
      -tag       The - means remove the tag

    Built-in attributes are:
      description:    Task description text
      status:         Status of task - pending, completed, deleted, waiting
      project:        Project name
      priority:       Priority
      due:            Due date
      recur:          Recurrence frequency
      until:          Expiration date of a task
      limit:          Desired number of rows in report, or 'page'
      wait:           Date until task becomes pending
      entry:          Date task was created
      end:            Date task was completed/deleted
      start:          Date task was started
      scheduled:      Date task is scheduled to start
      modified:       Date task was last modified
      depends:        Other tasks that this task depends upon

    Attribute modifiers make filters more precise.  Supported modifiers are:

      Modifiers         Example            Equivalent           Meaning
      ----------------  -----------------  -------------------  -------------------------
                        due:today          due = today          Fuzzy match
      not               due.not:today      due != today         Fuzzy non-match
      before, below     due.before:today   due < today          Exact date comparison
      after, above      due.after:today    due >= tomorrow      Exact date comparison
      none              project.none:      project == ''        Empty
      any               project.any:       project !== ''       Not empty
      is, equals        project.is:x       project == x         Exact match
      isnt              project.isnt:x     project !== x        Exact non-match
      has, contains     desc.has:Hello     desc ~ Hello         Pattern match
      hasnt,            desc.hasnt:Hello   desc !~ Hello        Pattern non-match
      startswith, left  desc.left:Hel      desc ~ '^Hel'        Beginning match
      endswith, right   desc.right:llo     desc ~ 'llo$'        End match
      word              desc.word:Hello    desc ~ '\bHello\b'   Boundaried word match
      noword            desc.noword:Hello  desc !~ '\bHello\b'  Boundaried word non-match

    Alternately algebraic expressions support:
      and  or  xor            Logical operators
      <  <=  =  !=  >=  >     Relational operators
      (  )                    Precedence

      task due.before:eom priority.not:L   list
      task '(due < eom and priority != L)'  list

    The default .taskrc file can be overridden with:
      task ... rc:<alternate file> ...
      task ... rc:~/.alt_taskrc ...

    The values in .taskrc (or alternate) can be overridden with:
      task ... rc.<name>=<value> ...
      task rc.color=off list

    Any command or attribute name may be abbreviated if still unique:
      task list project:Home
      task li       pro:Home

    Some task descriptions need to be escaped because of the shell:
      task add "quoted ' quote"
      task add escaped \' quote

    The argument -- tells Taskwarrior to treat all other args as description, even if they would otherwise be attributes or tags:
      task add -- project:Home needs scheduling

    Many characters have special meaning to the shell, including:
      $ ! ' " ( ) ; \ ` * ?  [ ] < > | & % # ~

## [Tips]

This sections lists useful command that may not be obvious to find:

-   List completed tasks for a project:

    :::: cmd-box


    `user `[`$`]`task completed project:test`


    ::::
-   Replace a description with spaces:

    :::: cmd-box


    `user `[`$`]`task 145 mod "/A Test/Not a test/"`


    ::::
-   Time tracking can be done with timewarrior, see [here for setting it up with taskwarrior](https://timewarrior.net/docs/taskwarrior/)

## [Troubleshooting]

### [Taskwarrior is not respecting the XDG Base Directory Specification]

Taskwarrior defaults to [\~/.taskrc]. If [\~/.taskrc] is missing but [\~./config/task/taskrc] is present, the latter will be used. If both files are present, [\~/.taskrc] takes precedence. Thus, the file should first be moved, not just copied:

`user `[`$`]`mkdir ~/.config/task/`

`user `[`$`]`mv ~/.taskrc ~/.config/task/taskrc`

## [Removal]

### [Unmerge]

`root `[`#`]`emerge --ask --depclean --verbose app-misc/task`

## [See Also]

-   [Timewarrior](https://wiki.gentoo.org/wiki/Timewarrior "Timewarrior") --- a time management tool for the terminal.
-   [Visual Interactive Taskwarrior](https://wiki.gentoo.org/wiki/Visual_Interactive_Taskwarrior "Visual Interactive Taskwarrior") --- curses-based front-end for [Taskwarrior] with [vim](https://wiki.gentoo.org/wiki/Vim "Vim")-like keybindings.