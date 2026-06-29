# OBS Project Bounty Program

The OBS Project has worked to create a program where community developers can work on specific new features of OBS Studio for compensation. These features are determined by OBS maintainers to have the potential for high-impact improvement to the product. Design proposals that would fulfill a bounty may be made either by individuals or teams of developers, but the final payout will be made to only one stakeholder.


## Bounty Process Flowchart

1. The OBS team publishes a [Request For Proposals (RFP)](https://github.com/obsproject/obs-studio/discussions/categories/requests-for-proposals-bounties) describing a feature that the team has decided should be prioritized, or a bug that is in need of being researched and fixed.
    * Initial Bounty Status set to **Accepting Proposals**
2. Developers write proposals for how they would implement the feature or fix the bug described in the RFP.
3. The OBS team works with developers to clarify and refine their proposals.
4. A proposal is accepted. The developer(s) responsible for the proposal work to implement the feature or bug fix according to their proposal.
    * Bounty status changed to **In Progress**
5. Pull requests are submitted to implement the proposal by the developers.
    * Bounty status changed to **Under Review**
6. Pull requests are reviewed by project maintainers, and the pull request developers make any changes to the pull requests accordingly.
7. Pull requests are merged into the master branch.
8. Developer(s) submit invoice to the [OBS Project Open Collective](https://opencollective.com/obsproject/projects/obs-project-bounty-program) for bounty amount, confirmed by OBS team members.
    * Bounty status changed to **Claimed**
9. Payment disbursed to developer(s) by the Open Source Collective from OBS Project collective funds.


## How to Claim a Bounty

We've created a process to ensure multiple contributors aren’t competing on the same project, and to make sure work is properly merged into OBS once completed.

1. Read the Request For Proposal document completely.
2. If you want to move forward, submit an proposal to the OBS team on your suggested implementation by replying to the RFP posting. Be sure to include as many details as requested by the spec, and be sure to address each of the completion criteria. For proposals that include UI changes, mockups are strongly encouraged.
    * Be sure to consult the **[Tips for Writing a Good Proposal](https://github.com/obsproject/obs-studio/wiki/Tips-for-Writing-a-Good-Proposal)** for advice on how to author a good proposal.
3. Work with the OBS team to finalize plans for the best implementation. Proposals will be judged on their maintainability, design quality, and adherence to spec. Note that other developers may submit competing proposals at this time as well.
4. If your proposal is accepted, you may begin code implementation that adheres to your proposal and following the [OBS contributing guidelines](https://github.com/obsproject/obs-studio/blob/master/CONTRIBUTING.rst).
5. Submit code as a draft in the appropriate `obsproject` repositories so OBS community leaders can track progress.
6. Once code is complete, remove draft status and notify OBS maintainers.
7. Update code with feedback from core OBS contributors as needed.
8. Wait for your code to be merged into the `master` branch.
9. [Submit an expense to Open Collective](https://opencollective.com/obs-project-bounty-program/expenses/new) for the amount of the bounty.


## Collaboration with OBS team

Collaboration with the OBS team is crucial to having your code pulled into OBS. During the proposal process, clarify any questions you or your team may have as early as possible. During development, use the pull request commenting feature. At any time, you can also comment in the `#development` channel in the OBS Discord server here: [https://obsproject.com/discord](https://obsproject.com/discord), though we encourage you to keep as much discussion on the RFP and pull requests as possible to keep the discussion public.


## Deadlines

If your team does not show code commits or interaction for two weeks at a time as part of an accepted feature bounty, then the bounty will be released for another team to work on. If the task remains in the **Accepting Proposals** state, and the team can demonstrate work on the feature, they can reclaim the task.

If you no longer wish to work on a project that has been granted to you, please notify the OBS team to reset the bounty as **Accepting Proposals**.


## Bounty Valuation

The OBS team currently uses a simple rubric to determine how to price a bounty. Generally speaking, RFPs are evaluated based on two main criteria:

* How complex is the feature/bugfix?
    * How long do we expect it may take to complete?
    * How much specialized knowledge do we expect it will require to implement?
* How high of a demand is there for this feature/bugfix?
    * How many people do we expect this to impact?
    * How frequently are we asked about this feature or bug?
    * How urgently does this need to be implemented?

In general, issues that are higher in complexity and higher in demand are given greater bounties.