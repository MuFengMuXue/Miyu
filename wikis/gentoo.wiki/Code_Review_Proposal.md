## Contents

-   [[1] [Code Review / Pull Requests]](#Code_Review_.2F_Pull_Requests)
    -   [[1.1] [Workflows]](#Workflows)
        -   [[1.1.1] [Example: Websites]](#Example:_Websites)
    -   [[1.2] [Infra specific workflows]](#Infra_specific_workflows)
        -   [[1.2.1] [Example: Easier VMs]](#Example:_Easier_VMs)

## [][Code Review / Pull Requests]

Today Gentoo has hundreds of git repos mastered on git.gentoo.org and mirrored to anongit.gentoo.org as well as to other places (e.g. github.) Users often craft patches and send them for review. Github popularized the concept of a \'pull request\' which was a straightforward way for a user to clone a git repository, craft a patch, and then submit a \"merge request\" for the original repository owner to merge back the change. Gentoo currently does not offer pull request functionality with inline reviews.

### [Workflows]

We have a bunch of guides on existing workflows such as:

-   [Submitting ebuilds](https://wiki.gentoo.org/wiki/Submitting_ebuilds "Submitting ebuilds")
-   [GitHub Pull Requests](https://wiki.gentoo.org/wiki/GitHub_Pull_Requests "GitHub Pull Requests")
-   [https://www.gentoo.org/glep/glep-0066.html](https://www.gentoo.org/glep/glep-0066.html)

These workflows basically involve a few steps:

    - Cloning the repo.
    - Crafting a patch.
    - Submitting the patch for inclusion.
    - Including the patch.

#### [Example: Websites]

Today we do have a large amount of different websites, which are mostly located in various repositories and maintained by a small group of developers. Creating an easy way for all developers to contribute to the websites can help us to involve more developers here.

### [Infra specific workflows]

Gentoo infra has traditionally been a fairly private segment of Gentoo. Most of our git repos are private. This privacy makes infra inaccessible to people because how we manage services is opaque. Contributing to infra is hard, onboarding people is hard. Sure our administration repos are, to quote a newcomer, \"A spaghetti mess\". However I think having an easy way to access them, to submit patches, and get them reviewed (including iterations) is important and will help us build more accessible maintenance.

#### [Example: Easier VMs]

Today we have a repo \'infra-as-code\' that we used to administrate some AWS resources. Devs often want VMs and we can easily make new VMs on AWS for developers. Today that mostly involves \"pinging someone to do some stuff, getting some back and forth on the requirements, then waiting some days, then maybe you get a VM.\" This results in no one asking for VMs which is probably not the best outcome. Instead we could have workflow like:

1.  Dev reads wiki guide on VM request.
2.  Dev goes to code.gentoo.org/repos/infra-as-code
3.  Dev forks this repo.
4.  Dev adds a new VM to the list of entries.
5.  Dev asks for merge request.
6.  Infra reviews, merges, and applies the request: VM now created.