## A Registered Categories

This section contains a number of well known categories and suggestions on how to use them:

- The [list of Main Categories](category-registry.md#main-category-registry "A.1. Main Categories") consists of those categories that every conforming desktop environment MUST support.

- The [list of Additional Categories](additional-category-registry.html "A.2. Additional Categories") provides categories that can be used to provide more fine grained information about the application.

- The [list of Reserved Categories](reserved-category-registry.html "A.3. Reserved Categories") contains categories that have a desktop-specific meaning.

Note that category names are case-sensitive.

## A.1 Main Categories

By including one of the Main Categories in an application's desktop entry file, the application will be ensured that it will show up in a section of the application menu dedicated to this category. If multiple Main Categories are included in a single desktop entry file, the entry may appear more than once in the menu.

Category-based menus based on the Main Categories listed in this specification do not provide a complete ontology for all available applications. Category-based menu implementations SHOULD therefore provide a "catch-all" submenu for applications that cannot be appropriately placed elsewhere.

The table below lists all Main Categories.

| Main Category | Description | Notes |
|----|----|----|
| AudioVideo | Application for presenting, creating, or processing multimedia (audio/video) |   |
| Audio | An audio application | Desktop entry must include AudioVideo as well |
| Video | A video application | Desktop entry must include AudioVideo as well |
| Development | An application for development |   |
| Education | Educational software |   |
| HealthFitness | Applications related to physical or mental health and fitness |   |
| Game | A game |   |
| Graphics | Application for viewing, creating, or processing graphics |   |
| Network | Network application such as a web browser |   |
| Office | An office type application |   |
| Science | Scientific software |   |
| Settings | Settings applications | Entries may appear in a separate menu or as part of a "Control Center" |
| System | System application, "System Tools" such as say a log viewer or network monitor |   |
| Utility | Small utility application, "Accessories" |   |
