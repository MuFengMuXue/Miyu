# Custom Themes

This page is meant for users wanting to create custom themes for Heroic Games Launcher.

## How To

To create a theme, you only need to place one `.css` file (and only one for each theme) with CSS definitions in a specific location defined by the user in the Accessibility settings.

Once a custom theme is selected, Heroic injects the content of the `.css` file in the body of the app. Any CSS rule applies for themes too (specificity, valid properties/values, etc).

## Themes Location

Heroic does not enforce a specific locations for custom themes. Users must specify a folder to look for `.css` files in the Accessibilty configuration. Once the path is set, Heroic will parse the content of that folder and include any `.css` file in the `Select Theme` drop down.

## Naming Conventions

### File name

In order for the theme to work properly, there are some considerations to follow:
- Only `.css` files are used as themes
- Files can include any type of character, keep in mind complex file names may create issues with the CSS rules (we recommend sticking to simple CSS-class-friendly file names)

### CSS body class

Heroic will set a CSS class in the body element based on the theme's file name:
- The `.css` extension is removed form the name
- Any white space and dot (`.` character) is replaced with a `_`
- Uncommon characters are used as-is and not removed (this may affect your CSS definitions)

Examples:
- `my-theme.css` will set the class `my-theme`
- `My Theme.css` will set the class `My_Theme`
- `Crazy?Theme?.css` will set the class `Crazy?Theme?`

If using uncommon characters like `?` in the file name, to properly match them as CSS selectors you have to escape them. From the previous example, the CSS selector will be `.Crazy\?Theme\?`.

### Reserved Names

Heroic includes this CSS classes for the built-in themes: `default`, `classic`, `old-school`, `dracula`, `marine`, `marine-classic`, `zombie`, and `zombie-classic`.

We recommend NOT using them as file names unless you want to extend the built-in style, since the theme's styles are always included.

## General Tips When Creating Themes

- You can turn on devtools in Heroic by clicking the tray icon > Debug, you can use that to inspect the selectors you need
- You can check the current themes files for idea on some common selectors and CSS variables for theming https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/blob/main/src/frontend/themes.scss
- You can check the main CSS files for available CSS variables https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/blob/main/src/frontend/index.scss#L1
- When editing a theme, you must unselect > reselect it in for Heroic to reload it
- CSS supports selectors nesting as a native feature, but it's different than SASS/SCSS nesting, be sure to use the correct syntax if using nesting

## General Tips When Sharing Themes

- You can submit and find community themes at https://github.com/Heroic-Games-Launcher/heroic-themes
- Don't overuse animations/transitions (some animations can impact performance a lot)
- Use the body class name as the base selector for all rules
- If linking to external resources, make sure they are optimized in size and quality

## Custom CSS advanced feature

This page only covers the use of Custom CSS Themes. If you are looking for the `Custom CSS` feature in Settings > Advanced, check [this other page](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/wiki/Custom-CSS-Snippets).
