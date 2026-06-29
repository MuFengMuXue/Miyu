# Luakit

Luakit is an extremely fast, lightweight and flexible web browser using the webkit engine.
It is customizable through lua scripts and fully usable with keyboard shortcuts.
It uses GTK 3 and WebKit2GTK.

## Installation
Install the  package.

## Basic usage
Press  to access the command prompt. You can do nearly everything from there.
Use  to autocomplete commands.

Use the  command to get information on the available keyboard shortcuts and what they do. (To see how the action for a particular keyboard shortcut is implemented in Lua, click anywhere in its help text.)

To quit, use the  command, or press  followed by .
You can also close the browser while remembering the session (i.e. restoring the tabs) by using the  command instead, or pressing  twice.

## Browsing
* Press  to open a prompt with the  command and enter the URI you want. Press  to edit the current URI.
* If it is not a recognized URI, Luakit will use the default search engine. See #Custom search engines.
* Specify which search engine to use by prefixing the entry with the appropriate keywork (e.g.  will search foobar on Google).
* Use common shortcuts to navigate. For emacs and vim aficionados, some of their regular shortcuts are provided. You can use the mouse as well.
* Use  to display the index of all visible links. Enter the appropriate number or a part of the string to open the link.
* Use  instead to open link in a new tab.
* Press  to open a new tab,  to close it. Press  to prompt for an URI to be opened in a new tab, and  to edit the current URI in a new tab.
* Press  to prompt for an URI to be opened in a new window, and  to edit the current URI in a new window.
* Switch from one tab to another by pressing  followed by  or , or use  and .
* You can switch to a specific tab with .
* Use  to go back in the browser history.
* Use  to go forward in the browser history.
* Reorder the tabs with .
* Reload the page with , stop the loading with .
* Re-open last closed tab with .
* Open downloads page by pressing  followed by  (or  for a new tab).
* Copy URI to primary selection with .
* View page source code with . Return to normal view with .
* View image source by pressing  followed by  (or  for  new tab).
* Inspect elements with . Repeat to open in a new window. Disable inspector with .

## Input fields
Many webpages have editable elements like dropdown lists, checkboxes, text fields and so on. While they work perfectly with the mouse, you may encounter some troubles using the follow commands.
In such a case, pressing the arrow keys may help.
Alternatively, the   shortcut can be used to focus input.

## Bookmarks
If enabled (default configuration), bookmarks can be used from within Luakit.

