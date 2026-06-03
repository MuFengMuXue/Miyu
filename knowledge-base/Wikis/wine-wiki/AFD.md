AFD is the "Ancillary Function Driver", which lives in afd.sys, exposes
the `\Device\Afd` device and manages at least the top layer of the
kernel networking stack for (TCP + UDP)/(IPv4 + IPv6) sockets. Each
socket handle exposed by ws2_32 is a file on the AFD device. That socket
handles correspond to kernel file handles should come as no surprise,
given that CreateIoCompletionPort() works on them—and this has been
basically true in Wine since forever.

## Overview

After 02a764e702 a few different applications (Rust applications using the Mio or Smol
libraries #50520, Starcraft
Remastered #50366, League of
Legends #50868) started
trying to use SIO_BASE_HANDLE on socket handles, followed by
DeviceIoControl calls on the returned handle.

At about the same time, Wine was in the middle of an effort to create a
PE/Unix split. In most cases this meant moving Unix library calls to a
separate .so module; in the case of consoles and sockets a better
solution was to follow Windows and make them win32 file handles,
whereupon the PE part of the module would only use NT ioctls on the
device, with all of the Unix code in ntdll or the server (or both). It
was pretty easy to recover device names via ObjectNameInformation, but
in neither case was the kernel interface documented, so we invented our
own ioctls.

The aforementioned applications gave me the needed hint. AFD ioctls
overloaded FILE_DEVICE_BEEP. At that point it was pretty easy to scan
through ioctls on the BEEP device to see which returned some status
other than STATUS_INVALID_DEVICE_REQUEST, and from there I started
passing parameters through to native (starting with the ones the
applications used, then moving on to the rest) to see if I could get
them to succeed and do something interesting. This was only partially
successful—I was able to decode several ioctls, but the rest remain a
mystery, and so do some of the parameters of the ioctls I successfully
decoded. For the rest I've elected to use our own ioctl numbers anyway
(using FILE_DEVICE_NETWORK).

Since it may become possible in the future to decode more ioctls
(through more fuzzing work, or something) I'm making a list of the
ioctls I've decoded below, plus my personal notes. There were also some
ioctls which I decoded but aren't useful for Wine (e.g. they're not
apparently versatile enough to implement some function we need, or they
interact weirdly with whatever private data native ws2_32 stores).

Note that it's not hard to find documentation on these online, including
in the source to the aforementioned Rust libraries. However, it appears
that all such documentation is derived from ReactOS, which is not
considered a legally safe source for use in Wine.

## Methods

Ioctl numbers were determined by calling NtDeviceIoControlFile() in a
loop, with FILE_DEVICE_BEEP, FILE_ANY_ACCESS, and all methods and I
think all function numbers. The ones I found ended up being all
consecutive (with varying methods) so I think it's likely I found most
of them anyway.

In order to determine parameter size, I mostly tried to vary the in_size
and out_size until return values changed. When that failed I tried
replacing in_buffer and/or out_buffer with pointers near the end of a
fixed allocation, so that the next page would be no-access and return
STATUS_ACCESS_VIOLATION; this often worked, especially for pointers
embedded in structures.

After figuring out input and output sizes on both 32 and 64 bit I
usually tried to fill the buffers with various realistic values, e.g. 0,
1, \~0, a valid pointer, maybe some bitfields, essentially trying to get
the ioctl to return success (or STATUS_PENDING, or some other error code
that gives me a further hint as to what it actually does.) Sometimes
this worked; sometimes it didn't.

I tried this process usually on several different types of sockets—a
newly created TCP and UDP socket, a bound TCP and UDP socket, a
connected TCP socket, a listening TCP socket, and a newly opened handle
on the AFD device (which at that point \*presumably\* has no socket
type. I was never actually able to figure out how that was assigned.)
Different behaviour there was sometimes a clue, as in the RECVFROM ioctl
which only worked on bound UDP sockets.

I didn't try anything past that, or really any sort of automated
fuzzing.

## Ioctls

- **0x800, METHOD_NEITHER**: This is "bind". The input structure looks like

  ``` c
  struct
  {
      int unknown;
      struct sockaddr addr; /* variable size */
  };
  ```

  In practice I believe it only returns STATUS_INVALID_PARAMETER if the
  input size is \< 6 (i.e. it needs at least the sa_family member).

  This was actually usable in Wine. However, use of this ioctl didn't
  actually allow getsockname() to be subsequently used on the socket; it
  returned EINVAL. This suggests that ws2_32 is caching some data on the
  user side; since sockets can be cross-process it leads me to believe
  that ws2_32 is actually caching data in shared memory (I haven't done
  any tests to confirm this though.) Because we haven't learned anything
  since Windows 98 I guess.

