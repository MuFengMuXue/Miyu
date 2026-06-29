# Common Lisp

Common Lisp is a highly dynamic, multi-paradigm language that emphasizes interactivity and performance. Being fully standardized, there are multiple independent implementations from which to choose.

## Installation
 (http://www.sbcl.org/) is the most popular FOSS implementation and generally has the highest compatibility across the ecosystem. Its compiler produces native machine code and the project has monthly releases.

It is configured in Lisp within , but you may not need this depending on the dependency management strategy you choose.

## Alternate implementations
There are numerous other implementations available. Apart from the options below, there are two major commercial Lisp implementations, Allegro and LispWorks, but they have strict licensing terms are not packaged within the Arch Linux ecosystem.

## Active
These function seamlessly with modern tooling and can be used for serious projects.

*
*
*
*

## Historical
While packages are available for these, library and tooling compatibility is sometimes dubious, and some implementations are no longer actively maintained.

*
*
*
*

## Dependency management
Dependency management in Common Lisp has traditionally involved Quicklisp, but in recent years modern alternatives have emerged.

## Vend
Vend is a simple tool for downloading and accessing dependencies directly within your project repository. It requires no special configuration.

After installing the  package, you can run  from the top directory of your project:

 Downloading dependencies.
 [vend Fetching FN-MACRO
 Fetching ARROW-MACROS
 [vend Fetching TRANSDUCERS
 ...
 Done.

After which  will start a REPL session.

## Editor integration
## Emacs
For Emacs users of Sly/Slime, the in-editor REPL can be configured via:

 (setq sly-default-lisp 'sbcl
       sly-lisp-implementations '((sbcl ("vend" "repl" "sbcl")  :coding-system utf-8-unix)
                                  (ecl  ("vend" "repl" "ecl")   :coding-system utf-8-unix)))

You're free to add other compilers in a similar manner. Adjust as necessary for Slime.

## Lem
Users of Lem can open a REPL with:

 C-u M-x slime  vend repl

## Vim
Unlike Emacs which supports multiple running Lisps, Slimv requires one standalone server that persists through Vim restarts.

If we want our dependencies in  to be visible to Slimv, we must start its server manually from our project directory:

 > cd project/
 > vend repl ecl --load /home/YOU/.vim/pack/common-lisp/start/slimv/slime/start-swank.lisp

Now,  (REPL Connect) within Vim will automatically find the running server, and you can load any system available in your project and in .

If you want to switch projects, you would need to quit the REPL server manually and restart it as above. You may also wish to set a shell alias or create a wrapper script for the long invocation shown above.

## OCICL
[https://github.com/ocicl/ocicl OCICL is a modern alternative to Quicklisp that distributes packages as OCI-compliant artifacts from centralised package repositories. Similar to Quicklisp, it must be configured by the user to take over and manage dependency loading.

After installing , run , which adds the following to your compiler configuration files:

 #-ocicl
 (when (probe-file #P"/home/green/.local/share/ocicl/ocicl-runtime.lisp")
   (load #P"/home/green/.local/share/ocicl/ocicl-runtime.lisp"))
 (asdf:initialize-source-registry
   (list :source-registry (list :directory (uiop:getcwd)) :inherit-configuration))

Now, within a REPL, any attempt to run  on an unknown dependency will automatically download it. Further project configuration is done with a  file, which you're intended to commit to your project repository. See the README for more setup and usage details.

## Quicklisp
Quicklisp is the original method for fetching and loading libraries into a Common Lisp program. By default it has a single, global package cache shared by all programs on your machine, and it pulls packages from a conservatively updated repository also called (perhaps confusingly) Quicklisp.

After installing the  package, it can be registered for a particular compiler as follows:

 > sbcl --load /usr/share/quicklisp/quicklisp.lisp
 * (quicklisp-quickstart:install)
 * (ql:add-to-init-file)

After which  can be used in all future REPL sessions to load a dependency, downloading it if necessary.

To update all packages installed through Quicklisp, run the following in a REPL:

 (ql:update-all-dists)

## Ultralisp
Ultralisp is an alternate Quicklisp repository that offers rolling releases of all packages, generally up-to-date with what is available on Github, etc.

To register it, run the following in a REPL:

 (ql-dist:install-dist "http://dist.ultralisp.org/" :prompt nil)

Then, if a package you load via  is newer in Ultralisp, it will be loaded from there instead of Quicklisp.

## Qlot
Alternatively, if you're fine with Quicklisp but want project-local dependencies, you can use Qlot ().

Once installed, a project repository can be initialized to use it via:

 qlot init

## Custom dependencies
With Qlot, all custom dependency locations are declared within a . For instance, to declare Ultralisp usage, simply add:

 dist http://dist.ultralisp.org

Or to specify a dependency on your local filesystem:

 local foobar /home/you/code/common-lisp/foobar

See Qlot's README for more options.

To install declared dependencies, run:

 qlot install

## Invoking a REPL
To load a REPL with the current Qlot environment, run:

 qlot exec sbcl

For Emacs users of Sly/Slime, consider configuring how your in-editor REPL is launched via:

 (setq sly-default-lisp 'qlot-sbcl
       sly-lisp-implementations '((qlot-sbcl ("qlot" "exec" "sbcl") :coding-system utf-8-unix)))

Adjust as necessary for Slime.

## Guix
Guix can be also used to download Common Lisp tools and libraries.

## Development environments
## Emacs
Common Lisp development is often done in Emacs, through slime or the newer sly. Both are widely adopted in the community and have a similar usage interface.

## Portacle
Portacle is an Emacs-based, all-in-one environment for Common Lisp development. Its aim is to easily on-ramp beginners to Lisp.

## Lem
Lem () is a newer editor in the style of Emacs, but written and configured entirely in Common Lisp. It has terminal and GUI frontends, and supports many languages.

## Vim
Slimv is a port of Slime from Emacs that utilizes Slime’s Swank backend server for a very similar experience to Emacs. To install the plugin manually:

 mkdir -p ~/.vim/pack/common-lisp/start
 cd ~/.vim/pack/common-lisp/start
 git clone --depth 1 https://github.com/kovisoft/slimv.git

Restart Vim and open a Common Lisp file. Slimv should be active, and  will start a REPL server and connect you to it.

## VSCode
Support for Common Lisp in VSCode is weakest among the editors, but still possible. The Alive plugin serves as a complete development environment alongside its own LSP, which requires manual installation.

## Tips
## Managing init files
Library authors often test their code with multiple compiler implementations. However, each implementation has their own uniquely named init file, such as  or , but the content of these files is often identical. Rather than handwrite these files for each compiler, you can create one master file and symlink the others to it. For instance, if you consider  to be your "master config", then:

 ln -s /home/you/.sbclrc .eclrc
 ln -s /home/you/.sbclrc .abclrc

And so on. The main init files are:

 ~/.sbclrc          # for SBCL
 ~/.abclrc          # for ABCL
 ~/.ccl-init.lisp   # for CCL
 ~/.clasprc         # for CLASP
 ~/.eclrc           # for ECL
 ~/.clisprc.lisp    # for CLISP
 ~/.cmucl-init.lisp # for CMUCL
 ~/.mkclrc          # for MKCL
 ~/.clinit.cl       # for Allegro

## Less verbose compilation output
SBCL in particular can be quite enthusiastic about the number of compiler "notes" it outputs. To silence these notes, while still displaying the usual errors and warnings, set the following in your :

 (declaim (sb-ext:muffle-conditions sb-ext:compiler-note))

## Troubleshooting
## Quicklisp can not load a local project
 is used to load both external dependencies but also local projects. However, if your local project is not located under , it will fail to load (or may even be pulled from online if you've published it).

In truth, Quicklisp is just fetching and organizing packages. Internally, it uses the ASDF build system to actually load them. It's also possible to load any local project or a package you've already downloaded via , and by default ASDF only looks in  for local projects.

While configurable, a simpler way around this is to use a symlink:

 ln -s /home/you/code/common-lisp/ common-lisp

## What are Projects, Systems, and Packages?
The rest of this article has used the term "package" in the way it is usually used in other programming languages, synonymous with "library". However, although standardized in the mid-90s, the earliest forms of Common Lisp date from the 80s, and so terms involving project management differ. In essence:

* Project: A group of systems. Sometimes called a "workspace" in other languages.
* System: A group of packages. These can represent both libraries and "executables".
* Package: A group of functions and type definitions. Often called a "module" in other languages, but can span multiple files.

As you can see, what is usually called a library elsewhere is known as a "system" in Common Lisp. Hence the name . See here for an example of an inter-depending, multi-system project.
