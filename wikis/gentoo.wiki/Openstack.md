[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Openstack&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Openstack "Project:Openstack")][Project](https://wiki.gentoo.org/wiki/Project:Openstack "Project:Openstack")

## Contents

-   [[1] [Openstack]](#Openstack)
-   [[2] [Before Installation]](#Before_Installation)
    -   [[2.1] [Controller node]](#Controller_node)
    -   [[2.2] [Network Node]](#Network_Node)
    -   [[2.3] [Compute Node]](#Compute_Node)
-   [[3] [Installation]](#Installation)
    -   [[3.1] [USE flags]](#USE_flags)
    -   [[3.2] [Emerge]](#Emerge)
    -   [[3.3] [Configuration]](#Configuration)
    -   [[3.4] [Testing]](#Testing)
    -   [[3.5] [Troubleshooting]](#Troubleshooting)
    -   [[3.6] [See also]](#See_also)
    -   [[3.7] [External resources]](#External_resources)

## [Openstack]

The OpenStack project aims to create an open and free IaaS platform.

## [Before Installation]

#### [Controller node]

Let\'s begin from the Controller node. Before installing Openstack specific services the system needs to be configured with two physical NIC, one for the *Management Network* and one to expose the Openstack API to the internet on the *Public Network*, with the following IP configuration:

  ---------------------- -------------
  Network Interface      IP Address
  Public Interface       1.1.1.1
  Management Interface   192.168.0.1
  ---------------------- -------------

#### [Network Node]

#### [Compute Node]

## [Installation]

You will need three Gentoo hosts to fully exploit the power of the OpenStack platform.

### [USE flags]

Cannot load package information. Is the atom *sys-cluster/openstack-meta* correct?

### [Emerge]

`root `[`#`]`emerge --ask sys-cluster/openstack-meta`

### [Configuration]

### [Testing]

### [Troubleshooting]

### [See also]

### [External resources]