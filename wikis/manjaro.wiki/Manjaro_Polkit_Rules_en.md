[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-Manjaro+Polkit+Rules&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=Manjaro_Polkit_Rules "Manjaro Polkit Rules (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=Manjaro_Polkit_Rules/tr "Manjaro Polkit Kuralları (56% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=Manjaro_Polkit_Rules/fr "Règles de Manjaro Polkit (100% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=Manjaro_Polkit_Rules/ru "Правила Manjaro Polkit (100% translated)")

## Contents

-   [[1] [What is polkit?]](#What_is_polkit.3F)
-   [[2] [What is polkit rules?]](#What_is_polkit_rules.3F)
-   [[3] [99-manjaro.rules]](#99-manjaro.rules)
-   [[4] [Conclusion]](#Conclusion)
-   [[5] [See Also]](#See_Also)

## [][What is polkit?]

**polkit** is an authorization manager and helps the system to manage who is allowed to do a certain task.

## [][What is polkit rules?]

Rules are definitions of the relationship between an application, the user and the system.

## [99-manjaro.rules]

Manjaro adds some useful rules for actions which would otherwise require the user to authenticate for a given action. The rules added by Manjaro are rules covering where the convenience of the user versus the system security becomes blurred.

Consider the following rules - all part of a ruleset installed on a default Manjaro system.

This first rule enables a user which is member of the administrative group **wheel** to handle disks and partitions without requiring the user to authenticate. This rule covers the usage of removable USB devices. Because of an overlap with the internal devices this rule **also** makes it possible for this administrative user to modify the system\'s internal devices.

    polkit.addRule(function(action, subject)
    });

The second rule allows any user to control if the system should be shut down or restarted

    polkit.addRule(function(action, subject)
    });

The third rule allows the upower daemon to hibernate or suspend the system

    polkit.addRule(function(action, subject)
    });

The fourth rule allows a member of the **network** group to use the bluetooth devices without authentication

    /* Allow users of network group to use blueman feature requiring root without authentication */
    polkit.addRule(function(action, subject)
    });

## [Conclusion]

Manjaro has added these rules to make the system easier - you could say less confusing - to the average user.

The rules is included in a file **99-manjaro.rules** which is installed/maintained using the package **manjaro-hotfixes**

## [See Also]

[polkit documentation](https://www.freedesktop.org/software/polkit/docs/latest/polkit.8.html)

\--Frede H. 14:02, 13 April 2020 (CEST)