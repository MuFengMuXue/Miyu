# Parchive

Parchive (Parity archive) is a file verification and repair tool using PAR2 files to detect damage in data files and repair them if necessary. It can be used with any kind of file.

## Installation
Install the  package. The commands , ,  and  are now available.

## How it works
 takes the input file(s) and interprets the input as a certain number of data blocks. Based on the data blocks,  then creates recovery blocks with the help of the Reed–Solomon error correction code. Later, you can trade any recovery block for any corrupted data block in order to repair the source data. You need as much recovery blocks as data blocks have gone corrupted in order to repair the file(s) successfully.

Let us say you want to calculate 30% of recovery information for a precious file:

 $ par2create -r30 file

Parchive now has created the  index file which is essentially not needed for recovery. Additionally, it has created the recovery blocks and has spread them into multiple files. If you created, say, 592 recovery blocks, you will find the files

 file.vol000+001.par2
 file.vol001+002.par2
 file.vol003+004.par2
 file.vol007+008.par2
 file.vol015+016.par2
 file.vol031+032.par2
 file.vol063+064.par2
 file.vol127+128.par2
 file.vol255+256.par2
 file.vol511+081.par2

The number left of the plus sign is the index of the first recovery block in the particular file and the number on the right the number of recovery blocks the file provides.

In the early days where no integrity check was done on link level these files proved useful since one could select recovery files based on the number of data blocks gone corrupted. If your download left you with 43 corrupted data blocks, you could convert the number to binary and instantly see what recovery files you had to fetch:

     32 16  8  4  2  1
 43 = 1  0  1  0  1  1

 → download *+032.par2, *+008.par2, *+002.par2 and *+001.par2.

This is very efficient in terms of bandwidth usage. One would finally call

 $ par2repair file*.par2

in order to repair the downloaded file(s). You can ignore the index file since Parchive can handle a missing index file. Sometimes it is useful to include the  parameter in order to reach an intact data block which would otherwise go undetected.

## Tips and tricks
## Batch-protecting your files
It may be the case that you do not want to serve clients recovery files, but want to ensure additional integrity of your files. In times of helium filled hard disk drives, shingled-bit technology, dense capacity per square centimeter, transfer losses etc. the probability of bit rot is high. Remember that you should always have (automated) backups of your data, but a little additional protection does not hurt, especially since we have so much storage available today. By creating  files you have a much more convenient way to verify the integrity of your data and restore the data than running application programs over the files and sieving for error outputs. Bit rot now can happen in both the original file(s) AND the recovery file(s), and you still can repair the original file(s).

As a consequence, one recovery file containing all recovery packets is sufficient (parameter ). This also reduces the amount of recovery data. An important question to answer is the percentage of redundancy you want to have. Especially for smaller files (<1 MiB) the amount of recovery data does not really correlate with the original file size:

{| class="wikitable"
! Original data !! percentage !! Recovery data (without index)
|-
| 184.8 KiB || 5 || 287.8 KiB
|-
| 184.8 KiB || 100 || 743.1 KiB
|-
| 3.4 MiB || 5 || 458.8 KiB
|-
| 3.4 MiB || 30 || 1.5 MiB
|-
| 3.4 MiB || 100 || 4 MiB
|-
| 1.7 GiB || 5 || 87.6 MiB
|}

5% is a reasonable amount of recovery data but you can go up to 100% recovery data for really important files. 100% recovery files can restore your file if you accidentally deleted the original one and you are too lazy to search for the file in your backup (you have one, have you? :).

Here is a simple script which runs over the current directory recursively and batch-protects the files:

{{hc|~/bin/batchprotect.sh|2=#!/bin/bash
readonly REDUNDENCY_PERCENTAGE=5
readonly PRINT_ON_SUCCESS=1

create_par2() {

  local current_file="${1}"
  if [ ! -e "${current_file}-5p.par2" ] && [ -s "${current_file}" ]; then
    if par2create -n1 -q -q -r"${REDUNDENCY_PERCENTAGE}" "${current_file}"; then

      if [ "${PRINT_ON_SUCCESS}" = 1 ]; then
        printf '\033\033[1;34m%s \033[1;32m%s \033[0m\n' \
                'Creating par2 on' "${current_file}" 'successful'
      fi

      rm "${current_file}.par2"
      mv "${current_file}".vol*par2 "${current_file}-${REDUNDENCY_PERCENTAGE}p.par2"
      return 0

    else
      printf '\033[1;37m%s \033[1;34m%s \033[1;31m%s \033[0m\n' \
              'Creating par2 on' "${current_file}" 'failed'
      return 1
    fi
  fi
}

verify_par2() {

  local current_file="${1}"
  if [ -f "${current_file}-${REDUNDENCY_PERCENTAGE}p.par2" ; then
    if par2verify -q -q "${current_file}-${REDUNDENCY_PERCENTAGE}p.par2"; then
      if [ "${PRINT_ON_SUCCESS}" = 1 ]; then
        printf '\033\033[1;34m%s \033[1;32m%s \033[0m\n' \
                'Verifying par2 on' "${current_file}" 'successful'
      fi
      return 0
    else
      printf '\033[1;37m%s \033[1;34m%s \033[1;31m%s \033[0m\n' \
              'Verifying par2 on' "${current_file}" 'failed'
      return 1
    fi
  fi
}

repair_par2() {

  local current_file="${1}"
  if [ -f "${current_file}-${REDUNDENCY_PERCENTAGE}p.par2" ; then
    if par2repair -p -q -q "${current_file}-${REDUNDENCY_PERCENTAGE}p.par2"; then
      if [ "${PRINT_ON_SUCCESS}" = 1 ]; then
        printf '\033\033[1;34m%s \033[1;32m%s \033[0m\n' \
                'Repairing' "${current_file}" 'successful'
      fi
      return 0
    else
      printf '\033[1;37m%s \033[1;34m%s \033[1;31m%s \033[0m\n' \
              'Repairing' "${current_file}" 'failed'
      return 1
    fi
  fi
}

main() {

  while read -r current_file; do
    # Create or verify
    if [ ! -e "${current_file}-${REDUNDENCY_PERCENTAGE}p.par2" ; then
      create_par2 "$current_file"
    else
      if ! verify_par2 "$current_file"; then
        repair_par2 "$current_file"
      fi
    fi
  # We ignore the file itself, any par2/sig extension and any .git directory and print without the leading ./
  done < <(find . -type f ! -name '*par2loop.sh' ! -name '*par2' ! -name '*.sig' ! -path '*.git*' -prune -a -printf '%P\n'  shuf)
}

main
}}

You would then call  in order to have all files in the current directory recursively protected by Parchive. Additionally, you do not have to maintain list of checksums since gpg can do that for you, too.

## Verification
 $ par2verify file-5.par2
 $ cfv file-5.par2
 $ gpg --verify file.sig

And, if you changed the path of the original file:

 $ par2verify -B / file-5.par2 /new/path/to/fileRenamed
 $ gpg --verify file.sig /new/path/to/fileRenamed

You can also change the path of the / file.
