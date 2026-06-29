# Managing Operation Policies

Operation policies are the rules used for each IPP operation in CUPS. These rules include things like "user must provide a password", "user must be in the system group", "allow only from the local system", and so forth. Until CUPS 1.2, these rules were largely hardcoded and could only be customized at a very basic level.

CUPS 1.2 and later provides a fine-grained policy layer which allows you to completely redefine the rules for each operation and/or printer. Each policy is named and defines access control rules for each IPP operation. This document describes how to manage policies and their rules.

## The Basics

Operation policies are used for all IPP requests sent to the scheduler and are evaluated *after* the [`Location`](man-cupsd.conf.html#Location) based access control rules. This means that operation policies can only add additional security restrictions to a request, never relax them. Use `Location` based access control rules for server-wide limits and operation policies for limits on individual printers, tasks, or services.

Policies are stored in the `cupsd.conf` file in [`Policy`](man-cupsd.conf.html#Policy) sections. Each policy has an alphanumeric name that is used to select it. Inside the policy section are one or more [`Limit`](man-cupsd.conf.html#LimitIPP) subsections which list the operations that are affected by the rules inside it. [Listing 1](#LISTING01) shows the default operation policy, appropriately called "default", that is shipped with CUPS.

The easiest way to add a policy to the `cupsd.conf` file is to use the web interface. Click on the `Administration` tab and then the `Edit Configuration File` button to edit the current `cupsd.conf` file. Click on the `Save Changes` button to save the changes and restart the scheduler. If you edit the `cupsd.conf` file from the console, make sure to [restart the cupsd process](man-cupsd.conf.html) before trying to use the new policy.

``` example
Listing 1: Default Operation Policy

 1    <Policy default>
 2      # Job-related operations must be done by the owner or an
      administrator...
 3      <Limit Send-Document Send-URI Hold-Job Release-Job
      Restart-Job Purge-Jobs Set-Job-Attributes
      Create-Job-Subscription Renew-Subscription
      Cancel-Subscription Get-Notifications Reprocess-Job
      Cancel-Current-Job Suspend-Current-Job Resume-Job
      CUPS-Move-Job CUPS-Get-Document>
 4        Require user @OWNER @SYSTEM
 5        Order deny,allow
 6      </Limit>
 7
 8      # All administration operations require an administrator
      to authenticate...
 9      <Limit CUPS-Add-Modify-Printer CUPS-Delete-Printer CUPS-Add-Modify-Class
      CUPS-Delete-Class CUPS-Set-Default>
10        AuthType Default
11        Require user @SYSTEM
12        Order deny,allow
13      </Limit>
14
15      # All printer operations require a printer operator
      to authenticate...
16      <Limit Pause-Printer Resume-Printer
      Set-Printer-Attributes Enable-Printer Disable-Printer
      Pause-Printer-After-Current-Job Hold-New-Jobs
      Release-Held-New-Jobs Deactivate-Printer Activate-Printer
      Restart-Printer Shutdown-Printer Startup-Printer
      Promote-Job Schedule-Job-After CUPS-Accept-Jobs
      CUPS-Reject-Jobs>
17        AuthType Default
18        Require user varies by OS
19        Order deny,allow
20      </Limit>
21
22      # Only the owner or an administrator can cancel or
      authenticate a job...
23      <Limit Cancel-Job CUPS-Authenticate-Job>
24        Require user @OWNER @SYSTEM
25        Order deny,allow
26      </Limit>
27
28      <Limit All>
29        Order deny,allow
30      </Limit>
31    </Policy>
```

### The Default CUPS Operation Policy

The policy definition starts with an opening `Policy` directive:

``` example
 1    <Policy default>
```

The first `Limit` subsection defines the rules for IPP job operations:

``` example
 3      <Limit Send-Document Send-URI Hold-Job Release-Job
      Restart-Job Purge-Jobs Set-Job-Attributes
      Create-Job-Subscription Renew-Subscription
      Cancel-Subscription Get-Notifications Reprocess-Job
      Cancel-Current-Job Suspend-Current-Job Resume-Job
      CUPS-Move-Job CUPS-Get-Document>
 4        Require user @OWNER @SYSTEM
 5        Order deny,allow
 6      </Limit>
```

The operation names are listed on a single line with spaces separating them. Each name corresponds to the IPP operation described in any of the IETF or PWG standards documents for the Internet Printing Protocol. [Table 1](#TABLE01) lists all of the operations that have been defined along with their usage in CUPS.

The access control rules are listed after the `Limit` line and are the same as those used for [`Location`](man-cupsd.conf.html#Location) sections. In this case, we require the owner of the job ("@OWNER") or a member of the [`SystemGroup`](man-cups-files.conf.html#SystemGroup) ("@SYSTEM") to do the operation. Because we do not include an [`AuthType`](man-cupsd.conf.html#AuthType) directive here, the user information can come from the IPP request itself or the authenticated username from the HTTP request. The administrative operations starting on line 9, however, *do* use the `AuthType` directive, and so administrative operations need to be authenticated:

``` example
 9      <Limit CUPS-Add-Modify-Printer CUPS-Delete-Printer CUPS-Add-Modify-Class
      CUPS-Delete-Class CUPS-Set-Default>
10        AuthType Default
11        Require user @SYSTEM
12        Order deny,allow
13      </Limit>
14
15      # All printer operations require a printer operator
      to authenticate...
16      <Limit Pause-Printer Resume-Printer
      Set-Printer-Attributes Enable-Printer Disable-Printer
      Pause-Printer-After-Current-Job Hold-New-Jobs
      Release-Held-New-Jobs Deactivate-Printer Activate-Printer
      Restart-Printer Shutdown-Printer Startup-Printer
      Promote-Job Schedule-Job-After CUPS-Accept-Jobs
      CUPS-Reject-Jobs>
17        AuthType Default
18        Require user varies by OS
19        Order deny,allow
20      </Limit>
```

The "Order deny,allow" line at the end of both `Limit` subsections allows the request to come from any system allowed by the `Location` sections elsewhere in the `cupsd.conf` file.

The `Cancel-Job` and `CUPS-Authenticate-Job` operations are listed separately to allow the web interface to more easily edit their policy without disturbing the rest. Like the rest of the job operations, we want the job's owner ("@OWNER") or an administrator ("@SYSTEM") to do it:

``` example
16      <Limit Cancel-Job CUPS-Authenticate-Job>
17        Require user @OWNER @SYSTEM
18        Order deny,allow
19      </Limit>
```

The last `Limit` subsection in any policy uses the special operation name `All`. CUPS will use the rules in this subsection for any operation you don't list specifically in the policy. In this case, all other operations are allowed without a username or authentication:

``` example
21      <Limit All>
22        Order deny,allow
23      </Limit>
24    </Policy>
```


| Name | Used by CUPS? | Description |
|----|----|----|
| `Activate-Printer` | No | Activates a printer or class. |
| `Cancel-Current-Job` | No | Cancels the current job on a printer or class. |
| `Cancel-Job` | Yes | Cancels a print job. |
| `Cancel-Jobs` | Yes | Cancels all print jobs. |
| `Cancel-My-Jobs` | Yes | Cancels a user's print job. |
| `Cancel-Subscription` | Yes | Cancels an event subscription. |
| `Close-Job` | Yes | Closes a user's print job so that it can be printed. |
| `Create-Job` | Yes | Creates a print job with no files or URIs. |
| `Create-Job-Subscriptions` | Yes | Creates one or more event subscriptions for a job. |
| `Create-Printer-Subscriptions` | Yes | Creates one or more event subscriptions for a printer or the server. |
| `Deactivate-Printer` | No | Deactivates a printer or class. |
| `Disable-Printer` | Yes | Stops a printer or class. |
| `Enable-Printer` | Yes | Starts a printer or class. |
| `Get-Job-Attributes` | Yes | Gets information and options associated with a job. |
| `Get-Jobs` | Yes | Gets a list of jobs. |
| `Get-Notifications` | Yes | Gets (pending) events for an event subscription. |
| `Get-Printer-Attributes` | Yes | Gets information and options associated with a printer or class. |
| `Get-Printer-Supported-Values` | Yes | Gets -supported attributes for a printer based on job options. |
| `Get-Subscription-Attributes` | Yes | Gets information for an event subscription. |
| `Get-Subscriptions` | Yes | Gets a list of event subscriptions. |
| `Hold-Job` | Yes | Holds a print job for printing. |
| `Hold-New-Jobs` | Yes | Holds new jobs submitted to a printer or class. |
| `Pause-Printer` | Yes | Stops a printer or class. |
| `Pause-Printer-After-Current-Job` | No | Stops a printer or class after the current job is finished. |
| `Print-Job` | Yes | Creates a print job with a single file. |
| `Print-URI` | No | Create a print job with a single URI. |
| `Promote-Job` | No | Prints a job before others. |
| `Purge-Jobs` | Yes | Cancels all jobs on the server or a printer or class and removes the job history information. |
| `Release-Held-New-Jobs` | Yes | Releases jobs that were held because of the Hold-New-Jobs operation. |
| `Release-Job` | Yes | Releases a print job for printing. |
| `Renew-Subscription` | Yes | Renews an event subscription that is about to expire. |
| `Reprocess-Job` | No | Reprints a job on a different printer or class; CUPS has the CUPS-Move-Job operation instead. |
| `Restart-Job` | Yes | Reprints a print job. |
| `Restart-Printer` | No | Restarts a printer or class, resuming print jobs as needed. |
| `Resubmit-Job` | No | Reprints a job with new options. |
| `Resume-Job` | No | Resumes printing of a stopped job. |
| `Resume-Printer` | Yes | Starts a printer or class. |
| `Schedule-Job-After` | No | Prints a job after others. |
| `Send-Document` | Yes | Adds a file to a print job. |
| `Send-URI` | No | Adds a URI to a print job. |
| `Set-Printer-Attributes` | Yes | Sets printer or class information; CUPS uses CUPS-Add-Modify-Printer and CUPS-Add-Modify-Class for most attributes instead. |
| `Set-Job-Attributes` | Yes | Changes job options. |
| `Shutdown-Printer` | No | Powers a printer or class off. |
| `Startup-Printer` | No | Powers a printer or class on. |
| `Suspend-Current-Job` | No | Stops the current job on a printer or class. |
| `Validate-Document` | No | Validates a document request before sending. |
| `Validate-Job` | Yes | Validates a print request before printing. |
| `CUPS-Accept-Jobs` | Yes | Sets a printer's or class' printer-is-accepting-jobs attribute to true. |
| `CUPS-Add-Modify-Class` | Yes | Adds or modifies a class. |
| `CUPS-Add-Modify-Printer` | Yes | Adds or modifies a printer. |
| `CUPS-Authenticate-Job` | Yes | Authenticates a job for printing. |
| `CUPS-Delete-Class` \* | Yes | Removes a class. |
| `CUPS-Delete-Printer` \* | Yes | Removes a printer. |
| `CUPS-Get-Classes` \* | Yes | Gets a list of classes. |
| `CUPS-Get-Default` \* | Yes | Gets the server/network default printer or class. |
| `CUPS-Get-Devices` \* | Yes | Gets a list of printer devices. |
| `CUPS-Get-Document` | Yes | Retrieves a document file from a job. |
| `CUPS-Get-PPDs` \* | Yes | Gets a list of printer drivers or manufacturers. |
| `CUPS-Get-Printers` \* | Yes | Gets a list of printers and/or classes. |
| `CUPS-Move-Job` | Yes | Moves a job to a different printer or class. |
| `CUPS-Reject-Jobs` | Yes | Sets a printer's or class' printer-is-accepting-jobs attribute to false. |
| `CUPS-Set-Default` \* | Yes | Sets the server/network default printer or class. |

Table 1: IPP Operation Names


\* = These operations only apply to the default policy.

## Creating Your Own Policies

The easiest way to create a new policy is to start with the default policy and then make changes to the copy. The first change you'll make is to give the policy a new name. Policy names can use the same characters as a printer name, specifically all printable characters except space, slash (/), and pound (#):

``` example
<Policy mypolicy>
```

Then you need to decide exactly what limits you want for the policy. For example, if you want to allow any user to cancel any other users' jobs, you can change the `Cancel-Job` limits to:

``` example
<Limit Cancel-Job>
  Order deny,allow
</Limit>
```

The directives inside the `Limit` subsection can use any of the normal limiting directives: [`Allow`](man-cupsd.conf.html#Allow), [`AuthType`](man-cupsd.conf.html#AuthType), [`Deny`](man-cupsd.conf.html#Deny), [`Encryption`](man-cupsd.conf.html#Encryption), [`Require`](man-cupsd.conf.html#Require), and [`Satisfy`](man-cupsd.conf.html#Satisfy). [Table 2](#TABLE02) lists some basic "recipes" for different access control rules.


<table width="80%" data-summary="Access Control Recipes">
<caption>Table 2: Access Control Recipes</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th>Access Level</th>
<th>Directives to Use</th>
</tr>
</thead>
<tbody>
<tr>
<td>Allow Everyone</td>
<td><pre><code>Order deny,allow
Allow from all</code></pre></td>
</tr>
<tr>
<td>Allow Everyone on the Local Network</td>
<td><pre><code>Order deny,allow
Allow from @LOCAL</code></pre></td>
</tr>
<tr>
<td>Deny Everyone/Disable Operation(s)</td>
<td><pre><code>Order allow,deny</code></pre></td>
</tr>
<tr>
<td>Require Login (System) Password</td>
<td><pre><code>AuthType Basic</code></pre></td>
</tr>
<tr>
<td>Require CUPS (lppasswd) Password</td>
<td><pre><code>AuthType BasicDigest</code></pre></td>
</tr>
<tr>
<td>Require Kerberos</td>
<td><pre><code>AuthType Negotiate</code></pre></td>
</tr>
<tr>
<td>Require the Owner of a Job or Subscription</td>
<td><pre><code>Require user @OWNER</code></pre></td>
</tr>
<tr>
<td>Require an Administrative User</td>
<td><pre><code>Require user @SYSTEM</code></pre></td>
</tr>
<tr>
<td>Require Member of Group "foogroup"</td>
<td><pre><code>Require user @foogroup</code></pre></td>
</tr>
<tr>
<td>Require "john" or "mary"</td>
<td><pre><code>Require user john mary</code></pre></td>
</tr>
<tr>
<td>Require Encryption</td>
<td><pre><code>Encryption Required</code></pre></td>
</tr>
</tbody>
</table>


### Creating a Policy for a Computer Lab

One common operating scenario is a computer lab. The lab is managed by one or more technicians that assist the users of the lab and handle the basic administration tasks. [Listing 2](#LISTING02) shows an operation policy that only allows access from the lab's subnet, 10.0.2.x, and allows the lab technicians, who are members of a special UNIX group for that lab called "lab999", to do job, printer, and subscription management operations.

``` example
Listing 2: Operation Policy for a Lab

 1    <Policy lab999>
 2      # Job- and subscription-related operations must be done
      by the owner, a lab technician, or an administrator...
 3      <Limit Send-Document Send-URI Hold-Job Release-Job
      Restart-Job Purge-Jobs Set-Job-Attributes
      Create-Job-Subscription Renew-Subscription
      Cancel-Subscription Get-Notifications Reprocess-Job
      Cancel-Current-Job Suspend-Current-Job Resume-Job
      CUPS-Move-Job Cancel-Job CUPS-Authenticate-Job CUPS-Get-Document>
 4        Require user @OWNER @lab999 @SYSTEM
 5        Order allow,deny
 6        Allow from 10.0.2.0/24
 7      </Limit>
 8
 9      # All administration operations require a lab technician
      or an administrator to authenticate...
10      <Limit Pause-Printer Resume-Printer
      Set-Printer-Attributes Enable-Printer Disable-Printer
      Pause-Printer-After-Current-Job Hold-New-Jobs
      Release-Held-New-Jobs Deactivate-Printer Activate-Printer
      Restart-Printer Shutdown-Printer Startup-Printer
      Promote-Job Schedule-Job-After CUPS-Accept-Jobs
      CUPS-Reject-Jobs CUPS-Set-Default>
11        AuthType Default
12        Require user @lab999 @SYSTEM
13        Order allow,deny
14        Allow from 10.0.2.0/24
15      </Limit>
16
17      # All other operations are allowed from the lab network...
18      <Limit All>
19        Order allow,deny
20        Allow from 10.0.2.0/24
21      </Limit>
22    </Policy>
```

## Using Policies

Once you have created a policy, you can use it in two ways. The first way is to assign it as the default policy for the system using the [`DefaultPolicy`](man-cupsd.conf.html#DefaultPolicy) directive in the `cupsd.conf` file. For example, add the following line to the `cupsd.conf` file to use the "lab999" policy from the previous section:

``` example
DefaultPolicy lab999
```

To associate the policy with one or more printers, use either the [lpadmin(8)](man-lpadmin.html) command or the web interface to change the operation policy for each printer. When using the **lpadmin** command, the `-o printer-op-policy=name` option sets the operation policy for a printer. For example, enter the following command to use the "lab999" policy from the previous section with a printer named "LaserJet4000":

``` command
lpadmin -p LaserJet4000 -o printer-op-policy=lab999
```

To make the same change in the web interface, go to the printer's web page, for example "http://localhost:631/printers/LaserJet4000", and choose `Set Default Options` from the `Administration` menu button. Click on the `Policies` link and choose the desired policy from the pull-down list. Click on `Set Default Options` to change the policy for the printer.
