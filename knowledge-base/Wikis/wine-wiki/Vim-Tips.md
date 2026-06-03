This page contains tips for using [Vim](https://www.vim.org/) to develop
Wine code. Feel free to add your own tips if you have them.

### VIMRC Files

Some of the tips on this page require you to make changes to your
vimrc file. This file can be used to customize the way Vim behaves. On
UNIX (or Linux) systems this file can be found in `$HOME/.vimrc` -- if
it does not exist it can be created. For more information, or for
information about vimrc's on other operating systems, use the Vim
command `help vimrc`. If you make a change to your vimrc file you will
need to restart Vim to see the changes.

### Custom Vim settings for Wine Tree

If you want Wine sourcecode to have different Vim settings to your
defaults, you can put the following in your vimrc file (see the section
on [VIMRC Files](#vimrc-files) for more information).

    if !exists("loaded_vimrc_autocmd")
        let loaded_vimrc_autocmd=1
        autocmd BufNewFile,BufRead /path/to/wine/tree/* set expandtab tabstop=8 softtabstop=4 shiftwidth=4 | hi link cCommentL cError
    endif

Then change `/path/to/wine/tree` to the directory you store your wine
source in. The settings shown above (expandtab, tabstop, etc) will set
Vim to use the indent style found in most of Wine's source code. It
will also cause C++ style comments to be shown as errors -- they don't
work in some compilers.

### Character Arrays in Vim

To convert a string to a character array using Vim, you can try adding
this line to your vimrc file (see the section on \[#vimrc VIMRC Files\]
for more information). This is useful for working with WCHAR strings in
Wine.

    :vmap ,c "zda{<C-R>=substitute(substitute(@z, '\(.\)', "'\\1',", "g"), "'\\(['\\\\]\\)'", "'\\\\\\1'", "g")<CR><ESC>a'\0'}<ESC>

#### Using the script

1. Prepare the text you want to format. Only put the characters that
   you want in the array.

   ![](/media/vim_carray01.png)

2. Enter *Visual* mode (press `v`). Move your cursor to select an area
   of text. See Vim's help pages for more information about Visual
   mode.

   ![](/media/vim_carray02.png)

3. Type `,c` (a comma, followed by c. Don't delay too long or Vim
   won't do it right).

   ![](/media/vim_carray03.png)

Done.

Characters such as quotes and slashes should be handled by the script,
but if for some reason this script doesn't work, feel free to make
improvements to it and put them up on this page.
