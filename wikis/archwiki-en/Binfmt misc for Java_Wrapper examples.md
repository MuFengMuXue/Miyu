# Binfmt misc for Java/Wrapper examples

These are examples of wrappers and C code which can be used to run Java programs via .

## jarwrapper
 #!/bin/bash
 # /usr/local/bin/jarwrapper - the wrapper for binfmt_misc/jar

 # set path to java using JAVA_HOME if available, otherwise assume it's on the PATH
 JAVA_PATH=${JAVA_HOME:+$JAVA_HOME/jre/bin/}java
 $JAVA_PATH -jar "$@"

## javawrapper
 #!/bin/bash
 # /usr/local/bin/javawrapper - the wrapper for binfmt_misc/java

 if [ -z "$1" ]; then
 	exec 1>&2
 	echo Usage: $0 class-file
 	exit 1
 fi

 CLASS=$1
 FQCLASS=`/usr/local/bin/javaclassname $1`
 FQCLASSN=`echo $FQCLASS | sed -e 's/^.*\.\(FQCLASSP=`echo $FQCLASS | sed -e 's-\.-/-g' -e 's-^[^/*$--' -e 's-/# for example:
 # CLASS=Test.class
 # FQCLASS=foo.bar.Test
 # FQCLASSN=Test
 # FQCLASSP=foo/bar

 unset CLASSBASE

 declare -i LINKLEVEL=0

 while :; do
 	if [ "`basename $CLASS .class`" == "$FQCLASSN" ; then
 		# See if this directory works straight off
 		cd -L `dirname $CLASS`
 		CLASSDIR=$PWD
 		cd $OLDPWD
 		if echo $CLASSDIR | grep -q "$FQCLASSP$"; then
 			CLASSBASE=`echo $CLASSDIR | sed -e "s.$FQCLASSP$.."`
 			break;
 		fi
 		# Try dereferencing the directory name
 		cd -P `dirname $CLASS`
 		CLASSDIR=$PWD
 		cd $OLDPWD
 		if echo $CLASSDIR | grep -q "$FQCLASSP$"; then
 			CLASSBASE=`echo $CLASSDIR | sed -e "s.$FQCLASSP$.."`
 			break;
 		fi
 		# If no other possible filename exists
 		if [ ! -L $CLASS ]; then
 			exec 1>&2
 			echo $0:
 			echo "  $CLASS should be in a" \
 			     "directory tree called $FQCLASSP"
 			exit 1
 		fi
 	fi
 	if [ ! -L $CLASS ]; then break; fi
 	# Go down one more level of symbolic links
 	let LINKLEVEL+=1
 	if [ $LINKLEVEL -gt 5 ]; then
 		exec 1>&2
 		echo $0:
 		echo "  Too many symbolic links encountered"
 		exit 1
 	fi
 	CLASS=`ls --color=no -l $CLASS | sed -e 's/^.* \(*\)$/\1/'`
 done

 if [ -z "$CLASSBASE" ]; then
 	if [ -z "$FQCLASSP" ]; then
 		GOODNAME=$FQCLASSN.class
 	else
 		GOODNAME=$FQCLASSP/$FQCLASSN.class
 	fi
 	exec 1>&2
 	echo $0:
 	echo "  $FQCLASS should be in a file called $GOODNAME"
 	exit 1
 fi

 if ! echo $CLASSPATH | grep -q "^\(.*:\)*$CLASSBASE\(:.*\)*"; then
 	# class is not in CLASSPATH, so prepend dir of class to CLASSPATH
 	if [ -z "${CLASSPATH}" ] ; then
 		export CLASSPATH=$CLASSBASE
 	else
 		export CLASSPATH=$CLASSBASE:$CLASSPATH
 	fi
 fi

 shift
 # set path to java using JAVA_HOME if available, otherwise assume it's on the PATH
 JAVA_PATH=${JAVA_HOME:+$JAVA_HOME/jre/bin/}java
 $JAVA_PATH $FQCLASS "$@"

## javaclassname (support for javawrapper)
This program is used by the javawrapper script above. Compile it with the command
 $ gcc -O2 -o javaclassname javaclassname.c
and move the executable to .
 /* javaclassname.c
  *
  * Extracts the class name from a Java class file; intended for use in a Java
  * wrapper of the type supported by the binfmt_misc option in the Linux kernel.
  *
  * Copyright (C) 1999 Colin J. Watson .
  *
  * This program is free software; you can redistribute it and/or modify
  * it under the terms of the GNU General Public License as published by
  * the Free Software Foundation; either version 2 of the License, or
  * (at your option) any later version.
  *
  * This program is distributed in the hope that it will be useful,
  * but WITHOUT ANY WARRANTY; without even the implied warranty of
  * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  * GNU General Public License for more details.
  *
  * You should have received a copy of the GNU General Public License
  * along with this program; if not, write to the Free Software
  * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
  */

 #include
 #include
 #include
 #include

 /* From Sun's Java VM Specification, as tag entries in the constant pool. */

 #define CP_UTF8 1
 #define CP_INTEGER 3
 #define CP_FLOAT 4
 #define CP_LONG 5
 #define CP_DOUBLE 6
 #define CP_CLASS 7
 #define CP_STRING 8
 #define CP_FIELDREF 9
 #define CP_METHODREF 10
 #define CP_INTERFACEMETHODREF 11
 #define CP_NAMEANDTYPE 12

 /* Define some commonly used error messages */

 #define seek_error() error("%s: Cannot seek\n", program)
 #define corrupt_error() error("%s: Class file corrupt\n", program)
 #define eof_error() error("%s: Unexpected end of file\n", program)
 #define utf8_error() error("%s: Only ASCII 1-255 supported\n", program);

 char *program;

 long *pool;

 u_int8_t read_8(FILE *classfile);
 u_int16_t read_16(FILE *classfile);
 void skip_constant(FILE *classfile, u_int16_t *cur);
 void error(const char *format, ...);
 int main(int argc, char **argv);

 /* Reads in an unsigned 8-bit integer. */
 u_int8_t read_8(FILE *classfile)
 {
 	int b = fgetc(classfile);
 	if(b == EOF)
 		eof_error();
 	return (u_int8_t)b;
 }

 /* Reads in an unsigned 16-bit integer. */
 u_int16_t read_16(FILE *classfile)
 {
 	int b1, b2;
 	b1 = fgetc(classfile);
 	if(b1 == EOF)
 		eof_error();
 	b2 = fgetc(classfile);
 	if(b2 == EOF)
 		eof_error();
 	return (u_int16_t)((b1 = cp_count)
 		corrupt_error();
 	if(!pool|| pool[this_class == -1)
 		corrupt_error();
 	if(fseek(classfile, pool+ 1, SEEK_SET))
 		seek_error();

 	classinfo_ptr = read_16(classfile);
 	if(classinfo_ptr = cp_count)
 		corrupt_error();
 	if(!pool[classinfo_ptr || pool== -1)
 		corrupt_error();
 	if(fseek(classfile, pool[classinfo_ptr + 1, SEEK_SET))
 		seek_error();

 	length = read_16(classfile);
 	for(i = 0; i < length; ++i)
 	{
 		u_int8_t x = read_8(classfile);
 		if((x & 0x80) || !x)
 		{
 			if((x & 0xE0) == 0xC0)
 			{
 				u_int8_t y = read_8(classfile);
 				if((y & 0xC0) == 0x80)
 				{
 					int c = ((x & 0x1f) << 6) + (y & 0x3f);
 					if(c) putchar(c);
 					else utf8_error();
 				}
 				else utf8_error();
 			}
 			else utf8_error();
 		}
 		else if(x == '/') putchar('.');
 		else putchar(x);
 	}
 	putchar('\n');
 	free(pool);
 	fclose(classfile);
 	return 0;
 }
