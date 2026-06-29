# Bisecting bugs with Git

Often when reporting bugs encountered with projects such as Mesa or Linux kernel, a user may be asked to bisect between the last known version that worked for them and the newer version which is causing them problems in order to see what is the troublesome commit. On Arch this can be done fairly trivially thanks to the functionality of the AUR.

## Reverting to an older release
It might be useful to confirm that it is the new package release that is causing the problem. Downgrading packages on Arch can be accomplished trivially as long as an older version of the package is still stored as cache on your system, or you can use Arch Linux Archive.

## Building package from git
In order to bisect we are going to need to build a version of package from git. This can be accomplished by building the -git package from the AUR.

## Setting up the bisect
Once package is successfully built you need to change into the git root directory in the  directory. The name of the git root directory is often the same as  (or without the  suffix):

 $ cd src/git_root

From there you can start the process of bisecting:

 $ git bisect start

The following command will show you all the tags you can use to specify where to bisect:

 $ git tag

Following on from the earlier example, we will assume that the version oldver worked for us while newver did not:

 $ git bisect good oldver
 $ git bisect bad newver

Now that we have our good and bad versions tagged we can proceed to test commits.

## Bisecting
Change back into the directory with the PKGBUILD. If you are still in the directory mentioned in the previous section this can be accomplished like so:

 $ cd ../..

You can now rebuild and install the specific revision of the package:

 $ makepkg -efsi

Once the new package is installed you can test for your previously discovered error. Return to the directory you were in the previous section:

 $ cd src/git_root

If you encountered your problem, tell that the revision was bad:

 $ git bisect bad

If you did not encounter your problem, tell that the revision it was good:

 $ git bisect good

Then do as described at the beginning of this section again and repeat until git bisect names the troublesome commit.

## Speeding up builds
## make
Make sure you are building with all of your cores. The fastest way to set this is:

 $ echo 'MAKEFLAGS="-j$(nproc)"' >> ~/.makepkg.conf

And monitor your builds with  to make sure the build is in fact using all your cores.

## modprobed-db
If bisecting the kernel, build times can be cut by 50% to 80% by disabling unused modules.

## ccache
If you are bisecting a large project built using , it might be possible to reduce build times by enabling ccache. It may take several build iterations before you start to see benefits from the cache, however. The likelihood of cache hits generally increases as the distance between bisection points decreases.

To be effective, before the first build configure

 $ ccache --set-config=sloppiness=locale,time_macros,include_file_mtime,include_file_ctime

especially because each git checkout may update more mtimes and ctimes than strictly necessary.

To monitor the effectiveness of ccache, before starting each build run

 $ ccache --zero-stats
 $ watch ccache --show-stats

## Restoring package
Reverting to an original version of the package can be done by installing the package from repositories with pacman.
