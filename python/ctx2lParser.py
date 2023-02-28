# Generated from ./ctx2lParser.g4 by ANTLR 4.12.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


from RuleContextWithAltNum import RuleContextWithAltNum

def serializedATN():
    return [
        4,1,62,778,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,59,
        7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,65,7,65,
        2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,71,2,72,
        7,72,2,73,7,73,2,74,7,74,2,75,7,75,2,76,7,76,2,77,7,77,2,78,7,78,
        2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,2,83,7,83,1,0,1,0,4,0,171,
        8,0,11,0,12,0,172,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,
        2,1,3,1,3,3,3,189,8,3,1,3,1,3,1,3,1,4,1,4,3,4,196,8,4,1,4,1,4,1,
        4,1,5,1,5,1,5,5,5,204,8,5,10,5,12,5,207,9,5,1,6,1,6,1,6,5,6,212,
        8,6,10,6,12,6,215,9,6,1,7,4,7,218,8,7,11,7,12,7,219,1,7,1,7,3,7,
        224,8,7,1,8,4,8,227,8,8,11,8,12,8,228,1,9,1,9,3,9,233,8,9,1,10,1,
        10,1,10,3,10,238,8,10,1,11,1,11,1,12,1,12,1,13,1,13,3,13,246,8,13,
        1,14,1,14,3,14,250,8,14,1,14,1,14,1,15,1,15,1,15,5,15,257,8,15,10,
        15,12,15,260,9,15,1,15,3,15,263,8,15,1,16,1,16,3,16,267,8,16,1,17,
        1,17,1,17,3,17,272,8,17,1,18,1,18,1,19,1,19,1,20,1,20,5,20,280,8,
        20,10,20,12,20,283,9,20,1,20,1,20,5,20,287,8,20,10,20,12,20,290,
        9,20,1,20,1,20,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,3,22,
        303,8,22,1,23,1,23,1,23,1,23,1,23,3,23,310,8,23,1,24,1,24,1,24,1,
        24,5,24,316,8,24,10,24,12,24,319,9,24,1,24,1,24,1,25,1,25,1,25,1,
        25,1,26,1,26,1,26,5,26,330,8,26,10,26,12,26,333,9,26,1,26,1,26,1,
        26,3,26,338,8,26,1,27,1,27,1,27,1,27,5,27,344,8,27,10,27,12,27,347,
        9,27,1,27,1,27,1,28,1,28,1,28,1,28,1,28,3,28,356,8,28,1,29,1,29,
        3,29,360,8,29,1,29,1,29,1,30,1,30,3,30,366,8,30,1,30,1,30,1,31,1,
        31,1,31,5,31,373,8,31,10,31,12,31,376,9,31,1,31,3,31,379,8,31,1,
        32,1,32,1,32,1,32,3,32,385,8,32,1,32,1,32,1,32,1,33,1,33,1,33,3,
        33,393,8,33,1,34,1,34,5,34,397,8,34,10,34,12,34,400,9,34,1,34,1,
        34,1,35,1,35,5,35,406,8,35,10,35,12,35,409,9,35,1,35,1,35,1,36,1,
        36,1,36,1,36,5,36,417,8,36,10,36,12,36,420,9,36,1,37,5,37,423,8,
        37,10,37,12,37,426,9,37,1,38,1,38,3,38,430,8,38,1,39,3,39,433,8,
        39,1,39,1,39,3,39,437,8,39,1,39,3,39,440,8,39,1,39,3,39,443,8,39,
        1,39,3,39,446,8,39,1,39,5,39,449,8,39,10,39,12,39,452,9,39,1,39,
        1,39,1,39,1,39,1,39,1,40,5,40,460,8,40,10,40,12,40,463,9,40,1,40,
        3,40,466,8,40,1,41,1,41,1,41,1,41,1,42,1,42,1,42,1,43,1,43,3,43,
        477,8,43,1,44,1,44,1,44,1,45,1,45,1,45,1,45,5,45,486,8,45,10,45,
        12,45,489,9,45,1,46,1,46,1,46,1,47,1,47,1,47,1,47,1,48,4,48,499,
        8,48,11,48,12,48,500,1,49,1,49,1,50,1,50,1,51,1,51,1,51,5,51,510,
        8,51,10,51,12,51,513,9,51,1,52,1,52,1,52,3,52,518,8,52,1,53,3,53,
        521,8,53,1,53,1,53,3,53,525,8,53,1,53,1,53,1,53,1,53,1,54,1,54,1,
        55,1,55,1,55,5,55,536,8,55,10,55,12,55,539,9,55,1,56,1,56,3,56,543,
        8,56,1,56,3,56,546,8,56,1,57,4,57,549,8,57,11,57,12,57,550,1,57,
        3,57,554,8,57,1,58,1,58,3,58,558,8,58,1,58,1,58,3,58,562,8,58,1,
        58,1,58,3,58,566,8,58,1,58,1,58,3,58,570,8,58,3,58,572,8,58,1,59,
        1,59,1,59,1,59,3,59,578,8,59,1,60,1,60,1,60,1,60,1,61,1,61,1,61,
        1,61,5,61,588,8,61,10,61,12,61,591,9,61,1,62,1,62,1,62,1,62,1,62,
        1,62,3,62,599,8,62,1,63,1,63,3,63,603,8,63,1,64,1,64,3,64,607,8,
        64,1,65,1,65,1,65,5,65,612,8,65,10,65,12,65,615,9,65,1,66,3,66,618,
        8,66,1,66,4,66,621,8,66,11,66,12,66,622,1,66,3,66,626,8,66,1,67,
        1,67,1,67,3,67,631,8,67,1,67,1,67,1,67,3,67,636,8,67,1,67,1,67,1,
        67,3,67,641,8,67,3,67,643,8,67,1,68,1,68,1,68,1,68,3,68,649,8,68,
        1,69,1,69,3,69,653,8,69,1,70,1,70,1,71,1,71,3,71,659,8,71,1,71,1,
        71,3,71,663,8,71,1,71,1,71,3,71,667,8,71,3,71,669,8,71,1,72,1,72,
        1,72,1,72,1,72,1,72,3,72,677,8,72,3,72,679,8,72,1,73,1,73,1,73,1,
        73,1,73,3,73,686,8,73,3,73,688,8,73,1,74,1,74,1,74,1,74,3,74,694,
        8,74,1,75,1,75,1,75,1,75,5,75,700,8,75,10,75,12,75,703,9,75,1,75,
        1,75,1,76,1,76,3,76,709,8,76,1,76,1,76,3,76,713,8,76,1,76,1,76,3,
        76,717,8,76,1,77,1,77,3,77,721,8,77,1,77,5,77,724,8,77,10,77,12,
        77,727,9,77,1,77,3,77,730,8,77,1,77,1,77,1,77,1,78,1,78,3,78,737,
        8,78,1,78,3,78,740,8,78,1,79,1,79,1,79,1,79,1,80,1,80,3,80,748,8,
        80,1,80,1,80,3,80,752,8,80,3,80,754,8,80,1,81,1,81,1,81,1,81,5,81,
        760,8,81,10,81,12,81,763,9,81,1,81,1,81,1,82,1,82,1,82,1,82,1,82,
        3,82,772,8,82,3,82,774,8,82,1,83,1,83,1,83,0,0,84,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,
        58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,
        102,104,106,108,110,112,114,116,118,120,122,124,126,128,130,132,
        134,136,138,140,142,144,146,148,150,152,154,156,158,160,162,164,
        166,0,4,1,0,1,2,2,0,3,3,11,11,2,0,19,19,23,25,2,0,41,41,44,44,815,
        0,170,1,0,0,0,2,176,1,0,0,0,4,181,1,0,0,0,6,186,1,0,0,0,8,193,1,
        0,0,0,10,200,1,0,0,0,12,208,1,0,0,0,14,217,1,0,0,0,16,226,1,0,0,
        0,18,230,1,0,0,0,20,237,1,0,0,0,22,239,1,0,0,0,24,241,1,0,0,0,26,
        243,1,0,0,0,28,247,1,0,0,0,30,253,1,0,0,0,32,264,1,0,0,0,34,271,
        1,0,0,0,36,273,1,0,0,0,38,275,1,0,0,0,40,277,1,0,0,0,42,293,1,0,
        0,0,44,302,1,0,0,0,46,309,1,0,0,0,48,311,1,0,0,0,50,322,1,0,0,0,
        52,337,1,0,0,0,54,339,1,0,0,0,56,355,1,0,0,0,58,357,1,0,0,0,60,363,
        1,0,0,0,62,369,1,0,0,0,64,380,1,0,0,0,66,392,1,0,0,0,68,394,1,0,
        0,0,70,403,1,0,0,0,72,412,1,0,0,0,74,424,1,0,0,0,76,429,1,0,0,0,
        78,432,1,0,0,0,80,461,1,0,0,0,82,467,1,0,0,0,84,471,1,0,0,0,86,476,
        1,0,0,0,88,478,1,0,0,0,90,481,1,0,0,0,92,490,1,0,0,0,94,493,1,0,
        0,0,96,498,1,0,0,0,98,502,1,0,0,0,100,504,1,0,0,0,102,506,1,0,0,
        0,104,514,1,0,0,0,106,520,1,0,0,0,108,530,1,0,0,0,110,532,1,0,0,
        0,112,545,1,0,0,0,114,553,1,0,0,0,116,571,1,0,0,0,118,573,1,0,0,
        0,120,579,1,0,0,0,122,583,1,0,0,0,124,598,1,0,0,0,126,602,1,0,0,
        0,128,606,1,0,0,0,130,608,1,0,0,0,132,625,1,0,0,0,134,642,1,0,0,
        0,136,644,1,0,0,0,138,650,1,0,0,0,140,654,1,0,0,0,142,668,1,0,0,
        0,144,678,1,0,0,0,146,687,1,0,0,0,148,693,1,0,0,0,150,695,1,0,0,
        0,152,716,1,0,0,0,154,718,1,0,0,0,156,734,1,0,0,0,158,741,1,0,0,
        0,160,753,1,0,0,0,162,755,1,0,0,0,164,773,1,0,0,0,166,775,1,0,0,
        0,168,171,3,2,1,0,169,171,3,4,2,0,170,168,1,0,0,0,170,169,1,0,0,
        0,171,172,1,0,0,0,172,170,1,0,0,0,172,173,1,0,0,0,173,174,1,0,0,
        0,174,175,5,0,0,1,175,1,1,0,0,0,176,177,5,2,0,0,177,178,5,32,0,0,
        178,179,5,46,0,0,179,180,3,10,5,0,180,3,1,0,0,0,181,182,5,1,0,0,
        182,183,5,32,0,0,183,184,5,46,0,0,184,185,3,12,6,0,185,5,1,0,0,0,
        186,188,5,36,0,0,187,189,5,46,0,0,188,187,1,0,0,0,188,189,1,0,0,
        0,189,190,1,0,0,0,190,191,3,10,5,0,191,192,5,37,0,0,192,7,1,0,0,
        0,193,195,5,36,0,0,194,196,5,46,0,0,195,194,1,0,0,0,195,196,1,0,
        0,0,196,197,1,0,0,0,197,198,3,12,6,0,198,199,5,37,0,0,199,9,1,0,
        0,0,200,205,3,14,7,0,201,202,5,46,0,0,202,204,3,14,7,0,203,201,1,
        0,0,0,204,207,1,0,0,0,205,203,1,0,0,0,205,206,1,0,0,0,206,11,1,0,
        0,0,207,205,1,0,0,0,208,213,3,16,8,0,209,210,5,46,0,0,210,212,3,
        16,8,0,211,209,1,0,0,0,212,215,1,0,0,0,213,211,1,0,0,0,213,214,1,
        0,0,0,214,13,1,0,0,0,215,213,1,0,0,0,216,218,3,18,9,0,217,216,1,
        0,0,0,218,219,1,0,0,0,219,217,1,0,0,0,219,220,1,0,0,0,220,223,1,
        0,0,0,221,222,5,6,0,0,222,224,3,26,13,0,223,221,1,0,0,0,223,224,
        1,0,0,0,224,15,1,0,0,0,225,227,3,32,16,0,226,225,1,0,0,0,227,228,
        1,0,0,0,228,226,1,0,0,0,228,229,1,0,0,0,229,17,1,0,0,0,230,232,3,
        20,10,0,231,233,3,142,71,0,232,231,1,0,0,0,232,233,1,0,0,0,233,19,
        1,0,0,0,234,238,3,6,3,0,235,238,3,22,11,0,236,238,3,24,12,0,237,
        234,1,0,0,0,237,235,1,0,0,0,237,236,1,0,0,0,238,21,1,0,0,0,239,240,
        7,0,0,0,240,23,1,0,0,0,241,242,5,11,0,0,242,25,1,0,0,0,243,245,3,
        166,83,0,244,246,3,28,14,0,245,244,1,0,0,0,245,246,1,0,0,0,246,27,
        1,0,0,0,247,249,5,36,0,0,248,250,3,30,15,0,249,248,1,0,0,0,249,250,
        1,0,0,0,250,251,1,0,0,0,251,252,5,37,0,0,252,29,1,0,0,0,253,258,
        3,26,13,0,254,255,5,34,0,0,255,257,3,26,13,0,256,254,1,0,0,0,257,
        260,1,0,0,0,258,256,1,0,0,0,258,259,1,0,0,0,259,262,1,0,0,0,260,
        258,1,0,0,0,261,263,5,34,0,0,262,261,1,0,0,0,262,263,1,0,0,0,263,
        31,1,0,0,0,264,266,3,34,17,0,265,267,3,142,71,0,266,265,1,0,0,0,
        266,267,1,0,0,0,267,33,1,0,0,0,268,272,3,8,4,0,269,272,3,36,18,0,
        270,272,3,38,19,0,271,268,1,0,0,0,271,269,1,0,0,0,271,270,1,0,0,
        0,272,35,1,0,0,0,273,274,5,1,0,0,274,37,1,0,0,0,275,276,7,1,0,0,
        276,39,1,0,0,0,277,281,3,42,21,0,278,280,3,46,23,0,279,278,1,0,0,
        0,280,283,1,0,0,0,281,279,1,0,0,0,281,282,1,0,0,0,282,284,1,0,0,
        0,283,281,1,0,0,0,284,288,3,74,37,0,285,287,3,72,36,0,286,285,1,
        0,0,0,287,290,1,0,0,0,288,286,1,0,0,0,288,289,1,0,0,0,289,291,1,
        0,0,0,290,288,1,0,0,0,291,292,5,0,0,1,292,41,1,0,0,0,293,294,3,44,
        22,0,294,295,3,166,83,0,295,296,5,35,0,0,296,43,1,0,0,0,297,298,
        5,20,0,0,298,303,5,22,0,0,299,300,5,21,0,0,300,303,5,22,0,0,301,
        303,5,22,0,0,302,297,1,0,0,0,302,299,1,0,0,0,302,301,1,0,0,0,303,
        45,1,0,0,0,304,310,3,48,24,0,305,310,3,54,27,0,306,310,3,58,29,0,
        307,310,3,60,30,0,308,310,3,64,32,0,309,304,1,0,0,0,309,305,1,0,
        0,0,309,306,1,0,0,0,309,307,1,0,0,0,309,308,1,0,0,0,310,47,1,0,0,
        0,311,317,5,15,0,0,312,313,3,50,25,0,313,314,5,35,0,0,314,316,1,
        0,0,0,315,312,1,0,0,0,316,319,1,0,0,0,317,315,1,0,0,0,317,318,1,
        0,0,0,318,320,1,0,0,0,319,317,1,0,0,0,320,321,5,5,0,0,321,49,1,0,
        0,0,322,323,3,166,83,0,323,324,5,41,0,0,324,325,3,52,26,0,325,51,
        1,0,0,0,326,331,3,166,83,0,327,328,5,49,0,0,328,330,3,166,83,0,329,
        327,1,0,0,0,330,333,1,0,0,0,331,329,1,0,0,0,331,332,1,0,0,0,332,
        338,1,0,0,0,333,331,1,0,0,0,334,338,5,11,0,0,335,338,3,68,34,0,336,
        338,5,10,0,0,337,326,1,0,0,0,337,334,1,0,0,0,337,335,1,0,0,0,337,
        336,1,0,0,0,338,53,1,0,0,0,339,340,5,18,0,0,340,345,3,56,28,0,341,
        342,5,34,0,0,342,344,3,56,28,0,343,341,1,0,0,0,344,347,1,0,0,0,345,
        343,1,0,0,0,345,346,1,0,0,0,346,348,1,0,0,0,347,345,1,0,0,0,348,
        349,5,35,0,0,349,55,1,0,0,0,350,351,3,166,83,0,351,352,5,41,0,0,
        352,353,3,166,83,0,353,356,1,0,0,0,354,356,3,166,83,0,355,350,1,
        0,0,0,355,354,1,0,0,0,356,57,1,0,0,0,357,359,5,16,0,0,358,360,3,
        62,31,0,359,358,1,0,0,0,359,360,1,0,0,0,360,361,1,0,0,0,361,362,
        5,5,0,0,362,59,1,0,0,0,363,365,5,17,0,0,364,366,3,62,31,0,365,364,
        1,0,0,0,365,366,1,0,0,0,366,367,1,0,0,0,367,368,5,5,0,0,368,61,1,
        0,0,0,369,374,3,166,83,0,370,371,5,34,0,0,371,373,3,166,83,0,372,
        370,1,0,0,0,373,376,1,0,0,0,374,372,1,0,0,0,374,375,1,0,0,0,375,
        378,1,0,0,0,376,374,1,0,0,0,377,379,5,34,0,0,378,377,1,0,0,0,378,
        379,1,0,0,0,379,63,1,0,0,0,380,384,5,50,0,0,381,382,3,66,33,0,382,
        383,5,33,0,0,383,385,1,0,0,0,384,381,1,0,0,0,384,385,1,0,0,0,385,
        386,1,0,0,0,386,387,3,166,83,0,387,388,3,68,34,0,388,65,1,0,0,0,
        389,393,3,166,83,0,390,393,5,20,0,0,391,393,5,21,0,0,392,389,1,0,
        0,0,392,390,1,0,0,0,392,391,1,0,0,0,393,67,1,0,0,0,394,398,5,14,
        0,0,395,397,5,61,0,0,396,395,1,0,0,0,397,400,1,0,0,0,398,396,1,0,
        0,0,398,399,1,0,0,0,399,401,1,0,0,0,400,398,1,0,0,0,401,402,5,59,
        0,0,402,69,1,0,0,0,403,407,5,13,0,0,404,406,5,58,0,0,405,404,1,0,
        0,0,406,409,1,0,0,0,407,405,1,0,0,0,407,408,1,0,0,0,408,410,1,0,
        0,0,409,407,1,0,0,0,410,411,5,56,0,0,411,71,1,0,0,0,412,413,5,31,
        0,0,413,414,3,166,83,0,414,418,5,35,0,0,415,417,3,106,53,0,416,415,
        1,0,0,0,417,420,1,0,0,0,418,416,1,0,0,0,418,419,1,0,0,0,419,73,1,
        0,0,0,420,418,1,0,0,0,421,423,3,76,38,0,422,421,1,0,0,0,423,426,
        1,0,0,0,424,422,1,0,0,0,424,425,1,0,0,0,425,75,1,0,0,0,426,424,1,
        0,0,0,427,430,3,78,39,0,428,430,3,106,53,0,429,427,1,0,0,0,429,428,
        1,0,0,0,430,77,1,0,0,0,431,433,3,96,48,0,432,431,1,0,0,0,432,433,
        1,0,0,0,433,434,1,0,0,0,434,436,5,2,0,0,435,437,3,70,35,0,436,435,
        1,0,0,0,436,437,1,0,0,0,437,439,1,0,0,0,438,440,3,88,44,0,439,438,
        1,0,0,0,439,440,1,0,0,0,440,442,1,0,0,0,441,443,3,90,45,0,442,441,
        1,0,0,0,442,443,1,0,0,0,443,445,1,0,0,0,444,446,3,92,46,0,445,444,
        1,0,0,0,445,446,1,0,0,0,446,450,1,0,0,0,447,449,3,86,43,0,448,447,
        1,0,0,0,449,452,1,0,0,0,450,448,1,0,0,0,450,451,1,0,0,0,451,453,
        1,0,0,0,452,450,1,0,0,0,453,454,5,32,0,0,454,455,3,100,50,0,455,
        456,5,35,0,0,456,457,3,80,40,0,457,79,1,0,0,0,458,460,3,82,41,0,
        459,458,1,0,0,0,460,463,1,0,0,0,461,459,1,0,0,0,461,462,1,0,0,0,
        462,465,1,0,0,0,463,461,1,0,0,0,464,466,3,84,42,0,465,464,1,0,0,
        0,465,466,1,0,0,0,466,81,1,0,0,0,467,468,5,29,0,0,468,469,3,70,35,
        0,469,470,3,68,34,0,470,83,1,0,0,0,471,472,5,30,0,0,472,473,3,68,
        34,0,473,85,1,0,0,0,474,477,3,48,24,0,475,477,3,94,47,0,476,474,
        1,0,0,0,476,475,1,0,0,0,477,87,1,0,0,0,478,479,5,26,0,0,479,480,
        3,70,35,0,480,89,1,0,0,0,481,482,5,28,0,0,482,487,3,166,83,0,483,
        484,5,34,0,0,484,486,3,166,83,0,485,483,1,0,0,0,486,489,1,0,0,0,
        487,485,1,0,0,0,487,488,1,0,0,0,488,91,1,0,0,0,489,487,1,0,0,0,490,
        491,5,27,0,0,491,492,3,70,35,0,492,93,1,0,0,0,493,494,5,50,0,0,494,
        495,3,166,83,0,495,496,3,68,34,0,496,95,1,0,0,0,497,499,3,98,49,
        0,498,497,1,0,0,0,499,500,1,0,0,0,500,498,1,0,0,0,500,501,1,0,0,
        0,501,97,1,0,0,0,502,503,7,2,0,0,503,99,1,0,0,0,504,505,3,102,51,
        0,505,101,1,0,0,0,506,511,3,104,52,0,507,508,5,46,0,0,508,510,3,
        104,52,0,509,507,1,0,0,0,510,513,1,0,0,0,511,509,1,0,0,0,511,512,
        1,0,0,0,512,103,1,0,0,0,513,511,1,0,0,0,514,517,3,132,66,0,515,516,
        5,51,0,0,516,518,3,166,83,0,517,515,1,0,0,0,517,518,1,0,0,0,518,
        105,1,0,0,0,519,521,5,19,0,0,520,519,1,0,0,0,520,521,1,0,0,0,521,
        522,1,0,0,0,522,524,5,1,0,0,523,525,3,48,24,0,524,523,1,0,0,0,524,
        525,1,0,0,0,525,526,1,0,0,0,526,527,5,32,0,0,527,528,3,108,54,0,
        528,529,5,35,0,0,529,107,1,0,0,0,530,531,3,110,55,0,531,109,1,0,
        0,0,532,537,3,112,56,0,533,534,5,46,0,0,534,536,3,112,56,0,535,533,
        1,0,0,0,536,539,1,0,0,0,537,535,1,0,0,0,537,538,1,0,0,0,538,111,
        1,0,0,0,539,537,1,0,0,0,540,542,3,114,57,0,541,543,3,122,61,0,542,
        541,1,0,0,0,542,543,1,0,0,0,543,546,1,0,0,0,544,546,1,0,0,0,545,
        540,1,0,0,0,545,544,1,0,0,0,546,113,1,0,0,0,547,549,3,116,58,0,548,
        547,1,0,0,0,549,550,1,0,0,0,550,548,1,0,0,0,550,551,1,0,0,0,551,
        554,1,0,0,0,552,554,1,0,0,0,553,548,1,0,0,0,553,552,1,0,0,0,554,
        115,1,0,0,0,555,557,3,118,59,0,556,558,3,142,71,0,557,556,1,0,0,
        0,557,558,1,0,0,0,558,572,1,0,0,0,559,561,3,144,72,0,560,562,3,142,
        71,0,561,560,1,0,0,0,561,562,1,0,0,0,562,572,1,0,0,0,563,565,3,120,
        60,0,564,566,3,142,71,0,565,564,1,0,0,0,565,566,1,0,0,0,566,572,
        1,0,0,0,567,569,3,68,34,0,568,570,5,42,0,0,569,568,1,0,0,0,569,570,
        1,0,0,0,570,572,1,0,0,0,571,555,1,0,0,0,571,559,1,0,0,0,571,563,
        1,0,0,0,571,567,1,0,0,0,572,117,1,0,0,0,573,574,3,166,83,0,574,577,
        7,3,0,0,575,578,3,144,72,0,576,578,3,120,60,0,577,575,1,0,0,0,577,
        576,1,0,0,0,578,119,1,0,0,0,579,580,5,36,0,0,580,581,3,110,55,0,
        581,582,5,37,0,0,582,121,1,0,0,0,583,584,5,38,0,0,584,589,3,124,
        62,0,585,586,5,34,0,0,586,588,3,124,62,0,587,585,1,0,0,0,588,591,
        1,0,0,0,589,587,1,0,0,0,589,590,1,0,0,0,590,123,1,0,0,0,591,589,
        1,0,0,0,592,593,3,126,63,0,593,594,5,36,0,0,594,595,3,128,64,0,595,
        596,5,37,0,0,596,599,1,0,0,0,597,599,3,126,63,0,598,592,1,0,0,0,
        598,597,1,0,0,0,599,125,1,0,0,0,600,603,3,166,83,0,601,603,5,31,
        0,0,602,600,1,0,0,0,602,601,1,0,0,0,603,127,1,0,0,0,604,607,3,166,
        83,0,605,607,5,10,0,0,606,604,1,0,0,0,606,605,1,0,0,0,607,129,1,
        0,0,0,608,613,3,132,66,0,609,610,5,46,0,0,610,612,3,132,66,0,611,
        609,1,0,0,0,612,615,1,0,0,0,613,611,1,0,0,0,613,614,1,0,0,0,614,
        131,1,0,0,0,615,613,1,0,0,0,616,618,3,162,81,0,617,616,1,0,0,0,617,
        618,1,0,0,0,618,620,1,0,0,0,619,621,3,134,67,0,620,619,1,0,0,0,621,
        622,1,0,0,0,622,620,1,0,0,0,622,623,1,0,0,0,623,626,1,0,0,0,624,
        626,1,0,0,0,625,617,1,0,0,0,625,624,1,0,0,0,626,133,1,0,0,0,627,
        630,3,136,68,0,628,631,3,142,71,0,629,631,1,0,0,0,630,628,1,0,0,
        0,630,629,1,0,0,0,631,643,1,0,0,0,632,635,3,146,73,0,633,636,3,142,
        71,0,634,636,1,0,0,0,635,633,1,0,0,0,635,634,1,0,0,0,636,643,1,0,
        0,0,637,643,3,138,69,0,638,640,3,68,34,0,639,641,5,42,0,0,640,639,
        1,0,0,0,640,641,1,0,0,0,641,643,1,0,0,0,642,627,1,0,0,0,642,632,
        1,0,0,0,642,637,1,0,0,0,642,638,1,0,0,0,643,135,1,0,0,0,644,645,
        3,166,83,0,645,648,7,3,0,0,646,649,3,146,73,0,647,649,3,154,77,0,
        648,646,1,0,0,0,648,647,1,0,0,0,649,137,1,0,0,0,650,652,3,154,77,
        0,651,653,3,140,70,0,652,651,1,0,0,0,652,653,1,0,0,0,653,139,1,0,
        0,0,654,655,3,142,71,0,655,141,1,0,0,0,656,658,5,42,0,0,657,659,
        5,42,0,0,658,657,1,0,0,0,658,659,1,0,0,0,659,669,1,0,0,0,660,662,
        5,43,0,0,661,663,5,42,0,0,662,661,1,0,0,0,662,663,1,0,0,0,663,669,
        1,0,0,0,664,666,5,45,0,0,665,667,5,42,0,0,666,665,1,0,0,0,666,667,
        1,0,0,0,667,669,1,0,0,0,668,656,1,0,0,0,668,660,1,0,0,0,668,664,
        1,0,0,0,669,143,1,0,0,0,670,679,3,158,79,0,671,679,3,160,80,0,672,
        679,3,148,74,0,673,679,5,3,0,0,674,676,5,49,0,0,675,677,3,162,81,
        0,676,675,1,0,0,0,676,677,1,0,0,0,677,679,1,0,0,0,678,670,1,0,0,
        0,678,671,1,0,0,0,678,672,1,0,0,0,678,673,1,0,0,0,678,674,1,0,0,
        0,679,145,1,0,0,0,680,688,3,160,80,0,681,688,3,156,78,0,682,688,
        3,148,74,0,683,685,5,49,0,0,684,686,3,162,81,0,685,684,1,0,0,0,685,
        686,1,0,0,0,686,688,1,0,0,0,687,680,1,0,0,0,687,681,1,0,0,0,687,
        682,1,0,0,0,687,683,1,0,0,0,688,147,1,0,0,0,689,690,5,52,0,0,690,
        694,3,152,76,0,691,692,5,52,0,0,692,694,3,150,75,0,693,689,1,0,0,
        0,693,691,1,0,0,0,694,149,1,0,0,0,695,696,5,36,0,0,696,701,3,152,
        76,0,697,698,5,46,0,0,698,700,3,152,76,0,699,697,1,0,0,0,700,703,
        1,0,0,0,701,699,1,0,0,0,701,702,1,0,0,0,702,704,1,0,0,0,703,701,
        1,0,0,0,704,705,5,37,0,0,705,151,1,0,0,0,706,708,5,1,0,0,707,709,
        3,162,81,0,708,707,1,0,0,0,708,709,1,0,0,0,709,717,1,0,0,0,710,712,
        5,11,0,0,711,713,3,162,81,0,712,711,1,0,0,0,712,713,1,0,0,0,713,
        717,1,0,0,0,714,717,3,158,79,0,715,717,5,3,0,0,716,706,1,0,0,0,716,
        710,1,0,0,0,716,714,1,0,0,0,716,715,1,0,0,0,717,153,1,0,0,0,718,
        729,5,36,0,0,719,721,3,48,24,0,720,719,1,0,0,0,720,721,1,0,0,0,721,
        725,1,0,0,0,722,724,3,94,47,0,723,722,1,0,0,0,724,727,1,0,0,0,725,
        723,1,0,0,0,725,726,1,0,0,0,726,728,1,0,0,0,727,725,1,0,0,0,728,
        730,5,32,0,0,729,720,1,0,0,0,729,730,1,0,0,0,730,731,1,0,0,0,731,
        732,3,130,65,0,732,733,5,37,0,0,733,155,1,0,0,0,734,736,5,2,0,0,
        735,737,3,70,35,0,736,735,1,0,0,0,736,737,1,0,0,0,737,739,1,0,0,
        0,738,740,3,162,81,0,739,738,1,0,0,0,739,740,1,0,0,0,740,157,1,0,
        0,0,741,742,5,11,0,0,742,743,5,48,0,0,743,744,5,11,0,0,744,159,1,
        0,0,0,745,747,5,1,0,0,746,748,3,162,81,0,747,746,1,0,0,0,747,748,
        1,0,0,0,748,754,1,0,0,0,749,751,5,11,0,0,750,752,3,162,81,0,751,
        750,1,0,0,0,751,752,1,0,0,0,752,754,1,0,0,0,753,745,1,0,0,0,753,
        749,1,0,0,0,754,161,1,0,0,0,755,756,5,39,0,0,756,761,3,164,82,0,
        757,758,5,34,0,0,758,760,3,164,82,0,759,757,1,0,0,0,760,763,1,0,
        0,0,761,759,1,0,0,0,761,762,1,0,0,0,762,764,1,0,0,0,763,761,1,0,
        0,0,764,765,5,40,0,0,765,163,1,0,0,0,766,774,3,166,83,0,767,768,
        3,166,83,0,768,771,5,41,0,0,769,772,3,166,83,0,770,772,5,11,0,0,
        771,769,1,0,0,0,771,770,1,0,0,0,772,774,1,0,0,0,773,766,1,0,0,0,
        773,767,1,0,0,0,774,165,1,0,0,0,775,776,7,0,0,0,776,167,1,0,0,0,
        101,170,172,188,195,205,213,219,223,228,232,237,245,249,258,262,
        266,271,281,288,302,309,317,331,337,345,355,359,365,374,378,384,
        392,398,407,418,424,429,432,436,439,442,445,450,461,465,476,487,
        500,511,517,520,524,537,542,545,550,553,557,561,565,569,571,577,
        589,598,602,606,613,617,622,625,630,635,640,642,648,652,658,662,
        666,668,676,678,685,687,693,701,708,712,716,720,725,729,736,739,
        747,751,753,761,771,773
    ]

