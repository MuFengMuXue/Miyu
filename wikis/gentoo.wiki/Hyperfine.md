[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Hyperfine&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Package information](https://packages.gentoo.org/packages/app-benchmarks/hyperfine)

[[]][GitHub](https://github.com/sharkdp/hyperfine)

[[]][Official documentation](https://github.com/sharkdp/hyperfine/blob/master/README.md)

**Hyperfine** is a command-line benchmarking tool. It runs an analysis across multiple runs, has support for arbitrary shell commands, and can export results to various formats.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Basic Benchmarks]](#Basic_Benchmarks)
    -   [[2.2] [Warmup runs]](#Warmup_runs)
    -   [[2.3] [Exporting results]](#Exporting_results)

## [Installation]

### [USE flags]

### [USE flags for] [app-benchmarks/hyperfine](https://packages.gentoo.org/packages/app-benchmarks/hyperfine) [[]] [A command-line benchmarking tool]

  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`debug`](https://packages.gentoo.org/useflags/debug)   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  ------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-01-05 19:35] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-benchmarks/hyperfine`

## [Usage]

### [Basic Benchmarks]

The simplest benchmark you can run is likely the `sleep` command. For example:

`user `[`$`]`hyperfine 'sleep 0.3'`

### [Warmup runs]

Warmup runs will likely come in handy if you are running a program that is I/O intensive, like [grep](https://wiki.gentoo.org/wiki/Grep "Grep"). This is because benchmarks can be heavily influenced by whether the disk caches are warm or cold.

If you wish to benchmark for a warm cache, you can run

`user `[`$`]`hyperfine --warmup 3 'grep -R TODO *'`

For cold caches, you can use the `-p`/`--prepare` option to run a special command before each timing run.

`user `[`$`]`hyperfine --prepare 'sync; echo 3 | sudo tee /proc/sys/vm/drop_caches' 'grep -R TODO *'`

### [Exporting results]

You can export hyperfine results to a various amount of formats, for markdown you would use `--export-markdown <file>` to create a table of the results.

The JSON output is more detailed and can be used in plotting charts.