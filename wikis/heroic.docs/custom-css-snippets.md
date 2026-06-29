# Custom CSS Snippets

Heroic has a feature to use [custom CSS themes](https://github.com/Heroic-Games-Launcher/HeroicGamesLauncher/wiki/Custom-Themes). This feature is good to style Heroic but users may want to edit the current theme without having to create a custom one, or they want to apply customizations to Heroic that will persist between changing themes without having to apply the same CSS to each theme.

For that, Heroic supports a `Custom CSS` advanced feature in Settings (in the sidebar) > Advanced.

This page collects a few frequently asked customizations.

## Hide store icons in library

```css
.store-icon {
  display: none;
}
```

## Hide `Documentation` sidebar item

```css
[data-tour="sidebar-docs"] {
 display: none !important;
}
```

## Hide donation sidebar item (:()

```css
[data-tour="sidebar-community"] {
 display: none;
}
```

## Hide `Stores` sidebar item

```css
.SidebarItemWithSubmenu:has([data-tour="sidebar-stores"]) {
 display: none;
}
```

## Change size of library cards

```css
.gameList {
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
}
```

Replace the `200px` with values.

## Hide `New version available!` badge in library

```css
.gameCardUpdateBadge {
  display: none;
}
```