class ctx2lParser ( Parser ):

    grammarFileName = "ctx2lParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'->'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'import'", "'fragment'", "'lexer'", "'parser'", 
                     "'grammar'", "'protected'", "'public'", "'private'", 
                     "'returns'", "'locals'", "'throws'", "'catch'", "'finally'", 
                     "'mode'" ]

    symbolicNames = [ "<INVALID>", "TOKEN_REF", "RULE_REF", "LEXER_CHAR_SET", 
                      "LBRACE", "RBRACE", "ARROW", "DOC_COMMENT", "BLOCK_COMMENT", 
                      "LINE_COMMENT", "INT", "STRING_LITERAL", "UNTERMINATED_STRING_LITERAL", 
                      "BEGIN_ARGUMENT", "BEGIN_ACTION", "OPTIONS", "TOKENS", 
                      "CHANNELS", "IMPORT", "FRAGMENT", "LEXER", "PARSER", 
                      "GRAMMAR", "PROTECTED", "PUBLIC", "PRIVATE", "RETURNS", 
                      "LOCALS", "THROWS", "CATCH", "FINALLY", "MODE", "COLON", 
                      "COLONCOLON", "COMMA", "SEMI", "LPAREN", "RPAREN", 
                      "RARROW", "LT", "GT", "ASSIGN", "QUESTION", "STAR", 
                      "PLUS_ASSIGN", "PLUS", "OR", "DOLLAR", "RANGE", "DOT", 
                      "AT", "POUND", "NOT", "ID", "WS", "ERRCHAR", "END_ARGUMENT", 
                      "UNTERMINATED_ARGUMENT", "ARGUMENT_CONTENT", "END_ACTION", 
                      "UNTERMINATED_ACTION", "ACTION_CONTENT", "UNTERMINATED_CHAR_SET" ]

    RULE_program = 0
    RULE_ruleDef = 1
    RULE_tokenDef = 2
    RULE_ruleSub = 3
    RULE_tokenSub = 4
    RULE_ruleAlts = 5
    RULE_tokenAlts = 6
    RULE_ruleAlt = 7
    RULE_tokenAlt = 8
    RULE_ruleAtom = 9
    RULE_ruleEbnf = 10
    RULE_ruleRef = 11
    RULE_ruleLiteral = 12
    RULE_expr = 13
    RULE_call = 14
    RULE_args = 15
    RULE_tokenAtom = 16
    RULE_tokenEbnf = 17
    RULE_tokenRef = 18
    RULE_tokenLiteral = 19
    RULE_grammarSpec = 20
    RULE_grammarDecl = 21
    RULE_grammarType = 22
    RULE_prequelConstruct = 23
    RULE_optionsSpec = 24
    RULE_option = 25
    RULE_optionValue = 26
    RULE_delegateGrammars = 27
    RULE_delegateGrammar = 28
    RULE_tokensSpec = 29
    RULE_channelsSpec = 30
    RULE_idList = 31
    RULE_action_ = 32
    RULE_actionScopeName = 33
    RULE_actionBlock = 34
    RULE_argActionBlock = 35
    RULE_modeSpec = 36
    RULE_rules = 37
    RULE_ruleSpec = 38
    RULE_parserRuleSpec = 39
    RULE_exceptionGroup = 40
    RULE_exceptionHandler = 41
    RULE_finallyClause = 42
    RULE_rulePrequel = 43
    RULE_ruleReturns = 44
    RULE_throwsSpec = 45
    RULE_localsSpec = 46
    RULE_ruleAction = 47
    RULE_ruleModifiers = 48
    RULE_ruleModifier = 49
    RULE_ruleBlock = 50
    RULE_ruleAltList = 51
    RULE_labeledAlt = 52
    RULE_lexerRuleSpec = 53
    RULE_lexerRuleBlock = 54
    RULE_lexerAltList = 55
    RULE_lexerAlt = 56
    RULE_lexerElements = 57
    RULE_lexerElement = 58
    RULE_labeledLexerElement = 59
    RULE_lexerBlock = 60
    RULE_lexerCommands = 61
    RULE_lexerCommand = 62
    RULE_lexerCommandName = 63
    RULE_lexerCommandExpr = 64
    RULE_altList = 65
    RULE_alternative = 66
    RULE_element = 67
    RULE_labeledElement = 68
    RULE_ebnf = 69
    RULE_blockSuffix = 70
    RULE_ebnfSuffix = 71
    RULE_lexerAtom = 72
    RULE_atom = 73
    RULE_notSet = 74
    RULE_blockSet = 75
    RULE_setElement = 76
    RULE_block = 77
    RULE_ruleref = 78
    RULE_characterRange = 79
    RULE_terminal = 80
    RULE_elementOptions = 81
    RULE_elementOption = 82
    RULE_identifier = 83

    ruleNames =  [ "program", "ruleDef", "tokenDef", "ruleSub", "tokenSub", 
                   "ruleAlts", "tokenAlts", "ruleAlt", "tokenAlt", "ruleAtom", 
                   "ruleEbnf", "ruleRef", "ruleLiteral", "expr", "call", 
                   "args", "tokenAtom", "tokenEbnf", "tokenRef", "tokenLiteral", 
                   "grammarSpec", "grammarDecl", "grammarType", "prequelConstruct", 
                   "optionsSpec", "option", "optionValue", "delegateGrammars", 
                   "delegateGrammar", "tokensSpec", "channelsSpec", "idList", 
                   "action_", "actionScopeName", "actionBlock", "argActionBlock", 
                   "modeSpec", "rules", "ruleSpec", "parserRuleSpec", "exceptionGroup", 
                   "exceptionHandler", "finallyClause", "rulePrequel", "ruleReturns", 
                   "throwsSpec", "localsSpec", "ruleAction", "ruleModifiers", 
                   "ruleModifier", "ruleBlock", "ruleAltList", "labeledAlt", 
                   "lexerRuleSpec", "lexerRuleBlock", "lexerAltList", "lexerAlt", 
                   "lexerElements", "lexerElement", "labeledLexerElement", 
                   "lexerBlock", "lexerCommands", "lexerCommand", "lexerCommandName", 
                   "lexerCommandExpr", "altList", "alternative", "element", 
                   "labeledElement", "ebnf", "blockSuffix", "ebnfSuffix", 
                   "lexerAtom", "atom", "notSet", "blockSet", "setElement", 
                   "block", "ruleref", "characterRange", "terminal", "elementOptions", 
                   "elementOption", "identifier" ]

    EOF = Token.EOF
    TOKEN_REF=1
    RULE_REF=2
    LEXER_CHAR_SET=3
    LBRACE=4
    RBRACE=5
    ARROW=6
    DOC_COMMENT=7
    BLOCK_COMMENT=8
    LINE_COMMENT=9
    INT=10
    STRING_LITERAL=11
    UNTERMINATED_STRING_LITERAL=12
    BEGIN_ARGUMENT=13
    BEGIN_ACTION=14
    OPTIONS=15
    TOKENS=16
    CHANNELS=17
    IMPORT=18
    FRAGMENT=19
    LEXER=20
    PARSER=21
    GRAMMAR=22
    PROTECTED=23
    PUBLIC=24
    PRIVATE=25
    RETURNS=26
    LOCALS=27
    THROWS=28
    CATCH=29
    FINALLY=30
    MODE=31
    COLON=32
    COLONCOLON=33
    COMMA=34
    SEMI=35
    LPAREN=36
    RPAREN=37
    RARROW=38
    LT=39
    GT=40
    ASSIGN=41
    QUESTION=42
    STAR=43
    PLUS_ASSIGN=44
    PLUS=45
    OR=46
    DOLLAR=47
    RANGE=48
    DOT=49
    AT=50
    POUND=51
    NOT=52
    ID=53
    WS=54
    ERRCHAR=55
    END_ARGUMENT=56
    UNTERMINATED_ARGUMENT=57
    ARGUMENT_CONTENT=58
    END_ACTION=59
    UNTERMINATED_ACTION=60
    ACTION_CONTENT=61
    UNTERMINATED_CHAR_SET=62

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ctx2lParser.EOF, 0)

        def ruleDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.RuleDefContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.RuleDefContext,i)


        def tokenDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.TokenDefContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.TokenDefContext,i)


        def getRuleIndex(self):
            return ctx2lParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ctx2lParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 170
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2]:
                    self.state = 168
                    self.ruleDef()
                    pass
                elif token in [1]:
                    self.state = 169
                    self.tokenDef()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 172 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==2):
                    break

            self.state = 174
            self.match(ctx2lParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleDefContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RULE_REF(self):
            return self.getToken(ctx2lParser.RULE_REF, 0)

        def COLON(self):
            return self.getToken(ctx2lParser.COLON, 0)

        def OR(self):
            return self.getToken(ctx2lParser.OR, 0)

        def ruleAlts(self):
            return self.getTypedRuleContext(ctx2lParser.RuleAltsContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_ruleDef

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRuleDef" ):
                return visitor.visitRuleDef(self)
            else:
                return visitor.visitChildren(self)




    def ruleDef(self):

        localctx = ctx2lParser.RuleDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_ruleDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(ctx2lParser.RULE_REF)
            self.state = 177
            self.match(ctx2lParser.COLON)
            self.state = 178
            self.match(ctx2lParser.OR)
            self.state = 179
            self.ruleAlts()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TokenDefContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TOKEN_REF(self):
            return self.getToken(ctx2lParser.TOKEN_REF, 0)

        def COLON(self):
            return self.getToken(ctx2lParser.COLON, 0)

        def OR(self):
            return self.getToken(ctx2lParser.OR, 0)

        def tokenAlts(self):
            return self.getTypedRuleContext(ctx2lParser.TokenAltsContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_tokenDef

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTokenDef" ):
                return visitor.visitTokenDef(self)
            else:
                return visitor.visitChildren(self)




    def tokenDef(self):

        localctx = ctx2lParser.TokenDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_tokenDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(ctx2lParser.TOKEN_REF)
            self.state = 182
            self.match(ctx2lParser.COLON)
            self.state = 183
            self.match(ctx2lParser.OR)
            self.state = 184
            self.tokenAlts()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleSubContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ctx2lParser.LPAREN, 0)

        def ruleAlts(self):
            return self.getTypedRuleContext(ctx2lParser.RuleAltsContext,0)


        def RPAREN(self):
            return self.getToken(ctx2lParser.RPAREN, 0)

        def OR(self):
            return self.getToken(ctx2lParser.OR, 0)

        def getRuleIndex(self):
            return ctx2lParser.RULE_ruleSub

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRuleSub" ):
                return visitor.visitRuleSub(self)
            else:
                return visitor.visitChildren(self)




    def ruleSub(self):

        localctx = ctx2lParser.RuleSubContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ruleSub)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(ctx2lParser.LPAREN)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 187
                self.match(ctx2lParser.OR)


            self.state = 190
            self.ruleAlts()
            self.state = 191
            self.match(ctx2lParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TokenSubContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ctx2lParser.LPAREN, 0)

        def tokenAlts(self):
            return self.getTypedRuleContext(ctx2lParser.TokenAltsContext,0)


        def RPAREN(self):
            return self.getToken(ctx2lParser.RPAREN, 0)

        def OR(self):
            return self.getToken(ctx2lParser.OR, 0)

        def getRuleIndex(self):
            return ctx2lParser.RULE_tokenSub

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTokenSub" ):
                return visitor.visitTokenSub(self)
            else:
                return visitor.visitChildren(self)




    def tokenSub(self):

        localctx = ctx2lParser.TokenSubContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tokenSub)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(ctx2lParser.LPAREN)
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 194
                self.match(ctx2lParser.OR)


            self.state = 197
            self.tokenAlts()
            self.state = 198
            self.match(ctx2lParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleAltsContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ruleAlt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.RuleAltContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.RuleAltContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(ctx2lParser.OR)
            else:
                return self.getToken(ctx2lParser.OR, i)

        def getRuleIndex(self):
            return ctx2lParser.RULE_ruleAlts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRuleAlts" ):
                return visitor.visitRuleAlts(self)
            else:
                return visitor.visitChildren(self)




    def ruleAlts(self):

        localctx = ctx2lParser.RuleAltsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ruleAlts)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.ruleAlt()
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 201
                self.match(ctx2lParser.OR)
                self.state = 202
                self.ruleAlt()
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TokenAltsContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tokenAlt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.TokenAltContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.TokenAltContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(ctx2lParser.OR)
            else:
                return self.getToken(ctx2lParser.OR, i)

        def getRuleIndex(self):
            return ctx2lParser.RULE_tokenAlts

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTokenAlts" ):
                return visitor.visitTokenAlts(self)
            else:
                return visitor.visitChildren(self)




    def tokenAlts(self):

        localctx = ctx2lParser.TokenAltsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tokenAlts)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.tokenAlt()
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 209
                self.match(ctx2lParser.OR)
                self.state = 210
                self.tokenAlt()
                self.state = 215
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleAltContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ruleAtom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.RuleAtomContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.RuleAtomContext,i)


        def ARROW(self):
            return self.getToken(ctx2lParser.ARROW, 0)

        def expr(self):
            return self.getTypedRuleContext(ctx2lParser.ExprContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_ruleAlt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRuleAlt" ):
                return visitor.visitRuleAlt(self)
            else:
                return visitor.visitChildren(self)




    def ruleAlt(self):

        localctx = ctx2lParser.RuleAltContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_ruleAlt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 216
                    self.ruleAtom()

                else:
                    raise NoViableAltException(self)
                self.state = 219 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 221
                self.match(ctx2lParser.ARROW)
                self.state = 222
                self.expr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TokenAltContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tokenAtom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.TokenAtomContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.TokenAtomContext,i)


        def getRuleIndex(self):
            return ctx2lParser.RULE_tokenAlt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTokenAlt" ):
                return visitor.visitTokenAlt(self)
            else:
                return visitor.visitChildren(self)




    def tokenAlt(self):

        localctx = ctx2lParser.TokenAltContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_tokenAlt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 225
                    self.tokenAtom()

                else:
                    raise NoViableAltException(self)
                self.state = 228 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleAtomContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ruleEbnf(self):
            return self.getTypedRuleContext(ctx2lParser.RuleEbnfContext,0)


        def ebnfSuffix(self):
            return self.getTypedRuleContext(ctx2lParser.EbnfSuffixContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_ruleAtom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRuleAtom" ):
                return visitor.visitRuleAtom(self)
            else:
                return visitor.visitChildren(self)




    def ruleAtom(self):

        localctx = ctx2lParser.RuleAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ruleAtom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.ruleEbnf()
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 48378511622144) != 0):
                self.state = 231
                self.ebnfSuffix()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleEbnfContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ruleSub(self):
            return self.getTypedRuleContext(ctx2lParser.RuleSubContext,0)


        def ruleRef(self):
            return self.getTypedRuleContext(ctx2lParser.RuleRefContext,0)


        def ruleLiteral(self):
            return self.getTypedRuleContext(ctx2lParser.RuleLiteralContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_ruleEbnf

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRuleEbnf" ):
                return visitor.visitRuleEbnf(self)
            else:
                return visitor.visitChildren(self)




    def ruleEbnf(self):

        localctx = ctx2lParser.RuleEbnfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ruleEbnf)
        try:
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.ruleSub()
                pass
            elif token in [1, 2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.ruleRef()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 236
                self.ruleLiteral()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleRefContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RULE_REF(self):
            return self.getToken(ctx2lParser.RULE_REF, 0)

        def TOKEN_REF(self):
            return self.getToken(ctx2lParser.TOKEN_REF, 0)

        def getRuleIndex(self):
            return ctx2lParser.RULE_ruleRef

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRuleRef" ):
                return visitor.visitRuleRef(self)
            else:
                return visitor.visitChildren(self)




    def ruleRef(self):

        localctx = ctx2lParser.RuleRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ruleRef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleLiteralContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL(self):
            return self.getToken(ctx2lParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return ctx2lParser.RULE_ruleLiteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRuleLiteral" ):
                return visitor.visitRuleLiteral(self)
            else:
                return visitor.visitChildren(self)




    def ruleLiteral(self):

        localctx = ctx2lParser.RuleLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_ruleLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(ctx2lParser.STRING_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(ctx2lParser.IdentifierContext,0)


        def call(self):
            return self.getTypedRuleContext(ctx2lParser.CallContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ctx2lParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.identifier()
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 244
                self.call()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ctx2lParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(ctx2lParser.RPAREN, 0)

        def args(self):
            return self.getTypedRuleContext(ctx2lParser.ArgsContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = ctx2lParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(ctx2lParser.LPAREN)
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==2:
                self.state = 248
                self.args()


            self.state = 251
            self.match(ctx2lParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.ExprContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ctx2lParser.COMMA)
            else:
                return self.getToken(ctx2lParser.COMMA, i)

        def getRuleIndex(self):
            return ctx2lParser.RULE_args

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgs" ):
                return visitor.visitArgs(self)
            else:
                return visitor.visitChildren(self)




    def args(self):

        localctx = ctx2lParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.expr()
            self.state = 258
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 254
                    self.match(ctx2lParser.COMMA)
                    self.state = 255
                    self.expr() 
                self.state = 260
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 261
                self.match(ctx2lParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TokenAtomContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tokenEbnf(self):
            return self.getTypedRuleContext(ctx2lParser.TokenEbnfContext,0)


        def ebnfSuffix(self):
            return self.getTypedRuleContext(ctx2lParser.EbnfSuffixContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_tokenAtom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTokenAtom" ):
                return visitor.visitTokenAtom(self)
            else:
                return visitor.visitChildren(self)




    def tokenAtom(self):

        localctx = ctx2lParser.TokenAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_tokenAtom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.tokenEbnf()
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 48378511622144) != 0):
                self.state = 265
                self.ebnfSuffix()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TokenEbnfContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tokenSub(self):
            return self.getTypedRuleContext(ctx2lParser.TokenSubContext,0)


        def tokenRef(self):
            return self.getTypedRuleContext(ctx2lParser.TokenRefContext,0)


        def tokenLiteral(self):
            return self.getTypedRuleContext(ctx2lParser.TokenLiteralContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_tokenEbnf

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTokenEbnf" ):
                return visitor.visitTokenEbnf(self)
            else:
                return visitor.visitChildren(self)




    def tokenEbnf(self):

        localctx = ctx2lParser.TokenEbnfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_tokenEbnf)
        try:
            self.state = 271
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 268
                self.tokenSub()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 269
                self.tokenRef()
                pass
            elif token in [3, 11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 270
                self.tokenLiteral()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TokenRefContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TOKEN_REF(self):
            return self.getToken(ctx2lParser.TOKEN_REF, 0)

        def getRuleIndex(self):
            return ctx2lParser.RULE_tokenRef

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTokenRef" ):
                return visitor.visitTokenRef(self)
            else:
                return visitor.visitChildren(self)




    def tokenRef(self):

        localctx = ctx2lParser.TokenRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_tokenRef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.match(ctx2lParser.TOKEN_REF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TokenLiteralContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL(self):
            return self.getToken(ctx2lParser.STRING_LITERAL, 0)

        def LEXER_CHAR_SET(self):
            return self.getToken(ctx2lParser.LEXER_CHAR_SET, 0)

        def getRuleIndex(self):
            return ctx2lParser.RULE_tokenLiteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTokenLiteral" ):
                return visitor.visitTokenLiteral(self)
            else:
                return visitor.visitChildren(self)




    def tokenLiteral(self):

        localctx = ctx2lParser.TokenLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_tokenLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            _la = self._input.LA(1)
            if not(_la==3 or _la==11):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GrammarSpecContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def grammarDecl(self):
            return self.getTypedRuleContext(ctx2lParser.GrammarDeclContext,0)


        def rules(self):
            return self.getTypedRuleContext(ctx2lParser.RulesContext,0)


        def EOF(self):
            return self.getToken(ctx2lParser.EOF, 0)

        def prequelConstruct(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.PrequelConstructContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.PrequelConstructContext,i)


        def modeSpec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.ModeSpecContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.ModeSpecContext,i)


        def getRuleIndex(self):
            return ctx2lParser.RULE_grammarSpec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGrammarSpec" ):
                return visitor.visitGrammarSpec(self)
            else:
                return visitor.visitChildren(self)




    def grammarSpec(self):

        localctx = ctx2lParser.GrammarSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_grammarSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.grammarDecl()
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1125899907334144) != 0):
                self.state = 278
                self.prequelConstruct()
                self.state = 283
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 284
            self.rules()
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 285
                self.modeSpec()
                self.state = 290
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 291
            self.match(ctx2lParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GrammarDeclContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def grammarType(self):
            return self.getTypedRuleContext(ctx2lParser.GrammarTypeContext,0)


        def identifier(self):
            return self.getTypedRuleContext(ctx2lParser.IdentifierContext,0)


        def SEMI(self):
            return self.getToken(ctx2lParser.SEMI, 0)

        def getRuleIndex(self):
            return ctx2lParser.RULE_grammarDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGrammarDecl" ):
                return visitor.visitGrammarDecl(self)
            else:
                return visitor.visitChildren(self)




    def grammarDecl(self):

        localctx = ctx2lParser.GrammarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_grammarDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.grammarType()
            self.state = 294
            self.identifier()
            self.state = 295
            self.match(ctx2lParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GrammarTypeContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEXER(self):
            return self.getToken(ctx2lParser.LEXER, 0)

        def GRAMMAR(self):
            return self.getToken(ctx2lParser.GRAMMAR, 0)

        def PARSER(self):
            return self.getToken(ctx2lParser.PARSER, 0)

        def getRuleIndex(self):
            return ctx2lParser.RULE_grammarType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGrammarType" ):
                return visitor.visitGrammarType(self)
            else:
                return visitor.visitChildren(self)




    def grammarType(self):

        localctx = ctx2lParser.GrammarTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_grammarType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.state = 297
                self.match(ctx2lParser.LEXER)
                self.state = 298
                self.match(ctx2lParser.GRAMMAR)
                pass
            elif token in [21]:
                self.state = 299
                self.match(ctx2lParser.PARSER)
                self.state = 300
                self.match(ctx2lParser.GRAMMAR)
                pass
            elif token in [22]:
                self.state = 301
                self.match(ctx2lParser.GRAMMAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrequelConstructContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def optionsSpec(self):
            return self.getTypedRuleContext(ctx2lParser.OptionsSpecContext,0)


        def delegateGrammars(self):
            return self.getTypedRuleContext(ctx2lParser.DelegateGrammarsContext,0)


        def tokensSpec(self):
            return self.getTypedRuleContext(ctx2lParser.TokensSpecContext,0)


        def channelsSpec(self):
            return self.getTypedRuleContext(ctx2lParser.ChannelsSpecContext,0)


        def action_(self):
            return self.getTypedRuleContext(ctx2lParser.Action_Context,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_prequelConstruct

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrequelConstruct" ):
                return visitor.visitPrequelConstruct(self)
            else:
                return visitor.visitChildren(self)




    def prequelConstruct(self):

        localctx = ctx2lParser.PrequelConstructContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_prequelConstruct)
        try:
            self.state = 309
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                self.optionsSpec()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
                self.delegateGrammars()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 306
                self.tokensSpec()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 4)
                self.state = 307
                self.channelsSpec()
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 5)
                self.state = 308
                self.action_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptionsSpecContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPTIONS(self):
            return self.getToken(ctx2lParser.OPTIONS, 0)

        def RBRACE(self):
            return self.getToken(ctx2lParser.RBRACE, 0)

        def option(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.OptionContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.OptionContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(ctx2lParser.SEMI)
            else:
                return self.getToken(ctx2lParser.SEMI, i)

        def getRuleIndex(self):
            return ctx2lParser.RULE_optionsSpec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptionsSpec" ):
                return visitor.visitOptionsSpec(self)
            else:
                return visitor.visitChildren(self)




    def optionsSpec(self):

        localctx = ctx2lParser.OptionsSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_optionsSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
            self.match(ctx2lParser.OPTIONS)
            self.state = 317
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==2:
                self.state = 312
                self.option()
                self.state = 313
                self.match(ctx2lParser.SEMI)
                self.state = 319
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 320
            self.match(ctx2lParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptionContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(ctx2lParser.IdentifierContext,0)


        def ASSIGN(self):
            return self.getToken(ctx2lParser.ASSIGN, 0)

        def optionValue(self):
            return self.getTypedRuleContext(ctx2lParser.OptionValueContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_option

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOption" ):
                return visitor.visitOption(self)
            else:
                return visitor.visitChildren(self)




    def option(self):

        localctx = ctx2lParser.OptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_option)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 322
            self.identifier()
            self.state = 323
            self.match(ctx2lParser.ASSIGN)
            self.state = 324
            self.optionValue()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptionValueContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.IdentifierContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(ctx2lParser.DOT)
            else:
                return self.getToken(ctx2lParser.DOT, i)

        def STRING_LITERAL(self):
            return self.getToken(ctx2lParser.STRING_LITERAL, 0)

        def actionBlock(self):
            return self.getTypedRuleContext(ctx2lParser.ActionBlockContext,0)


        def INT(self):
            return self.getToken(ctx2lParser.INT, 0)

        def getRuleIndex(self):
            return ctx2lParser.RULE_optionValue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptionValue" ):
                return visitor.visitOptionValue(self)
            else:
                return visitor.visitChildren(self)




    def optionValue(self):

        localctx = ctx2lParser.OptionValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_optionValue)
        self._la = 0 # Token type
        try:
            self.state = 337
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.identifier()
                self.state = 331
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==49:
                    self.state = 327
                    self.match(ctx2lParser.DOT)
                    self.state = 328
                    self.identifier()
                    self.state = 333
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
                self.match(ctx2lParser.STRING_LITERAL)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 335
                self.actionBlock()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 336
                self.match(ctx2lParser.INT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DelegateGrammarsContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(ctx2lParser.IMPORT, 0)

        def delegateGrammar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.DelegateGrammarContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.DelegateGrammarContext,i)


        def SEMI(self):
            return self.getToken(ctx2lParser.SEMI, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ctx2lParser.COMMA)
            else:
                return self.getToken(ctx2lParser.COMMA, i)

        def getRuleIndex(self):
            return ctx2lParser.RULE_delegateGrammars

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDelegateGrammars" ):
                return visitor.visitDelegateGrammars(self)
            else:
                return visitor.visitChildren(self)




    def delegateGrammars(self):

        localctx = ctx2lParser.DelegateGrammarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_delegateGrammars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.match(ctx2lParser.IMPORT)
            self.state = 340
            self.delegateGrammar()
            self.state = 345
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 341
                self.match(ctx2lParser.COMMA)
                self.state = 342
                self.delegateGrammar()
                self.state = 347
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 348
            self.match(ctx2lParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DelegateGrammarContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.IdentifierContext,i)


        def ASSIGN(self):
            return self.getToken(ctx2lParser.ASSIGN, 0)

        def getRuleIndex(self):
            return ctx2lParser.RULE_delegateGrammar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDelegateGrammar" ):
                return visitor.visitDelegateGrammar(self)
            else:
                return visitor.visitChildren(self)




    def delegateGrammar(self):

        localctx = ctx2lParser.DelegateGrammarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_delegateGrammar)
        try:
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.identifier()
                self.state = 351
                self.match(ctx2lParser.ASSIGN)
                self.state = 352
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.identifier()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TokensSpecContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TOKENS(self):
            return self.getToken(ctx2lParser.TOKENS, 0)

        def RBRACE(self):
            return self.getToken(ctx2lParser.RBRACE, 0)

        def idList(self):
            return self.getTypedRuleContext(ctx2lParser.IdListContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_tokensSpec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTokensSpec" ):
                return visitor.visitTokensSpec(self)
            else:
                return visitor.visitChildren(self)




    def tokensSpec(self):

        localctx = ctx2lParser.TokensSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_tokensSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(ctx2lParser.TOKENS)
            self.state = 359
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==2:
                self.state = 358
                self.idList()


            self.state = 361
            self.match(ctx2lParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChannelsSpecContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHANNELS(self):
            return self.getToken(ctx2lParser.CHANNELS, 0)

        def RBRACE(self):
            return self.getToken(ctx2lParser.RBRACE, 0)

        def idList(self):
            return self.getTypedRuleContext(ctx2lParser.IdListContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_channelsSpec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChannelsSpec" ):
                return visitor.visitChannelsSpec(self)
            else:
                return visitor.visitChildren(self)




    def channelsSpec(self):

        localctx = ctx2lParser.ChannelsSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_channelsSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 363
            self.match(ctx2lParser.CHANNELS)
            self.state = 365
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==2:
                self.state = 364
                self.idList()


            self.state = 367
            self.match(ctx2lParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdListContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.IdentifierContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ctx2lParser.COMMA)
            else:
                return self.getToken(ctx2lParser.COMMA, i)

        def getRuleIndex(self):
            return ctx2lParser.RULE_idList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdList" ):
                return visitor.visitIdList(self)
            else:
                return visitor.visitChildren(self)




    def idList(self):

        localctx = ctx2lParser.IdListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_idList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.identifier()
            self.state = 374
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 370
                    self.match(ctx2lParser.COMMA)
                    self.state = 371
                    self.identifier() 
                self.state = 376
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

            self.state = 378
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 377
                self.match(ctx2lParser.COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Action_Context(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT(self):
            return self.getToken(ctx2lParser.AT, 0)

        def identifier(self):
            return self.getTypedRuleContext(ctx2lParser.IdentifierContext,0)


        def actionBlock(self):
            return self.getTypedRuleContext(ctx2lParser.ActionBlockContext,0)


        def actionScopeName(self):
            return self.getTypedRuleContext(ctx2lParser.ActionScopeNameContext,0)


        def COLONCOLON(self):
            return self.getToken(ctx2lParser.COLONCOLON, 0)

        def getRuleIndex(self):
            return ctx2lParser.RULE_action_

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAction_" ):
                return visitor.visitAction_(self)
            else:
                return visitor.visitChildren(self)




    def action_(self):

        localctx = ctx2lParser.Action_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_action_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 380
            self.match(ctx2lParser.AT)
            self.state = 384
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 381
                self.actionScopeName()
                self.state = 382
                self.match(ctx2lParser.COLONCOLON)


            self.state = 386
            self.identifier()
            self.state = 387
            self.actionBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionScopeNameContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(ctx2lParser.IdentifierContext,0)


        def LEXER(self):
            return self.getToken(ctx2lParser.LEXER, 0)

        def PARSER(self):
            return self.getToken(ctx2lParser.PARSER, 0)

        def getRuleIndex(self):
            return ctx2lParser.RULE_actionScopeName

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActionScopeName" ):
                return visitor.visitActionScopeName(self)
            else:
                return visitor.visitChildren(self)




    def actionScopeName(self):

        localctx = ctx2lParser.ActionScopeNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_actionScopeName)
        try:
            self.state = 392
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self.identifier()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 390
                self.match(ctx2lParser.LEXER)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 391
                self.match(ctx2lParser.PARSER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionBlockContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN_ACTION(self):
            return self.getToken(ctx2lParser.BEGIN_ACTION, 0)

        def END_ACTION(self):
            return self.getToken(ctx2lParser.END_ACTION, 0)

        def ACTION_CONTENT(self, i:int=None):
            if i is None:
                return self.getTokens(ctx2lParser.ACTION_CONTENT)
            else:
                return self.getToken(ctx2lParser.ACTION_CONTENT, i)

        def getRuleIndex(self):
            return ctx2lParser.RULE_actionBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActionBlock" ):
                return visitor.visitActionBlock(self)
            else:
                return visitor.visitChildren(self)




    def actionBlock(self):

        localctx = ctx2lParser.ActionBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_actionBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.match(ctx2lParser.BEGIN_ACTION)
            self.state = 398
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==61:
                self.state = 395
                self.match(ctx2lParser.ACTION_CONTENT)
                self.state = 400
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 401
            self.match(ctx2lParser.END_ACTION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgActionBlockContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN_ARGUMENT(self):
            return self.getToken(ctx2lParser.BEGIN_ARGUMENT, 0)

        def END_ARGUMENT(self):
            return self.getToken(ctx2lParser.END_ARGUMENT, 0)

        def ARGUMENT_CONTENT(self, i:int=None):
            if i is None:
                return self.getTokens(ctx2lParser.ARGUMENT_CONTENT)
            else:
                return self.getToken(ctx2lParser.ARGUMENT_CONTENT, i)

        def getRuleIndex(self):
            return ctx2lParser.RULE_argActionBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgActionBlock" ):
                return visitor.visitArgActionBlock(self)
            else:
                return visitor.visitChildren(self)




    def argActionBlock(self):

        localctx = ctx2lParser.ArgActionBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_argActionBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(ctx2lParser.BEGIN_ARGUMENT)
            self.state = 407
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==58:
                self.state = 404
                self.match(ctx2lParser.ARGUMENT_CONTENT)
                self.state = 409
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 410
            self.match(ctx2lParser.END_ARGUMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModeSpecContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MODE(self):
            return self.getToken(ctx2lParser.MODE, 0)

        def identifier(self):
            return self.getTypedRuleContext(ctx2lParser.IdentifierContext,0)


        def SEMI(self):
            return self.getToken(ctx2lParser.SEMI, 0)

        def lexerRuleSpec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.LexerRuleSpecContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.LexerRuleSpecContext,i)


        def getRuleIndex(self):
            return ctx2lParser.RULE_modeSpec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModeSpec" ):
                return visitor.visitModeSpec(self)
            else:
                return visitor.visitChildren(self)




    def modeSpec(self):

        localctx = ctx2lParser.ModeSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_modeSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 412
            self.match(ctx2lParser.MODE)
            self.state = 413
            self.identifier()
            self.state = 414
            self.match(ctx2lParser.SEMI)
            self.state = 418
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==19:
                self.state = 415
                self.lexerRuleSpec()
                self.state = 420
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RulesContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ruleSpec(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.RuleSpecContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.RuleSpecContext,i)


        def getRuleIndex(self):
            return ctx2lParser.RULE_rules

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRules" ):
                return visitor.visitRules(self)
            else:
                return visitor.visitChildren(self)




    def rules(self):

        localctx = ctx2lParser.RulesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_rules)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 59244550) != 0):
                self.state = 421
                self.ruleSpec()
                self.state = 426
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleSpecContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parserRuleSpec(self):
            return self.getTypedRuleContext(ctx2lParser.ParserRuleSpecContext,0)


        def lexerRuleSpec(self):
            return self.getTypedRuleContext(ctx2lParser.LexerRuleSpecContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_ruleSpec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRuleSpec" ):
                return visitor.visitRuleSpec(self)
            else:
                return visitor.visitChildren(self)




    def ruleSpec(self):

        localctx = ctx2lParser.RuleSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_ruleSpec)
        try:
            self.state = 429
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.parserRuleSpec()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.lexerRuleSpec()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParserRuleSpecContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RULE_REF(self):
            return self.getToken(ctx2lParser.RULE_REF, 0)

        def COLON(self):
            return self.getToken(ctx2lParser.COLON, 0)

        def ruleBlock(self):
            return self.getTypedRuleContext(ctx2lParser.RuleBlockContext,0)


        def SEMI(self):
            return self.getToken(ctx2lParser.SEMI, 0)

        def exceptionGroup(self):
            return self.getTypedRuleContext(ctx2lParser.ExceptionGroupContext,0)


        def ruleModifiers(self):
            return self.getTypedRuleContext(ctx2lParser.RuleModifiersContext,0)


        def argActionBlock(self):
            return self.getTypedRuleContext(ctx2lParser.ArgActionBlockContext,0)


        def ruleReturns(self):
            return self.getTypedRuleContext(ctx2lParser.RuleReturnsContext,0)


        def throwsSpec(self):
            return self.getTypedRuleContext(ctx2lParser.ThrowsSpecContext,0)


        def localsSpec(self):
            return self.getTypedRuleContext(ctx2lParser.LocalsSpecContext,0)


        def rulePrequel(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.RulePrequelContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.RulePrequelContext,i)


        def getRuleIndex(self):
            return ctx2lParser.RULE_parserRuleSpec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParserRuleSpec" ):
                return visitor.visitParserRuleSpec(self)
            else:
                return visitor.visitChildren(self)




    def parserRuleSpec(self):

        localctx = ctx2lParser.ParserRuleSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_parserRuleSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 59244544) != 0):
                self.state = 431
                self.ruleModifiers()


            self.state = 434
            self.match(ctx2lParser.RULE_REF)
            self.state = 436
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 435
                self.argActionBlock()


            self.state = 439
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 438
                self.ruleReturns()


            self.state = 442
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 441
                self.throwsSpec()


            self.state = 445
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 444
                self.localsSpec()


            self.state = 450
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15 or _la==50:
                self.state = 447
                self.rulePrequel()
                self.state = 452
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 453
            self.match(ctx2lParser.COLON)
            self.state = 454
            self.ruleBlock()
            self.state = 455
            self.match(ctx2lParser.SEMI)
            self.state = 456
            self.exceptionGroup()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExceptionGroupContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exceptionHandler(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.ExceptionHandlerContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.ExceptionHandlerContext,i)


        def finallyClause(self):
            return self.getTypedRuleContext(ctx2lParser.FinallyClauseContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_exceptionGroup

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExceptionGroup" ):
                return visitor.visitExceptionGroup(self)
            else:
                return visitor.visitChildren(self)




    def exceptionGroup(self):

        localctx = ctx2lParser.ExceptionGroupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_exceptionGroup)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 458
                self.exceptionHandler()
                self.state = 463
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 465
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 464
                self.finallyClause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExceptionHandlerContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CATCH(self):
            return self.getToken(ctx2lParser.CATCH, 0)

        def argActionBlock(self):
            return self.getTypedRuleContext(ctx2lParser.ArgActionBlockContext,0)


        def actionBlock(self):
            return self.getTypedRuleContext(ctx2lParser.ActionBlockContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_exceptionHandler

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExceptionHandler" ):
                return visitor.visitExceptionHandler(self)
            else:
                return visitor.visitChildren(self)




    def exceptionHandler(self):

        localctx = ctx2lParser.ExceptionHandlerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_exceptionHandler)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            self.match(ctx2lParser.CATCH)
            self.state = 468
            self.argActionBlock()
            self.state = 469
            self.actionBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FinallyClauseContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINALLY(self):
            return self.getToken(ctx2lParser.FINALLY, 0)

        def actionBlock(self):
            return self.getTypedRuleContext(ctx2lParser.ActionBlockContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_finallyClause

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFinallyClause" ):
                return visitor.visitFinallyClause(self)
            else:
                return visitor.visitChildren(self)




    def finallyClause(self):

        localctx = ctx2lParser.FinallyClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_finallyClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 471
            self.match(ctx2lParser.FINALLY)
            self.state = 472
            self.actionBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RulePrequelContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def optionsSpec(self):
            return self.getTypedRuleContext(ctx2lParser.OptionsSpecContext,0)


        def ruleAction(self):
            return self.getTypedRuleContext(ctx2lParser.RuleActionContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_rulePrequel

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRulePrequel" ):
                return visitor.visitRulePrequel(self)
            else:
                return visitor.visitChildren(self)




    def rulePrequel(self):

        localctx = ctx2lParser.RulePrequelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_rulePrequel)
        try:
            self.state = 476
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 474
                self.optionsSpec()
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 2)
                self.state = 475
                self.ruleAction()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleReturnsContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURNS(self):
            return self.getToken(ctx2lParser.RETURNS, 0)

        def argActionBlock(self):
            return self.getTypedRuleContext(ctx2lParser.ArgActionBlockContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_ruleReturns

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRuleReturns" ):
                return visitor.visitRuleReturns(self)
            else:
                return visitor.visitChildren(self)




    def ruleReturns(self):

        localctx = ctx2lParser.RuleReturnsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_ruleReturns)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.match(ctx2lParser.RETURNS)
            self.state = 479
            self.argActionBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThrowsSpecContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THROWS(self):
            return self.getToken(ctx2lParser.THROWS, 0)

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.IdentifierContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ctx2lParser.COMMA)
            else:
                return self.getToken(ctx2lParser.COMMA, i)

        def getRuleIndex(self):
            return ctx2lParser.RULE_throwsSpec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThrowsSpec" ):
                return visitor.visitThrowsSpec(self)
            else:
                return visitor.visitChildren(self)




    def throwsSpec(self):

        localctx = ctx2lParser.ThrowsSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_throwsSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 481
            self.match(ctx2lParser.THROWS)
            self.state = 482
            self.identifier()
            self.state = 487
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 483
                self.match(ctx2lParser.COMMA)
                self.state = 484
                self.identifier()
                self.state = 489
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LocalsSpecContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOCALS(self):
            return self.getToken(ctx2lParser.LOCALS, 0)

        def argActionBlock(self):
            return self.getTypedRuleContext(ctx2lParser.ArgActionBlockContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_localsSpec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocalsSpec" ):
                return visitor.visitLocalsSpec(self)
            else:
                return visitor.visitChildren(self)




    def localsSpec(self):

        localctx = ctx2lParser.LocalsSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_localsSpec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self.match(ctx2lParser.LOCALS)
            self.state = 491
            self.argActionBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleActionContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AT(self):
            return self.getToken(ctx2lParser.AT, 0)

        def identifier(self):
            return self.getTypedRuleContext(ctx2lParser.IdentifierContext,0)


        def actionBlock(self):
            return self.getTypedRuleContext(ctx2lParser.ActionBlockContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_ruleAction

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRuleAction" ):
                return visitor.visitRuleAction(self)
            else:
                return visitor.visitChildren(self)




    def ruleAction(self):

        localctx = ctx2lParser.RuleActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_ruleAction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
            self.match(ctx2lParser.AT)
            self.state = 494
            self.identifier()
            self.state = 495
            self.actionBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleModifiersContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ruleModifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.RuleModifierContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.RuleModifierContext,i)


        def getRuleIndex(self):
            return ctx2lParser.RULE_ruleModifiers

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRuleModifiers" ):
                return visitor.visitRuleModifiers(self)
            else:
                return visitor.visitChildren(self)




    def ruleModifiers(self):

        localctx = ctx2lParser.RuleModifiersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_ruleModifiers)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 498 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 497
                self.ruleModifier()
                self.state = 500 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 59244544) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleModifierContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUBLIC(self):
            return self.getToken(ctx2lParser.PUBLIC, 0)

        def PRIVATE(self):
            return self.getToken(ctx2lParser.PRIVATE, 0)

        def PROTECTED(self):
            return self.getToken(ctx2lParser.PROTECTED, 0)

        def FRAGMENT(self):
            return self.getToken(ctx2lParser.FRAGMENT, 0)

        def getRuleIndex(self):
            return ctx2lParser.RULE_ruleModifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRuleModifier" ):
                return visitor.visitRuleModifier(self)
            else:
                return visitor.visitChildren(self)




    def ruleModifier(self):

        localctx = ctx2lParser.RuleModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_ruleModifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 502
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 59244544) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleBlockContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ruleAltList(self):
            return self.getTypedRuleContext(ctx2lParser.RuleAltListContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_ruleBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRuleBlock" ):
                return visitor.visitRuleBlock(self)
            else:
                return visitor.visitChildren(self)




    def ruleBlock(self):

        localctx = ctx2lParser.RuleBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_ruleBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self.ruleAltList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleAltListContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def labeledAlt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.LabeledAltContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.LabeledAltContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(ctx2lParser.OR)
            else:
                return self.getToken(ctx2lParser.OR, i)

        def getRuleIndex(self):
            return ctx2lParser.RULE_ruleAltList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRuleAltList" ):
                return visitor.visitRuleAltList(self)
            else:
                return visitor.visitChildren(self)




    def ruleAltList(self):

        localctx = ctx2lParser.RuleAltListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_ruleAltList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 506
            self.labeledAlt()
            self.state = 511
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 507
                self.match(ctx2lParser.OR)
                self.state = 508
                self.labeledAlt()
                self.state = 513
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabeledAltContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def alternative(self):
            return self.getTypedRuleContext(ctx2lParser.AlternativeContext,0)


        def POUND(self):
            return self.getToken(ctx2lParser.POUND, 0)

        def identifier(self):
            return self.getTypedRuleContext(ctx2lParser.IdentifierContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_labeledAlt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabeledAlt" ):
                return visitor.visitLabeledAlt(self)
            else:
                return visitor.visitChildren(self)




    def labeledAlt(self):

        localctx = ctx2lParser.LabeledAltContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_labeledAlt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self.alternative()
            self.state = 517
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==51:
                self.state = 515
                self.match(ctx2lParser.POUND)
                self.state = 516
                self.identifier()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LexerRuleSpecContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TOKEN_REF(self):
            return self.getToken(ctx2lParser.TOKEN_REF, 0)

        def COLON(self):
            return self.getToken(ctx2lParser.COLON, 0)

        def lexerRuleBlock(self):
            return self.getTypedRuleContext(ctx2lParser.LexerRuleBlockContext,0)


        def SEMI(self):
            return self.getToken(ctx2lParser.SEMI, 0)

        def FRAGMENT(self):
            return self.getToken(ctx2lParser.FRAGMENT, 0)

        def optionsSpec(self):
            return self.getTypedRuleContext(ctx2lParser.OptionsSpecContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_lexerRuleSpec

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexerRuleSpec" ):
                return visitor.visitLexerRuleSpec(self)
            else:
                return visitor.visitChildren(self)




    def lexerRuleSpec(self):

        localctx = ctx2lParser.LexerRuleSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_lexerRuleSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 519
                self.match(ctx2lParser.FRAGMENT)


            self.state = 522
            self.match(ctx2lParser.TOKEN_REF)
            self.state = 524
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 523
                self.optionsSpec()


            self.state = 526
            self.match(ctx2lParser.COLON)
            self.state = 527
            self.lexerRuleBlock()
            self.state = 528
            self.match(ctx2lParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LexerRuleBlockContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lexerAltList(self):
            return self.getTypedRuleContext(ctx2lParser.LexerAltListContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_lexerRuleBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexerRuleBlock" ):
                return visitor.visitLexerRuleBlock(self)
            else:
                return visitor.visitChildren(self)




    def lexerRuleBlock(self):

        localctx = ctx2lParser.LexerRuleBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_lexerRuleBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
            self.lexerAltList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LexerAltListContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lexerAlt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.LexerAltContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.LexerAltContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(ctx2lParser.OR)
            else:
                return self.getToken(ctx2lParser.OR, i)

        def getRuleIndex(self):
            return ctx2lParser.RULE_lexerAltList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexerAltList" ):
                return visitor.visitLexerAltList(self)
            else:
                return visitor.visitChildren(self)




    def lexerAltList(self):

        localctx = ctx2lParser.LexerAltListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_lexerAltList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 532
            self.lexerAlt()
            self.state = 537
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 533
                self.match(ctx2lParser.OR)
                self.state = 534
                self.lexerAlt()
                self.state = 539
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LexerAltContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lexerElements(self):
            return self.getTypedRuleContext(ctx2lParser.LexerElementsContext,0)


        def lexerCommands(self):
            return self.getTypedRuleContext(ctx2lParser.LexerCommandsContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_lexerAlt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexerAlt" ):
                return visitor.visitLexerAlt(self)
            else:
                return visitor.visitChildren(self)




    def lexerAlt(self):

        localctx = ctx2lParser.LexerAltContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_lexerAlt)
        self._la = 0 # Token type
        try:
            self.state = 545
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 540
                self.lexerElements()
                self.state = 542
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==38:
                    self.state = 541
                    self.lexerCommands()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LexerElementsContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lexerElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.LexerElementContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.LexerElementContext,i)


        def getRuleIndex(self):
            return ctx2lParser.RULE_lexerElements

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexerElements" ):
                return visitor.visitLexerElements(self)
            else:
                return visitor.visitChildren(self)




    def lexerElements(self):

        localctx = ctx2lParser.LexerElementsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_lexerElements)
        self._la = 0 # Token type
        try:
            self.state = 553
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 11, 14, 36, 49, 52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 548 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 547
                    self.lexerElement()
                    self.state = 550 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 5066618300286990) != 0)):
                        break

                pass
            elif token in [35, 37, 38, 46]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LexerElementContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def labeledLexerElement(self):
            return self.getTypedRuleContext(ctx2lParser.LabeledLexerElementContext,0)


        def ebnfSuffix(self):
            return self.getTypedRuleContext(ctx2lParser.EbnfSuffixContext,0)


        def lexerAtom(self):
            return self.getTypedRuleContext(ctx2lParser.LexerAtomContext,0)


        def lexerBlock(self):
            return self.getTypedRuleContext(ctx2lParser.LexerBlockContext,0)


        def actionBlock(self):
            return self.getTypedRuleContext(ctx2lParser.ActionBlockContext,0)


        def QUESTION(self):
            return self.getToken(ctx2lParser.QUESTION, 0)

        def getRuleIndex(self):
            return ctx2lParser.RULE_lexerElement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexerElement" ):
                return visitor.visitLexerElement(self)
            else:
                return visitor.visitChildren(self)




    def lexerElement(self):

        localctx = ctx2lParser.LexerElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_lexerElement)
        self._la = 0 # Token type
        try:
            self.state = 571
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 555
                self.labeledLexerElement()
                self.state = 557
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 48378511622144) != 0):
                    self.state = 556
                    self.ebnfSuffix()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 559
                self.lexerAtom()
                self.state = 561
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 48378511622144) != 0):
                    self.state = 560
                    self.ebnfSuffix()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 563
                self.lexerBlock()
                self.state = 565
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 48378511622144) != 0):
                    self.state = 564
                    self.ebnfSuffix()


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 567
                self.actionBlock()
                self.state = 569
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==42:
                    self.state = 568
                    self.match(ctx2lParser.QUESTION)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabeledLexerElementContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(ctx2lParser.IdentifierContext,0)


        def ASSIGN(self):
            return self.getToken(ctx2lParser.ASSIGN, 0)

        def PLUS_ASSIGN(self):
            return self.getToken(ctx2lParser.PLUS_ASSIGN, 0)

        def lexerAtom(self):
            return self.getTypedRuleContext(ctx2lParser.LexerAtomContext,0)


        def lexerBlock(self):
            return self.getTypedRuleContext(ctx2lParser.LexerBlockContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_labeledLexerElement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabeledLexerElement" ):
                return visitor.visitLabeledLexerElement(self)
            else:
                return visitor.visitChildren(self)




    def labeledLexerElement(self):

        localctx = ctx2lParser.LabeledLexerElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_labeledLexerElement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 573
            self.identifier()
            self.state = 574
            _la = self._input.LA(1)
            if not(_la==41 or _la==44):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 577
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 11, 49, 52]:
                self.state = 575
                self.lexerAtom()
                pass
            elif token in [36]:
                self.state = 576
                self.lexerBlock()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LexerBlockContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ctx2lParser.LPAREN, 0)

        def lexerAltList(self):
            return self.getTypedRuleContext(ctx2lParser.LexerAltListContext,0)


        def RPAREN(self):
            return self.getToken(ctx2lParser.RPAREN, 0)

        def getRuleIndex(self):
            return ctx2lParser.RULE_lexerBlock

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexerBlock" ):
                return visitor.visitLexerBlock(self)
            else:
                return visitor.visitChildren(self)




    def lexerBlock(self):

        localctx = ctx2lParser.LexerBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_lexerBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 579
            self.match(ctx2lParser.LPAREN)
            self.state = 580
            self.lexerAltList()
            self.state = 581
            self.match(ctx2lParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LexerCommandsContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RARROW(self):
            return self.getToken(ctx2lParser.RARROW, 0)

        def lexerCommand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.LexerCommandContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.LexerCommandContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ctx2lParser.COMMA)
            else:
                return self.getToken(ctx2lParser.COMMA, i)

        def getRuleIndex(self):
            return ctx2lParser.RULE_lexerCommands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexerCommands" ):
                return visitor.visitLexerCommands(self)
            else:
                return visitor.visitChildren(self)




    def lexerCommands(self):

        localctx = ctx2lParser.LexerCommandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_lexerCommands)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 583
            self.match(ctx2lParser.RARROW)
            self.state = 584
            self.lexerCommand()
            self.state = 589
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 585
                self.match(ctx2lParser.COMMA)
                self.state = 586
                self.lexerCommand()
                self.state = 591
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LexerCommandContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lexerCommandName(self):
            return self.getTypedRuleContext(ctx2lParser.LexerCommandNameContext,0)


        def LPAREN(self):
            return self.getToken(ctx2lParser.LPAREN, 0)

        def lexerCommandExpr(self):
            return self.getTypedRuleContext(ctx2lParser.LexerCommandExprContext,0)


        def RPAREN(self):
            return self.getToken(ctx2lParser.RPAREN, 0)

        def getRuleIndex(self):
            return ctx2lParser.RULE_lexerCommand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexerCommand" ):
                return visitor.visitLexerCommand(self)
            else:
                return visitor.visitChildren(self)




    def lexerCommand(self):

        localctx = ctx2lParser.LexerCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_lexerCommand)
        try:
            self.state = 598
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 592
                self.lexerCommandName()
                self.state = 593
                self.match(ctx2lParser.LPAREN)
                self.state = 594
                self.lexerCommandExpr()
                self.state = 595
                self.match(ctx2lParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 597
                self.lexerCommandName()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LexerCommandNameContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(ctx2lParser.IdentifierContext,0)


        def MODE(self):
            return self.getToken(ctx2lParser.MODE, 0)

        def getRuleIndex(self):
            return ctx2lParser.RULE_lexerCommandName

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexerCommandName" ):
                return visitor.visitLexerCommandName(self)
            else:
                return visitor.visitChildren(self)




    def lexerCommandName(self):

        localctx = ctx2lParser.LexerCommandNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_lexerCommandName)
        try:
            self.state = 602
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 600
                self.identifier()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 601
                self.match(ctx2lParser.MODE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LexerCommandExprContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(ctx2lParser.IdentifierContext,0)


        def INT(self):
            return self.getToken(ctx2lParser.INT, 0)

        def getRuleIndex(self):
            return ctx2lParser.RULE_lexerCommandExpr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexerCommandExpr" ):
                return visitor.visitLexerCommandExpr(self)
            else:
                return visitor.visitChildren(self)




    def lexerCommandExpr(self):

        localctx = ctx2lParser.LexerCommandExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_lexerCommandExpr)
        try:
            self.state = 606
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 604
                self.identifier()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 605
                self.match(ctx2lParser.INT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AltListContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def alternative(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.AlternativeContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.AlternativeContext,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(ctx2lParser.OR)
            else:
                return self.getToken(ctx2lParser.OR, i)

        def getRuleIndex(self):
            return ctx2lParser.RULE_altList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAltList" ):
                return visitor.visitAltList(self)
            else:
                return visitor.visitChildren(self)




    def altList(self):

        localctx = ctx2lParser.AltListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_altList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 608
            self.alternative()
            self.state = 613
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 609
                self.match(ctx2lParser.OR)
                self.state = 610
                self.alternative()
                self.state = 615
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AlternativeContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def elementOptions(self):
            return self.getTypedRuleContext(ctx2lParser.ElementOptionsContext,0)


        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.ElementContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.ElementContext,i)


        def getRuleIndex(self):
            return ctx2lParser.RULE_alternative

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlternative" ):
                return visitor.visitAlternative(self)
            else:
                return visitor.visitChildren(self)




    def alternative(self):

        localctx = ctx2lParser.AlternativeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_alternative)
        self._la = 0 # Token type
        try:
            self.state = 625
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 11, 14, 36, 39, 49, 52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 617
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 616
                    self.elementOptions()


                self.state = 620 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 619
                    self.element()
                    self.state = 622 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 5066618300286982) != 0)):
                        break

                pass
            elif token in [35, 37, 46, 51]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def labeledElement(self):
            return self.getTypedRuleContext(ctx2lParser.LabeledElementContext,0)


        def ebnfSuffix(self):
            return self.getTypedRuleContext(ctx2lParser.EbnfSuffixContext,0)


        def atom(self):
            return self.getTypedRuleContext(ctx2lParser.AtomContext,0)


        def ebnf(self):
            return self.getTypedRuleContext(ctx2lParser.EbnfContext,0)


        def actionBlock(self):
            return self.getTypedRuleContext(ctx2lParser.ActionBlockContext,0)


        def QUESTION(self):
            return self.getToken(ctx2lParser.QUESTION, 0)

        def getRuleIndex(self):
            return ctx2lParser.RULE_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = ctx2lParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_element)
        self._la = 0 # Token type
        try:
            self.state = 642
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,74,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 627
                self.labeledElement()
                self.state = 630
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [42, 43, 45]:
                    self.state = 628
                    self.ebnfSuffix()
                    pass
                elif token in [1, 2, 11, 14, 35, 36, 37, 46, 49, 51, 52]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 632
                self.atom()
                self.state = 635
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [42, 43, 45]:
                    self.state = 633
                    self.ebnfSuffix()
                    pass
                elif token in [1, 2, 11, 14, 35, 36, 37, 46, 49, 51, 52]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 637
                self.ebnf()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 638
                self.actionBlock()
                self.state = 640
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==42:
                    self.state = 639
                    self.match(ctx2lParser.QUESTION)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LabeledElementContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(ctx2lParser.IdentifierContext,0)


        def ASSIGN(self):
            return self.getToken(ctx2lParser.ASSIGN, 0)

        def PLUS_ASSIGN(self):
            return self.getToken(ctx2lParser.PLUS_ASSIGN, 0)

        def atom(self):
            return self.getTypedRuleContext(ctx2lParser.AtomContext,0)


        def block(self):
            return self.getTypedRuleContext(ctx2lParser.BlockContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_labeledElement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabeledElement" ):
                return visitor.visitLabeledElement(self)
            else:
                return visitor.visitChildren(self)




    def labeledElement(self):

        localctx = ctx2lParser.LabeledElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_labeledElement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 644
            self.identifier()
            self.state = 645
            _la = self._input.LA(1)
            if not(_la==41 or _la==44):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 648
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 11, 49, 52]:
                self.state = 646
                self.atom()
                pass
            elif token in [36]:
                self.state = 647
                self.block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EbnfContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(ctx2lParser.BlockContext,0)


        def blockSuffix(self):
            return self.getTypedRuleContext(ctx2lParser.BlockSuffixContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_ebnf

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEbnf" ):
                return visitor.visitEbnf(self)
            else:
                return visitor.visitChildren(self)




    def ebnf(self):

        localctx = ctx2lParser.EbnfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_ebnf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 650
            self.block()
            self.state = 652
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 48378511622144) != 0):
                self.state = 651
                self.blockSuffix()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockSuffixContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ebnfSuffix(self):
            return self.getTypedRuleContext(ctx2lParser.EbnfSuffixContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_blockSuffix

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockSuffix" ):
                return visitor.visitBlockSuffix(self)
            else:
                return visitor.visitChildren(self)




    def blockSuffix(self):

        localctx = ctx2lParser.BlockSuffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_blockSuffix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 654
            self.ebnfSuffix()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EbnfSuffixContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUESTION(self, i:int=None):
            if i is None:
                return self.getTokens(ctx2lParser.QUESTION)
            else:
                return self.getToken(ctx2lParser.QUESTION, i)

        def STAR(self):
            return self.getToken(ctx2lParser.STAR, 0)

        def PLUS(self):
            return self.getToken(ctx2lParser.PLUS, 0)

        def getRuleIndex(self):
            return ctx2lParser.RULE_ebnfSuffix

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEbnfSuffix" ):
                return visitor.visitEbnfSuffix(self)
            else:
                return visitor.visitChildren(self)




    def ebnfSuffix(self):

        localctx = ctx2lParser.EbnfSuffixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_ebnfSuffix)
        self._la = 0 # Token type
        try:
            self.state = 668
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 656
                self.match(ctx2lParser.QUESTION)
                self.state = 658
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==42:
                    self.state = 657
                    self.match(ctx2lParser.QUESTION)


                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 660
                self.match(ctx2lParser.STAR)
                self.state = 662
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==42:
                    self.state = 661
                    self.match(ctx2lParser.QUESTION)


                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 3)
                self.state = 664
                self.match(ctx2lParser.PLUS)
                self.state = 666
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==42:
                    self.state = 665
                    self.match(ctx2lParser.QUESTION)


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LexerAtomContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def characterRange(self):
            return self.getTypedRuleContext(ctx2lParser.CharacterRangeContext,0)


        def terminal(self):
            return self.getTypedRuleContext(ctx2lParser.TerminalContext,0)


        def notSet(self):
            return self.getTypedRuleContext(ctx2lParser.NotSetContext,0)


        def LEXER_CHAR_SET(self):
            return self.getToken(ctx2lParser.LEXER_CHAR_SET, 0)

        def DOT(self):
            return self.getToken(ctx2lParser.DOT, 0)

        def elementOptions(self):
            return self.getTypedRuleContext(ctx2lParser.ElementOptionsContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_lexerAtom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLexerAtom" ):
                return visitor.visitLexerAtom(self)
            else:
                return visitor.visitChildren(self)




    def lexerAtom(self):

        localctx = ctx2lParser.LexerAtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_lexerAtom)
        self._la = 0 # Token type
        try:
            self.state = 678
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,82,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 670
                self.characterRange()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 671
                self.terminal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 672
                self.notSet()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 673
                self.match(ctx2lParser.LEXER_CHAR_SET)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 674
                self.match(ctx2lParser.DOT)
                self.state = 676
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 675
                    self.elementOptions()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def terminal(self):
            return self.getTypedRuleContext(ctx2lParser.TerminalContext,0)


        def ruleref(self):
            return self.getTypedRuleContext(ctx2lParser.RulerefContext,0)


        def notSet(self):
            return self.getTypedRuleContext(ctx2lParser.NotSetContext,0)


        def DOT(self):
            return self.getToken(ctx2lParser.DOT, 0)

        def elementOptions(self):
            return self.getTypedRuleContext(ctx2lParser.ElementOptionsContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_atom

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = ctx2lParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 687
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 680
                self.terminal()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 681
                self.ruleref()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 3)
                self.state = 682
                self.notSet()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 4)
                self.state = 683
                self.match(ctx2lParser.DOT)
                self.state = 685
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 684
                    self.elementOptions()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NotSetContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(ctx2lParser.NOT, 0)

        def setElement(self):
            return self.getTypedRuleContext(ctx2lParser.SetElementContext,0)


        def blockSet(self):
            return self.getTypedRuleContext(ctx2lParser.BlockSetContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_notSet

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotSet" ):
                return visitor.visitNotSet(self)
            else:
                return visitor.visitChildren(self)




    def notSet(self):

        localctx = ctx2lParser.NotSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_notSet)
        try:
            self.state = 693
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,85,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 689
                self.match(ctx2lParser.NOT)
                self.state = 690
                self.setElement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 691
                self.match(ctx2lParser.NOT)
                self.state = 692
                self.blockSet()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockSetContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ctx2lParser.LPAREN, 0)

        def setElement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.SetElementContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.SetElementContext,i)


        def RPAREN(self):
            return self.getToken(ctx2lParser.RPAREN, 0)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(ctx2lParser.OR)
            else:
                return self.getToken(ctx2lParser.OR, i)

        def getRuleIndex(self):
            return ctx2lParser.RULE_blockSet

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockSet" ):
                return visitor.visitBlockSet(self)
            else:
                return visitor.visitChildren(self)




    def blockSet(self):

        localctx = ctx2lParser.BlockSetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_blockSet)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 695
            self.match(ctx2lParser.LPAREN)
            self.state = 696
            self.setElement()
            self.state = 701
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 697
                self.match(ctx2lParser.OR)
                self.state = 698
                self.setElement()
                self.state = 703
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 704
            self.match(ctx2lParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetElementContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TOKEN_REF(self):
            return self.getToken(ctx2lParser.TOKEN_REF, 0)

        def elementOptions(self):
            return self.getTypedRuleContext(ctx2lParser.ElementOptionsContext,0)


        def STRING_LITERAL(self):
            return self.getToken(ctx2lParser.STRING_LITERAL, 0)

        def characterRange(self):
            return self.getTypedRuleContext(ctx2lParser.CharacterRangeContext,0)


        def LEXER_CHAR_SET(self):
            return self.getToken(ctx2lParser.LEXER_CHAR_SET, 0)

        def getRuleIndex(self):
            return ctx2lParser.RULE_setElement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetElement" ):
                return visitor.visitSetElement(self)
            else:
                return visitor.visitChildren(self)




    def setElement(self):

        localctx = ctx2lParser.SetElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_setElement)
        self._la = 0 # Token type
        try:
            self.state = 716
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,89,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 706
                self.match(ctx2lParser.TOKEN_REF)
                self.state = 708
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 707
                    self.elementOptions()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 710
                self.match(ctx2lParser.STRING_LITERAL)
                self.state = 712
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 711
                    self.elementOptions()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 714
                self.characterRange()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 715
                self.match(ctx2lParser.LEXER_CHAR_SET)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(ctx2lParser.LPAREN, 0)

        def altList(self):
            return self.getTypedRuleContext(ctx2lParser.AltListContext,0)


        def RPAREN(self):
            return self.getToken(ctx2lParser.RPAREN, 0)

        def COLON(self):
            return self.getToken(ctx2lParser.COLON, 0)

        def optionsSpec(self):
            return self.getTypedRuleContext(ctx2lParser.OptionsSpecContext,0)


        def ruleAction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.RuleActionContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.RuleActionContext,i)


        def getRuleIndex(self):
            return ctx2lParser.RULE_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = ctx2lParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 718
            self.match(ctx2lParser.LPAREN)
            self.state = 729
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1125904201842688) != 0):
                self.state = 720
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 719
                    self.optionsSpec()


                self.state = 725
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==50:
                    self.state = 722
                    self.ruleAction()
                    self.state = 727
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 728
                self.match(ctx2lParser.COLON)


            self.state = 731
            self.altList()
            self.state = 732
            self.match(ctx2lParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RulerefContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RULE_REF(self):
            return self.getToken(ctx2lParser.RULE_REF, 0)

        def argActionBlock(self):
            return self.getTypedRuleContext(ctx2lParser.ArgActionBlockContext,0)


        def elementOptions(self):
            return self.getTypedRuleContext(ctx2lParser.ElementOptionsContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_ruleref

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRuleref" ):
                return visitor.visitRuleref(self)
            else:
                return visitor.visitChildren(self)




    def ruleref(self):

        localctx = ctx2lParser.RulerefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_ruleref)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 734
            self.match(ctx2lParser.RULE_REF)
            self.state = 736
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 735
                self.argActionBlock()


            self.state = 739
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 738
                self.elementOptions()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CharacterRangeContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(ctx2lParser.STRING_LITERAL)
            else:
                return self.getToken(ctx2lParser.STRING_LITERAL, i)

        def RANGE(self):
            return self.getToken(ctx2lParser.RANGE, 0)

        def getRuleIndex(self):
            return ctx2lParser.RULE_characterRange

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCharacterRange" ):
                return visitor.visitCharacterRange(self)
            else:
                return visitor.visitChildren(self)




    def characterRange(self):

        localctx = ctx2lParser.CharacterRangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_characterRange)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 741
            self.match(ctx2lParser.STRING_LITERAL)
            self.state = 742
            self.match(ctx2lParser.RANGE)
            self.state = 743
            self.match(ctx2lParser.STRING_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminalContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TOKEN_REF(self):
            return self.getToken(ctx2lParser.TOKEN_REF, 0)

        def elementOptions(self):
            return self.getTypedRuleContext(ctx2lParser.ElementOptionsContext,0)


        def STRING_LITERAL(self):
            return self.getToken(ctx2lParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return ctx2lParser.RULE_terminal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerminal" ):
                return visitor.visitTerminal(self)
            else:
                return visitor.visitChildren(self)




    def terminal(self):

        localctx = ctx2lParser.TerminalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_terminal)
        self._la = 0 # Token type
        try:
            self.state = 753
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 745
                self.match(ctx2lParser.TOKEN_REF)
                self.state = 747
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 746
                    self.elementOptions()


                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 749
                self.match(ctx2lParser.STRING_LITERAL)
                self.state = 751
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 750
                    self.elementOptions()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementOptionsContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(ctx2lParser.LT, 0)

        def elementOption(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.ElementOptionContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.ElementOptionContext,i)


        def GT(self):
            return self.getToken(ctx2lParser.GT, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(ctx2lParser.COMMA)
            else:
                return self.getToken(ctx2lParser.COMMA, i)

        def getRuleIndex(self):
            return ctx2lParser.RULE_elementOptions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementOptions" ):
                return visitor.visitElementOptions(self)
            else:
                return visitor.visitChildren(self)




    def elementOptions(self):

        localctx = ctx2lParser.ElementOptionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_elementOptions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 755
            self.match(ctx2lParser.LT)
            self.state = 756
            self.elementOption()
            self.state = 761
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 757
                self.match(ctx2lParser.COMMA)
                self.state = 758
                self.elementOption()
                self.state = 763
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 764
            self.match(ctx2lParser.GT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementOptionContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ctx2lParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(ctx2lParser.IdentifierContext,i)


        def ASSIGN(self):
            return self.getToken(ctx2lParser.ASSIGN, 0)

        def STRING_LITERAL(self):
            return self.getToken(ctx2lParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return ctx2lParser.RULE_elementOption

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementOption" ):
                return visitor.visitElementOption(self)
            else:
                return visitor.visitChildren(self)




    def elementOption(self):

        localctx = ctx2lParser.ElementOptionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_elementOption)
        try:
            self.state = 773
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,100,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 766
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 767
                self.identifier()
                self.state = 768
                self.match(ctx2lParser.ASSIGN)
                self.state = 771
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 2]:
                    self.state = 769
                    self.identifier()
                    pass
                elif token in [11]:
                    self.state = 770
                    self.match(ctx2lParser.STRING_LITERAL)
                    pass
                else:
                    raise NoViableAltException(self)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RULE_REF(self):
            return self.getToken(ctx2lParser.RULE_REF, 0)

        def TOKEN_REF(self):
            return self.getToken(ctx2lParser.TOKEN_REF, 0)

        def getRuleIndex(self):
            return ctx2lParser.RULE_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = ctx2lParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 775
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





