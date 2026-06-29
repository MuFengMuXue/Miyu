**SELinux** is a mandatory access control system which enables a more fine-grained mechanism permitting the security administrator to define user privileges. Unlike the standard discretionary access control in place for Linux (where the end user can still decide for himself how his resources are accessed by others) a mandatory access control system is fully governed through a security policy. With SELinux, enforcement of the access controls is done by the Linux kernel, governed through a security policy that is loaded at start of the system.

## [Introduction]

![Police.png](/images/thumb/b/bf/Police.png/128px-Police.png)

Linux has a well-known *discretionary* access control system, based on the permission mask set on resources and the ownership of the resource versus the run-time privileges of a process. Some additional security features are available as well, such as capabilities and extended ACLs, which allow administrators to fine-tune the secure state of their system. But even all those features still prove to be discretionary in their model.

A discretionary model means that the owner of a resource can still decide how the resource is shared on the system. A directory can be made world-writable by its owner, and from that point onward all processes on the system can write to the directory. With a *mandatory* access control system, the access to resources is governed through a mandatory system that cannot be worked around from. With SELinux, this is the SELinux security subsystem running in the Linux kernel.

## [SELinux resources]

A [quick introduction to SELinux](https://wiki.gentoo.org/wiki/SELinux/Quick_introduction "SELinux/Quick introduction") helps to have a high-level idea behind the SELinux security subsystem. It covers the difference between discretionary and mandatory access control, the [labeled](https://wiki.gentoo.org/wiki/SELinux/Labels "SELinux/Labels") approach that SELinux takes and how it is integrated in the Linux operating system.

For more in-depth information, please refer to the following resources.

  --------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Concepts
  [Type enforcement](https://wiki.gentoo.org/wiki/SELinux/Type_enforcement "SELinux/Type enforcement")                              Controlling accesses is done in most cases through a type-enforcement based approach.
  [Role-based access control](https://wiki.gentoo.org/wiki/SELinux/Role-based_access_control "SELinux/Role-based access control")   Ensuring a least privilege approach on a Linux system using SELinux\' RBAC model.
  [User-based access control](https://wiki.gentoo.org/wiki/SELinux/User-based_access_control "SELinux/User-based access control")   Ensuring segregation of users, even when they run using the same domains and accessing the same types.
  [Information flow control](https://wiki.gentoo.org/wiki/SELinux/Information_flow_control "SELinux/Information flow control")      Limiting information flow based on security clearance and sensitivities.
  [Unconfined domains](https://wiki.gentoo.org/wiki/SELinux/Unconfined_domains "SELinux/Unconfined domains")                        When SELinux protections are not needed in all cases, unconfined domains can be used.
  User guides
  [Installation](https://wiki.gentoo.org/wiki/SELinux/Installation "SELinux/Installation")                                          The main resource for installing and enabling SELinux on a Gentoo system.
  [Users and logins](https://wiki.gentoo.org/wiki/SELinux/Users_and_logins "SELinux/Users and logins")                              Mapping Linux users (logins) to SELinux users.
  [Managing labels](https://wiki.gentoo.org/wiki/SELinux/Labels "SELinux/Labels")                                                   Setting and configuring file (and other resource) labels.
  [Policy](https://wiki.gentoo.org/wiki/SELinux/Policy "SELinux/Policy")                                                            The SELinux policy defines the acceptable behavior on a system; it can be rebuilt by administrators, loaded and unloaded (through its modular design) and tweaked by adding more policy rules.
  [Logging](https://wiki.gentoo.org/wiki/SELinux/Logging "SELinux/Logging")                                                         SELinux usually logs denials in the audit log (or system log if no auditing is enabled).
  [Booleans](https://wiki.gentoo.org/wiki/SELinux/Booleans "SELinux/Booleans")                                                      Enable or disable additional policy controls through SELinux booleans.
  [States](https://wiki.gentoo.org/wiki/SELinux/States "SELinux/States")                                                            SELinux can be enabled or disabled, and running in enforcing, partial permissive or full permissive mode.
  Expert documentation
  [Policy development](https://wiki.gentoo.org/wiki/Project:SELinux/Development "Project:SELinux/Development")                      Updating SELinux policy to suit your needs, and send patches to Gentoo or even upstream projects.
  [Policy store](https://wiki.gentoo.org/wiki/SELinux/Policy_store "SELinux/Policy store")                                          The policy store contains the SELinux policy binaries; multiple stores can be defined on a system.
  [Networking support](https://wiki.gentoo.org/wiki/SELinux/Networking "SELinux/Networking")                                        SELinux supports port labeling, but also packet-based access controls through SECMARK and peer-to-peer labeling support.
  Reference material
  [FAQ](https://wiki.gentoo.org/wiki/SELinux/FAQ "SELinux/FAQ")                                                                     Frequently Asked Questions on SELinux and SELinux integration in Gentoo.
  [SELinux policy language](https://wiki.gentoo.org/wiki/SELinux/Language "SELinux/Language")                                       Supported SELinux language constructs.
  [Policy module specific information](https://wiki.gentoo.org/wiki/SELinux/Module_list "SELinux/Module list")                      More in-depth information about particular SELinux policy modules.
  --------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## [Development]

For engineers and developers, we provide the following resources:

  ----------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------
  Upstream projects
  [Linux Security Modules](https://wiki.gentoo.org/wiki/SELinux/LSM "SELinux/LSM")                                  The integration of SELinux in the Linux kernel is done through the LSM subsystem.
  [Reference policy](https://wiki.gentoo.org/wiki/SELinux/Reference_policy "SELinux/Reference policy")              All Linux distributions base their SELinux policies on the reference policy.
  [SELinux userspace project](https://wiki.gentoo.org/wiki/SELinux/Userspace_project "SELinux/Userspace project")   The software that engineers and administrators use to work with SELinux.
  Gentoo Linux integration
  [Gentoo SELinux project](https://wiki.gentoo.org/wiki/Project:SELinux "Project:SELinux")                          Project site of the Gentoo SELinux project.
  [Profiles](https://wiki.gentoo.org/wiki/SELinux/Gentoo_profiles "SELinux/Gentoo profiles")                        Enabling SELinux support in default Gentoo profiles.
  [Policy packages](https://wiki.gentoo.org/wiki/SELinux/Gentoo_policy_packages "SELinux/Gentoo policy packages")   Information on how the Gentoo packages push out SELinux policies to a system.
  ----------------------------------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------

## [Learning SELinux]

We also provide the following resources to gradually learn about SELinux.

  ----------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------
  Online resources
  [SELinux tutorials](https://wiki.gentoo.org/wiki/SELinux/Tutorials "SELinux/Tutorials")   More than a dozen small tutorials that introduce you to SELinux and its Gentoo integration.
  ----------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------

## [News]

#### [][February 15, 2020: Refpolicy policies 2.20190609 are now available]

On June 9th, the SE Linux reference policy project released the 2.20190609 version of the SELinux policies. Gentoo now includes those policies (as unstable for **[x86]**, **[amd64]**, and **[arm]** for now), ready for testing.

\

#### [][July 01, 2018: Refpolicy policies 2.20180701 are now available]

On July 1st, the Reference Policy Project released the 2.20180701 version of the SELinux policies. Gentoo now includes those policies (\~arch for now), ready for testing.

\

## [Support state]

**SELinux user space:**

-   [Upstream](https://github.com/SELinuxProject/selinux/wiki/Releases): 3.10
-   [Gentoo](https://packages.gentoo.org/packages/sys-libs/libselinux): 3.9 (stable), 3.10 (testing)

**SELinux policies:**

-   [Upstream](https://github.com/SELinuxProject/refpolicy/releases): 2.20260312
-   [Gentoo](https://packages.gentoo.org/package/sec-policy/selinux-base): 2.20250618_p1-r1 (stable), 2.20260312_p1 (testing)

## [SELinux in Gentoo]

The integration of SELinux in Gentoo is handled by the [SELinux](https://wiki.gentoo.org/wiki/Project:SELinux "Project:SELinux") sub-project of the [Gentoo Hardened](https://wiki.gentoo.org/wiki/Project:Hardened "Project:Hardened") project.

**Problems with SELinux in Gentoo?**

-   [Report a bug](https://bugs.gentoo.org) in Bugzilla

**Want some help?**

-   Try the [gentoo-hardened](http://news.gmane.org/gmane.linux.gentoo.hardened) mailing list
-   Call out to us through IRC on Libera.Chat\'s [[#gentoo-hardened](ircs://irc.libera.chat/#gentoo-hardened)] ([[webchat](https://web.libera.chat/#gentoo-hardened)]) channel.

## [External resources]

-   [The Inevitability of Failure: The Flawed Assumption of Security in Modern Computing Environments](https://www.nsa.gov/Portals/70/documents/resources/everyone/digital-media-center/publications/research-papers/the-inevitability-of-failure-paper.pdf) explains the need for mandatory access controls.
-   [The Flask Security Architecture: System Support for Diverse Security Policies](https://www.nsa.gov/Portals/70/documents/resources/everyone/digital-media-center/publications/research-papers/flask-security-architecture-paper.pdf) explains the security architecture of Flask, the architecture used by SELinux.