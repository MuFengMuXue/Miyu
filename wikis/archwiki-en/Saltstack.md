# Saltstack

From docs.saltproject.io:

:Salt is a new approach to infrastructure management. Easy enough to get running in minutes, scalable enough to manage tens of thousands of servers, and fast enough to communicate with them in seconds.
:Salt delivers a dynamic communication bus for instrastructures that can be used for orchestration, remote execution, configuration management and much more.

## Installation
Install the  package.

## Components of Salt Stack
Salt is at its core a Remote Execution solution. Running pre-defined or arbitrary commands on remote hosts. Salt functions on a master/minion topology. A master server acts as a central control bus for the clients (called minions), and the minions connect back to the master.

## Salt Master
The default configuration is suitable for the vast majority of installations. Start/enable .

The Salt master can also be started in the foreground in debug mode, greatly increasing the command output:

 # salt-master -l debug

The Salt master needs to bind to 2 TCP network ports on the system, these ports are 4505 and 4506.

## Salt Minion
The Salt Minion can operate with or without a Salt Master. This wiki assumes that the minion will be connected to the master. For information on how to run a master-less minion please see the masterless quickstart guide: https://docs.saltproject.io/en/latest/topics/tutorials/quickstart.html

The Salt minion only needs to be aware of one piece of information to run, the network location of the master. By default the minion will look for the DNS name salt for the master, making the easiest approach to set internal DNS to resolve the name salt back to the Salt Master IP. Otherwise the minion configuration file will need to be edited, edit the configuration option master to point to the DNS name or the IP of the Salt Master.

Now that the master can be found, start/enable .

Or to run in debug mode

 # salt-minion -l debug

## Salt Key
Salt authenticates minion using public key encryption and authentication. For a minion to start accepting commands from the master the minion keys need to be accepted. The salt-key command is used to manage all of the keys on the master. To list the keys that are on the master run salt-key list command:

 # salt-key -L

The keys that have been rejected, accepted and pending acceptance are listed. To accept a minion:

 # salt-key -a minion.example.com

Or you can accept all keys at once with :

 # salt-key -A

## Salt Cloud
Salt can also be used to provision cloud servers on most major cloud providers. In order to connect to these providers, additional dependencies may be required.  is required for many popular providers such as Rackspace and Amazon. Further details for configuring your cloud provider can be found at the official wiki: https://docs.saltproject.io/en/latest/topics/cloud/

## Salt commands
After connecting and accepting the minion on the Salt master, you can now send commands to the minion. Salt commands allow for a vast set of functions to be executed and for specific minion and groups of minions to be targeted for execution. This makes the salt command very powerful, but the command is also very usable, and easy to understand.

The salt command is comprised of command options, target specification, the function to execute, and arguments to the function. A simple command to start with looks like this:

 # salt '*' test.ping

The * is the target, which specifies all minions, and test.ping tells the minions to run the test.ping function. This salt command will tell all of the minions to execute the test.ping in parallel and return the result.

For more commands see documentation or run:

 # salt '*' sys.doc

## Salt States
In addition to running commands, salt can use what are known as states. A state is like a configuration file that allows setting up a new installation in the exact same way. A state can also be ran on that install after several weeks to make sure the computer is still in a known configuration.

## Salt Environments
States can be separated into different environments. These environments can be used for making changes in a test environment before moving to a production machine, configuring a group of servers the same way, etc. The base environment is  by default, and sometimes  must be manually created.

Different environments can be set up in the salt-master file. Check  for more info.

## Creating a State
A state is a text file with the .sls extension, located within a configured environment. This assumes the only the default base environment set up.

Create a file in  called , with the following content:

Now run the state:

 # salt '*' state.apply test

Salt will search the base environment folder for anything called  and apply the configuration it finds to all servers. In this case, netcat will be installed on all servers.

For more information on state file syntax and using states, see here: https://docs.saltproject.io/en/latest/topics/tutorials/starting_states.html

## The top file
The top file is the main way to apply different configs to different servers at once. The top file is called  and is placed in the root of an environment. The top file configuration can be ran with the following command:

 # salt '*' state.apply

Let us assume we have 2 servers: fs01, web01. Let us also assume we have 3 states in the base environment: , , . Here is a sample:

When state.apply is ran, the top file is read, and the states are applied to the correct servers. IE: nettools on all servers, samba on fs01, apache on web01.

## Scheduling Tasks
Enable the salt scheduler on the minion with

 # salt 'minion-name' schedule.enable

Install  on the master and any minions that will be using the scheduler and restart the salt-minion service on that server. Remember, you can easily install  and restart the salt-minion service on all minions using a state or a salt '*' command.

Assume , stored in , needs to be run every Monday on fs01. This can be accomplished by placing the following into a state file and running it.

  configure_samba_daily:
    schedule.present:
      - function: state.sls
      - job_args:
        - samba
      - when:
        - Monday 5:00am

Run

 # salt 'minion-name' schedule.list

to verify the job was placed on the schedule.

For more details on configuring schedules, see https://docs.saltproject.io/en/latest/ref/states/all/salt.states.schedule.html
