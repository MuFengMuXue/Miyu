# Snap documentation

**Snaps** are self-contained application packages that work across different Linux distributions on many different platforms, from embedded devices and desktops, to servers and the cloud.

The snap daemon, *snapd*, handles installation, confinement, and updates, allowing developers to focus on their applications while users get a consistent experience across platforms.

Snap packages and snapd solve the problem of inconsistent application packaging and deployment by providing a unified system that works the same way regardless of the underlying Linux distribution or hardware.

Snaps are useful for application developers seeking a universal packaging solution, system administrators managing diverse Linux environments, IoT and embedded device makers, and organizations where security and consistent deployments are priorities.

For guidance on building snaps, see the [Snapcraft build-tool documentation](https://documentation.ubuntu.com/snapcraft/stable/).

## In this documentation

### First steps

Get snap running and take a tour of its core features before diving deeper.

* **Install snapd**: [Install the snap daemon](https://snapcraft.io/docs/tutorials/install-the-daemon/) • [Distribution support](https://snapcraft.io/docs/reference/administration/distribution-support/)
* **Explore snap**: [Get started](https://snapcraft.io/docs/tutorials/get-started/) with snap's main features on a single page

### Managing snaps

Install, configure, and maintain snaps day-to-day. Control updates, interfaces, services, and data.

* **Configuration**: [Configure snaps](https://snapcraft.io/docs/how-to-guides/manage-snaps/configure-snaps/) • [Apps and aliases](https://snapcraft.io/docs/how-to-guides/manage-snaps/apps-and-aliases/) • [Set system options](https://snapcraft.io/docs/how-to-guides/manage-snaps/set-system-options/) • [Configure snaps with confdb](https://snapcraft.io/docs/how-to-guides/manage-snaps/configure-snaps-with-confdb/)
* **Updates**: [Manage updates](https://snapcraft.io/docs/how-to-guides/manage-snaps/manage-updates/) • [Manage validation sets](https://snapcraft.io/docs/how-to-guides/manage-snaps/manage-validation-sets/)
* **Services and resources**: [Control services](https://snapcraft.io/docs/how-to-guides/manage-snaps/control-services/) • [Use quota resources](https://snapcraft.io/docs/how-to-guides/manage-snaps/use-resource-quotas/) • [Create data snapshots](https://snapcraft.io/docs/how-to-guides/manage-snaps/create-data-snapshots/) • [Disk space awareness](https://snapcraft.io/docs/how-to-guides/manage-snaps/disk-space-awareness/) • [Data locations](https://snapcraft.io/docs/reference/administration/data-locations/)  • [Work with components](https://snapcraft.io/docs/how-to-guides/manage-snaps/using-components/)
* **Troubleshooting**: [Fix common issues](https://snapcraft.io/docs/how-to-guides/manage-snaps/fix-common-issues/)

### Security and confinement

Understand how snaps use Linux security technologies to isolate applications and protect your system.

* **Confinement**: [Snap confinement](https://snapcraft.io/docs/explanation/security/snap-confinement/) • [Classic confinement](https://snapcraft.io/docs/explanation/security/classic-confinement/) • [Security policies](https://snapcraft.io/docs/explanation/security/security-policies/)
* **Interfaces**: [All about interfaces](https://snapcraft.io/docs/explanation/interfaces/all-about-interfaces/) • [Interface auto-connection](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/) • [Interface hooks](https://snapcraft.io/docs/explanation/interfaces/interface-hooks/) • [Super-privileged interfaces](https://snapcraft.io/docs/explanation/interfaces/super-privileged-interfaces/) • [Connect interfaces](https://snapcraft.io/docs/how-to-guides/manage-snaps/connect-interfaces/) • [Interface reference](https://snapcraft.io/docs/reference/interfaces/)
* **Verification**: [Assertions](https://snapcraft.io/docs/explanation/security/assertions/) • [Snapd release process](https://snapcraft.io/docs/explanation/security/snapd-release-process/)

### Snap development

For guidance on building snaps, see the [Snapcraft build-tool documentation](https://documentation.ubuntu.com/snapcraft/stable/).

Extend snap functionality using the REST API, internal tooling, and in-development features.

* **APIs and tools**: [REST API](https://snapcraft.io/docs/how-to-guides/snap-development/use-the-rest-api/) • [Use snapctl](https://snapcraft.io/docs/how-to-guides/snap-development/use-snapctl/) • [Environment variables](https://snapcraft.io/docs/reference/development/environment-variables/) • [Supported snap hooks](https://snapcraft.io/docs/reference/development/supported-snap-hooks/) • [API authentication and authorization](https://snapcraft.io/docs/explanation/security/api-authentication-and-authorization/)
* **Publishing**: [Public, private and unlisted snaps](https://snapcraft.io/docs/reference/administration/public-private-unlisted-snaps/)
* **Desktop integration**: [XDG desktop portals](https://snapcraft.io/docs/explanation/snap-development/xdg-desktop-portals/)
* **Testing**: [Using snap try](https://snapcraft.io/docs/how-to-guides/snap-development/snap-try/) • [Install modes](https://snapcraft.io/docs/explanation/snap-development/install-modes/) • [Debug snaps](https://snapcraft.io/docs/how-to-guides/snap-development/debug-snaps/) • [Test snapd fixes](https://snapcraft.io/docs/how-to-guides/snap-development/test-snapd-fixes/) • [In-development features](https://snapcraft.io/docs/reference/development/experimental-features/)
* **YAML schemas**: [The snap.yaml](https://snapcraft.io/docs/reference/development/yaml-schemas/the-snap-format/) • [Gadget snap](https://snapcraft.io/docs/reference/development/yaml-schemas/the-gadget-snap/) • [Kernel snap](https://snapcraft.io/docs/reference/development/yaml-schemas/the-kernel-snap/)

### System internals

Understand how the snap system works: updates, channels, confinement, storage, and performance.

* **Updates and versions**: [Refresh awareness](https://snapcraft.io/docs/explanation/how-snaps-work/refresh-awareness/) • [Channels and tracks](https://snapcraft.io/docs/explanation/how-snaps-work/channels-and-tracks/) • [Revisions](https://snapcraft.io/docs/explanation/how-snaps-work/revisions/) • [Transactional updates](https://snapcraft.io/docs/explanation/how-snaps-work/transactional-updates/) • [Snap deltas](https://snapcraft.io/docs/explanation/how-snaps-work/snap-deltas/)
* **Components and configuration**: [Snap components](https://snapcraft.io/docs/explanation/how-snaps-work/snap-components/) • [Confdb configuration mechanism](https://snapcraft.io/docs/explanation/how-snaps-work/confdb-configuration-mechanism/) • [Parallel installs](https://snapcraft.io/docs/explanation/how-snaps-work/parallel-installs/) • [Network requirements](https://snapcraft.io/docs/reference/administration/network-requirements/) • [Timer string format](https://snapcraft.io/docs/reference/administration/timer-string-format/)
* **Performance**: [Snap performance](https://snapcraft.io/docs/explanation/how-snaps-work/snap-performance/) • [System architecture](https://snapcraft.io/docs/reference/system-architecture/)

## How this documentation is organised

This documentation uses the [Diátaxis documentation structure](https://diataxis.fr/).

* [Tutorials](https://snapcraft.io/docs/tutorials/) take you step-by-step through building and deploying your first Ubuntu Core image.
* [How-to guides](https://snapcraft.io/docs/how-to-guides/) provide instructions for specific tasks like customizing snaps, deploying to platforms, and managing devices.
* [Reference](https://snapcraft.io/docs/reference/) provides technical specifications, formats, and details you need while working.
* [Explanation](https://snapcraft.io/docs/explanation/) provides conceptual context about architecture, security, storage, and update mechanisms.

## Project and community

Snap and Snapcraft are members of the Ubuntu family. They're both open source projects that welcome community involvement, contributions, suggestions, fixes and constructive feedback.

* [Our Code of Conduct](https://ubuntu.com/community/code-of-conduct)
* [Get support](https://forum.snapcraft.io/c/snap/14)
* [Join the Discourse forum](https://forum.snapcraft.io/)
* [Interactive chat on Matrix.org](https://matrix.to/#/#snapd:ubuntu.com)
* [Contribute to our documentation](https://snapcraft.io/docs/contributing/)
* [Project roadmap](https://forum.snapcraft.io/t/the-snapd-roadmap/1973)

Thinking about using snap for your next project? [Get in touch!](https://forum.snapcraft.io/)
