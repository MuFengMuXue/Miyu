# Apache Spark

Apache Spark is an open-source cluster computing framework originally developed in the AMPLab at UC Berkeley. In contrast to Hadoop's two-stage disk-based MapReduce paradigm, Spark's in-memory primitives provide performance up to 100 times faster for certain applications. By allowing user programs to load data into a cluster's memory and query it repeatedly, Spark is well-suited to machine learning algorithms.

## Installation
Install the  package.

## Configuration
Some environment variables are set in .

{| class="wikitable"
|-
! ENV
! Value
! Description
|-
| PATH
|
| Spark binaries
|}

You may need to adjust your  environment variable if your shell inhibits :

 export PATH=$PATH:/opt/apache-spark/bin

## Enable R support
The R package sparkR is distributed with the package but not built during installation. To connect to Spark from R you must first build the package by running

 # $SPARK_HOME/R/install-dev.sh

as described in . You may also wish to build the package documentation following the instructions in .

Once the sparkR R package has been built you can connect using .
