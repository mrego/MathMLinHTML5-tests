#!/usr/bin/python

from utils import mathfont
import fontforge

arrowCodePoint = 0x2192

v = 3 * mathfont.em
f = mathfont.create("stretchstack-bottomshiftdown%d" % v)
mathfont.createSquareGlyph(f, arrowCodePoint)
f.math.LowerLimitBaselineDropMin = 0
f.math.LowerLimitGapMin = 0
f.math.OverbarExtraAscender = 0
f.math.OverbarVerticalGap = 0
f.math.StretchStackBottomShiftDown = v
f.math.StretchStackGapAboveMin = 0
f.math.StretchStackGapBelowMin = 0
f.math.StretchStackTopShiftUp = 0
f.math.UnderbarExtraDescender = 0
f.math.UnderbarVerticalGap = 0
f.math.UpperLimitBaselineRiseMin = 0
f.math.UpperLimitGapMin = 0
mathfont.save(f)

v = 11 * mathfont.em
f = mathfont.create("stretchstack-gapbelowmin%d" % v)
mathfont.createSquareGlyph(f, arrowCodePoint)
f.math.LowerLimitBaselineDropMin = 0
f.math.LowerLimitGapMin = 0
f.math.OverbarExtraAscender = 0
f.math.OverbarVerticalGap = 0
f.math.StretchStackBottomShiftDown = 0
f.math.StretchStackGapAboveMin = 0
f.math.StretchStackGapBelowMin = v
f.math.StretchStackTopShiftUp = 0
f.math.UnderbarExtraDescender = 0
f.math.UnderbarVerticalGap = 0
f.math.UpperLimitBaselineRiseMin = 0
f.math.UpperLimitGapMin = 0
mathfont.save(f)

v = 5 * mathfont.em
f = mathfont.create("stretchstack-topshiftup%d" % v)
mathfont.createSquareGlyph(f, arrowCodePoint)
f.math.LowerLimitBaselineDropMin = 0
f.math.LowerLimitGapMin = 0
f.math.OverbarExtraAscender = 0
f.math.OverbarVerticalGap = 0
f.math.StretchStackBottomShiftDown = 0
f.math.StretchStackGapAboveMin = 0
f.math.StretchStackGapBelowMin = 0
f.math.StretchStackTopShiftUp = v
f.math.UnderbarExtraDescender = 0
f.math.UnderbarVerticalGap = 0
f.math.UpperLimitBaselineRiseMin = 0
f.math.UpperLimitGapMin = 0
mathfont.save(f)

v = 7 * mathfont.em
f = mathfont.create("stretchstack-gapabovemin%d" % v)
mathfont.createSquareGlyph(f, arrowCodePoint)
f.math.LowerLimitBaselineDropMin = 0
f.math.LowerLimitGapMin = 0
f.math.OverbarExtraAscender = 0
f.math.OverbarVerticalGap = 0
f.math.StretchStackBottomShiftDown = 0
f.math.StretchStackGapAboveMin = v
f.math.StretchStackGapBelowMin = 0
f.math.StretchStackTopShiftUp = 0
f.math.UnderbarExtraDescender = 0
f.math.UnderbarVerticalGap = 0
f.math.UpperLimitBaselineRiseMin = 0
f.math.UpperLimitGapMin = 0
mathfont.save(f)