- **0x801, METHOD_NEITHER**: This is "connect". The input structure looks
  like

  ``` c
  struct
  {
      intptr_t unk1;
      intptr_t unk2;
      SOCKET unk3;
      struct sockaddr addr; /* variable size */
  };
  ```
  and the output structure is

  ``` c
  struct
  {
      intptr_t unk1;
      intptr_t unk2;
  };
  ```

  unk3 is known to be a socket handle because it returns
  STATUS_INVALID_HANDLE/STATUS_OBJECT_TYPE_MISMATCH otherwise, but
  \*only\* for the uninitialized AFD socket handle. (Is this ioctl
  overloaded?)

  If unk2 is nonzero the ioctl returns STATUS_INVALID_PARAMETER. In this
  respect it's known to be pointer-size and not integer-size. unk1 might
  be an int with padding, though; changing it to different values had no
  effect. Same for the output parameters; note though that the output
  didn't break on alignment (STATUS_DATATYPE_MISALIGNMENT_ERROR) whereas
  most pointers for most ioctls do.

  I don't remember what's returned in output on a successful call though.
  It might be zeroes.

- **0x802, METHOD_NEITHER**: This is "listen". The input structure looks
  like

  ``` c
  struct
  {
      int unknown1;
      int backlog;
      int unknown2;
  };
  ```

  This was useful in Wine. The only awkward thing about it is that calling
  this ioctl followed by accept() causes the latter to return EINVAL. My
  guess is that accept() is trying to validate some user-side state.

- **0x803, METHOD_BUFFERED**: This is the first half of accept/WSAAccept,
  called on the listener. There is no input; the output structure looks
  like

  ``` c
  struct
  {
      unsigned int id;
      struct sockaddr addr; /* variable size */
  };
  ```

  "id" is a monotonically increasing number (per socket; it starts at 1)
  denoting the identity of an individual connection. This is later passed
  to the next ioctl, the second half of accept. addr is the remote addr.
  The ioctl pends until there is a connection available; it does \*not\*
  return the same connection again on the next call though. Can return
  STATUS_BUFFER_TOO_SMALL after STATUS_PENDING if the output buffer is too
  small. Returns the addr size as Information.