* The  command opens the bookmarks page. (Shortcut:  followed by , or  for a new tab).
* The  command adds the URI specified (or the current tab's URI, if omitted) to the bookmarks by specified tags. Starting from version 2012-09-13-r1, bookmarks page will be opened (new tab) in new bookmark editing mode before saving. (Shortcut: ).

## Configuration
Configuration is done in . It is not
necessary anymore to copy and modify . Some settings can also be
modified with the  command, unless you set them in  with:

## Key bindings
Most bindings will require some knowledge of Luakit, but you can at least do
simple things rebinding:

{{hc|~/.config/luakit/userconf.lua|2=
local modes = require "modes"

-- Creates new bindings from old ones.
modes.remap_binds("normal", -- This is the mode in which the bindings are active.
  {
  --  new     old     removes the old binding (defaults to false)
     {"O",    "t",    true},
  -- define as many as you wish
    {"Control-=", "zi"},
    ...
  })
}}

To bind keys to commands, you can use the following template:

{{hc|~/.config/luakit/userconf.lua|2=
modes.add_binds("normal", {
-- {"",
--  "",
--  function (w) w:enter_cmd("") end}
  {"O", "Open URL in a new tab.",
   function (w) w:enter_cmd(":tabopen ") end},
   ...
})
}}

For inspiration, see , where the default
bindings are defined.

## Homepage
Set your homepage as follows:

## Custom search engines
To search with the default search engine, press  and type the phrases. To search with a different engine, type its name after  and then the phrases.

You can virtually add any search engine you want. Make a search on the website you want and copy paste the URI to the Luakit configuration by replacing the searched terms with an . Example:

The variable is used as a keyword for the  command in Luakit.

Set the default search engine by using this same keyword:

Instead of strings, you can defined search engines as functions that return a
string. For instance, here is a Wikipedia search engine that lets you specify
a language (defaulting to English):

If called as , this will open the Arch Linux
page on the English Wikipedia; with ,
this will use the French Wikipedia instead.

## Download location
To specify download location:

Default location is  if it exists,  otherwise.

## Adblock
Adblock is loaded by default, but you need to:

* Fetch an adblock-compatible list, like Easylist, and save it to .
* Restart Luakit to load the extension.
* Use  command within Luakit to turn Adblock's list(s) you downloaded on Adblock itself becomes enabled on startup.
Full info on enabled lists and AdBlock state can be found using  or   at  internal page, if the  module is enabled, which is not a mandatory part.

## Bookmarks management
## Sync
Starting from version 2012.09.13, Luakit bookmarks are stored in an SQLite database: .

You can put a symbolic link in place of the default file to store your bookmarks anywhere on your machine.
This way if your are using a cloud sync application like Dropbox, you can keep your bookmarks synchronized between your different computers.

## Converting plain text bookmarks to SQLite format
Bookmarks were stored in a simple plain text file: . Each line is a bookmark. It is composed of 2 fields, the link and the group which are separated by a tab character.

To use bookmarks with the latest Luakit release, the file must be converted.
A sample Lua script will do that:

{{hc|bookmarks_plain_to_sqlite.lua|
local usage = luakit -c bookmarks_plain_to_sqlite.lua [bookmark plaintext path db path
]]

local old_db_path, new_db_path = unpack(uris)

if not old_db_path or not new_db_path then
   io.stdout:write(usage)
   luakit.quit(1)
end

-- One-pass file read into 'data' var.
old_db = assert(io.open(old_db_path, "r"))
local data = old_db:read("*all")
assert(old_db:close())

-- Init new_db, otherwise sqlite queries will fail.
new_db = sqlite3{ filename = new_db_path }
new_db:exec("CREATE TABLE IF NOT EXISTS bookmarks (id INTEGER PRIMARY KEY, uri TEXT NOT NULL, title TEXT NOT NULL, desc TEXT NOT NULL, tags TEXT NOT NULL, created INTEGER, modified INTEGER )")

-- Fill
local url,tag

for line in data:gmatch("do

   if string.len(line) > 1 then

      print ("["..line.."")

      -- Get url and tag (if present) from first line.
      _, _, url, tag = string.find(line, "(-- Optional yet convenient output.
      io.write(url)
      io.write("\t")
      io.write(tag)
      io.write("\n")

      -- DB insertion. Nothing will be overwritten. If URL and/or tag already exists, then a double is created.
      new_db:exec("INSERT INTO bookmarks VALUES (NULL, ?, ?, ?, ?, ?, ?)",
                  {
                     url, "", "", tag or "",
                     os.time(), os.time()
                  })
      end
end

print("Import finished.")
print("\nVacuuming database...")
new_db:exec "VACUUM"
print("Vacuum done.")

luakit.quit(0)
}}

As stated at beginning of the script, it must be ran with Luakit:

 $ luakit -c bookmarks_plain_to_sqlite.lua path/to/plaintext/bookmark path/to/db

The old plaintext bookmarks will be left unchanged. If the DB bookmarks do not exist, the file will be created. If it exists, do not worry, none of the previous bookmarks will be touched. However, this behaviour implies that you might get some doubles.

## Import from Firefox
To import bookmarks from Firefox, first they must be exported to an HTML file using its bookmarks manager. After that the XML file can be converted to a Luakit format.

The following one-line awk command will do that:

{{bc|
$ cat bookmarks.html | awk '
{gsub(/\"/," ")}
//{FS=">";gsub(/");og=g;g=$(NF-2);FS=" "}
//{x++;if(x>= 3)gl[x-3=g}
//{x--;if(x==2)g=og"2"}
/HREF/{gsub(//," ");if(g!=""){if(og!=g){printf "\n";og=g};printf "%s\t",$4;if(x>=3){for(i=0;i" here.
// {
    FS=">"
    gsub(/")
    oldgroup=group
    group=$(NF-2)
    FS=" "
}

# Each time a  is encountered, it means we step into a subfolder.
# 'count' is the depth level.
# Base level starts at 2 (Firefox fault).
# 'groupline' is an array of all parent folders.
// {
    count++
    if ( count >= 3 )
        groupline}

# On , we step out.
# If if return to the base level (i.e. not in a folder), then we give 'group' a fake name different
# from 'oldgroup' to make sure a line will be skipped (see below).
// {
    count--
    if( count == 2 )
        group=oldgroup"ROOT"
}

# The bookmark name.
# If oldgroup is different than group, (i.e. folder changed) then we skip a line.
# If we are in a folder, then we print the group name, i.e. all parents plus the current folder
# separated by an hyphen.
/HREF/ {
    gsub(//," ")
    if (group != "")
    {
        if(oldgroup != group)
        {
            printf "\n"
            oldgroup=group
        }
        printf "%s\t",$4
        if ( count >= 3 )
        {
            for ( i=0 ; i > bookmarks

Then convert the generated plain text bookmarks to the SQLite format as described at #Converting plain text bookmarks to SQLite format.

## Export bookmarks
The following script let you export Luakit bookmarks from its SQLite format to a plain text file. The resulting file may be suitable for other web browsers, or may be easily parsed by import scripts.

{{hc|bookmarks_sqlite_to_plain.lua|
-- USER CONFIG

local sep = " "

-- END OF USER CONFIG

local usage = [[Usage: luakit -c bookmarks_sqlite_to_plain.lua [bookmark db path plain path

DB scheme is

    bookmarks (
        id INTEGER PRIMARY KEY,
        uri TEXT NOT NULL,
        title TEXT NOT NULL,
        desc TEXT NOT NULL,
        tags TEXT NOT NULL,
        created INTEGER,
        modified INTEGER
    );
]]

local old_db_path, new_db_path = unpack(uris)

if not old_db_path or not new_db_path then
   io.stdout:write(usage)
   luakit.quit(1)
end

-- One-pass file read into 'data' var.
new_db = assert(io.open(new_db_path, "w"))

-- Open old_db
old_db = sqlite3{ filename = old_db_path }

-- Load all db values to a string variable.
local rows = old_db:exec  SELECT * FROM bookmarks

-- Iterate over all entries.
-- Note: it could be faster to use one single concatenation for all entries, but
-- it would be much more code and not so flexible. It is desirable to focus on
-- clarity. After all, only a few hundred lines are handled.
for _, b in ipairs(rows) do

   -- Change %q for %s to remove double quotes if needed.
   -- You can toggle the desired fields with comments.
   local outputstr =
      string.format("%q%s", b.uri or "", sep) ..
      string.format("%q%s", b.title or "", sep) ..
      string.format("%q%s", b.desc or "", sep) ..
      string.format("%q%s- ", b.tags or "", sep) ..
      ((b.created or "" ) .. sep) ..
      ((b.modified or "" ) .. sep) ..
      "\n"

   -- Write entry to file.
   new_db:write(outputstr)
end

print("Export done.")

assert(new_db:close())

luakit.quit(0)
}}

As stated at beginning of the script, it must be ran with Luakit:

 $ luakit -c bookmarks_plain_to_sqlite.lua path/to/plaintext/bookmarks path/to/database

## Tor
Once Tor has been setup, simply run:

 $ torsocks luakit --nounique

## Custom CSS
Locate the  sub-directory within luakit's data storage directory.
Normally, this is located at . Create the
directory if it does not already exist.
Move any CSS rules to a new file within that directory. The filename must end in .
Make sure you specify which sites your stylesheet should apply to. The way to
do this is to use  rules. The Stylish wiki page Applying styles to specific sites may be helpful.
Run  to detect new stylesheet files and reload any changes to
existing stylesheet files; it is not necessary to restart luakit.

To open the styles menu, run the command . Here you can
enable/disable stylesheets, open stylesheets in your text editor, and view
which stylesheets are active.

If a stylesheet is disabled for all pages, its state will be listed as
"Disabled". If a stylesheet is enabled for all pages, but does not apply to
the current page, its state will be listed as "Enabled". If a stylesheet is
enbaled for all pages _and_ it applies to the current page, its state will be
listed as "Active".
