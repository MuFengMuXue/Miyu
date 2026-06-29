### Why Wine is so important

A lot of people in popular discussion forums keep thinking that Wine is
"the last thing that Linux needs" or that it is "not important". We are
listing some info here that is supposed to thoroughly defeat these and
other claims.

### Supply diversification

Diversifying your supply is universally considered to be an important
aspect of risk management.

Yet, The US Department of Justice has
"[found](https://www.usdoj.gov/atr/cases/f3800/msjudgex.htm#iiia)" that
Microsoft Windows is run by more than 95% of personal computers. Even
taking Apple's Mac OS into account, Microsoft Windows is still present
on more than 80% of computers, and this is likely also true in most
other countries, not just in the US. Thus governments, companies and
home users all over the world ultimately depend on a single provider:
Microsoft.

The question is not whether Microsoft has evil intents, or whether it
may go out of business, but whether its plans match yours. A company may
want to deploy thin clients to simplify administration and save money on
per-client Windows licenses. But is Microsoft going to make it viable
and undercut its Windows market? Where is the alternative if Microsoft
implements its software subscription model? If Microsoft is not
interested in catering to your market, then you have no other provider
to turn to.

### Large, homogeneous populations can lead to large problems

Another aspect is that in both society and nature, large homogeneous
populations can allow an otherwise narrow problem to become
catastrophic. In biology, genetically similar individuals share many
vulnerabilities, and in a large enough population, a disease that might
have only infected a few can become a massive epidemic. Societies that
rely too much on [monoculture](https://en.wikipedia.org/wiki/Monoculture)
can suffer famines when their primary crop succumbs to blight or
drought. Economies that over-specialize in a few industries become
poorer and more unstable in the long run.

Although software may not be as high a priority in the big picture, one
would expect developers to learn from these examples and encourage
diversity when it comes to implementing popular APIs, but have they? As
mentioned above, Microsoft Windows is run on an overwhelming proportion
of personal computers. Even taking into account the variations between
different versions of Windows, mostly between Windows 9x and the Windows
NT family, installations of the Windows code-base definitely qualify as
a large, homogeneous population. One on which most governments, most
businesses, and many households depend on.

The elements of this population, like all other complex systems, are not
miraculously exempt from vulnerabilities. The Code Red epidemic of the
summer of 2001 is there to remind us of that. Code Red did what any
"virus" presented with a large homogeneous population would do: it
infected more than [359.000
computers](https://www.caida.org/research/security/code-red/) in just the
first day. Fortunately, it infected a less common member of the Windows
family and was quite harmless: it did not randomly corrupt files or
format your hard-drive.
[1](https://www.wired.com/news/technology/0,1282,45681,00.html),
[2](https://www.caida.org/research/security/code-red/)

It is only a matter of time before a more [virulent
worm](https://en.wikipedia.org/wiki/Warhol_worm) appears. The only way to
decrease its impact is to diversify the OS population. This issue is now
considered serious enough that security analysts are calling our
reliance on Microsoft Windows a [threat to national
security](https://web.archive.org/web/20050516194259/https://www.networkworld.com/weblogs/security/003535.html).

While Wine is not a sandbox and is vulnerable to malware that plays by
the rules of the Win32 API, it is immune to many problems that plague
Microsoft Windows. Wine is an alternate implementation of the Win32 API,
runs on top of several different OSes, and is probably less likely to
have zero-day vulnerabilities because it is developed in the open. In a
sense, running Wine even benefits those who don't use it. As more people
run Win32 programs through alternatives such as Wine, exploits unique to
Microsoft's implementation have fewer
[vectors](https://en.wikipedia.org/wiki/Vector_%28epidemiology%29) to
pass between, and Windows users benefit from greater [herd
immunity](https://en.wikipedia.org/wiki/Herd_immunity).

### Any Windows replacement must run Windows applications

The dependency is not so much on Microsoft Windows as it is on Windows
applications. Boxed off-the-shelf applications, games, in-house
applications, vertical market applications, are what prevents users,
companies and governments from switching to another operating system.
Even if 90% of the needs of most users are taken care of if you can
provide them with an office suite, an email client, a browser, and a
media player, then there will still be a remaining 10% of their needs,
potentially critical needs, that are not met. Unfortunately these
remaining 10% are spread across a wide spectrum of applications:
thousands of applications running the gamut from games to specialized
accounting software for French farms, via Italian encyclopedias, German
tax software, child education software, banking software, in-house
software representing years of development, etc. It is the availability
of all this software that makes Windows so compelling and its monopoly
so strong. No platform will become mainstream unless it runs a
significant portion of that software and lets individuals, companies and
governments preserve their investments in that software.

### Chicken-and-egg problem for Linux on the desktop

This brings us to the chicken and egg issue of Linux on the desktop.
Until Linux can provide equivalents for the above applications, its
market share on the desktop will stagnate. But until the market share of
Linux on the desktop rises, no vendor will develop applications for
Linux. How does one break this vicious circle?

Again, Wine can provide an answer. By letting users reuse the Windows
applications they have invested time and money in, Wine dramatically
lowers the barrier that prevents users from switching to Linux. This
then makes it possible for Linux to take off on the desktop, which
increases its market share in that segment. In turn, this makes it
viable for companies to produce Linux versions of their applications,
and for new products to come out just for the Linux market.

This reasoning could be dismissed easily if Wine was only capable of
running Solitaire. However now it can run [Microsoft
Office](https://appdb.winehq.org/appview.php?appId=31), multimedia
applications such as
[QuickTime](https://appdb.winehq.org/appview.php?appId=1029) and [Windows
Media Player](https://appdb.winehq.org/appview.php?appId=131), and even
games such as [Max Payne](https://appdb.winehq.org/appview.php?appId=661)
or [Unreal Tournament
3](https://appdb.winehq.org/objectManager.php?sClass=application&iId=5937).
Almost any other complex application can be made to run well given a bit
of time. And each time that work is done to add one application to this
list, many other applications benefit from this work and become usable
too.

Have a look at our [Application Database](https://appdb.winehq.org/) to
get an idea on what can be run under Wine.

### Wine benefits

Last but not least, Wine can provide benefits over Windows right now:

- Wine makes it possible to take advantage of all the Unix strong points
  (stability, flexibility, remote administration) while still using the
  Windows applications you depend on.
- Unix has always made it possible to write powerful scripts. Wine makes
  it possible to call Windows applications from scripts that can also
  leverage the Unix environment to its full extent.
- Wine makes it possible to access Windows applications remotely, even
  if they are a few thousand miles away.
- Wine makes it economical to use thin clients: simply install Wine on a
  Linux server, and voila, you can access these Windows applications
  from any X terminal.
- Wine can also be used to make existing Windows applications available
  on the Web by using VNC and its Javascript/HTML5 client.
- Wine is Open Source Software, so you can extend it to suit your needs
  or have one of many companies do it for you.