- **0x804, METHOD_BUFFERED**: Second half of accept/WSAAccept. No output;
  input structure looks like

  ``` c
  struct
  {
      int unknown;
      unsigned int id;
      SOCKET socket;
  };
  ```

  This ioctl is done on the listener. "socket" is a new socket to accept
  into (sort of like AcceptEx, but this ioctl pair doesn't seem versatile
  enough for AcceptEx.) "id" has to be a valid id (though I don't remember
  if it \*has\* to have been returned from the previous ioctl or if you
  can anticipate it.)

  The way this is done is weird. It looks like it's supposed to be for
  WSAAccept, but it doesn't return quality information (but maybe that was
  just a feature never implemented in WSAAccept?) It's also not
  immediately clear how to do CF_REJECT (IIRC the "unknown" parameter
  didn't really respond to different values.)

- **0x805, METHOD_NEITHER**: This is recv. Starcraft Remastered tried to use
  this, which made decoding easier than it would otherwise have been.
  The input parameters are

  ```c 
  struct afd_recv_params
  {
      const WSABUF *buffers;
      unsigned int count;
      int recv_flags;
      int msg_flags;
  };
  ```

  IIRC none of these parameters are written to (and in fact they can be
  cleared immediately after calling the ioctl) but the buffers are.

  This is mostly tested so I won't go into detail on it.

- **0x806, METHOD_NEITHER**: This is recvfrom. Input parameters look like

  ``` c
  struct
  {
      const WSABUF *buffers;
      unsigned int count;
      int recv_flags;
      int msg_flags;
      struct sockaddr *addr;
      int *addrlen;
  };
  ```

  (I think this is right, I've lost a couple of my notes but I don't think
  there are any parameters at the end.)

  Basically the same as RECV; the address is written to via those pointers
  (and not, of course, via the output buffer, that would be silly.) Only
  valid on a bound UDP socket.

- **0x807, METHOD_NEITHER**: This is send. Input parameters are basically
  the same as recv, though I think some of the msg flags are ignored
  (specifically it's not necessary to specify NOT_OOB).

- **0x808, METHOD_NEITHER**: This is sendto, I think. I didn't actually test
  this but it is also only valid on a bound UDP socket, and the
  placement among the ioctl numbers is pretty suggestive.

- **0x809, METHOD_BUFFERED**: This is poll. This was needed by multiple
  applications (because they wanted to do an async poll, I guess, and
  Windows doesn't really have a documented API corresponding to that).
  Also this version doesn't have the well-known WSAPoll bug where it
  won't report connection failure. (The WSAPoll bug was fixed on newer
  windows 10 but this ioctl works even on older windows.)

  Parameters are documented and tested in wine so I won't go into too much
  detail. I will mention that the unknown boolean is passed as 1 by
  starcraft. IIRC If you do that and set timeout to anything but LLONG_MAX
  it returns STATUS_INVALID_PARAMETER. This may be a way of explicitly
  marking infinite timeout (in my implementation I assume that LLONG_MAX
  is infinite, à la TIMEOUT_INFINITE, but that might not actually be true.

  Starcraft Remastered occasionally passes two flags that I couldn't
  figure out the identity of. Also, the WSAEnumNetworkEvents ioctl
  suggests that there are 13 flags (and we currently only know the purpose
  of 9.)

- **0x80a, METHOD_NEITHER**: Couldn't easily figure this one out. It takes
  16 bytes in, 0 out, returns success on the new UDP socket and the
  connected TCP socket but EINVAL otherwise.

- **0x80b, METHOD_NEITHER**: getsockname, documented and tested.

- **0x80c, METHOD_NEITHER**: This is sort of like FIONREAD + SIOCATMARK.
  Output is this:

  ``` c
  struct
  {
      unsigned int normal;
      unsigned int oob;
  };
  ```

  where "normal" is the number of unread normal bytes and "oob" is the
  number of unread oob bytes. This would arguably have been sort-of-useful
  for upstream Wine but we can't actually return the oob count, so I used
  separate ioctls instead.

- **0x80d, METHOD_NEITHER**: Unknown. Accepts an integer as input, and
  returns 2 pointer-sized things as output. The integer can be 1, 2, or
  3 or it returns STATUS_INVALID_PARAMETER (IIRC), the output is all ~0.
  The input values make me think of shutdown, but IIRC it doesn't
  actually act like shutdown (also, why the output?)

- **0x80e, METHOD_NEITHER**: Unknown. Accepts 16 bytes as input, 0 output.
  If the first integer is 1 or 2 it succeeds, otherwise fails. Only
  valid on a TCP socket but it doesn't seem to matter which.

- **0x80f, METHOD_NEITHER**: getpeername. Like getosckname, except (a) it
  doesn't work on the socket returned from accept(); (b) it doesn't
  return the address length \[in fact IIRC it returns garbage matching
  the next ioctl.\] This is another piece of evidence to support the
  "cached locally in shared memory" hypothesis.

- **0x810, METHOD_NEITHER**: This takes no input and returns a huge
  structure describing socket information. The output structure is:

  ```c
  struct afd_sock_info
  {
      int state_flags; // 0x1 == bound, 0x2 == connected
      int family;
      int type;
      int protocol;
      int min_addrlen; // or max_addrlen? or size of sockname/peername?
      int max_addrlen; // or min_addrlen? or size of peername/sockname?
      int unk6;
      int unk7;
      int unk8;
      int unk9; /* 0x2000... snd/rcvbuf? */
      int unk10; /* 0x2000... snd/rcvbuf? */
      int unk11; /* 0x1000 */
      int unk12; /* 1 */
      int catalog_id;
      int xp1_flags;
      int provider_flags; /* probably? always 8 */
      int unk16;
      int unk17;
      int unk18;
      int unk19;
      int unk20;
      int unk21;
      int unk22;
      int unk23;
      int unk24;
      int unk25;
      GUID provider_guid;
      int unk30; /* sizeof(void *) */
      int unk31; /* looks like random junk */
      /* these are variable sized */
      struct sockaddr sockname; /* except that s_addr is (sometimes) zero... */
      struct sockaddr peername;
      int family2; /* same as family... */
  };
  ```

  All of the other unk\* are zero. Possibly they represent different
  sockopts, but I tried setting a bunch of sockopts and they didn't seem
  to affect the output at all. I may not have actually tested
  sndbuf/rcvbuf.

- **0x811, METHOD_NEITHER**: Returns success even with no input/output.

- **0x812-0x815, METHOD_NEITHER**: Returns success even with no
  input/output, but only on TCP sockets (otherwise
  STATUS_INVALID_PARAMETER).

- **0x816-0x819, METHOD_NEITHER**: As 0x811.

- **0x81a-0x81d, METHOD_NEITHER**: As 0x812-0x815.

- **0x81e, METHOD_NEITHER**: 16 bytes in, 16 out, mystery which just returns
  STATUS_INVALID_PARAMETER.

- **0x81f, METHOD_NEITHER**: 46/64 bytes in. Possibly 0 out but I couldn't
  get this to return anything but STATUS_INVALID_PARAMETER.

- **0x820, METHOD_NEITHER**: 20 bytes in, 0 out, always
  STATUS_INVALID_PARAMETER. From its proximity to the next I'd almost
  think WSAAsyncSelect(), but I couldn't get it to work. It's honestly
  possible that WSAAsyncSelect is handled entirely on the user side with
  no kernel support.

- **0x821, METHOD_NEITHER**: This is WSAEventSelect(), used and tested in
  wine.

- **0x822, METHOD_NEITHER**: This is WSAEnumNetworkEvents(), used and tested
  in wine.

- **0x823, METHOD_BUFFERED**: Couldn't even figure out parameter sizes; all
  I get is STATUS_INVALID_PARAMETER.

- **0x824, METHOD_BUFFERED**

- **0x825, METHOD_BUFFERED**: 76/88 in (32/64-bit), 0 out, return
  STATUS_SUCCESS. Based on the below I think this is SIO_SET_QOS.

- **0x826, METHOD_BUFFERED**: 0 in, 76/88 out. The returned values look
  potentially like a QOS structure, so my guess is SIO_GET_QOS. I didn't
  verify this though.

- **0x827, METHOD_NEITHER**: Returns success, like 0x811.

- **0x828, METHOD_BUFFERED**: 16 bytes in, but always returns
  STATUS_INVALID_PARAMETER.

- **0x829, METHOD_NEITHER**: 12 bytes in. Only valid on listening socket (I
  think I know this because otherwise it won't even validate the input
  buffer length).

- **0x82a, METHOD_NEITHER**: 12 bytes in. If the first 4 bytes is 1 it
  returns STATUS_NOT_SUPPORTED, otherwise STATUS_INVALID_PARAMETER.

- **0x82b, METHOD_BUFFERED**: 24/32 bytes in (32/64-bit),
  STATUS_INVALID_PARAMETER.

- **0x82c, METHOD_NEITHER**: 2 bytes in, 4 bytes out, returns
  STATUS_SUCCESS. The output is always 0.

- **0x82d, METHOD_BUFFERED**: Same as 0x82b, except it returns
  STATUS_PENDING.

- **0x82e, METHOD_NEITHER**: This was about where I stopped bothering even
  trying to figure out ioctl parameters and decided just to use custom
  ioctls for most of ours. I have no information about this except it
  returns STATUS_INVALID_PARAMETER with 0 in/out size. This is true for
  all below except where noted.

- **0x82f, METHOD_NEITHER**: Returns STATUS_INVALID_PARAMETER on any socket
  returned from WSASocket(), but STATUS_INVALID_DEVICE_REQUEST when
  called with an uninitialized file on the AFD device.

- **0x830, METHOD_NEITHER**: 16/24 bytes in (32/64-bit), but returns
  STATUS_INVALID_CONNECTION if not called on a connected TCP socket.

- **0x831, METHOD_NEITHER**: 12 bytes in, returns STATUS_INVALID_ADDRESS. I
  think I tried addresses and none worked though.

- **0x832, METHOD_NEITHER**: Returns STATUS_ACCESS_VIOLATION.

- **0x833-0x837, METHOD_NEITHER**

- **0x838, METHOD_OUT_DIRECT**

- **0x839-0x83f, METHOD_NEITHER**

- **0x840-0x842, METHOD_NEITHER**: Returns STATUS_INVALID_HANDLE.

- **0x843, METHOD_BUFFERED**

- **0x844, METHOD_NEITHER**

- **0x845, METHOD_NEITHER**: Returns STATUS_SUCCESS.

Some number of the last few aren't available on older versions, but I
forget how many and how old.
