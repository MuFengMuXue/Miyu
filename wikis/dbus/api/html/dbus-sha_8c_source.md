dbus-sha.c

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-sha.c SHA-1 implementation

3 \*

4 \* Copyright (C) 2003 Red Hat Inc.

5 \* Copyright (C) 1995 A. M. Kuchling

6 \* SPDX-License-Identifier: (AFL-2.1 OR GPL-2.0-or-later) AND LicenseRef-pycrypto-orig

7 \*

8 \* Licensed under the Academic Free License version 2.1

9 \*

10 \* This program is free software; you can redistribute it and/or modify

11 \* it under the terms of the GNU General Public License as published by

12 \* the Free Software Foundation; either version 2 of the License, or

13 \* (at your option) any later version.

14 \*

15 \* This program is distributed in the hope that it will be useful,

16 \* but WITHOUT ANY WARRANTY; without even the implied warranty of

17 \* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the

18 \* GNU General Public License for more details.

19 \*

20 \* You should have received a copy of the GNU General Public License

21 \* along with this program; if not, write to the Free Software

22 \* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

23 \*

24 \*/

25

26\#include \<config.h\>

27\#include "dbus-internals.h"

28\#include "dbus-sha.h"

29\#include "dbus-marshal-basic.h" /\* for byteswap routines \*/

30\#include \<string.h\>

31

32/\* The following comments have the history of where this code

33 \* comes from. I actually copied it from GNet in GNOME CVS.

34 \* - hp@redhat.com

35 \*/

36

37/\*

38 \* sha.h : Implementation of the Secure Hash Algorithm

39 \*

40 \* Part of the Python Cryptography Toolkit, version 1.0.0

41 \*

42 \* Copyright (C) 1995, A.M. Kuchling

43 \*

44 \* Distribute and use freely; there are no restrictions on further

45 \* dissemination and usage except those imposed by the laws of your

46 \* country of residence.

47 \*

48 \*/

49

50/\* SHA: NIST's Secure Hash Algorithm \*/

51

52/\* Based on SHA code originally posted to sci.crypt by Peter Gutmann

53 in message \<30ajo5\$oe8@ccu2.auckland.ac.nz\>.

54 Modified to test for endianness on creation of SHA objects by AMK.

55 Also, the original specification of SHA was found to have a weakness

56 by NSA/NIST. This code implements the fixed version of SHA.

57\*/

58

59/\* Here's the first paragraph of Peter Gutmann's posting:

60

61The following is my SHA (FIPS 180) code updated to allow use of the "fixed"

62SHA, thanks to Jim Gillogly and an anonymous contributor for the information on

63what's changed in the new version. The fix is a simple change which involves

64adding a single rotate in the initial expansion function. It is unknown

65whether this is an optimal solution to the problem which was discovered in the

66SHA or whether it's simply a bandaid which fixes the problem with a minimum of

67effort (for example the reengineering of a great many Capstone chips).

68\*/

69

89\#ifndef DOXYGEN_SHOULD_SKIP_THIS

90

91/\* The SHA block size and message digest sizes, in bytes \*/

92

93\#define SHA_DATASIZE 64

94\#define SHA_DIGESTSIZE 20

95

96/\* The SHA f()-functions. The f1 and f3 functions can be optimized to

97 save one boolean operation each - thanks to Rich Schroeppel,

98 rcs@cs.arizona.edu for discovering this \*/

99

100/\*#define f1(x,y,z) ( ( x & y ) \| ( ~x & z ) ) // Rounds 0-19 \*/

101\#define f1(x,y,z) ( z ^ ( x & ( y ^ z ) ) ) /\* Rounds 0-19 \*/

102\#define f2(x,y,z) ( x ^ y ^ z ) /\* Rounds 20-39 \*/

103/\*#define f3(x,y,z) ( ( x & y ) \| ( x & z ) \| ( y & z ) ) // Rounds 40-59 \*/

104\#define f3(x,y,z) ( ( x & y ) \| ( z & ( x \| y ) ) ) /\* Rounds 40-59 \*/

