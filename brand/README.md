# Brand assets

`ministry-of-data-emblem.png` is the master artwork: a globe on a column inside a laurel
wreath of circuit traces, star above, with MINISTRY OF DATA set beneath — near-black on
transparency at 1024×1536, portrait.

It replaced an earlier royal-arms lockup that was too UK-centric. Both were single-ink
silhouettes, which is what lets the site draw them as a CSS mask filled with the current
ink: the source colour is irrelevant, so the mark renders navy in light mode and warm
off-white in dark from one file. Everything in `static/logo/` is derived from it:

    crest.png            emblem only, no wordmark — masthead and footer mask
    lockup@2x.png        the full portrait lockup — hero mask
    static/favicon.png   arms, squared and padded

The two logo files are used as CSS `mask-image` and filled with the current ink, so one
asset serves both light and dark. Sizes are chosen for the largest place each is drawn:
the emblem never exceeds ~90px, the lockup reaches 300px tall in the hero.

To regenerate after editing the master:

    convert brand/ministry-of-data-emblem.png -trim +repage /tmp/trim.png
    convert /tmp/trim.png -crop 1006x1000+0+0 +repage -trim +repage /tmp/emblem.png
    convert /tmp/emblem.png -resize 320x -strip -colors 32 static/logo/crest.png
    convert /tmp/trim.png   -resize 700x -strip -colors 32 static/logo/lockup@2x.png
    convert /tmp/emblem.png -resize 112x -background none -gravity center \
            -extent 128x128 -strip -colors 24 static/favicon.png

The crop height (1000) is the blank gutter between the emblem and the wordmark; re-find it
if the artwork changes.
