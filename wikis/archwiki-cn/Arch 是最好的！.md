**翻译状态：**

  * 本文（或部分内容）译自 [Arch is the best](<https://wiki.archlinux.org/title/Arch_is_the_best> "arch:Arch is the best")，最近一次同步于 2020-07-19，若英文版本有所[更改](<https://wiki.archlinux.org/title/Arch_is_the_best?diff=0&oldid=625837>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/Arch_is_the_best_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

**Arch is the best** 项目是一个非常复杂的和精致的，自我提升和令人兴奋的项目（虽然或许有点过度工程），该项目给出了 Arch 的优越性的证明。 

##  历史

这个有远见的项目最初是由 Arch 社区的长期成员 [lucke](<https://bbs.archlinux.org/profile.php?id=2529>) 在 2008 年 4 月设计的，它是一个简单的 shell 脚本，提供了"Arch is the best"的无可辩驳的证明。它是通过一个[论坛帖子](<https://bbs.archlinux.org/viewtopic.php?id=47306>)向全世界宣布的，从而启发了其他人的思想，他们立即开始将它移植到多种不同的语言中，包括编程语言和口头语言，以便地球上的每一个人都能充分欣赏和受益于这一革命性的发现。 

##  代码

"Arch is the best"项目被移植到许多编程语言中。 

1C:Enterprise 7.7/8/8.1/8.2
    一种特定于过程域的编译动态类型化编程语言，主要类似于 VisualBasic，在俄罗斯和其他独联体国家广泛使用的"1C:Enterprise"产品中。
    
    Предупреждение("Arch is the best!");
    
ABAP
    高级业务应用程序设计语言。
    
    REPORT zwhat_is_the_best.
    WRITE 'Arch is the best'.
    
Ada
    一种系统关键编程语言。
    
    with Ada.Text_IO;
    use Ada.Text_IO;
    procedure ArchIsTheBest is
    begin
       Put_Line("Arch is the best!");
    end ArchIsTheBest;
    
APL
    一种编程语言。
    
    'Arch is the best!'
    
AppleScript
    由 Apple Inc. 创建的一种脚本语言，自 System 7 起内置于 Classic Mac OS 中，并内置于所有 macOS 版本中。
    
    display alert "Arch is the best!"
    say "Indeed, Arch is the best."
    
ArnoldC
    基于 Arnold Schwarzenegger 的一行程序设计语言。
    
    IT'S SHOWTIME
    TALK TO THE HAND "Arch is the best!"
    YOU HAVE BEEN TERMINATED
    
ATS
    一种使用依赖类型来提高程序可靠性的函数式编程语言。
    
    implement main () = println! "Arch is the best!"
    
Awk
    一种数据驱动的程序设计语言，用于处理基于文本的数据。
    
    BEGIN {
       print "Arch is the best!"
    }
    
BASIC
    一种脚本语言，是 20 世纪 60 年代最常用的计算机编程语言之一，被认为是学生在使用 FORTRAN 等功能更强大的语言之前学习的第一步。
    
    10 PRINT "Arch is the best!"
    
Batch
    一种用于 Windows 的脚本语言，可用于自动执行任务或只是享受一些乐趣。
    
    @echo off
    echo Arch is the best!
    pause
    
Befunge
    被认为是第一种基于 ASCII 的二维通用通用语言（在某种意义上，"you could plausibly write Hunt the Wumpus in it"）。
    
    <v"Arch is the best!"0
     <,_@#:
    
BIRL
    类似于 ArnoldC，但是对于 Bambam 的[[1]](<https://www.youtube.com/watch?v=3_qEE2i6h5Q>)。
    
    HORA DO SHOW
        CE QUER VER ESSA PORRA? ("Arch is the best!\n");
        BORA CUMPADE 0;
    BIRL
    
Boo
    针对 .NET 和 Mono 的稳定的面向对象的静态类型编程语言，具有受 python 启发的语法，并特别关注通过语言和编译器可扩展性功能（例如宏和自定义编译管道）进行元编程。
    
    print "Arch is the best!"
    
Bourne shell
    原始程序，应该与任何 shell 兼容。
    
    #!/bin/sh
    echo "Arch is the best!"
    
Bourne shell（备用）
    方便将输出传递到您喜爱的 IRC/email/IM 客户端。任何 shell 都能用。
    
    #!/bin/sh
    yes Arch is the best!
    
Bourne shell（动态更新）
    
    #!/bin/sh
    w3m -dump "https://wiki.archlinux.org/index.php/Arch_is_the_best" | sed -n '/^Translations/,/^Encodings/p'
    
或
    
     #!/bin/bash
     curl -s "https://wiki.archlinux.org/index.php?title=Arch_is_the_best&action=raw" | sed -n '/==Translations==/,$p' | sed "s/^\(.*\)$/* \1:/;t;s/^[^=]/  &/"
    
brainfuck
    旨在建立最小编译器并符合图灵完备性的语言，其名字也暗示程式码很难读懂。
    
    ++>++++++>+++++<+[>[->+<]<->++++++++++<]>>.<[-]>[-<++>]
    <----------------.---------------.+++++.<+++[-<++++++++++>]<.
    >>+.++++++++++.<<.>>+.------------.---.<<.>>---.
    +++.++++++++++++++.+.<<+.[-]++++++++++.
    
C
    注意这个项目中使用的三个空格缩进，很像其他高级的语言使用的缩进。
    
    #include <stdio.h>
    #include <stdlib.h>
    int main(void)
    {
       puts("Arch is the best!");
       return EXIT_SUCCESS;
    }
    
C#
    旨在成为一种简单、现代、通用、面向对象的编程语言。
    
    using System;
    public class ArchIsTheBest
    {
       static public void Main ()
       {
          Console.WriteLine ("Arch is the best!");
       }
    }
    
C++
    Arch == Linux++
    
    #include <iostream>
    #include <cstdlib>
    int main ()
    {
       std::cout << "Arch is the best!" << std::endl;
       return EXIT_SUCCESS;
    }
    
COBOL
    一种简单、轻量级的编程语言。
    
        IDENTIFICATION DIVISION.
        PROGRAM-ID.  TheBest.
    
        PROCEDURE DIVISION.
            DISPLAY "Arch is the best!".
            STOP RUN.
    
CoffeeScript
    一种可编译为 JavaScript 的编程语言。
    
    alert 'Arch is the best!'
    
Clojure
    在 JVM 上运行的 Lisp 方言。
    
    (def translations {"english" "Arch is the best!",
                       "german" "Arch ist das Beste!",
                       "australian" "Arch is fair dinkum, mate!",
                       "h4x0r" "arhc 51 7he be57!",
                       "spanish" "¡Arch es el mejor!"})
    
    (defn read-choice []
      (println "\nAvailable languages: ")
      (doall (map #(println (key %)) translations))
      (print "Enter language or Ctrl-c: ") (flush)
      (translations (read-line) :badinput))
    
    (defn arch-is-the-best []
      (loop [choice (read-choice)]
        (case choice
          :badinput (do (print "\nBad input!\n")
                        (recur (read-choice)))
          (do (print "\n" choice "\n")
              (recur (read-choice))))))
    
或
    
    (def translations {"english" "Arch is the best!",
                       "german" "Arch ist das Beste!",
                       "australian" "Arch is fair dinkum, mate!",
                       "h4x0r" "arhc 51 7he be57!",
                       "spanish" "¡Arch es el mejor!"
                       "street" "Arch iz da shizzle ma nizzle"})
    (while 1
      (println "\nPick a language:\n" (map #(key %) translations) "\n language: ")
      (println (translations (read-line) "Not a valid language")))
    
或
    
    (prn "Arch is the best!")
    
Common Lisp
    在 SBCL 上测试，可以随意添加更多的翻译。
    
    #!/usr/bin/sbcl --script
    (defparameter *best-list* '((English "Arch is the best!")
                (Chinese "Arch, 她出类拔萃!")
              (German "Arch ist das Beste!")
              (Greek "Το Arch είναι το καλύτερο!")
              (Latin "Arch optimum est!")
              (French "Arch est le meilleur!")))
    (defun aitb ()
      (format t "Available languages: ~{~{~@(~a~)~*~}~^, ~}.~%" *best-list*)
      (loop for input = (progn (format t "~&Input the desired language, (or 'quit'): ~%")
                               (force-output)
                               (read-line))
         if (string-equal input "quit")
         do (loop-finish)
         else
         do (let ((language-def
                   (assoc input *best-list*
                          :key (lambda (lang) (symbol-name lang))
                          :test #'string-equal)))
              (if language-def
                  (format t "~&~A~%" (second language-def))
                  (format t "~&Invalid language.~%"))))
      (format t "~&May the Arch be with you!~%"))
    (aitb)
    
Common Lisp（备用）
    应该在任何实现上运行（Clisp，Allegro，SBCL ...）
    
    (princ "Arch is the best!")
    
Crystal
    一种面向对象的类似 Ruby 的语言。
    
    puts "Arch is the best!"
    
Crystal（通过 web 服务器）
    用于一次将消息分发给多个朋友。
    
    # For giving the message to your friends
    require "http/server"
    
    server = HTTP::Server.new(80) do |context|
      context.response.content_type = "text/plain"
        context.response.print "Arch is the best!"
    end
    
    puts "Listening."
    server.listen
    
csh
    一个类似 C 的 shell.
    
    #!/bin/csh
    echo "Arch is the best!"
    
CSS
    一种样式表语言，主要用于设置网页样式。
    
    body * {
        display: none;
    }
    
    body::before {
        content: "Arch is the best!";
        font-family: monospace;
        font-size: 2.7rem;
        position: absolute;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%);
    }
    
D
    一种 C 风格的语言。有后见之明，以及现代化的便利。
    
     import std.stdio : writeln;
     void main()
     {
         writeln("Arch is the best");
     }
    
Dart
    谷歌的 JavaScript 杀手
    
     main(){
       print('Arch is the best');
     }
    
Dogescript
    友好的 JavaScript
    
     console.loge with '                So Arch'
     console.loge with '     Much Good'
     console.loge with '                          Wow'
    
Ebuild
    Gentoo 的构建脚本格式。
    
    DESCRIPTION="Arch is the best!"
    SRC_URI="https://wiki.archlinux.org/index.php/Arch_is_the_best"
    
    LICENSE="GFDL_1.3"
    SLOT="0"
    KEYWORDS=""
    IUSE=""
    
    DEPEND=""
    RDEPEND=""
    
    src_compile() {
    einfo "Arch is the best!"
    }
    
Emacs Lisp
    GNU Emacs 和 XEmacs 文本编辑器使用的 Lisp 编程语言的方言
    
     (message "Arch is the best!")
    
Emojicode
    一种无分隔符，面向对象，命令式，高级的混合语言，以表情符号作为固定点和方法。
    
    🏁 🍇
        😀 🔤Arch is the best!🔤❗️
    🍉
    
Elixir
    一种动态的功能语言，旨在构建可扩展和可维护的应用程序
    
    IO.puts "Arch is the best!"
    
Erlang
    并发的，垃圾收集的编程语言和运行时系统。
    
    -module(arch).
    -export([is_the_best/0]).
       is_the_best() -> io:fwrite("Arch is the best!\n").
    
或在进程之间使用消息传递
    
     -module(arch).
     -export([ultimate_question/0,the_answer/0]).
     the_answer() ->
         receive
             {Client,who_is_the_best} ->
                 Client ! {self(),"Arch is the best!"};
             {Client,_} ->
                 Client ! {self(),"Taco Taco Taco!"}
         end,
         the_answer().
     ultimate_question() ->
         Pid = spawn(arch,the_answer,[]),
         Pid ! {self(),who_is_the_best},
         receive
             {Pid,Response} -> io:format("~s~n",[Response])
         end.
    
F#
    一种强类型，功能优先的编程语言，用于编写简单的代码来解决复杂的问题。
    
    printfn "Arch is the best!"
    
Factor
    基于高级堆栈的语言。
    
    "Arch is the best" print
    
FIM++
    可以使用 Java 类的一种冗长，命令式，动态类型和解释性语言。
    
    Dear Princess Celestia: Letter About Arch Linux.
    Today I learned:
        I wrote "Arch is the best!".
    Your faithful student, Twilight Sparkle
    
Forth
    基于堆栈的语言。
    
    ." Arch is the best" cr -- kiss way
    
Fortran95
    
    program arch
       print *,"Arch is the best!"
    end program arch
    
Genie
    一种新的编程语言，它允许使用更现代的编程样式，同时能够毫不费力地本地创建和使用GObjects。
    
    init
     print "Arch is the best"
    
Gjs
    GNOME 的 Javascript 绑定。它主要基于 Spidermonkey javascript 引擎和 GObject 自省框架。
    
    #!/usr/bin/env gjs
    print ('Arch is the best');
    
Go
    由 Google 创建的一种语言，它是 C，C++和 Python 之间的一个可爱的孩子。
    
    package main
    
    import "fmt"
    
    func main() {
     fmt.Println("Arch is the best!")
    }
    
Groovy
    使用 Java 虚拟机的一种敏捷和动态语言。
    
    println 'Arch is the best!' 
    
Haskell
    IO 是一种简单无问题的语言。
    
    main = putStrLn "Arch is the best!"
    
HTML
    一种用于创建和定义网页及其内容的标记语言。
    
    <!DOCTYPE html>
    <html lang='en'>
       <head>
          <title>Arch is the best!</title>
       </head>
       <body>
           
    Arch is the best!
    
       </body>
    </html>

Idris
    具有依赖类型的通用纯函数式编程语言。Haskell，但更疯狂。
    
    module Main
    
    main : IO ()
    main = putStrLn "Arch is the best!"
    
Io
    受 Smalltalk，Self，Lua，Lisp，Act1 和 NewtonScript 启发的纯面向对象编程语言。
    
    "Arch is the best!" println
    
Java
    这是一种非常便携的语言，几乎可以在任何东西上运行，甚至可以在您的烤面包机上运行！
    
    public class ArchIsTheBest {
       public static void main(String[] args) {
           System.out.println("Arch is the best!");
       }
    }
    
JavaScript
    也称为 ECMAScript，这是一种基于原型的面向对象的脚本语言。
    
    console.log('Arch is the best!');
    
JavaScript（在网络浏览器中）
    
    alert('Arch is the best!');
    
Julia
    数值计算的新方法。
    
    println("Arch is the best!")
    
Kotlin
    JetBrains 试图赢得世界统治。
    
    fun main() {
       println("Arch is the best!")
    }
    
LilyPond
    功能强大的音乐雕刻程序，具有类似 LaTeX 的直观输入语言。
    
    \version "2.12.3"
    \include "english.ly"
    \header { title = "Arch is the best!" }
    \score
    {
       <<
          \relative c' { c4 e g c \bar "||" }
          \addlyrics   { Arch is the best! }
       >>
    }
    
LOLCODE
    为什么不呢？
    
    HAI
    CAN HAS STDIO?
    VISIBLE "ARCH IS TEH PWNZ LOL!"
    KTHXBYE
    
Lua
    一种轻量级，可扩展的编程语言。
    
    print "Arch is the best!"
    
Malbolge
    为使编程尽可能困难而创建的语言。
    
    bCBA@?>=<;:9876543210/.-,+*)('&%$#"!~}|{zyxwvutsrqponmlkjihgfedcba`_^]
    \[ZYXWVUTSRQPONMLKJIHGFEDCBA@?>=<;:9y16543210/.-,+*)('&}C#"!~}|{zyxwvu
    tsrqponmlkjihgfedcba`_^]\[ZYXWVUTSRQPONMLK-CgGFEDCBA@?>=<;:98x6543210/
    .-,+*)('&%$#"!~}|u;yxwpun4rqpRhmf,jihgIe^$ba`_^]\[ZYXQVUTMqQPONMFjJI+A
    eEDC%A:^>=<|:981U54t21*/.-&Jk)('&}C#"!aw={z\xwvun4lqpi/mlkjiKaf_%p
    
Matlab
    MathWorks开发的专有编程语言。
    
    disp('Arch is the best!');
    
Morpho
    Morpho 是一种支持过程式、面向对象和函数式编程的多范式编程语言。
    
    writeln("Arch is the best!");
    
Myrddin
    一种旨在控制和简化的系统编程语言，具有强大的类型检查，泛型，类型推断，闭包和特征。
    
    /* mbld -b aitb aitb.myr */
    use std
    const main = {
      std.put("Arch is the best!\n")
    }
    
NASM / Yasm (i686)
    请注意，该字符串位于 .text 部分中，感觉更好。
    
    ;nasm -f elf32 arch.asm
    ;ld -o arch arch.o
    ;./arch
    
    section .text
    global _start
    _start:
    mov edx,len
    mov ecx,msg
    mov ebx,1
    mov eax,4
    int 0x80
    xor ebx,ebx
    mov eax,1
    int 0x80
    msg: db "Arch is the best!",10
    len equ $-msg
    
NASM / Yasm (x86_64)
    采用了 AMD 的好用的新指令 _syscall_ 。
    
    ;nasm -f elf64 arch.asm
    ;ld -o arch arch.o
    ;./arch
    
    section .text
    global _start
    s:
        db 'Arch is the best!',0ah
    l equ $-s
    _start:
        mov rax,1
        mov rdi,1
        mov rsi,s
        mov rdx,l
        syscall
        mov rax,60
        xor rdi,rdi
        syscall
    
Nim
    可移植的轻量级编程语言。
    
    echo "Arch is the best!"
    
node.js
    一个基于 Chrome 的 JavaScript 运行时构建的平台，可使用事件驱动的非阻塞 I/O 模型轻松构建快速，可扩展的网络应用程序，从而使其轻巧高效，非常适合跨分布式设备运行的数据密集型实时应用程序。
    
    console.log('Arch is the best!');
    
node.js（http 服务器）
    一个可以发出"Arch is the best!"信息的 node.js 程序。使用 HTTP
    
    require('http').createServer((req,res) => {res.writeHead(200, {'Content-Type': 'text/plain'});res.end('Arch is the best!');}).listen(80);
    
Objective-C
    一种反射型，面向对象的编程语言，将 Smalltalk 样式的消息传递添加到 C 编程语言中。
    
    NSLog(@"Arch is the best!");
    
OCaml
    Caml 编程语言的主要实现。
    
    print_endline "Arch is the best!"
    
Octave
    高级解释语言，主要用于数值计算。
    
    printf("Arch is the best!\n")
    
Ook!
    将 brainfuck 翻译成了猩猩的语言。
    
    Ook. Ook. Ook. Ook. Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook? Ook. Ook. Ook. Ook! Ook? Ook. Ook? Ook! Ook? Ook! Ook! Ook. Ook? Ook. Ook. Ook? Ook. Ook? Ook! Ook? Ook. Ook! Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook? Ook. Ook? Ook! Ook. Ook? Ook. Ook? Ook! Ook. Ook? Ook. Ook! Ook? Ook! Ook! Ook? Ook! Ook. Ook? Ook! Ook? Ook! Ook! Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook? Ook? Ook! Ook? Ook. Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook? Ook! Ook! Ook? Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook? Ook? Ook! Ook? Ook. Ook! Ook. Ook. Ook? Ook. Ook? Ook. Ook. Ook! Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook? Ook. Ook? Ook. Ook! Ook. Ook. Ook? Ook. Ook? Ook. Ook. Ook! Ook. Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook? Ook. Ook? Ook. Ook! Ook. Ook. Ook? Ook. Ook? Ook! Ook! Ook! Ook! Ook! Ook! Ook! Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook. Ook. Ook. Ook! Ook. Ook? Ook. Ook? Ook. Ook. Ook. Ook! Ook. Ook! Ook? Ook! Ook! Ook? Ook! Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook. Ook! Ook.
    
Pascal
    一种有影响力的命令式和过程式编程语言。
    
    program ArchIsTheBest;
    begin
      writeln('Arch is the best!');
    end.
    
Pepe
    一种使您想大吼大叫的编程语言。[在线运行](<https://soaku.github.io/Pepe/#W2YsXy!chH!8gGYa-!d2!d4GH-!ca@K!k!kKXwGUa>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-17 ⓘ]
    
    # Arch
    reeEeeeeeE reeEEEeeEe reeEEeeeEE REeEEeEeee Reee rEeeEeeeee reee
    
    # is t
    reeEEeEeeE RrEeEEEeeEE rEeEEEeEee reee
    
    # he
    Reee RrEeEEeeEeE rreEe rEEeerEEee reEe
    
    # BEST!
    reeEEeeeEe reee reeeEeeeeE
    
Perl
    一种高级通用通用解释型动态编程语言。
    
    #!/usr/bin/env perl
    print "Arch is the best!\n";
    
Perl 6
    Perl 家族的最新成员。
    
    #!/usr/bin/env perl6
    say 'Arch is the best!';
    
PHP
    通用脚本语言。
    
    <?php
    echo "Arch is the best!\n";
    
Pixilang
    让我像素化。
    
    print("Arch is the best!",0,0,#1897D1)
    frame
    
Pony
    面向对象，参与者模型，功能安全的高性能编程语言。
    
    actor Main
      new create(env: Env) =>
        env.out.print("Arch is the best!")
    
Portable GNU assembler
    `as -o arch.o arch.s && ld -o arch -O0 arch.o`
    
       .section .data
    archIsBest:
       .ascii  "Arch is the best!\n"
    archIsBest_len:
       .long   . - archIsBest
       .section .text
       .globl _start
    _start:
       xorl %ebx, %ebx
       movl $4, %eax
       xorl %ebx, %ebx
       incl %ebx
       leal archIsBest, %ecx
       movl archIsBest_len, %edx
       int $0x80
       xorl %eax, %eax
       incl %eax
       xorl %ebx, %ebx
       int $0x80
    
PostScript
    与打印机通话的语言。
    
    %!PS
    /monospace 60 selectfont
    10 420 moveto
    (Arch is the best!) show
    showpage
    
Powershell
    基于 .NET 的基于任务的命令行 shell 和脚本语言。
    
    Write-Output "Arch is the best!"
    
Processing
    专为电子艺术和视觉设计而构建的开源编程语言和 IDE。
    
    println("Arch is the best!");
    
Prolog
    与人工智能和计算语言学相关的通用逻辑编程语言。
    
    format('Arch is the best~n',[]).
    
Python
    一种通用的高级编程语言。
    
    print('Arch is the best!')
    
QBASIC
    基于 QuickBASIC 的 BASIC 编程语言变体的解释器。
    
    PRINT "Arch is the best!"
    
R
    统计计算的语言（还有更多！）。
    
    archIsBest <- function() { cat("Arch is the best!\n") }
    archIsBest()
    
Racket
    Lisp-Scheme 系列中的通用多范式编程语言。
    
    #lang racket
    
    (let ([str "Arch is the best!\n"])
        (write-string str)
        (values))
    
Ruby
    一种动态的，反射性的，通用的面向对象的编程语言。
    
    #!/usr/bin/ruby -w
    puts 'Arch is the best!'
    
Rust
    Rust 是一种系统编程语言，运行速度极快，几乎可以防止所有崩溃，并消除了数据争用。
    
    fn main() {
        println!("Arch is the best!");
    }
    
Salt
    Salt 是自动化框架
    
     salt '*' event.fire '{"data":"Arch Is the best!"}' 'arch/best'
    
Scala
    在 JVM 上运行的一种多范例语言。
    
     object ArchIsBest extends App {
         println("Arch is the best!")
     }
    
Scheme
    Lisp 的方言。
    
    (display "Arch is the best!\n")
    
Seed
    一个库和解释器，通过 GNOME 平台动态地桥接 WebKit JavaScriptCore 引擎。
    
    #!/usr/bin/env seed
    print ('Arch is the best');
    
Shakespeare Programming Language
    旨在"_make a language with beautiful source code_ [...]"
    
    Arch is the Best.
    
    Arthur, a young man who is the best.
    Isabella, a likewise young woman who be.
    The Ghost, an undead who is the article.
    Beatrice, a young woman who is an adjective.
    
                        Act I: Setting of the Variables.
    
                        Scene I: Setting of Isabella and Arthur.
    
    [Enter Arthur and Isabella]
    
    Arthur:
     You are as dirty as the square of the sum of a rotten smelly foul devil
     and a vile lie! You are as bold as the sum of yourself and an evil hog!
    
    Isabella:
     Thou art as big as the square of a cute fair sweet flower! You are as proud
     as the sum of thyself and a cow.
    
    [Exit Arthur]
    
                        Scene II: Setting of The Ghost.
    
    [Enter The Ghost]
    
    Isabella:
     You art as loving as myself. Thou are as huge as the sum of yourself and twice
     a red old hair. You are as cowardly as the sum of yourself and a fat goat!
    
    [Exit Isabella]
    
                        Scene III: Setting of Beatrice.
    
    [Enter Beatrice]
    
    The Ghost:
     Thou are as good as the sum of Isabella and a mighty fine rich noble King.
    
    [Exeunt The Ghost and Beatrice]
    
                        Act II: Printing Arch is the Best.
    
                        Scene I: Arch.
    
    [Enter Arthur and Beatrice]
    
    Beatrice:
     Speak thy mind! You art as peaceful as the quotient between thyself and the
     clearest Lord.
    
    Arthur:
     Speak your mind!
    
    [Exeunt Arthur and Beatrice]
    
    [Enter Isabella and The Ghost]
    
    The Ghost:
     Thou are as normal as the sum of thyself and a town. Speak thy mind!
    
    Isabella:
     Speak your mind!
    
    [Exit Isabella]
    
    [Enter Arthur]
    
    The Ghost:
     Speak thy mind!
    
    [Exit Arthur]
    
                        Scene II: is.
    
    [Enter Beatrice]
    
    Beatrice:
     Thou are as old as the sum of yourself and a nose. Speak your mind!
    
    The Ghost:
     You art as pretty as the sum of thyself and a face. Speak your mind.
    
    [Exit The Ghost]
    
    [Enter Arthur]
    
    Beatrice:
     Speak thy mind.
    
                        Scene III: the.
    
    Arthur:
     You are as blue as the sum of yourself and a hamster. Speak thy mind!
    
    [Exit Arthur]
    
    [Enter The Ghost]
    
    Beatrice:
     You are as prompt as the sum of thyself and a lie! Speak your mind.
    
    [Exit Beatrice]
    
    [Enter Isabella]
    
    The Ghost:
     You art as happy as the sum of thyself and a large moon. Speak thy mind!
    
    [Exit The Ghost]
    
    [Enter Arthur]
    
    Isabella:
     Speak thy mind.
    
    [Exit Arthur]
    
                        Scene IV: Best.
    
    [Enter Beatrice]
    
    Beatrice:
     Thou are as blue as the sum of the sum of a curse and thyself and a bad
     codpiece. Speak your mind! You art as lovely as the sum of the sum of the
     happiness and yourself and a blossoming flower. Speak thy mind.
    
    Isabella:
     You are as healthy as the sum of yourself and a plague! Speak thy mind.
     Thou art as huge as the sum of thyself and a hero. Speak your mind!
    
    [Exit Beatrice]
    
    [Enter Arthur]
    
    Isabella:
     You art as green as the sum of thyself and a mother. Speak your mind.
    
    [Exeunt]
    
Shoes
    使用 Shoes 作为 GUI 的 Ruby 版本。
    
    Shoes.app :width => 135, :height => 30 do
        para "Arch is the Best!"
    end
    
Smalltalk
    Smalltalk 是一种面向对象的动态类型的反射式编程语言。
    
    Transcript show: 'Arch is the best!'.
    
Solidity
    以太坊智能合约的面向对象编程语言。
    
    pragma solidity ^0.6.0;
    
    contract ArchIsTheBest {
      function archIsTheBest() external pure returns (string memory) {
        return "Arch is the best!";
      }
    }
    
SQL
    结构化查询语言，关系数据库的查询语言
    
    SELECT 'Arch is the best!';
    SELECT 'Arch is the best!' from dual; -- for Oracle DB
    
Standard ML
    一种具有编译时类型检查和类型推断功能的通用，模块化，功能性编程语言。
    
    print "Arch is the best!\n"
    
Swift
    Apple Inc. 开发的一种通用，多范式，已编译的编程语言。
    
    print("Arch is the best!")
    
Tcl/Tk
    一种脚本语言，通常用于快速原型制作，脚本化应用程序，GUI 和测试。
    
    #!/usr/bin/env tclsh
    puts "Arch is the best!"
    
TrumpScript
    一种基于特朗普总统话语的脚本语言。
    
    say it with me, "Arch is the best!";
    america is great.
    
UEFI
    可扩展的固件框架
    
    #include <Uefi.h>
    EFI_STATUS EFIAPI
    ArchIsTheBest (
                  IN EFI_HANDLE        ImageHandle,
                  IN EFI_SYSTEM_TABLE  *SystemTable
                  )
    {
       SystemTable -> ConOut-> OutputString(SystemTable->ConOut, L"Arch is the best!\n"); 
       return EFI_SUCCESS;
    }
    
V
    简单，快速，安全，可编译的语言，用于开发可维护的软件。
    
    fn main() {
            println('Arch is the best!')
    }
    
Vala
    Vala 是一种新的编程语言，旨在将现代编程语言功能带给 GNOME 开发人员，而无需施加任何其他运行时要求，并且与使用 C 编写的应用程序和库相比，无需使用其他 ABI。
    
    void main(string[] args) {
    stdout.printf("\nArch is the best!\n\n");
    }
    
var'aq
    [战士的编程语言](<https://freshmeat.sourceforge.net/projects/varaq>)
    
    "Arch is the best!" cha'
    
Verilog
    一种硬件描述语言，标准化为 IEEE 1364
    
    module top;
      initial $display("Arch is the best!");
    endmodule
    
VHDL
    VHSIC 硬件描述语言
    
    use std.textio.all;
    
    entity top is
    end top;
    
    architecture behaviour of top is begin
      process begin
        write (output, String'("Arch is the best!"));
        wait;
      end process;
    end behaviour;
    
VimScript
    Vim 文本编辑器的脚本语言。
    
    echo "Arch is the best!"
    
Visual Basic
    Microsoft 为其组件对象模型（COM）编程模型提供的第三代事件驱动编程语言和集成开发环境（IDE）。
    
    Module Arch
      Sub Main()
          MsgBox("Arch is the best!")
      End Sub
    End Module
    
wenyan-lang
    古代汉语的编程语言。
    
    吾有一言。曰「「阿祺，盡善矣。」」。書之。
    
Wiring（Arduino）
    麻省理工学院开发的开源编程语言"处理"为基础。
    
    void setup()
    {
       Serial.begin(9600);
    }
    void loop()
    {
       Serial.print("Arch is the best!");
    }
    
X11
    X11 是独立于体系结构的系统，用于显示图形用户界面。

`cc -lX11 arch.c`
    
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    
    #include <X11/Xlib.h>
    
    int main()
    {
           Display *d;
           Window w;
           XEvent e;
           int s;
    
           if (!(d = XOpenDisplay(NULL))) {
                   fprintf(stderr, "Couldn't open display, but Arch is the best!\n");
                   exit(1);
           }
    
           s = DefaultScreen(d);
           w = XCreateSimpleWindow(d, RootWindow(d,s), 0, 0, 110, 20, 0, 
                                   0, WhitePixel(d,s));
           XSelectInput(d, w, ExposureMask | KeyPressMask);
           XMapWindow(d,w);
    
           while (1) {
                   XNextEvent(d, &e);
                   if (e.type == Expose) {
                           XDrawString(d, w, DefaultGC(d, s), 5, 15, "Arch is the best!", 17);
                   }
           }
    
           XCloseDisplay(d);
           return 0;
    }
    
Z3
    Microsoft Research 的定理证明器
    
    (define-const arch String "Arch is the best")
    (simplify (str.++ arch))
    
Zig
    一种通用的编程语言和工具链，用于维护健壮，最佳和可重用的软件。打算弃用 C。
    
    const std = @import("std");
    
    pub fn main() !void {
        std.debug.warn("Arch is the best!\n", .{});
    }
    
Zimbu
    一种快速，易学且类似于 JS 的编程语言。
    
    FUNC Main() int
      IO.write("Arch is the best!")
      RETURN 0
    }
    
Zsh
    UNIX 命令解释器（shell），与 ksh 极为相似，但包含许多增强功能。
    
    #!/bin/zsh -f
    setopt extendedglob
    print -- $(tput setaf 2) ${$(<<<${${${(@j: :)${(@s:_:)${:-What_Linux_is_the_best?}}}/* (#b)([A-Z]i)/Arch $match[1]}} tr '?' '!')} $(tput sgr0)
    