105\#define f4(x,y,z) ( x ^ y ^ z ) /\* Rounds 60-79 \*/

106

107/\* The SHA Mysterious Constants \*/

108

109\#define K1 0x5A827999L /\* Rounds 0-19 \*/

110\#define K2 0x6ED9EBA1L /\* Rounds 20-39 \*/

111\#define K3 0x8F1BBCDCL /\* Rounds 40-59 \*/

112\#define K4 0xCA62C1D6L /\* Rounds 60-79 \*/

113

114/\* SHA initial values \*/

115

116\#define h0init 0x67452301L

117\#define h1init 0xEFCDAB89L

118\#define h2init 0x98BADCFEL

119\#define h3init 0x10325476L

120\#define h4init 0xC3D2E1F0L

121

122/\* Note that it may be necessary to add parentheses to these macros if they

123 are to be called with expressions as arguments \*/

124/\* 32-bit rotate left - kludged with shifts \*/

125

126\#define ROTL(n,X) ( ( ( X ) \<\< n ) \| ( ( X ) \>\> ( 32 - n ) ) )

127

128/\* The initial expanding function. The hash function is defined over an

129 80-word expanded input array W, where the first 16 are copies of the input

130 data, and the remaining 64 are defined by

131

132 W\[ i \] = W\[ i - 16 \] ^ W\[ i - 14 \] ^ W\[ i - 8 \] ^ W\[ i - 3 \]

133

134 This implementation generates these values on the fly in a circular

135 buffer - thanks to Colin Plumb, colin@nyx10.cs.du.edu for this

136 optimization.

137

138 The updated SHA changes the expanding function by adding a rotate of 1

139 bit. Thanks to Jim Gillogly, jim@rand.org, and an anonymous contributor

140 for this information \*/

141

142\#define expand(W,i) ( W\[ i & 15 \] = ROTL( 1, ( W\[ i & 15 \] ^ W\[ (i - 14) & 15 \] ^ \\

143 W\[ (i - 8) & 15 \] ^ W\[ (i - 3) & 15 \] ) ) )

144

145

146/\* The prototype SHA sub-round. The fundamental sub-round is:

147

148 a' = e + ROTL( 5, a ) + f( b, c, d ) + k + data;

149 b' = a;

150 c' = ROTL( 30, b );

151 d' = c;

152 e' = d;

153

154 but this is implemented by unrolling the loop 5 times and renaming the

