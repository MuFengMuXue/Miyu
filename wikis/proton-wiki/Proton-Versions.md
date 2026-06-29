## Proton Stable

This is **the default flavor of Proton** that carries version number next to it, e.g. `Proton 8.0-3`. It's released after extensive QA testing and a public release candidate phase ([example](https://github.com/ValveSoftware/Proton/issues/6240#issue-1412203214)).

[Sometimes](https://twitter.com/Plagman2/status/1595247355879911424) upcoming Proton stable is released as `Proton Next` to facilitate more public testing ahead of a proper release.

## Proton Experimental

This flavor is intended for **public testing of experimental features**. The games that are working only with Proton Experimental (as listed in the [changelog](Changelog)) are tested for regressions prior to the release.

## Proton Hotfix

It's a special version of Proton that contains **targeted fixes for new, important games**. It's used when there's no time to do a proper Stable or Experimental release. **It's intended to be short lived** and be phased out once the fix matures and is released as a part of one of the other flavors.

## Proton Bleeding Edge

This is an **automated and untested** release of Proton that happens on Experimental's beta branch (find Proton Experimental in Steam's Library -> properties -> betas). It automatically picks up latest developemnt in dxvk, vkd3d-proton, dxvk-nvapi, vkd3d and Proton's wine.

**It can eat your game prefix / saves. Use it at your own risk.**