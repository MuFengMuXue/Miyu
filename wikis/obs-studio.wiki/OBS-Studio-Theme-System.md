# Overview

OBS uses the Qt Development Framework for the implementation of its UI. Specifically it uses the Qt Widgets system.

> Styles (classes that inherit QStyle) draw on behalf of widgets and encapsulate the look and feel of a GUI. The QStyle class is an abstract base class that encapsulates the look and feel of a GUI. Qt's built-in widgets use it to perform nearly all of their drawing, ensuring that they look exactly like the equivalent native widgets.

[_Styles and Style Aware Widgets - Qt Documentation_](https://doc.qt.io/qt-6/style-reference.html)

Qt Style Sheets are a powerful mechanism that allows you to customize the appearance of widgets, in addition to what is already possible by subclassing QStyle. The concepts, terminology, and syntax of Qt Style Sheets are heavily inspired by HTML Cascading Style Sheets (CSS) but adapted to the world of widgets.

The result of this is a style sheet file with the extension .qss. The appearance of OBS Studio is dictated almost entirely by these style sheet files. 

> [!IMPORTANT]  
> QSS is very similar to CSS, but it is important to remember that it is **NOT** CSS. Not all features of CSS are available and some properties may behave slightly differently than expected. There are also properties unique to certain widgets that can be customized with QSS.

[_Qt Style Sheets Reference_](https://doc.qt.io/qt-6/stylesheet-reference.html)

# Composable Themes

As of version 30.2, OBS Studio expands upon these style sheets with additional functionality in order to streamline our theme work and allow for easier customization by users. 

Theme files will largely remain QSS, but have custom sections for OBS-specific data. They may contain variables that need to be subsituted with values, and as such are not directly loadable as QSS files. All themes in this new system must make use of the Qt search path prefix (`theme:`) to identify external assets (images, SVGs, etc.).

# Theme Files

The result of these additions is three new file types which are combined and processed to output a resulting Qt Style Sheet.

- **O**BS **B**ase **T**heme (.obt)
- **O**BS **V**ariant **T**heme (.ovt)
- **O**BS **H**igh-Contrast **A**djustment (.oha)

A **Base Theme** defines the core aspects of a theme. Most if not all of a given appearance for the app should be contained within this file. The appearance of all widgets needs to be defined in this file or Qt will fallback to it's default appearance for widgets, which may not be as desired and will vary by operating system.

> [!WARNING]  
> Yami contains many core definitions for the appearance of widgets throughout the app.
>
> If you are developing custom themes it is **highly recommended** that you use Yami as a Base Theme and apply your changes in a Variant Theme. If you create your own Base Theme, you are opting out of the OBS appearance for all widgets and will be responsible for keeping your base theme up to date with every new release!
>
> Do **NOT** copy Yami into a new base theme only to make minor changes or adjustments. Your theme is likely to break with new releases of OBS!

A **Variant Theme** contains modifications or additions to a base theme. Any variables declared in a variant theme will override those in the base theme. The style sheet rules of the variant theme will then be **appended** to the end of the base theme. Similar to CSS the rules of both files will be applied, with specificity being the final arbiter. Variant themes must ensure their rules at least match the specificity of any base theme rules they wish to change as well as unset any values they may want removed. Note that a variant theme can also extend another variant theme as long as the top level theme in the dependency chain is a base theme.

## File Locations

New theme files and assets should be stored in the user configuration theme data folder rather than OBS's install directory. This applies both to new base themes as well as variants for existing themes.

The mandatory `theme:` search path prefix for external assets searches both the OBS install directory and user configuration directory. This makes it possible to reuse assets that ship with core OBS without having to copy them or require theme files to be put into the OBS installation directory. For example, `url(theme:Dark/unassigned.svg)` will first look for the file in OBS's core files, then in the user theme data folder.

Default user theme folder locations:

- **Windows:** `%APPDATA%\obs-studio\themes`
- **macOS:** `~/Library/Application Support/obs-studio/themes`
- **Linux** (non-Flatpak)**:** `${XDG_CONFIG_HOME}/obs-studio/themes`
- **Linux** (Flatpak)**:** `~/.var/app/com.obsproject.Studio/config/obs-studio/themes`

# OBS Theme Data

These theme files support two new OBS-specific blocks: **@OBSThemeMeta** and **@OBSThemeVars**

> [!CAUTION]
> It is important that both these special at-rule style blocks are at the top of the file. The parser will strip any lines up to and including the end of the final OBS-specific object before it is passed to Qt.

### @OBSThemeMeta

This block contains information about the theme and has specific properties.

| Key  | Value |
| ------------- | ------------- |
| name  | The display name of this theme or style to show in the settings dropdown |
| id  | Unique identifier for identifying this theme internally |
| author | Creator of this theme or style |
| dark  | Indicates if the visual appearance of this theme is dark for matching certain UI elements such as icons |
| extends | The id of another theme that this theme inherits from before providing overrides. Used only in theme variants |

```css
OBSThemeMeta {
    name: 'Example';
    id: 'com.obsproject.Yami.ExampleVariant';
    extends: 'com.obsproject.Yami';
    author: 'Warchamp7';
    dark: 'true';
}
```

### @OBSThemeVars

This block contains declarations for variables to be used throughout the rest of the style sheet. These declarations must follow a few specific rules.

- Variable names must be prefixed with two hyphens (--) similar to CSS.
- Variable names can only contain alphanumeric digits and underscores.
- Variable names CANNOT contain dashes like in CSS.

> [!IMPORTANT]
> Variables can **ONLY** be declared within the @OBSThemeVars block. It is NOT possible to do scoped overrides of variables like in CSS.

| Valid | Example | Notes |
| ------------- | ------------- | ------------- |
| ✅ | `--primary: #0777FF;`  | |
| ✅ | `--danger_color: "red";`  | |
| ✅ | `--warning_text_color1: rgb(200, 255, 40);`  | |
| 🚫 | `--text-color: "white";`  | _Invalid: Hyphens cannot be used in variable names_ |

Variable values can be any valid qss value such as colors, numbers with or without units, keywords, etc. Keywords must be enclosed in quotations when setting variables.

| Valid | Example | Notes |
| ------------- | ------------- | ------------- |
| ✅ | `--padding_small: 2px;` | |
| ✅ | `--border_style: "solid";` | |
| ✅ | `--font_family: "Open Sans";` | |
| 🚫 | `--font-color: yellow;` | _Invalid: String values or keywords must be in quotations_ |

Variables can then be referenced using the var() function similar to CSS. This function can also be used in variable declarations to reference another variable.

| Valid | Example | Notes |
| ------------- | ------------- | ------------- |
| ✅ | `--main_color: "blue";` | |
| ✅ | `--button_color: var(--main_color);` | |
| 🚫 | `--button_color: --main_color;` | _Invalid: Reference is missing var() function_ |
| 🚫 | `--button_color: var(main_color);` | _Invalid: Variable name is missing -- prefix_ |

This allows for easily defining values to be used throughout the style sheet as well keeping similar styles isolated from each other.

Another added feature of this block is the calc() function. calc() takes exactly 2 values and an operator separated by whitespace for basic arithmetic. You cannot do math with 3 or more values in a single calc but you can nest multiple calc() usages.

> [!IMPORTANT]
> calc() can only be used in the @OBSThemeVars block. It cannot be used in QSS rules.

If two values both contain measurement units the units must match.

| Valid | Example | Notes |
| ------------- | ------------- | ------------- |
| ✅ | `–-padding_base: calc(2px * 3);` | Result: 6px |
| ✅ | `–-padding_large: calc(calc(2px * 3) + 4px);` | Result: 10px |
| ✅ | `-–padding_small: calc(var(--padding_base) / 2);` | Result: 3px |
| 🚫 | `-–unit_mix: calc(2px * 5pt);` | _Invalid: Mixed unit types_ |
| 🚫 | `–-many_values: calc(2 * 4 * 8);` | _Invalid: Too many values_ |
| 🚫 | `–-bad_syntax: calc(2+5);` | _Invalid: Operator not surrounded by whitespace_ |

# Example

A simple example of this structure in action.

**Simple.obt**
```css
@OBSThemeMeta {
  name: "Simple";
  id: "simple_theme";
}

@OBSThemeVars {
  –-main_color: "red";
}

QWidget {
  color: var(--main_color);
}
```

**Blue.ovt**
```css
@OBSThemeMeta {
  name: "Blue";
  id: "simple_blue";
  extends: "simple_theme";
}

@OBSThemeVars {
  –-main_color: "blue";
  -–alt_color: "yellow";
}

QLineEdit {
  color: var(--alt_color);
}
```

In this example, the base theme declares a variable `--main_color` with the color red and applies it as the text color for all QWidgets. Functionally this will change the color of text throughout the majority of the app to red as most widgets inherit from QWidget.

In the variant style, the value of `--main_color` is changed to blue. An additional variable `-–alt_color` unique to the variant is declared with the color yellow and applied only to QLineEdit widgets.

The final result when using the **Simple** theme in the **Blue** style will result in text in the app displaying in blue, with the exception of QLineEdit text which will be yellow. The red color of the base theme is overridden and not used.

**Generated QSS**
```css
/* Simple.obt */
/* main_color overridden in the ovt */
QWidget {
  color: blue;
}

/* Blue.ovt */
/* Style rules in the variant are appended
 * after the contents of the obt */
QLineEdit {
  color: yellow;
}
```

# Theme Development 

The addition of variables and this theme inheritance system significantly improves the workflow of adjusting the appearance of OBS Studio as we no longer have to maintain each of the individual theme style sheets. Instead we simply update the base theme and variants only have to apply their specific changes, rather than be a mostly duplicated QSS file. This also will make it easier for us to offer additional styles going forward.

This also streamlines the ability for users to create their own themes or color variants. In many cases, themes only modify a few colors but they have to maintain an entire copy of the original OBS theme QSS. This is especially problematic when an update makes large changes to an aspect of the UI or introduces entirely new widgets, as a user's custom theme will be missing those new style rules entirely and can often break.

In the future we also intend to allow themes and variants to mark variables as customizable. This will expose those values in the Appearance tab and allow users to customize aspects of the theme like colors, padding, and font size directly in the app.

## Automatic Reload

In order to simplify OBS theme development we added an "auto-reload" feature that will automatically apply changes made to the file(s) of the currently active theme.

To enable this feature look for the `[Appearance]` section in the `user.ini` and add the following:
```ini
AutoReload=true
```

