# Son of Grid Engine

The Son of Grid Engine is a community project to continue Sun's old gridengine, which was a grid computing computer cluster software system (otherwise known as a batch-queuing system).

## Installation
Install the  package for both qmaster and execution host.

## Configuration
## Qmaster host configuration
Use the  script to do the qmaster host configuration.

 # cd /opt/sge && ./install_qmaster

You can then start/enable

## Execution host configuration
Before the execution host configuration, you need to configure your execution host as an administrative host on the qmaster host.

 # source /opt/sge/your_sge_cell_name/common/settings.sh
 # qconf -ah your_execution_host_name

Then put the sge cell directory from the qmaster host, , under the same path on your execution host.

Now use the  script to do the execution host configuration.

 # cd /opt/sge && ./install_execd

You can then start/enable

After configuration, you can remove your execution host from the administrative host list.

 # qconf -dh your_execution_host_name
