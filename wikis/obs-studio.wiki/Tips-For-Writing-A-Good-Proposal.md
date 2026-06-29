# Tips for Writing a Good Proposal

With the advent of the [OBS Project Bounty Program](https://github.com/obsproject/obs-studio/wiki/OBS-Project-Bounty-Program), the OBS Project is now soliciting proposals for a number of features and bugs that we want to direct community efforts toward. We are using a "Request For Proposals" system, whereby each bounty acts as a specification, and requests that potential developers submit proposals for how they would approach the design and development of the specified feature or bug.

This document is intended to be a guide for would-be bounty hunters who wish to submit a proposal to ensure their proposal has sufficient detail in order to be considered for acceptance.

## Tips

* Be sure your proposal addressed ***all requirements in the "Request For Proposal" section*** of the RFP. This includes any considerations for changes that must be implemented across multiple platforms.
    * We know that not all developers are capable of full cross-platform development, both in terms of API knowledge and physical resources (e.g. hardware for compiling on all platforms). If you have concerns about how your proposal might be implemented on another platform, feel free to submit the proposal with those sections as stubs, and ask the community for help filling them out.
* If your proposal includes changes to the UI, include mockups where possible. These do not need to be fancy, but should at least communicate the concept behind what you intend to change.
* If your proposal requires the use of a new library, please include a discussion of why you chose the given library, and why you did not go with alternatives.
* Implementation details should err on the side of specificity. Detail on any new planned APIs, data structures, and architectural considerations are appreciated.
* Time estimates are not required by any means, and we know that commitment level can vary given open source work is largely done during people's free time. However, a very rough estimate would be appreciated, if reasonable for you to include.