155 variables ( e, a, b, c, d ) = ( a', b', c', d', e' ) each iteration.

156 This code is then replicated 20 times for each of the 4 functions, using

157 the next 20 values from the W\[\] array each time \*/

158

159\#define subRound(a, b, c, d, e, f, k, data) \\

160 ( e += ROTL( 5, a ) + f( b, c, d ) + k + data, b = ROTL( 30, b ) )

161

162\#endif /\* !DOXYGEN_SHOULD_SKIP_THIS \*/

163

164/\* Perform the SHA transformation. Note that this code, like MD5, seems to

165 break some optimizing compilers due to the complexity of the expressions

166 and the size of the basic block. It may be necessary to split it into

167 sections, e.g. based on the four subrounds

168

169 Note that this corrupts the context-\>data area \*/

170

171static void

172SHATransform(dbus_uint32_t \*digest, dbus_uint32_t \*data)

173{

174 dbus_uint32_t A, B, C, D, E; /\* Local vars \*/

175 dbus_uint32_t eData\[16\]; /\* Expanded data \*/

176

177 /\* Set up first buffer and local data buffer \*/

178 A = digest\[0\];

179 B = digest\[1\];

180 C = digest\[2\];

181 D = digest\[3\];

182 E = digest\[4\];

183 memmove (eData, data, SHA_DATASIZE);

184

185 /\* Heavy mangling, in 4 sub-rounds of 20 interations each. \*/

186 subRound (A, B, C, D, E, f1, K1, eData\[0\]);

187 subRound (E, A, B, C, D, f1, K1, eData\[1\]);

188 subRound (D, E, A, B, C, f1, K1, eData\[2\]);

189 subRound (C, D, E, A, B, f1, K1, eData\[3\]);

190 subRound (B, C, D, E, A, f1, K1, eData\[4\]);

191 subRound (A, B, C, D, E, f1, K1, eData\[5\]);

192 subRound (E, A, B, C, D, f1, K1, eData\[6\]);

193 subRound (D, E, A, B, C, f1, K1, eData\[7\]);

194 subRound (C, D, E, A, B, f1, K1, eData\[8\]);

195 subRound (B, C, D, E, A, f1, K1, eData\[9\]);

196 subRound (A, B, C, D, E, f1, K1, eData\[10\]);

197 subRound (E, A, B, C, D, f1, K1, eData\[11\]);

198 subRound (D, E, A, B, C, f1, K1, eData\[12\]);

199 subRound (C, D, E, A, B, f1, K1, eData\[13\]);

200 subRound (B, C, D, E, A, f1, K1, eData\[14\]);

201 subRound (A, B, C, D, E, f1, K1, eData\[15\]);

202 subRound (E, A, B, C, D, f1, K1, expand ( eData, 16) );

203 subRound (D, E, A, B, C, f1, K1, expand ( eData, 17) );

204 subRound (C, D, E, A, B, f1, K1, expand ( eData, 18) );

205 subRound (B, C, D, E, A, f1, K1, expand ( eData, 19) );

206

207 subRound (A, B, C, D, E, f2, K2, expand ( eData, 20) );

208 subRound (E, A, B, C, D, f2, K2, expand ( eData, 21) );

209 subRound (D, E, A, B, C, f2, K2, expand ( eData, 22) );

210 subRound (C, D, E, A, B, f2, K2, expand ( eData, 23) );

211 subRound (B, C, D, E, A, f2, K2, expand ( eData, 24) );

212 subRound (A, B, C, D, E, f2, K2, expand ( eData, 25) );

213 subRound (E, A, B, C, D, f2, K2, expand ( eData, 26) );

214 subRound (D, E, A, B, C, f2, K2, expand ( eData, 27) );

215 subRound (C, D, E, A, B, f2, K2, expand ( eData, 28) );

216 subRound (B, C, D, E, A, f2, K2, expand ( eData, 29) );

217 subRound (A, B, C, D, E, f2, K2, expand ( eData, 30) );

218 subRound (E, A, B, C, D, f2, K2, expand ( eData, 31) );

219 subRound (D, E, A, B, C, f2, K2, expand ( eData, 32) );

220 subRound (C, D, E, A, B, f2, K2, expand ( eData, 33) );

221 subRound (B, C, D, E, A, f2, K2, expand ( eData, 34) );

222 subRound (A, B, C, D, E, f2, K2, expand ( eData, 35) );

223 subRound (E, A, B, C, D, f2, K2, expand ( eData, 36) );

224 subRound (D, E, A, B, C, f2, K2, expand ( eData, 37) );

225 subRound (C, D, E, A, B, f2, K2, expand ( eData, 38) );

226 subRound (B, C, D, E, A, f2, K2, expand ( eData, 39) );

227

228 subRound (A, B, C, D, E, f3, K3, expand ( eData, 40) );

229 subRound (E, A, B, C, D, f3, K3, expand ( eData, 41) );

230 subRound (D, E, A, B, C, f3, K3, expand ( eData, 42) );

231 subRound (C, D, E, A, B, f3, K3, expand ( eData, 43) );

232 subRound (B, C, D, E, A, f3, K3, expand ( eData, 44) );

233 subRound (A, B, C, D, E, f3, K3, expand ( eData, 45) );

234 subRound (E, A, B, C, D, f3, K3, expand ( eData, 46) );

235 subRound (D, E, A, B, C, f3, K3, expand ( eData, 47) );

236 subRound (C, D, E, A, B, f3, K3, expand ( eData, 48) );

237 subRound (B, C, D, E, A, f3, K3, expand ( eData, 49) );

238 subRound (A, B, C, D, E, f3, K3, expand ( eData, 50) );

239 subRound (E, A, B, C, D, f3, K3, expand ( eData, 51) );

240 subRound (D, E, A, B, C, f3, K3, expand ( eData, 52) );

241 subRound (C, D, E, A, B, f3, K3, expand ( eData, 53) );

242 subRound (B, C, D, E, A, f3, K3, expand ( eData, 54) );

243 subRound (A, B, C, D, E, f3, K3, expand ( eData, 55) );

244 subRound (E, A, B, C, D, f3, K3, expand ( eData, 56) );

245 subRound (D, E, A, B, C, f3, K3, expand ( eData, 57) );

246 subRound (C, D, E, A, B, f3, K3, expand ( eData, 58) );

247 subRound (B, C, D, E, A, f3, K3, expand ( eData, 59) );

248

249 subRound (A, B, C, D, E, f4, K4, expand ( eData, 60) );

250 subRound (E, A, B, C, D, f4, K4, expand ( eData, 61) );

251 subRound (D, E, A, B, C, f4, K4, expand ( eData, 62) );

252 subRound (C, D, E, A, B, f4, K4, expand ( eData, 63) );

253 subRound (B, C, D, E, A, f4, K4, expand ( eData, 64) );

254 subRound (A, B, C, D, E, f4, K4, expand ( eData, 65) );

255 subRound (E, A, B, C, D, f4, K4, expand ( eData, 66) );

256 subRound (D, E, A, B, C, f4, K4, expand ( eData, 67) );

257 subRound (C, D, E, A, B, f4, K4, expand ( eData, 68) );

258 subRound (B, C, D, E, A, f4, K4, expand ( eData, 69) );

259 subRound (A, B, C, D, E, f4, K4, expand ( eData, 70) );

260 subRound (E, A, B, C, D, f4, K4, expand ( eData, 71) );

261 subRound (D, E, A, B, C, f4, K4, expand ( eData, 72) );

262 subRound (C, D, E, A, B, f4, K4, expand ( eData, 73) );

263 subRound (B, C, D, E, A, f4, K4, expand ( eData, 74) );

264 subRound (A, B, C, D, E, f4, K4, expand ( eData, 75) );

265 subRound (E, A, B, C, D, f4, K4, expand ( eData, 76) );

266 subRound (D, E, A, B, C, f4, K4, expand ( eData, 77) );

267 subRound (C, D, E, A, B, f4, K4, expand ( eData, 78) );

268 subRound (B, C, D, E, A, f4, K4, expand ( eData, 79) );

269

270 /\* Build message digest \*/

271 digest\[0\] += A;

272 digest\[1\] += B;

273 digest\[2\] += C;

274 digest\[3\] += D;

275 digest\[4\] += E;

276}

277

278/\* When run on a little-endian CPU we need to perform byte reversal on an

279 array of longwords. \*/

280

281\#ifdef WORDS_BIGENDIAN

282\#define swap_words(buffer, byte_count)

283\#else

284static void

285swap_words (dbus_uint32_t \*buffer,

286 int byte_count)

287{

288 byte_count /= sizeof (dbus_uint32_t);

289 while (byte_count--)

290 {

291 \*buffer = DBUS_UINT32_SWAP_LE_BE (\*buffer);

292 ++buffer;

293 }

294}

295\#endif

296

297static void

298sha_init (DBusSHAContext \*context)

299{

300 /\* Set the h-vars to their initial values \*/

301 context-\>digest\[0\] = h0init;

302 context-\>digest\[1\] = h1init;

303 context-\>digest\[2\] = h2init;

304 context-\>digest\[3\] = h3init;

305 context-\>digest\[4\] = h4init;

306

307 /\* Initialise bit count \*/

308 context-\>count_lo = context-\>count_hi = 0;

309}

310

311static void

312sha_append (DBusSHAContext \*context,

313 const unsigned char \*buffer,

314 unsigned int count)

315{

316 dbus_uint32_t tmp;

317 unsigned int dataCount;

318

319 /\* Update bitcount \*/

320 tmp = context-\>count_lo;

321 if (( context-\>count_lo = tmp + ( ( dbus_uint32_t) count \<\< 3) ) \< tmp)

322 context-\>count_hi++; /\* Carry from low to high \*/

323 context-\>count_hi += count \>\> 29;

324

325 /\* Get count of bytes already in data \*/

326 dataCount = (int) (tmp \>\> 3) & 0x3F;

327

328 /\* Handle any leading odd-sized chunks \*/

329 if (dataCount)

330 {

331 unsigned char \*p = (unsigned char \*) context-\>data + dataCount;

332

333 dataCount = SHA_DATASIZE - dataCount;

334 if (count \< dataCount)

335 {

336 memmove (p, buffer, count);

337 return;

338 }

339 memmove (p, buffer, dataCount);

340 swap_words (context-\>data, SHA_DATASIZE);

341 SHATransform (context-\>digest, context-\>data);

342 buffer += dataCount;

343 count -= dataCount;

344 }

345

346 /\* Process data in SHA_DATASIZE chunks \*/

347 while (count \>= SHA_DATASIZE)

348 {

349 memmove (context-\>data, buffer, SHA_DATASIZE);

350 swap_words (context-\>data, SHA_DATASIZE);

351 SHATransform (context-\>digest, context-\>data);

352 buffer += SHA_DATASIZE;

353 count -= SHA_DATASIZE;

354 }

355

356 /\* Handle any remaining bytes of data. \*/

357 memmove (context-\>data, buffer, count);

358}

359

360

361/\* Final wrapup - pad to SHA_DATASIZE-byte boundary with the bit pattern

362 1 0\* (64-bit count of bits processed, MSB-first) \*/

363

364static void

365sha_finish (DBusSHAContext \*context, unsigned char digest\[20\])

366{

367 int count;

368 unsigned char \*data_p;

369

370 /\* Compute number of bytes mod 64 \*/

371 count = (int) context-\>count_lo;

372 count = (count \>\> 3) & 0x3F;

373

374 /\* Set the first char of padding to 0x80. This is safe since there is

375 always at least one byte free \*/

376 data_p = (unsigned char \*) context-\>data + count;

377 \*data_p++ = 0x80;

378

379 /\* Bytes of padding needed to make 64 bytes \*/

380 count = SHA_DATASIZE - 1 - count;

381

382 /\* Pad out to 56 mod 64 \*/

383 if (count \< 8)

384 {

385 /\* Two lots of padding: Pad the first block to 64 bytes \*/

386 memset (data_p, 0, count);

387 swap_words (context-\>data, SHA_DATASIZE);

388 SHATransform (context-\>digest, context-\>data);

389

390 /\* Now fill the next block with 56 bytes \*/

391 memset (context-\>data, 0, SHA_DATASIZE - 8);

392 }

393 else

394 /\* Pad block to 56 bytes \*/

395 memset (data_p, 0, count - 8);

396

397 /\* Append length in bits and transform \*/

398 context-\>data\[14\] = context-\>count_hi;

399 context-\>data\[15\] = context-\>count_lo;

400

401 swap_words (context-\>data, SHA_DATASIZE - 8);

402 SHATransform (context-\>digest, context-\>data);

403 swap_words (context-\>digest, SHA_DIGESTSIZE);

404 memmove (digest, context-\>digest, SHA_DIGESTSIZE);

405}

406

/\* End of internals \*/

408

420void

421\_dbus_sha_init (DBusSHAContext \*context)

422{

423 sha_init (context);

424}

425

432void

433\_dbus_sha_update (DBusSHAContext \*context,

434 const DBusString \*data)

435{

436 unsigned int inputLen;

437 const unsigned char \*input;

438

439 input = (const unsigned char\*) \_dbus_string_get_const_data (data);

440 inputLen = \_dbus_string_get_length (data);

441

442 sha_append (context, input, inputLen);

443}

444

456dbus_bool_t

457\_dbus_sha_final (DBusSHAContext \*context,

458 DBusString \*results)

459{

460 unsigned char digest\[20\];

461

462 sha_finish (context, digest);

463

464 if (!\_dbus_string_append_len (results, (const char \*) digest, 20))

465 return FALSE;

466

467 /\* some kind of security paranoia, though it seems pointless

468 \* to me given the nonzeroed stuff flying around

469 \*/

470 \_DBUS_ZERO(\*context);

471

472 return TRUE;

473}

474

483dbus_bool_t

484\_dbus_sha_compute (const DBusString \*data,

485 DBusString \*ascii_output)

486{

487 DBusSHAContext context;

488 DBusString digest;

489

490 \_dbus_sha_init (&context);

491

492 \_dbus_sha_update (&context, data);

493

494 if (!\_dbus_string_init (&digest))

495 return FALSE;

496

497 if (!\_dbus_sha_final (&context, &digest))

498 goto error;

499

500 if (!\_dbus_string_hex_encode (&digest, 0, ascii_output,

501 \_dbus_string_get_length (ascii_output)))

502 goto error;

503

504 \_dbus_string_free (&digest);

505

506 return TRUE;

507

508 error:

509 \_dbus_string_free (&digest);

510 return FALSE;

511}

512

/\* end of exported functions \*/

\_DBUS_ZERO

\#define \_DBUS_ZERO(object)

Sets all bits in an object to zero.

**Definition** dbus-internals.h:194

TRUE

\#define TRUE

Expands to "1".

**Definition** dbus-macros.h:41

FALSE

\#define FALSE

Expands to "0".

**Definition** dbus-macros.h:44

\_dbus_sha_compute

dbus_bool_t \_dbus_sha_compute(const DBusString \*data, DBusString \*ascii_output)

Computes the ASCII hex-encoded shasum of the given data and appends it to the output string.

**Definition** dbus-sha.c:484

\_dbus_sha_init

void \_dbus_sha_init(DBusSHAContext \*context)

Initializes the SHA context.

**Definition** dbus-sha.c:421

\_dbus_sha_update

void \_dbus_sha_update(DBusSHAContext \*context, const DBusString \*data)

Feeds more data into an existing shasum computation.

**Definition** dbus-sha.c:433

\_dbus_sha_final

dbus_bool_t \_dbus_sha_final(DBusSHAContext \*context, DBusString \*results)

SHA finalization.

**Definition** dbus-sha.c:457

\_dbus_string_init

dbus_bool_t \_dbus_string_init(DBusString \*str)

Initializes a string.

**Definition** dbus-string.c:182

\_dbus_string_append_len

dbus_bool_t \_dbus_string_append_len(DBusString \*str, const char \*buffer, int len)

Appends block of bytes with the given length to a DBusString.

**Definition** dbus-string.c:1170

\_dbus_string_free

void \_dbus_string_free(DBusString \*str)

Frees a string created by \_dbus_string_init(), and fills it with the same contents as \_DBUS_STRING_IN...

**Definition** dbus-string.c:278

\_dbus_string_get_length

int \_dbus_string_get_length(const DBusString \*str)

Gets the length of a string (not including nul termination).

**Definition** dbus-string.c:784

\_dbus_string_hex_encode

dbus_bool_t \_dbus_string_hex_encode(const DBusString \*source, int start, DBusString \*dest, int insert_at)

Encodes a string in hex, the way MD5 and SHA-1 are usually encoded.

**Definition** dbus-string.c:2382

\_dbus_string_get_const_data

const char \* \_dbus_string_get_const_data(const DBusString \*str)

Gets the raw character buffer from a const string.

**Definition** dbus-string.c:513

DBusSHAContext

Struct storing state of the SHA algorithm.

**Definition** dbus-sha.h:40

DBusSHAContext::digest

dbus_uint32_t digest\[5\]

Message digest.

**Definition** dbus-sha.h:41

DBusSHAContext::data

dbus_uint32_t data\[16\]

SHA data buffer.

**Definition** dbus-sha.h:44

DBusSHAContext::count_lo

dbus_uint32_t count_lo

64-bit bit count

**Definition** dbus-sha.h:42

DBusSHAContext::count_hi

dbus_uint32_t count_hi

No clue.

**Definition** dbus-sha.h:43

DBusString

**Definition** dbus-string.h:47
