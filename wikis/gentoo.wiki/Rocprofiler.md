[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Rocprofiler&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][GitHub](https://github.com/ROCm-Developer-Tools/roctracer)

**rocprofiler** is the profiler utility for GPGPU programs written in [HIP](https://wiki.gentoo.org/wiki/HIP "HIP").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Profiling]](#Profiling)
    -   [[2.2] [Viewing results]](#Viewing_results)
    -   [[2.3] [Performance Counters]](#Performance_Counters)
        -   [[2.3.1] [Legacy GPUs]](#Legacy_GPUs)
-   [[3] [External resources]](#External_resources)
-   [[4] [References]](#References)

## [Installation]

[[[dev-util/rocprofiler]](https://packages.gentoo.org/packages/dev-util/rocprofiler)[]] pulls [HIP](https://wiki.gentoo.org/wiki/HIP "HIP") toolchain (provided by [[[dev-util/hip]](https://packages.gentoo.org/packages/dev-util/hip)[]]) along with profiling/tracing libraries, headers, and scripts.

### [Emerge]

Install [[[dev-util/rocprofiler]](https://packages.gentoo.org/packages/dev-util/rocprofiler)[]]:

`root `[`#`]`emerge --ask dev-util/rocprofiler`

## [Usage]

Detailed usage can be found in [rocprof document](https://docs.amd.com/bundle/AMD-ROCProfiler-User-Guide-v5.1/page/rocprof_Command_Line_Tool.html).

### [Profiling]

To simply profile GPU kernels in a program, run the following command:

`user `[`$`]`rocprof `

This will generate a `results.csv` containing execution duration of kernels.

To simply trace a program, collecting HIP/HSA API calls and kernel execution details, run the following command:

`user `[`$`]`rocprof --sys-trace `

This will further generates `results.json`， which is a standard trace file.

Full command line arguments can be viewed by running `rocprof --help`.

### [Viewing results]

There are various viewers, including [Chromium](https://wiki.gentoo.org/wiki/Chromium "Chromium") and [perfetto](https://ui.perfetto.dev/).

Using `chrome://tracing` to load and view trace files should be the simplest method, and does not require network.

Note that Debian has stripped the tracing ^[\[1\]](#cite_note-1)^ of its chromium package.

### [Performance Counters]

** Warning**\
Gentoo has stripped out the [proprietary AQL profiler library](https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.2.1/page/Overview_of_ROCm_Installation_Methods.html#d3219e567). AQL may refer to [architected queuing language](https://llvm.org/docs/AMDGPUUsage.html#hsa-aql-queue) or [asynchronous queuing language](https://docs.amd.com/bundle/ROCDebugger_User_and_API/page/index.html). Use the following workaround only if you\'re willing to accept AMD\'s proprietary EULA at `/opt/rocm-5.5.0/share/doc/hsa-amd-aqlprofile` after extracting the `.deb` package.

Accessing performance counters requires the use of the proprietary AQL profiler library, which has been stripped from Gentoo. Thus, rocprofiler will crash when one attempts to list or record performance counters.

`user `[`$`]`rocprof --list-basic `

    RPL: on '230607_034945' from '/usr' in '/root':
    Basic HW counters:
    /usr/bin/rocprof: line 389:   574 Segmentation fault      (core dumped) /usr/bin/rocprof-ctrl

To restore performance counters, edit `dev-libs/rocr-runtime` and remove `"$/$-4.3.0_no-aqlprofiler.patch"`, then edit `dev-util/rocprofiler` and remove `"$/$-4.3.0-no-aqlprofile.patch"` and `"$/$-5.3.3-remove-aql-in-cmake.patch`. Finally, obtain a copy of `libhsa-amd-aqlprofile64.so` (as of writing, it\'s `libhsa-amd-aqlprofile64.so.1.0.50500`) from [https://repo.radeon.com/rocm/apt/debian/pool/main/h/hsa-amd-aqlprofile/](https://repo.radeon.com/rocm/apt/debian/pool/main/h/hsa-amd-aqlprofile/) by extracting the apt package. Finally, copy `libhsa-amd-aqlprofile64.so.1.0.50500` to `/usr/lib64/` and create a symlink `libhsa-amd-aqlprofile64.so` to the versioned library.

According to Gentoo developer Marek Szuba:

> For the record, this profiler has long since been deprecated in favour of RCP ([https://github.com/GPUOpen-Tools/radeon_compute_profiler](https://github.com/GPUOpen-Tools/radeon_compute_profiler)). Between that and it being proprietary, I would very much advise against adding it to the tree. And yes, candrews and I *will* eventually get to packaging RCP for Gentoo :-)

While it\'s generally true, if raw performance counters are needed, there\'s no alternative way than using `rocprofile` and `hsa-amd-aqlprofile`. Thus, the writer of this Gentoo Wiki article believes that the long-term solution is making proprietary library an opt-in option by a USE flag.

#### [Legacy GPUs]

** Note**\
One can find ebuilds for historical hsa-amd-aqlprofile versions at this 3rd-party overlay: [https://github.com/justxi/rocm/tree/master/media-libs/hsa-amd-aqlprofile](https://github.com/justxi/rocm/tree/master/media-libs/hsa-amd-aqlprofile). For Polaris (gfx803), it\'s supported by `hsa-amd-aqlprofile-4.3.0`.

Furthermore, older graphics cards are not supported by `hsa-amd-aqlprofile`. Due to its proprietary nature, it\'s not possible to patch the source to re-enable support (unlike how pre-VEGA hardware is re-enabled in `dev-libs/rocm-opencl-runtime`). But it\'s possible to install older versions of the library.

`user `[`$`]`rocprof --list-basic `

    RPL: on '230607_065133' from '/usr' in '/usr/local/lib'
    Basic HW counters:
    ERROR: rocprofiler_iterate_info(), Translate(), ImportMetrics: bad block name 'GRBM', GFXIP is not supported(gfx803)

## [External resources]

-   [AMD ROCProfiler User Guide v5.1](https://docs.amd.com/bundle/AMD-ROCProfiler-User-Guide-v5.1/page/rocprof_Command_Line_Tool.html) -- The official user guide

## [References]

1.  [[[↑](#cite_ref-1)] [[https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=922431](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=922431)]]