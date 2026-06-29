# What has changed?
We’ve changed the way RGB colors are blended by using a gamma of 1.0, i.e. linearly.

This means that there are some visual changes in how colors and brightness are blended together, and also how transparent sources now blend linearly with the background. This means that with lighter backgrounds, the background will contribute more to the resulting color.


Some background: https://www.youtube.com/watch?v=LKnqECcg6Gw

More background: https://blog.johnnovak.net/2016/09/21/what-every-coder-should-know-about-gamma/

# Why did we change this?
There have been fairly substantial changes in the graphics/color pipeline to support SRGB format textures and render targets, which naturally leads to blend operations occurring in linear space, so proper blending was an automatic by-product. Among the issues that this fixes are:

* Dark artifacts you would normally see where colors would meet: https://blog.johnnovak.net/2016/09/21/what-every-coder-should-know-about-gamma/#colour-blending

* Hue and brightness shifts when alpha blending: https://blog.johnnovak.net/2016/09/21/what-every-coder-should-know-about-gamma/#alpha-blending--compositing


# How do I deal with this?

You can hopefully configure your content creation software to behave like OBS does.
This should make it easier to author your assets with the same behavior as OBS 27, and make it more intuitive to achieve the look/style you want.

### Photoshop
You can press Ctrl+Shift+K, and enable "Blend RGB Colors Using Gamma": 1.0.

![photoshop](https://i.imgur.com/i47tM3V.png)

### After Effects
Go to "Project Settings" -> "Color Settings" tab and set "Blend Colors Using 1.0 Gamma"

![After Effects](https://i.imgur.com/MLPNy63.png)

### Adobe Premiere
Sequence > Sequence Settings. At the bottom check "Composite in Linear Color"

![AdobePremiere](https://i.imgur.com/w6aYt8w.png)

### GIMP
Image > Precision > Linear Light

![gimp](https://i.imgur.com/eP35v8R.png)

Other software may have a similar feature under a different name. Try searching for your software + "linear light", "gamma 1.0", "linear color" or similar.
***
If the exported images/videos have semi-transparency in them, you need to configure the image/media sources in OBS to use linear alpha. We don’t enable this by default for partial backwards compatibility with OBS 26. There is a new linear space checkbox in their source properties. Media Sources have the checkbox as of OBS Studio 27.0.1.

![obsCheckbox](https://i.imgur.com/ALC2H5l.png)

# Doing the math

Colors are often expressed as 8-bit sRGB gamma-encoded color channels between 0 and 255 inclusive.

### Example: Find the color linearly halfway between `[127, 127, 127]` and `[255, 255, 255]`.

Averaging the compressed values is not the right approach.

```
(127 + 255) / 2 = 191
[191, 191, 191]
```

Take the two values, and normalize them between `0` and `1`, `127/255 = 0.498` and `255/255 = 1.0`.

Decompress them to linear values. See https://en.wikipedia.org/wiki/SRGB for the functions.

```
0.498 > 0.04045
((0.498 + 0.055) / 1.055) ^ 2.4 = 0.212
1.0 > 0.04045
((1.0 + .055) / 1.055) ^ 2.4 = 1.0
```

So `0.212` and `1.0` are the linear values. Take the average `(0.212 + 1.0) / 2 = 0.606` and convert back to compressed.

```
0.606 > 0.0031308
(1.055 * (0.606 ^ (1 / 2.4))) - 0.055 = 0.801
```

Remapping back to `0 - 255`, `255 * 0.801 = 204`, so the halfway color is `[204, 204, 204]`.

### Example: Blend one-third linear white into `[0, 0, 0]` and `[127, 127, 127]`

You can't just divide `[255, 255, 255]` by 3 to get `[85, 85, 85]` and add them to the background colors. This would be the wrong approach:

```
[0, 0, 0] + [85, 85, 85] = [85, 85, 85]
[127, 127, 127] + [85, 85, 85] = [212, 212, 212]
```

We know the linear value of `1.0` is `1.0`, and `0.0` is `0.0`. Just add one-third white to black, `1/3 * 1.0 + 0.0 = 0.333`

```
0.333 > 0.0031308
(1.055 * (0.333 ^ (1 / 2.4))) - 0.055 = 0.613
0.613 * 255 = 156
```

So one-third white blended into `[0, 0, 0]` is `[156, 156, 156]`. You might be tempted to add `[156, 156, 156]` to `[127, 127, 127]` for the problem of blending one-third white into `[127, 127, 127]`, but then you get the invalid color of `[283, 283, 283]`. You need to add the contribution in linear space.

From the previous example, we know the linear value for `127/255` is `0.212`. Add `0.333` to that to get `0.546`, then recompress.

```
0.546 > 0.0031308
(1.055 * (0.546 ^ (1 / 2.4))) - 0.055 = 0.765
0.765 * 255 = 195
```

Adding one-third white to `[127, 127, 127]` is `[195, 195, 195]`.