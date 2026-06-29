# Trash

## Description

Portal for trashing files

This simple interface lets sandboxed applications send files to the trashcan.

This documentation describes version 1 of this interface.

## Properties

### org.freedesktop.portal.Trash:version

    version readable u

## Methods

### org.freedesktop.portal.Trash.TrashFile

    TrashFile (
      IN fd h,
      OUT result u
    )

Sends a file to the trashcan. Applications are allowed to trash a file if they can open it in r/w mode.

fd  
file descriptor for the file to trash

result  
the result. 0 if trashing failed, 1 if trashing succeeded, other values may be returned in the future
