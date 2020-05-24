Fred's ImageMagick Scripts: DICE

# Fred's ImageMagick Scripts

## DICE

[Download Script](http://www.fmwconcepts.com/imagemagick/downloadcounter.php?scriptname=dice&dirname=dice)

last modified: September 26, 2017

USAGE: dice [-s size] [-p percent] [-c center] [-r radii] [-R rounding] [-n] [-e ecolor] infile [maskfile] outfile

USAGE: dice [h|-help]
-s ... size ....... size of square patches; integer>0; default=16
-p ... percent .... percentage of patches to randomly process;
................... 0<=integer<=100; default=100 (all patches)
-c ... center ..... x and y center coordinates of the round rectangle mask
................... with white on the inside and black on the outside; comma
................... separate pair of integers>=0; default=center of image
-r ... radii ...... x and y radii of a round rectangle mask; comma
................... separated pair of integers>=0; default="0,0" (no mask)
-R ... rounding ... round rectangle corner radii expressed as pair of
................... comma separated integers>=0; default="0,0"
-n ................ negate mask (invert black and white); note only the
................... black area will be diced
-e ... ecolor ..... edge color of mask boundary to show on the resulting
................... image; any valid opaque IM color; default=do not
................... show edge of mask

maskfile is an optional binary (b/w) mask image the same size as the infile
PURPOSE: To randomly rotate each successive square-sized patch in the image.

DESCRIPTION: DICE rotates each successive non-overlapping square-sized patch in the image by a random choice of 0, 90, 180 and 270 degrees. An optional round rectangle mask may be defined to delineate where the dicing will be shown. Or an external mask image may be provided.

ARGUMENTS:

-s size ... SIZE of the square-sized patches to randomize; Values are integers>1. The default=16.

-p percent ... PERCENT is the percentage of patches to randomly process. Values are 0<=integers<=100. The default=100 (all patches).

-c center ... CENTER is the x and y center coordinates of the round rectangle mask with white on the inside and black on the outside; comma separate pair of integers>=0; default=center of image

-r radii ... RADII are the x and y radii of a round rectangle mask expressed as a comma separated pair of integers>=0. The default="0,0" (no mask).

-R rounding ... ROUNDING is the round rectangle corner radii expressed as a pair of comma separated values. Values are integers>=0. The default="0,0".

-n negate ... NEGATE the mask (invert black and white).

-e ecolor ... ECOLOR is the edge color of the mask boundary to show on the resulting image. Any valid opaque IM color is allowed. The default is not to show the edge boundary on the image.

NOTE: The script runs slowly. A 256x256 sized image processed on my INTEL Mac Mini in about 15 sec for dimension 16 and about 3 sec for dimension 32. Thus larger sized patches will process faster.

CAVEAT: No guarantee that this script will work on all platforms, nor that trapping of inconsistent parameters is complete and foolproof. Use At Your Own Risk.