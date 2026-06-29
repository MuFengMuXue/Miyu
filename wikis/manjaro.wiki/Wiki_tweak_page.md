Other languages:

[English] • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Wiki_tweak_page/tr "Wiki düzenleme sayfası (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Wiki_tweak_page/ru "Страница настройки Вики (100% translated)")

## Contents

-   [[1] [How to create templates]](#How_to_create_templates)
    -   [[1.1] [Usage]](#Usage)

## [How to create templates]

**If you feel a template is missing or needs improvement?**

------------------------------------------------------------------------

Use this [Discussion link](//wiki.manjaro.org/index.php?title=Talk:Wiki_tweak_page "Talk:Wiki tweak page") and discuss the change with your fellow editors.

Before creating new templates the existing [Template collection](//wiki.manjaro.org/index.php?title=Help:Template "Help:Template") and preferably use one of them.

Create a new page to serve as base

    Example: http://wiki.manjaro.org/index.php/Template:TemplateNameBase

After creating the page, edit it by taking the code below as example

    <noinclude>}</noinclude>
    <includeonly>}}|}}|#rgb|#rgb}}</includeonly>

Template arguments explained

\- rgb is the hex code for the border\'s color. - rgb is the hex code for the background color. - Box is the template where these templates take their formatting.

Save your Template Base page and create a new page.

    Example: http://wiki.manjaro.org/index.php/Template:TemplateName

After creating the page, edit it and use below code as example

    <noinclude>}</noinclude>
    <includeonly>}}}}}}</includeonly>

Always preview your changes and fix bugs before you finally save the new template

### [Usage]

}