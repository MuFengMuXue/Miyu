# Snap deltas

A snap delta contains only the differences between one revision of a snap and another. They're used to save bandwidth when downloading and uploading snap package updates to the [Snap Store](https://snapcraft.io/docs/reference/glossary/).

Snap deltas come in two forms, _download_ deltas and _upload_ deltas.

## Download deltas

Download deltas enable snap updates to be distributed in a bandwidth-efficient manner, with no extra effort from the developer.

Whenever a snap is released to a channel, the store automatically generates a binary delta between the previously released snap revision and the newly released snap revision.

Once the delta has been generated, clients with a sufficiently new snapd will download the delta file instead of the full snap file of the revision they're updating to. The downloaded delta will then be applied to the client's existing snap and all assertions about the snap are verified by snapd, which ensures that the client ends up with a snap that is bit-for-bit identical to the snap it would have downloaded without the delta.

If the delta is too close in size to a full-size snap, it is discarded and a full download is used instead.

Snap deltas are completely transparent to the developer and there is no way to disable them. If a delta update is available, the delta will be downloaded and applied.

Download deltas are enabled by default in _snapd 2.23+_.

## Upload deltas

Upload deltas effectively use the same mechanism as download deltas, with the main difference being that the delta is generated locally by Snapcraft when a developer initiates an upload for a new version of their snap. The delta contains only the differences between the most recently uploaded revision and the new local revision. Once uploaded, the Snap Store applies the delta to reconstruct the complete snap, verifying its integrity via its digital signature.

## Saving space with deltas

The space savings provided by deltas vary depending on the size of the snap, how often it gets updated, and how compressible the snap is (snaps that can be compressed into a small size will benefit less from deltas than snaps that are difficult to compress). In practice, the delta download size is around 30% of the full snap size.

The exact size of a delta can be determined with `snap refresh`.
