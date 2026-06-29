[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Switching+Branches&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Switching_Branches "Switching Branches (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Switching_Branches/ru "Переключение ветвей (100% translated)") • ‎[עברית](//wiki.manjaro.org/index.php?title=Switching_Branches/he "מעבר בין ענפים (25% translated)") • ‎[فارسی](//wiki.manjaro.org/index.php?title=Switching_Branches/fa "تعویض شاخه‌ها (75% translated)") • ‎[中文（中国大陆）‎](//wiki.manjaro.org/index.php?title=Switching_Branches/zh-cn "切换分支 (75% translated)")

## Contents

-   [[1] [Overview]](#Overview)
    -   [[1.1] [Changing to another branch]](#Changing_to_another_branch)
    -   [[1.2] [Questions]](#Questions)
        -   [[1.2.1] [How do I go back after changing to one of the testing branches?]](#How_do_I_go_back_after_changing_to_one_of_the_testing_branches.3F)
        -   [[1.2.2] [How do I check, which branch I am currently on?]](#How_do_I_check.2C_which_branch_I_am_currently_on.3F)

# [Overview]

**Info**

------------------------------------------------------------------------

Manjaro specific packages downloaded and installed from the *Testing branch* or *Unstable branch* will, by nature, not have been fully tested, and may be unstable. Please refer to [System Maintenance](//wiki.manjaro.org/index.php?title=System_Maintenance "System Maintenance") Section for important maintenance information.

\
One of the many features that sets Manjaro apart from other Arch-based distributions is that it uses its own dedicated software branches, rather than relying on those provided by Arch itself. In fact, to ensure continued stability and reliability, Manjaro actually uses three distinct branches:

-   **Stable branch**: The packages that come to stable have gone through roughly a couple of weeks testing by the users of the *Unstable/Testing* repos, before they get the packages. These packages are usually free of any problems.
-   **Testing branch**: This is the second line of defense. Being a larger number of users than those using *Unstable*, they refine the work done prior to them by providing feedback on the packages they recieve on updates.
-   **Unstable branch**: Unstable is synced several times a day with Arch package releases. Only a subset of Arch packages are modified to suit Manjaro. Those that use *Unstable* need to have the skills to get themselves out of trouble when they move their system to this branch. They are the Manjaro users who are most likely to need to use such skills. Due to the feedback from the users of the *Unstable* repo, many issues are caught and fixed at this level. Although the very latest software will be located here, [using the *unstable branch* is usually safe but - in rare cases - may cause issues with your system!]

**Summing up**, Manjaro packages start their lives in the *unstable* branch. Once they are a deemed stable, they are moved to the *testing* branch, where more tests will be realized to ensure the package is ready to be submitted to the *stable* branch.

\

**Note on unstable branch**

------------------------------------------------------------------------

**Remember**: Manjaro specific packages such as kernels, kernel modules and Manjaro applications enter the repo on *unstable* branch and it is those packages which are considered unstable when they enter.

Unmodifed packages synced from Arch repo are considered stable as they have already been vetted by Archlinux Community.

## [Changing to another branch]

**Have you considered?**

------------------------------------------------------------------------

Why not become an active part of the Manjaro community by becoming a tester?

In order to access a branch, you need to change your pacman-mirrors configuration.

You should substitute the value colored in green (for illustrative purposes only) to one of the following: **stable**, **testing** or **unstable**.

    sudo pacman-mirrors --api --set-branch

After you changed the branch, rebuild the mirrorlist and update your packages:

[user \$ ][ sudo pacman-mirrors \--fasttrack 5 && sudo pacman -Syu [COPY TO CLIPBOARD]]

\

## [Questions]

### [][How do I go back after changing to one of the testing branches?]

Going back to the stable branch is easy. All you have to do is to repeat the above, and use *stable* as the branch value.

**Be aware** that after switching to a more stable branch you will receive messages from pacman, informing about newer packages installed than available in the repo. Don\'t be alarmed as the situation will resolve itself when the packages reaches your current branch.

If for whatever reason you *do* wish to also \'downgrade\' packages while changing branches add an extra *u* to the pacman command:

[user \$ ][ sudo pacman -Syuu [COPY TO CLIPBOARD]]

\

### [][How do I check, which branch I am currently on?]

[user \$ ][ pacman-mirrors -G [COPY TO CLIPBOARD]]

\