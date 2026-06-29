If you want to test a new feature on a PR with a label `Seeking Tester`,
you can download the package and try it.

## Steps to download

### Create Github account

If you have not created Github account, you need to create your account before downloading.
If you have your account, you just need to log-in to Github.

### Downloading from PR

1. At first, go to the PR that you want to test.
2. Scroll down and find `All checks have passed` and click a button `Show all checks`.
   ![obs-pr-show-checks-button](https://user-images.githubusercontent.com/780600/156292381-484b3f9b-62da-4374-8542-9b39f076fa55.png)
3. Once `CI Multiplatform Build` appears, click a link `Details`.
   ![obs-pr-detail-button](https://user-images.githubusercontent.com/780600/156292409-829bbdd8-08af-45fb-8d31-e338d0ffbcaa.png)
4. Build results will be displayed. Click `Summary` on the top left.

   ![obs-actions-summary-button](https://user-images.githubusercontent.com/780600/156292434-878f0782-1e91-4a29-8f26-d11dfd00acc5.png)
5. Find a section `Artifacts` on the bottom. Finally, download the package you want to test.
   ![obs-actions-artifact-list](https://user-images.githubusercontent.com/780600/156292453-c01beeb8-1264-4357-bc5e-535a7ab676ba.png)

Note that the binary packages are not available for PRs without the label `Seeking Tester`.
