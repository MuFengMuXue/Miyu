# JPEG XL

From Wikipedia:JPEG XL:

:JPEG XL is a royalty-free raster-graphics file format that supports both lossy and lossless compression. It is designed to outperform existing raster formats and thus become their universal replacement.

## Usage
 comes with the official encoder/decoder programs: cjxl and djxl. JPEG XL is also supported by  and . To convert existing formats to jxl (JPEG files are compressed losslessly by default) use:

 $ cjxl input.jpg lossless.jxl

To display image metadata:

 $ jxlinfo input.jxl

Exiftool also supports jxl since 12.25, but might be limited by some metadata that needs to be decoded.  flag can be passed to cjxl to keep metadata uncompressed, making it possible for Exiftool to parse it.

For file de-duplication purposes, it might be desirable to get the checksum of the actual encoded image:

 $ exiftool -api ImageHashType=MD5 -ImageDataHash

## Support
Browsers:

* Firefox (nightly): set  to  in .
* Chromium: Enable the flag .

Image viewers:

* Gwenview: install
*
*

Previewers:

* Dolphin: install
*
