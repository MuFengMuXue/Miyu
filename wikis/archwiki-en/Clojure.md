# Clojure

Clojure is a dialect of Lisp and a dynamic, functional, general-purpose programming language that targets the Java Virtual Machine, the CLR and JavaScript.

## Installation
Install the  package.

## REPL
To run the REPL, install leiningen by  package. After installation, you will need to create this directory for lein.
 mkdir -p ~/.lein
Then in a terminal type:
 lein repl

## m2 repo location
To change the location of the m2 repo add this to your profiles.clj:
 {:user {:local-repo #=(eval (str (System/getenv "XDG_CACHE_HOME") "/m2"))
         :repositories  {"local" {:url #=(eval (str "file://" (System/getenv "XDG_DATA_HOME") "/m2"))
                                  :releases {:checksum :ignore}}}
         }}
