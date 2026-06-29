**翻译状态：**

  * 本文（或部分内容）译自 [PDF, PS and DjVu](<https://wiki.archlinux.org/title/PDF,_PS_and_DjVu> "arch:PDF, PS and DjVu")，最近一次同步于 2025-01-12，若英文版本有所[更改](<https://wiki.archlinux.org/title/PDF,_PS_and_DjVu?diff=0&oldid=824943>)，则您可以帮助同步与[翻译](<../zh-cn/Help:%E7%BF%BB%E8%AF%91.html> "Help:翻译")更改的内容。
  * 您可以在 [ArchWiki 的对应页面](<https://wiki.archlinux.org/title/PDF,_PS_and_DjVu_\(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87\)?action=history>)找到本文翻译的**原始** 修订历史。
  * 本文可能与英文原文存在出入。

本文涵盖用于查看、编辑和转换 [PDF](<https://en.wikipedia.org/wiki/PDF> "wikipedia:PDF")、[PostScript](<https://en.wikipedia.org/wiki/PostScript> "wikipedia:PostScript")（PS）、[DjVu](<https://en.wikipedia.org/wiki/DjVu> "wikipedia:DjVu")（ _déjà vu_ ）与 [XPS](<https://en.wikipedia.org/wiki/Open_XML_Paper_Specification> "wikipedia:Open XML Paper Specification")文件的软件。 

##  引擎

  * **DjVuLibre** — 该套件用于创建、操作和查看 DjVu 文档。

     <https://djvu.sourceforge.net/> || [djvulibre](<https://archlinux.org/packages/?name=djvulibre>)包

  * **[Ghostscript](<https://en.wikipedia.org/wiki/Ghostscript> "wikipedia:Ghostscript")** — PostScript 和 PDF 的解释器。提供 [gs(1)](<https://man.archlinux.org/man/gs.1>) 命令行界面，另请参阅 `/usr/share/doc/ghostscript/*/Use.htm`（[在线阅读](<https://ghostscript.readthedocs.io/en/latest/Use.html>)），以及许多封装脚本，如 _ps2pdf_ 和 _pdf2ps_ 。

     <https://ghostscript.com/> || [ghostscript](<https://archlinux.org/packages/?name=ghostscript>)包

  * **libgxps** — 基于 GObject 的库，用于处理和渲染 XPS 文档。

     <https://wiki.gnome.org/Projects/libgxps> || [libgxps](<https://archlinux.org/packages/?name=libgxps>)包

  * **libspectre** — 用于渲染 Postscript 文档的小型库。

     <https://www.freedesktop.org/wiki/Software/libspectre> || [libspectre](<https://archlinux.org/packages/?name=libspectre>)包

  * **[Mupdf](<https://en.wikipedia.org/wiki/MuPDF> "wikipedia:MuPDF")** — MuPDF 是一款轻量级 PDF、XPS 和 EPUB 阅读器，由软件库、命令行工具和阅读器组成。

     <https://mupdf.com/> || [libmupdf](<https://archlinux.org/packages/?name=libmupdf>)包

  * **[Poppler](<https://en.wikipedia.org/wiki/Poppler_\(software\)> "wikipedia:Poppler \(software\)")** — 基于 Xpdf 的 PDF 渲染库。要使 Poppler 支持中日韩（中文、日文、韩文）语言，请[安装](<../zh-cn/Help:%E9%98%85%E8%AF%BB.html#%E5%AE%89%E8%A3%85%E8%BD%AF%E4%BB%B6%E5%8C%85> "安装") [poppler-data](<https://archlinux.org/packages/?name=poppler-data>)包。

     <https://poppler.freedesktop.org/> || [poppler](<https://archlinux.org/packages/?name=poppler>)包

##  查看器

###  帧缓冲区

  * **fbgs** — 用于 linux 帧缓冲控制台的勉强可用的 PostScript/pdf 查看器。

     <https://www.kraxel.org/blog/linux/fbida/> || [fbida](<https://archlinux.org/packages/?name=fbida>)包

  * **fbpdf** — 基于 MuPDF 的小型帧缓冲 PDF 与 DjVu 查看器，带有 [Vim](<../zh-cn/Vim.html> "Vim") 键绑定，用 C 语言编写。

     <https://repo.or.cz/w/fbpdf.git> || [fbpdf-git](<https://aur.archlinux.org/packages/fbpdf-git/>)AUR

  * **jfbview** — 帧缓冲 PDF 和图像浏览器。其功能包括类似 Vim 的控件、缩放至合适、TOC（大纲）视图和快速多线程渲染。

     <https://github.com/jichu4n/jfbview> || [jfbview](<https://aur.archlinux.org/packages/jfbview/>)AUR

###  图形化

**注意：** 某些[网络浏览器](<../zh-cn/%E5%BA%94%E7%94%A8%E7%A8%8B%E5%BA%8F%E5%88%97%E8%A1%A8/%E4%BA%92%E8%81%94%E7%BD%91.html#%E7%BD%91%E7%BB%9C%E6%B5%8F%E8%A7%88%E5%99%A8> "网络浏览器")可以显示 PDF 文件，例如使用 [PDF.js](<https://github.com/mozilla/pdf.js>)。

  * **apvlv** — 轻量级文档查看器，使用 GTK 库与 [Vim](<../zh-cn/Vim.html> "Vim") 键绑定。支持 PDF、DjVu、EPUB、HTML 和 TXT。

     <https://naihe2010.github.io/apvlv/> || [apvlv](<https://aur.archlinux.org/packages/apvlv/>)AUR

  * **Atril** — 适用于 MATE 的简单多页文档查看器。支持 DjVu、DVI、EPS、EPUB、PDF、PostScript、TIFF、XPS 和 Comicbook。

     <https://github.com/mate-desktop/atril> || [atril](<https://archlinux.org/packages/?name=atril>)包

  * **CorePDF** — 基于 Qt 和 poppler 的简单轻量级 PDF 查看器。是 C-Suite 的一部分。

     <https://cubocore.gitlab.io/> || [corepdf](<https://aur.archlinux.org/packages/corepdf/>)AUR

  * **Deepin Document Viewer** — A一款简单的 PDF 和 DjVu 阅读器，支持书签、高亮显示和注释。

     <https://github.com/linuxdeepin/deepin-reader> || [deepin-reader](<https://archlinux.org/packages/?name=deepin-reader>)包

  * **DjView** — DjVu 文档查看器

     <https://djvu.sourceforge.net/djview4.html> || [djview](<https://archlinux.org/packages/?name=djview>)包

  * **[Emacs](<../zh-cn/Emacs.html> "Emacs")** — 另请参阅 [pdf-tools](<https://github.com/vedang/pdf-tools>)，了解改进后的 pdf 支持（[emacs-pdf-tools-git](<https://aur.archlinux.org/packages/emacs-pdf-tools-git/>)AUR），以及 [djvu 软件包](<https://elpa.gnu.org/packages/djvu.html>)，了解对 djvu 的支持。

     <https://www.gnu.org/software/emacs/> || [emacs](<https://archlinux.org/packages/?name=emacs>)包

  * **ePDFView** — 使用 Poppler 和 GTK 库的轻量级 PDF 文档查看器。已停止开发。

     <http://freecode.com/projects/epdfview> || [epdfview-git](<https://aur.archlinux.org/packages/epdfview-git/>)AUR

  * **[Foxit Reader](<https://en.wikipedia.org/wiki/Foxit_Reader> "wikipedia:Foxit Reader")** — 小巧、快速（与 Acrobat 相比）的专有 PDF 查看器。发布时间（安全更新除外）为 [Linux 版已停止开发（2020 年 11 月）](<https://web.archive.org/web/20221006020600/https://forums.foxitsoftware.com/forum/portable-document-format-pdf-tools/foxit-reader/180532-linux-how-to-get-automatically-updates-for-foxit-reader-free-version#post186480>)。

     <https://www.foxitsoftware.com/pdf-reader/> || [foxitreader](<https://aur.archlinux.org/packages/foxitreader/>)AUR

  * **[GNOME Document Viewer](</wzh/index.php?title=GNOME/Document_viewer&action=edit&redlink=1> "GNOME/Document viewer（页面不存在）")** — 使用 GTK 的 GNOME 文档查看器。支持 DjVu、DVI、EPS、PDF、PostScript、TIFF、XPS 和 Comicbook。是 [gnome](<https://archlinux.org/groups/x86_64/gnome/>)包组 的一部分。

     <https://apps.gnome.org/Evince/> || [evince](<https://archlinux.org/packages/?name=evince>)包

  * **gv** — Ghostscript 解释器的图形用户界面，允许查看和浏览 PostScript 和 PDF 文档。

     <https://www.gnu.org/software/gv/> || [gv](<https://aur.archlinux.org/packages/gv/>)AUR

  * **[llpp](</wzh/index.php?title=Llpp&action=edit&redlink=1> "Llpp（页面不存在）")** — 基于 MuPDF 的快速 PDF 阅读器，支持连续滚动页面、书签和全文搜索。

     <https://repo.or.cz/w/llpp.git> || [llpp](<https://aur.archlinux.org/packages/llpp/>)AUR

  * **[MuPDF](<../zh-cn/MuPDF.html> "MuPDF")** — 使用可移植 C 语言编写的快速 EPUB、FictionBook、PDF、XPS 和 Comicbook 查看器。支持中日韩字体并具有类似 vim 的绑定功能。

     <https://mupdf.com/> || [mupdf](<https://archlinux.org/packages/?name=mupdf>)包

  * **[Okular](<https://en.wikipedia.org/wiki/Okular> "wikipedia:Okular")** — KDE 的通用文档查看器。支持 CHM、Comicbook、DjVu、DVI、EPUB、FictionBook、Mobipocket、ODT、PDF、Plucker、PostScript、TIFF 和 XPS。是 [kde-graphics](<https://archlinux.org/groups/x86_64/kde-graphics/>)包组 的一部分。

     <https://okular.kde.org/> || [okular](<https://archlinux.org/packages/?name=okular>)包

  * **Papers** — 使用 GTK 的 GNOME 文档查看器。支持 DjVu、PDF、TIFF 与 Comicbook。

     <https://apps.gnome.org/Papers/> || [papers](<https://archlinux.org/packages/?name=papers>)包

  * **pdfpc** — Presenter console with multi-monitor support for PDF files.

     <https://pdfpc.github.io/> || [pdfpc](<https://archlinux.org/packages/?name=pdfpc>)包

  * **qpdfview** — 标签式文档查看器。它使用 Poppler 支持 PDF，使用 libspectre 支持 PS，使用 DjVuLibre 支持 DjVu，使用 CUPS 支持打印，并使用 Qt 工具包制作界面。

     <https://launchpad.net/qpdfview> || [qpdfview](<https://aur.archlinux.org/packages/qpdfview/>)AUR

  * **Sioyek** — 基于 MuPDF 的轻量级 PDF 阅读器，具有专为阅读研究论文和技术书籍而设计的功能，如标记、书签、高亮显示、可搜索命令调色板、跳转到参考文献等。

     <https://sioyek.info/> || [sioyek](<https://aur.archlinux.org/packages/sioyek/>)AUR

  * **[Xpdf](<https://en.wikipedia.org/wiki/Xpdf> "wikipedia:Xpdf")** — 可解码 LZW 和读取加密 PDF 的阅读器。

     <https://www.xpdfreader.com/> || [xpdf](<https://archlinux.org/packages/?name=xpdf>)包

  * **Xreader** — X-Apps 项目的文档查看器。支持 DjVu、DVI、EPUB、PDF、PostScript、TIFF、XPS 和 Comicbook。

     <https://github.com/linuxmint/xreader/> || [xreader](<https://archlinux.org/packages/?name=xreader>)包

  * **[Zathura](</wzh/index.php?title=Zathura&action=edit&redlink=1> "Zathura（页面不存在）")** — 高度可定制、功能强大的文档查看器（基于插件）。支持 PDF、DjVu、PostScript 和 Comicbook。

     <https://pwmt.org/projects/zathura/> || [zathura](<https://archlinux.org/packages/?name=zathura>)包

####  比较

[![](../File:Tango-inaccurate.png)](<../File:Tango-inaccurate.png>)**本文或本章节的事实准确性存在争议。**

**原因：** 在 MuPDF 和 llpp 中填写 PDF 表单的功能似乎是不可用的。（在 [Talk:PDF、PS 与 DjVu](<../zh-cn/Talk:PDF%E3%80%81PS_%E4%B8%8E_DjVu.html>) 中讨论）

名称 | PDF | PostScript | DjVu | XPS | PDF 表格 | PDF 注释 | 非矩形选择 | 许可证   
---|---|---|---|---|---|---|---|---  
[Adobe Reader](<https://en.wikipedia.org/wiki/Adobe_Reader> "wikipedia:Adobe Reader") | 定制的 | – | – | – | 是 | – | 是 | 专有   
apvlv  | Poppler | – | DjVuLibre | – | 否 | – | 否 (至少没有默认) | GPLv2   
Atril  | Poppler | libspectre | DjVuLibre | libgxps | 是 | – | – | GPLv2   
DjView  | – | – | DjVuLibre | – | – | – | – | GPLv2   
[Emacs](<../zh-cn/Emacs.html> "Emacs") | Ghostscript1 | DjVuLibre1 | – | 否 | 是 | 是 | GPLv3   
Emacs pdf-tools  | Poppler | – | – | – | – | 是 | 是 | GPLv3   
ePDFView  | Poppler | – | – | – | 否 | – | – | GPLv2   
[Foxit Reader](<https://en.wikipedia.org/wiki/Foxit_Reader> "wikipedia:Foxit Reader") | 定制的 | – | – | – | 是 | 是 | 是 | 专有   
[GNOME Document Viewer](</wzh/index.php?title=GNOME/Document_viewer&action=edit&redlink=1> "GNOME/Document viewer（页面不存在）") | Poppler | libspectre | DjVuLibre | libgxps | 是 | 是 | 是 | GPLv2   
gv  | Ghostscript | – | – | 否 | – | – | GPLv3   
[llpp](</wzh/index.php?title=Llpp&action=edit&redlink=1> "Llpp（页面不存在）") | libmupdf | – | – | libmupdf | 是 | – | – | GPLv3   
[MuPDF](<../zh-cn/MuPDF.html> "MuPDF") | 定制的 | – | – | Custom | 是 ([mupdf-gl](<https://archlinux.org/packages/?name=mupdf-gl>)包) | 是 ([mupdf-gl](<https://archlinux.org/packages/?name=mupdf-gl>)包) | 是 ([mupdf-gl](<https://archlinux.org/packages/?name=mupdf-gl>)包) | AGPLv3   
[Okular](<https://en.wikipedia.org/wiki/Okular> "wikipedia:Okular") | Poppler | libspectre | DjVuLibre | 定制的 | 是 | 是 | 是 | GPL、LGPL   
PDF4QT  | 定制的 | – | – | – | 否 | 是 | 是 | LGPLv3   
pdfpc  | Poppler | – | – | – | 否 | – | – | GPLv2   
qpdfview  | Poppler | libspectre1 | DjVuLibre1 | – | 是 | 是 | – | GPLv2   
[Xpdf](<https://en.wikipedia.org/wiki/Xpdf> "wikipedia:Xpdf") | 定制的 | – | – | – | 否 | – | – | GPLv3   
Xreader  | Poppler | libspectre1 | DjVuLibre1 | libgxps1 | 是 | 是 | 是 | GPLv2   
[Zathura](</wzh/index.php?title=Zathura&action=edit&redlink=1> "Zathura（页面不存在）") | libmupdf1 / Poppler1 | libspectre1 | DjVuLibre1 | libmupdf1 | 否 | 否 | 是 | zlib   
  
  1. 需要安装可选依赖项

#### PDF forms

The _PDF forms_ column in the above table refers to [AcroForms](<https://en.wikipedia.org/wiki/PDF#Forms> "wikipedia:PDF") support. If you do not need your input to be directly extractable from the PDF, you can also use the applications in [#Graphical PDF editing](<#Graphical_PDF_editing>) to put text on top of a PDF. PDF forms can be created with [LibreOffice Writer](<../zh-cn/LibreOffice.html> "LibreOffice") (_View > Toolbars > Form Controls_) and the [advanced PDF editors](<#Advanced_editors>). 

The proprietary and deprecated [XFA](<https://en.wikipedia.org/wiki/XFA> "wikipedia:XFA") format for forms is not fully supported by Poppler[[1]](<https://gitlab.freedesktop.org/poppler/poppler/issues/199>)[[2]](<https://gitlab.freedesktop.org/poppler/poppler/issues/530>) and only supported by [Adobe Reader](<#Graphical>) and [Master PDF Editor](<#Advanced_editors>). 

Alternatively, web browsers such as [Firefox](<../zh-cn/Firefox.html> "Firefox") or [Chromium](<../zh-cn/Chromium.html> "Chromium") feature a built-in PDF viewer capable of filling out forms. 

## Graphical PDF editing

### Editors that can import PDF files

  * [Scribus](</wzh/index.php?title=Scribus&action=edit&redlink=1> "Scribus（页面不存在）") can import and export PDF; text is imported as polygons.[[3]](<https://wiki.scribus.net/canvas/Importing_PDF_files_as_Vector_Graphics>)
  * [LibreOffice Draw](<../zh-cn/LibreOffice.html> "LibreOffice") can import and export PDF; text is imported as text; embedded fonts are substituted.[[4]](<https://bugs.documentfoundation.org/show_bug.cgi?id=82163>)[[5]](<https://ask.libreoffice.org/en/question/38991/garbled-text-when-opening-pdfs-in-draw/>)
  * [Inkscape](<../zh-cn/Inkscape.html> "Inkscape") can import and export PDF; text is imported as cloned glyphs or text; with the latter embedded fonts are substituted.
  * Graphics editors like [GIMP](<../zh-cn/GIMP.html> "GIMP") and [krita](<https://archlinux.org/packages/?name=krita>)包 can also import and export PDFs at the cost of [rasterization](<https://en.wikipedia.org/wiki/Raster_graphics> "wikipedia:Raster graphics").

### Basic editors

  * **flpsed** — A PostScript and PDF annotator, only supports text boxes.

     <https://flpsed.org/flpsed.html> || [flpsed](<https://aur.archlinux.org/packages/flpsed/>)AUR

  * **HandyOutliner for DjVu / PDF** — Make easier and faster the process of creating bookmarks for DjVu and PDF documents.

     <https://handyoutlinerfo.sourceforge.net> || [handyoutliner-bin](<https://aur.archlinux.org/packages/handyoutliner-bin/>)AUR

  * **jPDF Tweak** — Java Swing application that can combine, split, rotate, reorder, watermark, encrypt, sign, and otherwise tweak PDF files.

     <https://jpdftweak.sourceforge.net/> || [jpdftweak](<https://aur.archlinux.org/packages/jpdftweak/>)AUR

  * **Paper Clip** — PDF document metadata editor to edit the title, author, keywords and more details.

     <https://apps.gnome.org/PdfMetadataEditor/> || [paper-clip](<https://archlinux.org/packages/?name=paper-clip>)包

  * **PDF Arranger** — Helps merge or split pdf documents and rotate, crop and rearrange pages. It is a maintained fork of PDF-Shuffler.

     <https://github.com/jeromerobert/pdfarranger> || [pdfarranger](<https://archlinux.org/packages/?name=pdfarranger>)包

  * **PDF Chain** — GTK front-end for [PDFtk](<#PDF_tools>), written in C++, supporting concatenation, burst, watermarks, attaching files and more.

     <https://pdfchain.sourceforge.net/> || [pdfchain](<https://aur.archlinux.org/packages/pdfchain/>)AUR

  * **PdfJumbler** — Simple tool to rearrange, merge, delete and rotate pages in PDF files.

     <https://github.com/mgropp/pdfjumbler> || [pdfjumbler](<https://aur.archlinux.org/packages/pdfjumbler/>)AUR

  * **PDF Mix Tool** — Qt front-end for [PoDoFo](<#Libraries>), written in C++, supports splitting, merging, rotating and mixing PDF files.

     <https://scarpetta.eu/pdfmixtool/> || [pdfmixtool](<https://archlinux.org/packages/?name=pdfmixtool>)包

  * **PDFsam** — Open source application, written in Java, supports merging, splitting and rotating.

     <https://pdfsam.org/> || [pdfsam](<https://aur.archlinux.org/packages/pdfsam/>)AUR

  * **PDF Slicer** — Simple application to extract, merge, rotate and reorder pages of PDF documents.

     <https://junrrein.github.io/pdfslicer/> || [pdfslicer](<https://archlinux.org/packages/?name=pdfslicer>)包

  * **PDF Tricks** — Simple, efficient application for small manipulations in PDF files using Ghostscript.

     <https://github.com/muriloventuroso/pdftricks> || [pdftricks](<https://archlinux.org/packages/?name=pdftricks>)包

### Cropping tools

  * **briss** — Java GUI to crop pages of PDF documents to one or more regions selected.

     <https://sourceforge.net/projects/briss/> || [briss](<https://aur.archlinux.org/packages/briss/>)AUR

  * **krop** — Simple graphical tool to crop the pages of PDF files.

     <https://arminstraub.com/software/krop> || [krop](<https://aur.archlinux.org/packages/krop/>)AUR

  * **pdfCropMargins** — Automatically crops the margins of PDF files.

     <https://github.com/abarker/pdfCropMargins> || [pdfcropmargins](<https://aur.archlinux.org/packages/pdfcropmargins/>)AUR

  * **PdfHandoutCrop** — Tool to crop pdf handout with multiple pages per sheet.

     <https://cges30901.github.io/pdfhandoutcrop/> || [pdfhandoutcrop](<https://aur.archlinux.org/packages/pdfhandoutcrop/>)AUR

### Advanced editors

  * **Master PDF Editor** — Functional proprietary PDF editor. Latest version free for non-commercial use. The _-free_ package is outdated but lacks a watermark.

     <https://code-industry.net/free-pdf-editor/> || [masterpdfeditor](<https://aur.archlinux.org/packages/masterpdfeditor/>)AUR, [masterpdfeditor-free](<https://aur.archlinux.org/packages/masterpdfeditor-free/>)AUR

  * **[PDF Studio](</wzh/index.php?title=PDF_Studio&action=edit&redlink=1> "PDF Studio（页面不存在）")** — All-in-one proprietary PDF editor similar to Adobe Acrobat.

     <https://www.qoppa.com/pdfstudio/> || [pdfstudio-bin](<https://aur.archlinux.org/packages/pdfstudio-bin/>)AUR

  * **PDF4QT** — Open source PDF editor.

     <https://jakubmelka.github.io/> || [pdf4qt](<https://aur.archlinux.org/packages/pdf4qt/>)AUR

#### Comparison of advanced editors

Name | Cost (USD, lifetime) | Page Labels | Form Designer | Content Editing (Text and Images) | Optimize PDFs | Digitally Sign PDFs | License   
---|---|---|---|---|---|---|---  
Master PDF Editor  | 85.34 | 否 | 是 | 是 | 是 | 是 | proprietary   
Qoppa PDF Studio Standard  | 99 | 是 | 否 | 否 | 否 | 否 | proprietary   
Qoppa PDF Studio Pro  | 139 | 是 | 是 | 是 | 是 | 是 | proprietary   
  
##  PDF 工具

参见 [Ghostscript](<#%E5%BC%95%E6%93%8E>)。 

  * **Camelot** — Camelot: 为人类提取 PDF 表格。

     <https://github.com/atlanhq/camelot> || [python-camelot](<https://aur.archlinux.org/packages/python-camelot/>)AUR, [python-camelot-git](<https://aur.archlinux.org/packages/python-camelot-git/>)AUR

  * **Coherent PDF** — 专有的非自由命令行工具，用于处理 PDF 文件，包括合并、加密、解密、缩放、裁剪、旋转、书签、印章、徽标和页码。

     <https://community.coherentpdf.com/> || [cpdf](<https://aur.archlinux.org/packages/cpdf/>)AUR

  * **DiffPDF** — 比较两个 PDF 文件中每一页的文本或视觉外观。

     <https://gitlab.com/eang/diffpdf> || [diffpdf](<https://archlinux.org/packages/?name=diffpdf>)包

  * **mupdf-tools** — 作为 MuPDF 的一部分而开发的工具，包含 [mutool(1)](<https://man.archlinux.org/man/mutool.1>) 和 _muraster_ 。

     <https://mupdf.com> || [mupdf-tools](<https://archlinux.org/packages/?name=mupdf-tools>)包

  * **pdfcpu** — 用于创建和修改 PDF 的命令行工具。

     <https://github.com/pdfcpu/pdfcpu> || [pdfcpu-bin](<https://aur.archlinux.org/packages/pdfcpu-bin/>)AUR

  * **pdf_extbook** — 提取已添加书签的 PDF 页面

     <https://github.com/raffaem/pdf_extbook> || [pdf_extbook-git](<https://aur.archlinux.org/packages/pdf_extbook-git/>)AUR

  * **pdfgrep** — 命令行实用程序，用于搜索 PDF 文件中的文本。

     <https://pdfgrep.org/> || [pdfgrep](<https://archlinux.org/packages/?name=pdfgrep>)包

  * **pdfjam** — 可用于将 PDF 文件放大、连接、旋转和翻转，并将其排列成适合书籍装帧的格式。

     <https://github.com/DavidFirth/pdfjam> || [texlive-binextra](<https://archlinux.org/packages/?name=texlive-binextra>)包

  * **pdfminer.six** — 由社区维护的 PDF 文档文本提取工具 pdfminer 的分叉版。

     <https://github.com/pdfminer/pdfminer.six> || [python-pdfminer](<https://archlinux.org/packages/?name=python-pdfminer>)包

  * **pdf2svg** — 将 PDF 文件转换为 SVG 文件。

     <http://www.cityinthesky.co.uk/opensource/pdf2svg/> || [pdf2svg](<https://archlinux.org/packages/?name=pdf2svg>)包

  * **[PDFtk](<https://en.wikipedia.org/wiki/PDFtk> "wikipedia:PDFtk")** — 用于处理 PDF 文档日常事务的简易工具。

     <https://gitlab.com/pdftk-java/pdftk> || [pdftk](<https://archlinux.org/packages/?name=pdftk>)包

  * **[QPDF](<https://en.wikipedia.org/wiki/QPDF> "wikipedia:QPDF")** — 内容保护型 PDF 转换系统

     <https://github.com/qpdf/qpdf> || [qpdf](<https://archlinux.org/packages/?name=qpdf>)包

  * **Stapler** — 使用 [PyPDF2](<#Python>) 库的 PDFtk 轻型替代程序。

     <https://github.com/hellerbarde/stapler> || [stapler](<https://aur.archlinux.org/packages/stapler/>)AUR, [stapler-git](<https://aur.archlinux.org/packages/stapler-git/>)AUR

  * **Tabula** — Tabula 是一款用于释放被困在 PDF 文件中的数据表的工具。

     <https://tabula.technology> || [tabula](<https://aur.archlinux.org/packages/tabula/>)AUR, [tabula-java](<https://aur.archlinux.org/packages/tabula-java/>)AUR

  * **Vector Slicer** — 从 SVG 导出多页 PDF。

     <https://gitlab.gnome.org/World/design/vector-slicer> || [vector-slicer](<https://archlinux.org/packages/?name=vector-slicer>)包

  * **verapdf** — 专用的开放源代码文件格式验证器，涵盖所有 PDF/A 和 PDF/UA 部分和一致性级别。

     <https://verapdf.org> || [verapdf](<https://aur.archlinux.org/packages/verapdf/>)AUR

## Command snippets

### Create a PDF from images

With [GraphicsMagick](<../zh-cn/ImageMagick.html> "GraphicsMagick"): 
    
    $ gm convert 1.jpg 2.jpg 3.jpg out.pdf
    
With [ImageMagick](<../zh-cn/ImageMagick.html> "ImageMagick"): 
    
    $ magick 1.jpg 2.jpg 3.jpg out.pdf
    
Note that ImageMagick's output is lossy. For lossless PDF creation from jpeg, use [img2pdf](<https://archlinux.org/packages/?name=img2pdf>)包. 

### Concatenate PDFs

With Ghostscript: 
    
    $ gs -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=out.pdf -dBATCH 1.pdf 2.pdf 3.pdf
    
With PDFtk: 
    
    $ pdftk 1.pdf 2.pdf 3.pdf cat output out.pdf
    
With Poppler: 
    
    $ pdfunite 1.pdf 2.pdf 3.pdf out.pdf
    
With QPDF: 
    
    $ qpdf --empty --pages 1.pdf 2.pdf 3.pdf -- out.pdf
    
### Extract text from PDF

With Poppler and maintaining the layout: 
    
    $ pdftotext -layout in.pdf out.txt
    
See also [pdftotext(1)](<https://man.archlinux.org/man/pdftotext.1>). 

With [calibre](<https://archlinux.org/packages/?name=calibre>)包: 
    
    $ ebook-convert in.pdf out.txt
    
Results vary between applications, depending on the PDF file. 

### Decrypt a PDF

This section lists commands to decrypt a PDF to an unencrypted file. Note that most [PDF viewers](<#Viewers>) also support encrypted PDFs. 

With PDFtk: 
    
    $ pdftk in.pdf input_pw _password_ output out.pdf
    
With Poppler to PostScript: 
    
    $ pdftops -upw _password_ in.pdf out.ps
    
With QPDF: 
    
    $ qpdf --decrypt --password=_password_ in.pdf out.pdf
    
**提示：** Forgotten passwords might be recovered with [pdfcrack](<https://archlinux.org/packages/?name=pdfcrack>)包, see [pdfcrack(1)](<https://man.archlinux.org/man/pdfcrack.1>).

### Encrypt a PDF

The _user password_ is used for encryption, the _owner password_ to restrict operations once the document is decrypted, for more information, see [Wikipedia:PDF#Encryption and signatures](<https://en.wikipedia.org/wiki/PDF#Encryption_and_signatures> "wikipedia:PDF"). 

With PDFtk: 
    
    $ pdftk in.pdf output out.pdf user_pw _password_
    
With [PoDoFo](<#Libraries>): 
    
    $ podofoencrypt -u _user_password_ -o _owner_password_ in.pdf out.pdf
    
With QPDF: 
    
    $ qpdf --encrypt _user_password_ _owner_password_ _key_length_ -- in.pdf out.pdf
    
where `_key_length_` can be 40, 128 or 256. 

### Extract images from a PDF

With [poppler](<https://archlinux.org/packages/?name=poppler>)包, saving images as JPEG: 
    
    $ pdfimages _infile_.pdf -j _outfileroot_
    
###  Extract page range from PDF, split multipage PDF document

With Ghostscript as a single file[[6]](<https://forums.freebsd.org/threads/split-pdf-file.58902/#post-336971>)
    
    $ gs -sDEVICE=pdfwrite -dNOPAUSE -dBATCH -dSAFER -dFirstPage=_first_ -dLastPage=_last_ -sOutputFile=_outfile_.pdf _infile_.pdf
    
With PDFtk as a single file: 
    
    $ pdftk _infile_.pdf cat _first_ -_last_ output _outfile_.pdf
    
With Poppler as separate files: 
    
    $ pdfseparate -f _first_ -l _last_ _infile_.pdf _outfileroot_ -%d.pdf
    
With QPDF as a single file: 
    
    $ qpdf --empty --pages _infile_.pdf _first_ -_last_ -- _outfile_.pdf
    
With mutool as a single file: 
    
    $ mutool clean -g _infile_.pdf _outfile_.pdf _first_ -_last_
    
###  Impose a PDF (nup)

PDF [Imposition](<https://en.wikipedia.org/wiki/Imposition> "wikipedia:Imposition") is the process by which multiple input pages are combined into one output page, layed out into a _rows_ x _columns_ grid. 

It can be done with [pdfjam](<#PDF_tools>) (notice that wrapper scripts such as _pdfnup_ and _pdfbook_ are deprecated): 
    
    $ pdfjam --nup _rows_ x _columns_ _input.pdf_ --outfile _output.pdf_
    
or with [pdfsak](<https://github.com/raffaem/pdfsak>): 
    
    $ pdfsak --input-file _input.pdf_ --output _output.pdf_ --nup _rows_ _columns_
    
### Inspect metadata

With [ExifTool](</wzh/index.php?title=ExifTool&action=edit&redlink=1> "ExifTool（页面不存在）"): 
    
    $ exiftool -All file.pdf
    
With Poppler: 
    
    $ pdfinfo file.pdf
    
### Remove metadata

#### Using ExifTool

With [ExifTool](</wzh/index.php?title=ExifTool&action=edit&redlink=1> "ExifTool（页面不存在）"): 
    
    $ exiftool -All= -overwrite_original input.pdf
    $ mv input.pdf /tmp/temp.pdf
    $ qpdf --linearize /tmp/temp.pdf input.pdf
    
The linearize step is needed to prevent recovery of deleted metadata. See [this SuperUser question](<https://superuser.com/q/1482619/400542>) and the related [ExifTool forum thread](<https://exiftool.org/forum/index.php/topic,3943.msg54610.html#msg54610>). 

#### Using pdftk

Many PDFs store document metadata using both an Info dictionary (old school) and an XMP stream (new school). This pdftk command remove the XMP stream from the PDF altogether. It does not remove the Info dictionary. 

Note that objects inside the PDF might have their own, separate XMP metadata streams, and that this command does not remove those. It only removes the PDF’s document‐level XMP stream. 
    
    $ pdftk _input.pdf_ drop_xmp output _output.pdf_
    
### Reduce size of a PDF

PDF size can be reduced by setting an appropriate optimization or compression level. 

With Ghostscript one of: 
    
    $ ps2pdf -dPDFSETTINGS=/screen in.pdf out.pdf
    
or 
    
    $ gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/printer -sOutputFile=out.pdf in.pdf
    
For different settings see the [documentation](<https://ghostscript.readthedocs.io/en/latest/VectorDevices.html#controls-and-features-specific-to-postscript-and-pdf-input>). 

There is also [shrinkpdf](<https://aur.archlinux.org/packages/shrinkpdf/>)AUR, a script wrapping gs. 

### Rasterize a PDF

These commands will convert your PDF into images. 

With [GraphicsMagick](<../zh-cn/ImageMagick.html> "GraphicsMagick") to convert a specific page into an image file: 
    
    $ gm convert -density _dpi_ _infile_.pdf[_page_] _outfile_.jpg
    
With [ImageMagick](<../zh-cn/ImageMagick.html> "ImageMagick") to convert a specific page into an image file: 
    
    $ magick convert -density _dpi_ _infile_.pdf[_page_] _outfile_.jpg
    
With [ImageMagick](<../zh-cn/ImageMagick.html> "ImageMagick") to convert all pages into another PDF file composed by an image file per page: 
    
    $ magick convert -density _dpi_ _infile_.pdf _outfile_.pdf
    
**警告：** This will increase the file size of your PDF substantially. Use it for example if your printer is not able to print your PDF correctly.

With Poppler to convert all pages into one image file per page: 
    
    $ pdftoppm -jpeg -r _dpi_ _infile_.pdf _outfileroot_
    
With Poppler to convert a specific page into an image file: 
    
    $ pdftoppm -jpeg -r _dpi_ -f _page_ -singlefile _infile_.pdf _outfileroot_
    
### Split PDF pages

With mupdf-tools to split every page vertically into two pages: 
    
    $ mutool poster -y 2 in.pdf out.pdf
    
Can be used to undo simple [imposition](<#Impose_a_PDF_\(nup\)>). 

### Add an image

Adding an image to any location in a PDF can be done 

  * with [ImageMagick](<../zh-cn/ImageMagick.html> "ImageMagick") (convert), [xv](<https://aur.archlinux.org/packages/xv/>)AUR and [pdftk](<https://archlinux.org/packages/?name=pdftk>)包. ([Wrapper script](<http://emmanuel.branlard.free.fr/work/linux/dev/SignPDF/SignPDF>))
  * with [xournal](<https://aur.archlinux.org/packages/xournal/>)AUR
  * with [LibreOffice](<../zh-cn/LibreOffice.html> "LibreOffice")

Details on these and other solutions can be found [on StackExchange](<https://unix.stackexchange.com/questions/85873/how-can-i-add-a-signature-png-to-a-pdf-in-linux>). 

### Add digital signature to PDF

[jsignpdf](<https://aur.archlinux.org/packages/jsignpdf/>)AUR can digitally sign PDF files with X.509 certificates in GUI and CLI. 

Readers such as Okular and MuPDF can sign PDFs with digital signatures. This requires a PFX certificate, which can be created with an [OpenSSL command](<../zh-cn/OpenSSL.html#Generate_a_self-signed_certificate_with_private_key_in_a_single_command> "OpenSSL"): 
    
    $ openssl req -x509 -days 365 -newkey rsa:2048 -keyout _cert.pem_ -out _cert.pem_
    $ openssl pkcs12 -export -in _cert.pem_ -out _cert.pfx_
    
MuPDF users can then sign PDFs with the `_cert.pfx_` using the graphical interface, or its [mutool-sign](<https://mupdf.readthedocs.io/en/latest/mutool-sign.html>) tool. 

Okular users must import `_cert.pfx_` into a certificate store such as the one in the default Firefox profile.[[7]](<https://docs.kde.org/trunk5/en/okular/okular/signatures.html>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2024-01-13 ⓘ] With Firefox this is done through _Settings > Privacy & Security > View Certificates > Your Certificates > Import_ and selecting _cert.pfx_. Afterwards Okular will offer this certificate to be used when signing PDFs. 

Libreoffice can also sign PDFs.[[8]](<https://help.libreoffice.org/6.3/en-US/text/shared/guide/digital_signatures.html>)

### Removing annotations from a PDF

With [pdftk](<https://archlinux.org/packages/?name=pdftk>)包 [[9]](<https://stackoverflow.com/questions/49598797/remove-pdf-annotations-via-command-line/49614525#49614525>): 
    
    $ pdftk in.pdf output - uncompress | sed '/^\/Annots/d' | pdftk - output out.pdf compress
    
With [perl-cam-pdf](<https://aur.archlinux.org/packages/perl-cam-pdf/>)AUR: 
    
    $ rewritepdf.pl -C in.pdf out.pdf
    
See <https://superuser.com/a/1051543> for more information. 

### Add page numbers

With [pdfsak](<https://github.com/raffaem/pdfsak>): 
    
    $ pdfsak --input-file input.pdf --output output.pdf --text "\large \$page/\$pages" br 0.99 0.99 --latex-engine xelatex --font "Noto Regular"
    
### Add page labels

Page labels are logical page numbers shown in the navigation bar of your PDF reader. They are useful for example if the first pages of the PDF are indices numbered with roman numbers (I, II, etc.), while the page numbered "1" corresponds to a PDF page greater than 1, and you want the page number shown in the navigation bar to corresponds to the page number shown in the physical page. 

This should not be confused with adding page numbers into a physical page. See [section 12.4.2 of PDF reference](<https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/PDF32000_2008.pdf#page=382>) to better understand page labels. 

  1. Using [pagelabels-py](<https://github.com/lovasoa/pagelabels-py>), let's say we have a PDF named `my_document.pdf`, that has 12 pages. 
     * Pages 1 to 4 should be labelled `Intro I` to `Intro IV`.
     * Pages 5 to 9 should be labelled `2` to `6`.
     * Pages 10 to 12 should be labelled `Appendix A` to `Appendix C`
     * We can issue the following list of commands: 
           
           $ python3 -m pagelabels --delete "my_document.pdf"
           $ python3 -m pagelabels --startpage 1 --prefix "Intro " --type "roman uppercase" "my_document.pdf"
           $ python3 -m pagelabels --startpage 5 --firstpagenum 2 "my_document.pdf"
           $ python3 -m pagelabels --startpage 10 --prefix "Appendix " --type "letters uppercase" "my_document.pdf" 

     * **注意：** pagelabels-py will convert your file to PDF 1.3 specification

  2. Using [pdftk](<https://archlinux.org/packages/?name=pdftk>)包, create a `metadata.txt` file with labels: 
         
         PageLabelBegin
         PageLabelNewIndex: 1
         PageLabelStart: 1
         PageLabelPrefix: Cover
         PageLabelNumStyle: NoNumber
         PageLabelBegin
         PageLabelNewIndex: 2
         PageLabelStart: 1
         PageLabelPrefix: Back Cover
         PageLabelNumStyle: NoNumber
         PageLabelBegin
         PageLabelNewIndex: 3
         PageLabelStart: 1
         PageLabelNumStyle: LowercaseRomanNumerals
         PageLabelBegin
         PageLabelNewIndex: 27
         PageLabelStart: 1
         PageLabelNumStyle: DecimalArabicNumerals 

     * Where: 

PageLabelBegin
    signal a new page label definition will follow
PageLabelNewIndex
    is the PDF page index from which the numbering style applies, counting from one. The numbering style will continue until the next page label or, if there are no more page labels, until the end of the document.
PageLabelStart
    is the starting number. For example, if you specify 5 here, the pages will be numbered 5, 6, 7, ...
PageLabelPrefix
    a text to put before the number in page labels.
PageLabelNumStyle
    can be `DecimalArabicNumerals`, `UppercaseRomanNumerals`, `LowercaseRomanNumerals`, `UppercaseLetters`, `LowercaseLetters` or `NoNumber`.
     * Then use: 
           
           pdftk book.pdf update_info_utf8 metadata.txt output book-with-metadata.pdf

See [this SuperUser question](<https://superuser.com/questions/232553/how-to-change-internal-page-numbers-in-the-meta-data-of-a-pdf>) for more details. 

### Extract bookmarks

With pdftk: 
    
    $ pdftk file.pdf dump_data_utf8 | grep '^Bookmark'
    
With qpdf: 
    
    $ qpdf --json --json-key=outlines file.pdf
    
See <https://unix.stackexchange.com/questions/143886/how-to-extract-bookmarks-from-a-pdf-file> for more information. 

### Add bookmarks

#### With pdftk

Create a text file `bookmark_definitions.txt` with bookmark definitions in the following format: 
    
    BookmarkBegin
    BookmarkTitle: Chapter 1
    BookmarkLevel: 1
    BookmarkPageNumber: 1
    BookmarkBegin
    BookmarkTitle: Chapter 1.1
    BookmarkLevel: 2
    BookmarkPageNumber: 2
    BookmarkBegin
    BookmarkTitle: Chapter 1.2
    BookmarkLevel: 2
    BookmarkPageNumber: 3
    BookmarkBegin
    BookmarkTitle: Chapter 1.3
    BookmarkLevel: 2
    BookmarkPageNumber: 4
    BookmarkBegin
    BookmarkTitle: Chapter 1.3.1
    BookmarkLevel: 3
    BookmarkPageNumber: 5
    BookmarkBegin
    BookmarkTitle: Chapter 2
    BookmarkLevel: 1
    BookmarkPageNumber: 6
    
Where 

BookmarkBegin
    signal a new bookmark definition
BookmarkTitle
    the title of the bookmark
BookmarkLevel
    the level of the bookmark in the hierarchy
BookmarkPageNumber
    the page number the bookmark redirects to

In this example, the above file will create the following bookmark structure: 

  * Chapter 1 
    * Chapter 1.1
    * Chapter 1.2
    * Chapter 1.3 
      * Chapter 1.3.1
  * Chapter 2

Apply the bookmarks with the following command: 
    
    $ pdftk _input.pdf_ update_info_utf8 _bookmark_definitions.txt_ output _output.pdf_
    
### Extract pages contained within a bookmark

To extract the pages contained within a bookmark, you can use [pdf_extbook-git](<https://aur.archlinux.org/packages/pdf_extbook-git/>)AUR. 

With `pdf_extbook _file_` you will be prompted on what bookmark whose pages you want to extract and where to save it. To extract all bookmarks of a given hierarchical level: 
    
    $ pdf_extbook _file_ -a _level_ _output_file_stem_
    
### Remove blank pages

One can use the following script to remove blank pages form a PDF file (credit: [SuperUser post](<https://superuser.com/a/1307895>)): 
    
    #!/bin/sh
    
    IN="$1"
    filename=$(basename "${IN}")
    filename="${filename%.*}"
    PAGES=$(pdfinfo "$IN" | grep ^Pages: | tr -dc '0-9')
    
    non_blank() {
    	for i in $(seq 1 $PAGES); do
    		PERCENT=$(gs -o - -dFirstPage=${i} -dLastPage=${i} -sDEVICE=ink_cov "$IN" | grep CMYK | nawk 'BEGIN { sum=0; } {sum += $1 + $2 + $3 + $4;} END { printf "%.5f\n", sum } ')
    		if [ $(echo "$PERCENT > 0.001" | bc) -eq 1 ]; then
    			echo $i
    			#echo $i 1>&2
    		fi
    		echo -n . 1>&2
    	done | tee "$filename.tmp"
    	echo 1>&2
    }
    
    set +x
    pdftk "${IN}" cat $(non_blank) output "${filename}_noblanks.pdf"
    
Use it like `pdf_remove_blank_pages input.pdf`. 

The script needs [pdftk](<https://archlinux.org/packages/?name=pdftk>)包, [nawk](<https://archlinux.org/packages/?name=nawk>)包 and [ghostscript](<https://archlinux.org/packages/?name=ghostscript>)包. 

### Find fonts used in a PDF

The [pdffonts(1)](<https://man.archlinux.org/man/pdffonts.1>) command (from [poppler](<https://archlinux.org/packages/?name=poppler>)包), can be used to find which fonts a PDF uses and if they have been embedded in it or not: 
    
    $ pdffonts _file_.pdf
    
    name                                 type              encoding         emb sub uni object ID
    ------------------------------------ ----------------- ---------------- --- --- --- ---------
    Times-Roman                          Type 1            Custom           no  no  no       8  0
    Times-Italic                         Type 1            Standard         no  no  no       9  0
    Times-Bold                           Type 1            Standard         no  no  no       7  0
    Helvetica                            Type 1            Standard         no  no  no      34  0
    Helvetica-Bold                       Type 1            Standard         no  no  no      35  0
    
This can be used when having issues displaying properly the text in a PDF, to determine if missing [fonts](<../zh-cn/%E5%AD%97%E4%BD%93.html> "Fonts") or their [metric-compatible equivalent](</wzh/index.php?title=Metric-compatible_fonts&action=edit&redlink=1> "Metric-compatible fonts（页面不存在）") need to be installed. 

### Repair broken PDF file

With [ghostscript](<https://archlinux.org/packages/?name=ghostscript>)包: 
    
    $ gs -o _repaired.pdf_ -sDEVICE=pdfwrite -dPDFSETTINGS=/prepress _corrupted.pdf_
    
With [poppler](<https://archlinux.org/packages/?name=poppler>)包: 
    
    $ pdftocairo -pdf _corrupted.pdf_ _repaired.pdf_
    
With [mupdf-tools](<https://archlinux.org/packages/?name=mupdf-tools>)包: 
    
    $ mutool clean _corrupted.pdf_ _repaired.pdf_
    
Reference: <https://superuser.com/q/278562>

###  Convert PDF to PDF/A standard

With [ghostscript](<https://archlinux.org/packages/?name=ghostscript>)包: 
    
    $ gs -dPDFA -dBATCH -dNOPAUSE -sColorConversionStrategy=UseDeviceIndependentColor -sDEVICE=pdfwrite -dPDFACompatibilityPolicy=2 -sOutputFile=_document_pdfa.pdf_ _document.pdf_
    
Reference: <https://stackoverflow.com/a/56459053>

###  Validate PDF/A compliance

Using [verapdf](<https://aur.archlinux.org/packages/verapdf/>)AUR you can validate the compliance of your PDF to different flavours of the PDF/A standard: 
    
    $ verapdf --flavour 1a --format text _document.pdf_
    
## DjVu tools

  * [DjVuLibre](<#Engines>) provides many command-line tools, like [ddjvu(1)](<https://man.archlinux.org/man/ddjvu.1>) for example.
  * **img2djvu** — Single-pass DjVu encoder based on DjVu Libre and ImageMagick.

     <https://github.com/ashipunov/img2djvu> || [img2djvu-git](<https://aur.archlinux.org/packages/img2djvu-git/>)AUR

  * **pdf2djvu** — Creates DjVu files from PDF files.

     <https://jwilk.net/software/pdf2djvu> || [pdf2djvu](<https://aur.archlinux.org/packages/pdf2djvu/>)AUR

### Convert DjVu to images

Break Djvu into separate pages: 
    
    $ djvmcvt -i input.djvu /path/to/out/dir output-index.djvu
    
Convert Djvu pages into images: 
    
    $ ddjvu --format=tiff page.djvu page.tiff
    
Convert Djvu pages into PDF: 
    
    $ ddjvu --format=pdf inputfile.djvu ouputfile.pdf
    
You can also use _\--page_ to export specific pages: 
    
    $ ddjvu --format=tiff --page=1-10 input.djvu output.tiff
    
this will convert pages from 1 to 10 into one tiff file. 

### Processing images

You can use [scantailor-advanced](<https://archlinux.org/packages/?name=scantailor-advanced>)包 to: 

  * fix orientation
  * split pages
  * deskew
  * crop
  * adjust margins

### Make DjVu from images

There is a useful script [img2djvu-git](<https://aur.archlinux.org/packages/img2djvu-git/>)AUR. 
    
    $ img2djvu -c1 -d600 -v1 ./out
    
it will create 600 DPI `out.djvu` from all files in `./out` directory. 

Alternatively, you can try [didjvu](<https://aur.archlinux.org/packages/didjvu/>)AUR, which seems to create smaller files especially on images with well defined background. 

## PostScript tools

  * **pstotext** — Converts PostScript files to text.

     <https://www.cs.wisc.edu/~ghost/doc/pstotext.htm> || [pstotext](<https://aur.archlinux.org/packages/pstotext/>)AUR

  * [Ghostscript](<#Engines>)

### ps2pdf

_ps2pdf_ is a wrapper around ghostscript to convert PostScript to PDF: 
    
    $ ps2pdf -sPAPERSIZE=a4 -dOptimize=true -dEmbedAllFonts=true YourPSFile.ps
    
Explanation: 

  * with `-sPAPERSIZE=something` you define the paper size. For valid PAPERSIZE values, see [[10]](<https://ghostscript.com/doc/current/Use.htm#Known_paper_sizes>)[[失效链接](<https://zh.wikipedia.org/wiki/Wikipedia:%E5%A4%B1%E6%95%88%E9%93%BE%E6%8E%A5> "zhwp:Wikipedia:失效链接") 2022-09-22 ⓘ].
  * `-dOptimize=true` lets the created PDF be optimised for loading.
  * `-dEmbedAllFonts=true` makes the fonts look always nice.

**注意：** You cannot choose the paper orientation in ps2pdf. If your input PS file is healthy, it already contains the orientation information. If you are trying to use an Encapsulated PS file, you will have problems, if it does not fit in the `-sPAPERSIZE` you specified, because EPS files usually do not contain paper orientation information. A workaround is creating a new paper in ghostscript settings (call it e.g. "slide") and use it as `-sPAPERSIZE=slide`.

## Libraries

###  C/C++

  * **libharu** — C library for generating PDF documents.

     <https://github.com/libharu/libharu> || [libharu](<https://archlinux.org/packages/?name=libharu>)包, Lua binding: [lua-hpdf](<https://aur.archlinux.org/packages/lua-hpdf/>)AUR

  * **PoDoFo** — A C++ library to work with the PDF file format.

     <https://podofo.sourceforge.net> || [podofo](<https://archlinux.org/packages/?name=podofo>)包

### Python

  * **borb** — borb is a library for reading, creating and manipulating PDF files in python.

     <https://borbpdf.com/>, <https://github.com/jorisschellekens/borb> || 未被打包？[在 AUR 里搜索](<https://aur.archlinux.org/packages/>)

  * **pdfrw** — A pure Python library that reads and writes PDFs.

     <https://github.com/pmaupin/pdfrw> || [python-pdfrw](<https://archlinux.org/packages/?name=python-pdfrw>)包

  * **PyPDF** — A pure-Python library built as a PDF toolkit.

     <https://github.com/py-pdf/pypdf> || [python-pypdf](<https://archlinux.org/packages/?name=python-pypdf>)包

  * **PyX** — Python library for the creation of PostScript and PDF files.

     <https://pyx.sourceforge.net> || [python-pyx](<https://archlinux.org/packages/?name=python-pyx>)包

  * **ReportLab** — A proven industry-strength PDF generating solution

     <https://www.reportlab.com/> || [python-reportlab](<https://archlinux.org/packages/?name=python-reportlab>)包

### Java

  * **iText Core** — iText is a more versatile, programmable and enterprise-grade PDF solution that allows you to embed its functionalities within your own software for digital transformation.

     <https://itextpdf.com/products/itext-core> || [itext-rups-bin](<https://aur.archlinux.org/packages/itext-rups-bin/>)AUR

  * **OpenPDF** — OpenPDF is a free Java library for creating and editing PDF files with a LGPL and MPL open source license. OpenPDF is based on a fork of iText.

     <https://github.com/LibrePDF/OpenPDF> || 未被打包？[在 AUR 里搜索](<https://aur.archlinux.org/packages/>)

## See also

  * [List of applications/Documents#OCR software](<../zh-cn/List_of_applications/Documents.html#OCR_software> "List of applications/Documents")
  * [List of applications/Documents#Readers and viewers](<../zh-cn/List_of_applications/Documents.html#Readers_and_viewers> "List of applications/Documents")
  * [List of applications/Documents#Stylus note-taking](<../zh-cn/List_of_applications/Documents.html#Stylus_note-taking> "List of applications/Documents")
  * [Wikipedia:List of PDF software](<https://en.wikipedia.org/wiki/List_of_PDF_software> "wikipedia:List of PDF software")
  * PDF References 
    * [PDF Reference and Adobe Extensions to the PDF Specification](<https://opensource.adobe.com/dc-acrobat-sdk-docs/pdfstandards/PDF32000_2008.pdf>)
    * [Wikipedia:PDF#Further reading](<https://en.wikipedia.org/wiki/PDF#Further_reading> "wikipedia:PDF")
