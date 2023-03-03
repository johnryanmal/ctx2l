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
        4,1,62,800,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
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
        2,79,7,79,2,80,7,80,2,81,7,81,2,82,7,82,2,83,7,83,2,84,7,84,2,85,
        7,85,1,0,1,0,4,0,175,8,0,11,0,12,0,176,1,0,1,0,1,1,1,1,1,1,3,1,184,
        8,1,1,1,1,1,1,2,1,2,1,2,3,2,191,8,2,1,2,1,2,1,3,1,3,3,3,197,8,3,
        1,3,1,3,1,3,1,4,1,4,3,4,204,8,4,1,4,1,4,1,4,1,5,1,5,1,5,5,5,212,
        8,5,10,5,12,5,215,9,5,1,6,1,6,1,6,5,6,220,8,6,10,6,12,6,223,9,6,
        1,7,4,7,226,8,7,11,7,12,7,227,1,7,1,7,3,7,232,8,7,1,8,4,8,235,8,
        8,11,8,12,8,236,1,9,3,9,240,8,9,1,9,1,9,3,9,244,8,9,1,10,1,10,1,
        10,3,10,249,8,10,1,11,1,11,1,12,1,12,1,13,3,13,256,8,13,1,13,1,13,
        3,13,260,8,13,1,14,1,14,3,14,264,8,14,1,14,1,14,1,15,1,15,1,15,5,
        15,271,8,15,10,15,12,15,274,9,15,1,15,3,15,277,8,15,1,16,3,16,280,
        8,16,1,16,1,16,3,16,284,8,16,1,17,1,17,1,17,3,17,289,8,17,1,18,1,
        18,1,19,1,19,1,20,1,20,1,20,1,21,1,21,1,22,1,22,5,22,302,8,22,10,
        22,12,22,305,9,22,1,22,1,22,5,22,309,8,22,10,22,12,22,312,9,22,1,
        22,1,22,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,3,24,325,8,
        24,1,25,1,25,1,25,1,25,1,25,3,25,332,8,25,1,26,1,26,1,26,1,26,5,
        26,338,8,26,10,26,12,26,341,9,26,1,26,1,26,1,27,1,27,1,27,1,27,1,
        28,1,28,1,28,5,28,352,8,28,10,28,12,28,355,9,28,1,28,1,28,1,28,3,
        28,360,8,28,1,29,1,29,1,29,1,29,5,29,366,8,29,10,29,12,29,369,9,
        29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,3,30,378,8,30,1,31,1,31,3,
        31,382,8,31,1,31,1,31,1,32,1,32,3,32,388,8,32,1,32,1,32,1,33,1,33,
        1,33,5,33,395,8,33,10,33,12,33,398,9,33,1,33,3,33,401,8,33,1,34,
        1,34,1,34,1,34,3,34,407,8,34,1,34,1,34,1,34,1,35,1,35,1,35,3,35,
        415,8,35,1,36,1,36,5,36,419,8,36,10,36,12,36,422,9,36,1,36,1,36,
        1,37,1,37,5,37,428,8,37,10,37,12,37,431,9,37,1,37,1,37,1,38,1,38,
        1,38,1,38,5,38,439,8,38,10,38,12,38,442,9,38,1,39,5,39,445,8,39,
        10,39,12,39,448,9,39,1,40,1,40,3,40,452,8,40,1,41,3,41,455,8,41,
        1,41,1,41,3,41,459,8,41,1,41,3,41,462,8,41,1,41,3,41,465,8,41,1,
        41,3,41,468,8,41,1,41,5,41,471,8,41,10,41,12,41,474,9,41,1,41,1,
        41,1,41,1,41,1,41,1,42,5,42,482,8,42,10,42,12,42,485,9,42,1,42,3,
        42,488,8,42,1,43,1,43,1,43,1,43,1,44,1,44,1,44,1,45,1,45,3,45,499,
        8,45,1,46,1,46,1,46,1,47,1,47,1,47,1,47,5,47,508,8,47,10,47,12,47,
        511,9,47,1,48,1,48,1,48,1,49,1,49,1,49,1,49,1,50,4,50,521,8,50,11,
        50,12,50,522,1,51,1,51,1,52,1,52,1,53,1,53,1,53,5,53,532,8,53,10,
        53,12,53,535,9,53,1,54,1,54,1,54,3,54,540,8,54,1,55,3,55,543,8,55,
        1,55,1,55,3,55,547,8,55,1,55,1,55,1,55,1,55,1,56,1,56,1,57,1,57,
        1,57,5,57,558,8,57,10,57,12,57,561,9,57,1,58,1,58,3,58,565,8,58,
        1,58,3,58,568,8,58,1,59,4,59,571,8,59,11,59,12,59,572,1,59,3,59,
        576,8,59,1,60,1,60,3,60,580,8,60,1,60,1,60,3,60,584,8,60,1,60,1,
        60,3,60,588,8,60,1,60,1,60,3,60,592,8,60,3,60,594,8,60,1,61,1,61,
        1,61,1,61,3,61,600,8,61,1,62,1,62,1,62,1,62,1,63,1,63,1,63,1,63,
        5,63,610,8,63,10,63,12,63,613,9,63,1,64,1,64,1,64,1,64,1,64,1,64,
        3,64,621,8,64,1,65,1,65,3,65,625,8,65,1,66,1,66,3,66,629,8,66,1,
        67,1,67,1,67,5,67,634,8,67,10,67,12,67,637,9,67,1,68,3,68,640,8,
        68,1,68,4,68,643,8,68,11,68,12,68,644,1,68,3,68,648,8,68,1,69,1,
        69,1,69,3,69,653,8,69,1,69,1,69,1,69,3,69,658,8,69,1,69,1,69,1,69,
        3,69,663,8,69,3,69,665,8,69,1,70,1,70,1,70,1,70,3,70,671,8,70,1,
        71,1,71,3,71,675,8,71,1,72,1,72,1,73,1,73,3,73,681,8,73,1,73,1,73,
        3,73,685,8,73,1,73,1,73,3,73,689,8,73,3,73,691,8,73,1,74,1,74,1,
        74,1,74,1,74,1,74,3,74,699,8,74,3,74,701,8,74,1,75,1,75,1,75,1,75,
        1,75,3,75,708,8,75,3,75,710,8,75,1,76,1,76,1,76,1,76,3,76,716,8,
        76,1,77,1,77,1,77,1,77,5,77,722,8,77,10,77,12,77,725,9,77,1,77,1,
        77,1,78,1,78,3,78,731,8,78,1,78,1,78,3,78,735,8,78,1,78,1,78,3,78,
        739,8,78,1,79,1,79,3,79,743,8,79,1,79,5,79,746,8,79,10,79,12,79,
        749,9,79,1,79,3,79,752,8,79,1,79,1,79,1,79,1,80,1,80,3,80,759,8,
        80,1,80,3,80,762,8,80,1,81,1,81,1,81,1,81,1,82,1,82,3,82,770,8,82,
        1,82,1,82,3,82,774,8,82,3,82,776,8,82,1,83,1,83,1,83,1,83,5,83,782,
        8,83,10,83,12,83,785,9,83,1,83,1,83,1,84,1,84,1,84,1,84,1,84,3,84,
        794,8,84,3,84,796,8,84,1,85,1,85,1,85,0,0,86,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,
        60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,
        102,104,106,108,110,112,114,116,118,120,122,124,126,128,130,132,
        134,136,138,140,142,144,146,148,150,152,154,156,158,160,162,164,
        166,168,170,0,4,1,0,1,2,2,0,3,3,11,11,2,0,41,41,44,44,2,0,19,19,
        23,25,840,0,174,1,0,0,0,2,180,1,0,0,0,4,187,1,0,0,0,6,194,1,0,0,
        0,8,201,1,0,0,0,10,208,1,0,0,0,12,216,1,0,0,0,14,225,1,0,0,0,16,
        234,1,0,0,0,18,239,1,0,0,0,20,248,1,0,0,0,22,250,1,0,0,0,24,252,
        1,0,0,0,26,255,1,0,0,0,28,261,1,0,0,0,30,267,1,0,0,0,32,279,1,0,
        0,0,34,288,1,0,0,0,36,290,1,0,0,0,38,292,1,0,0,0,40,294,1,0,0,0,
        42,297,1,0,0,0,44,299,1,0,0,0,46,315,1,0,0,0,48,324,1,0,0,0,50,331,
        1,0,0,0,52,333,1,0,0,0,54,344,1,0,0,0,56,359,1,0,0,0,58,361,1,0,
        0,0,60,377,1,0,0,0,62,379,1,0,0,0,64,385,1,0,0,0,66,391,1,0,0,0,
        68,402,1,0,0,0,70,414,1,0,0,0,72,416,1,0,0,0,74,425,1,0,0,0,76,434,
        1,0,0,0,78,446,1,0,0,0,80,451,1,0,0,0,82,454,1,0,0,0,84,483,1,0,
        0,0,86,489,1,0,0,0,88,493,1,0,0,0,90,498,1,0,0,0,92,500,1,0,0,0,
        94,503,1,0,0,0,96,512,1,0,0,0,98,515,1,0,0,0,100,520,1,0,0,0,102,
        524,1,0,0,0,104,526,1,0,0,0,106,528,1,0,0,0,108,536,1,0,0,0,110,
        542,1,0,0,0,112,552,1,0,0,0,114,554,1,0,0,0,116,567,1,0,0,0,118,
        575,1,0,0,0,120,593,1,0,0,0,122,595,1,0,0,0,124,601,1,0,0,0,126,
        605,1,0,0,0,128,620,1,0,0,0,130,624,1,0,0,0,132,628,1,0,0,0,134,
        630,1,0,0,0,136,647,1,0,0,0,138,664,1,0,0,0,140,666,1,0,0,0,142,
        672,1,0,0,0,144,676,1,0,0,0,146,690,1,0,0,0,148,700,1,0,0,0,150,
        709,1,0,0,0,152,715,1,0,0,0,154,717,1,0,0,0,156,738,1,0,0,0,158,
        740,1,0,0,0,160,756,1,0,0,0,162,763,1,0,0,0,164,775,1,0,0,0,166,
        777,1,0,0,0,168,795,1,0,0,0,170,797,1,0,0,0,172,175,3,2,1,0,173,
        175,3,4,2,0,174,172,1,0,0,0,174,173,1,0,0,0,175,176,1,0,0,0,176,
        174,1,0,0,0,176,177,1,0,0,0,177,178,1,0,0,0,178,179,5,0,0,1,179,
        1,1,0,0,0,180,181,5,2,0,0,181,183,5,32,0,0,182,184,5,46,0,0,183,
        182,1,0,0,0,183,184,1,0,0,0,184,185,1,0,0,0,185,186,3,10,5,0,186,
        3,1,0,0,0,187,188,5,1,0,0,188,190,5,32,0,0,189,191,5,46,0,0,190,
        189,1,0,0,0,190,191,1,0,0,0,191,192,1,0,0,0,192,193,3,12,6,0,193,
        5,1,0,0,0,194,196,5,36,0,0,195,197,5,46,0,0,196,195,1,0,0,0,196,
        197,1,0,0,0,197,198,1,0,0,0,198,199,3,10,5,0,199,200,5,37,0,0,200,
        7,1,0,0,0,201,203,5,36,0,0,202,204,5,46,0,0,203,202,1,0,0,0,203,
        204,1,0,0,0,204,205,1,0,0,0,205,206,3,12,6,0,206,207,5,37,0,0,207,
        9,1,0,0,0,208,213,3,14,7,0,209,210,5,46,0,0,210,212,3,14,7,0,211,
        209,1,0,0,0,212,215,1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,
        11,1,0,0,0,215,213,1,0,0,0,216,221,3,16,8,0,217,218,5,46,0,0,218,
        220,3,16,8,0,219,217,1,0,0,0,220,223,1,0,0,0,221,219,1,0,0,0,221,
        222,1,0,0,0,222,13,1,0,0,0,223,221,1,0,0,0,224,226,3,18,9,0,225,
        224,1,0,0,0,226,227,1,0,0,0,227,225,1,0,0,0,227,228,1,0,0,0,228,
        231,1,0,0,0,229,230,5,6,0,0,230,232,3,26,13,0,231,229,1,0,0,0,231,
        232,1,0,0,0,232,15,1,0,0,0,233,235,3,32,16,0,234,233,1,0,0,0,235,
        236,1,0,0,0,236,234,1,0,0,0,236,237,1,0,0,0,237,17,1,0,0,0,238,240,
        3,40,20,0,239,238,1,0,0,0,239,240,1,0,0,0,240,241,1,0,0,0,241,243,
        3,20,10,0,242,244,3,146,73,0,243,242,1,0,0,0,243,244,1,0,0,0,244,
        19,1,0,0,0,245,249,3,6,3,0,246,249,3,22,11,0,247,249,3,24,12,0,248,
        245,1,0,0,0,248,246,1,0,0,0,248,247,1,0,0,0,249,21,1,0,0,0,250,251,
        7,0,0,0,251,23,1,0,0,0,252,253,5,11,0,0,253,25,1,0,0,0,254,256,5,
        47,0,0,255,254,1,0,0,0,255,256,1,0,0,0,256,257,1,0,0,0,257,259,3,
        170,85,0,258,260,3,28,14,0,259,258,1,0,0,0,259,260,1,0,0,0,260,27,
        1,0,0,0,261,263,5,36,0,0,262,264,3,30,15,0,263,262,1,0,0,0,263,264,
        1,0,0,0,264,265,1,0,0,0,265,266,5,37,0,0,266,29,1,0,0,0,267,272,
        3,26,13,0,268,269,5,34,0,0,269,271,3,26,13,0,270,268,1,0,0,0,271,
        274,1,0,0,0,272,270,1,0,0,0,272,273,1,0,0,0,273,276,1,0,0,0,274,
        272,1,0,0,0,275,277,5,34,0,0,276,275,1,0,0,0,276,277,1,0,0,0,277,
        31,1,0,0,0,278,280,3,40,20,0,279,278,1,0,0,0,279,280,1,0,0,0,280,
        281,1,0,0,0,281,283,3,34,17,0,282,284,3,146,73,0,283,282,1,0,0,0,
        283,284,1,0,0,0,284,33,1,0,0,0,285,289,3,8,4,0,286,289,3,36,18,0,
        287,289,3,38,19,0,288,285,1,0,0,0,288,286,1,0,0,0,288,287,1,0,0,
        0,289,35,1,0,0,0,290,291,5,1,0,0,291,37,1,0,0,0,292,293,7,1,0,0,
        293,39,1,0,0,0,294,295,3,170,85,0,295,296,3,42,21,0,296,41,1,0,0,
        0,297,298,7,2,0,0,298,43,1,0,0,0,299,303,3,46,23,0,300,302,3,50,
        25,0,301,300,1,0,0,0,302,305,1,0,0,0,303,301,1,0,0,0,303,304,1,0,
        0,0,304,306,1,0,0,0,305,303,1,0,0,0,306,310,3,78,39,0,307,309,3,
        76,38,0,308,307,1,0,0,0,309,312,1,0,0,0,310,308,1,0,0,0,310,311,
        1,0,0,0,311,313,1,0,0,0,312,310,1,0,0,0,313,314,5,0,0,1,314,45,1,
        0,0,0,315,316,3,48,24,0,316,317,3,170,85,0,317,318,5,35,0,0,318,
        47,1,0,0,0,319,320,5,20,0,0,320,325,5,22,0,0,321,322,5,21,0,0,322,
        325,5,22,0,0,323,325,5,22,0,0,324,319,1,0,0,0,324,321,1,0,0,0,324,
        323,1,0,0,0,325,49,1,0,0,0,326,332,3,52,26,0,327,332,3,58,29,0,328,
        332,3,62,31,0,329,332,3,64,32,0,330,332,3,68,34,0,331,326,1,0,0,
        0,331,327,1,0,0,0,331,328,1,0,0,0,331,329,1,0,0,0,331,330,1,0,0,
        0,332,51,1,0,0,0,333,339,5,15,0,0,334,335,3,54,27,0,335,336,5,35,
        0,0,336,338,1,0,0,0,337,334,1,0,0,0,338,341,1,0,0,0,339,337,1,0,
        0,0,339,340,1,0,0,0,340,342,1,0,0,0,341,339,1,0,0,0,342,343,5,5,
        0,0,343,53,1,0,0,0,344,345,3,170,85,0,345,346,5,41,0,0,346,347,3,
        56,28,0,347,55,1,0,0,0,348,353,3,170,85,0,349,350,5,49,0,0,350,352,
        3,170,85,0,351,349,1,0,0,0,352,355,1,0,0,0,353,351,1,0,0,0,353,354,
        1,0,0,0,354,360,1,0,0,0,355,353,1,0,0,0,356,360,5,11,0,0,357,360,
        3,72,36,0,358,360,5,10,0,0,359,348,1,0,0,0,359,356,1,0,0,0,359,357,
        1,0,0,0,359,358,1,0,0,0,360,57,1,0,0,0,361,362,5,18,0,0,362,367,
        3,60,30,0,363,364,5,34,0,0,364,366,3,60,30,0,365,363,1,0,0,0,366,
        369,1,0,0,0,367,365,1,0,0,0,367,368,1,0,0,0,368,370,1,0,0,0,369,
        367,1,0,0,0,370,371,5,35,0,0,371,59,1,0,0,0,372,373,3,170,85,0,373,
        374,5,41,0,0,374,375,3,170,85,0,375,378,1,0,0,0,376,378,3,170,85,
        0,377,372,1,0,0,0,377,376,1,0,0,0,378,61,1,0,0,0,379,381,5,16,0,
        0,380,382,3,66,33,0,381,380,1,0,0,0,381,382,1,0,0,0,382,383,1,0,
        0,0,383,384,5,5,0,0,384,63,1,0,0,0,385,387,5,17,0,0,386,388,3,66,
        33,0,387,386,1,0,0,0,387,388,1,0,0,0,388,389,1,0,0,0,389,390,5,5,
        0,0,390,65,1,0,0,0,391,396,3,170,85,0,392,393,5,34,0,0,393,395,3,
        170,85,0,394,392,1,0,0,0,395,398,1,0,0,0,396,394,1,0,0,0,396,397,
        1,0,0,0,397,400,1,0,0,0,398,396,1,0,0,0,399,401,5,34,0,0,400,399,
        1,0,0,0,400,401,1,0,0,0,401,67,1,0,0,0,402,406,5,50,0,0,403,404,
        3,70,35,0,404,405,5,33,0,0,405,407,1,0,0,0,406,403,1,0,0,0,406,407,
        1,0,0,0,407,408,1,0,0,0,408,409,3,170,85,0,409,410,3,72,36,0,410,
        69,1,0,0,0,411,415,3,170,85,0,412,415,5,20,0,0,413,415,5,21,0,0,
        414,411,1,0,0,0,414,412,1,0,0,0,414,413,1,0,0,0,415,71,1,0,0,0,416,
        420,5,14,0,0,417,419,5,61,0,0,418,417,1,0,0,0,419,422,1,0,0,0,420,
        418,1,0,0,0,420,421,1,0,0,0,421,423,1,0,0,0,422,420,1,0,0,0,423,
        424,5,59,0,0,424,73,1,0,0,0,425,429,5,13,0,0,426,428,5,58,0,0,427,
        426,1,0,0,0,428,431,1,0,0,0,429,427,1,0,0,0,429,430,1,0,0,0,430,
        432,1,0,0,0,431,429,1,0,0,0,432,433,5,56,0,0,433,75,1,0,0,0,434,
        435,5,31,0,0,435,436,3,170,85,0,436,440,5,35,0,0,437,439,3,110,55,
        0,438,437,1,0,0,0,439,442,1,0,0,0,440,438,1,0,0,0,440,441,1,0,0,
        0,441,77,1,0,0,0,442,440,1,0,0,0,443,445,3,80,40,0,444,443,1,0,0,
        0,445,448,1,0,0,0,446,444,1,0,0,0,446,447,1,0,0,0,447,79,1,0,0,0,
        448,446,1,0,0,0,449,452,3,82,41,0,450,452,3,110,55,0,451,449,1,0,
        0,0,451,450,1,0,0,0,452,81,1,0,0,0,453,455,3,100,50,0,454,453,1,
        0,0,0,454,455,1,0,0,0,455,456,1,0,0,0,456,458,5,2,0,0,457,459,3,
        74,37,0,458,457,1,0,0,0,458,459,1,0,0,0,459,461,1,0,0,0,460,462,
        3,92,46,0,461,460,1,0,0,0,461,462,1,0,0,0,462,464,1,0,0,0,463,465,
        3,94,47,0,464,463,1,0,0,0,464,465,1,0,0,0,465,467,1,0,0,0,466,468,
        3,96,48,0,467,466,1,0,0,0,467,468,1,0,0,0,468,472,1,0,0,0,469,471,
        3,90,45,0,470,469,1,0,0,0,471,474,1,0,0,0,472,470,1,0,0,0,472,473,
        1,0,0,0,473,475,1,0,0,0,474,472,1,0,0,0,475,476,5,32,0,0,476,477,
        3,104,52,0,477,478,5,35,0,0,478,479,3,84,42,0,479,83,1,0,0,0,480,
        482,3,86,43,0,481,480,1,0,0,0,482,485,1,0,0,0,483,481,1,0,0,0,483,
        484,1,0,0,0,484,487,1,0,0,0,485,483,1,0,0,0,486,488,3,88,44,0,487,
        486,1,0,0,0,487,488,1,0,0,0,488,85,1,0,0,0,489,490,5,29,0,0,490,
        491,3,74,37,0,491,492,3,72,36,0,492,87,1,0,0,0,493,494,5,30,0,0,
        494,495,3,72,36,0,495,89,1,0,0,0,496,499,3,52,26,0,497,499,3,98,
        49,0,498,496,1,0,0,0,498,497,1,0,0,0,499,91,1,0,0,0,500,501,5,26,
        0,0,501,502,3,74,37,0,502,93,1,0,0,0,503,504,5,28,0,0,504,509,3,
        170,85,0,505,506,5,34,0,0,506,508,3,170,85,0,507,505,1,0,0,0,508,
        511,1,0,0,0,509,507,1,0,0,0,509,510,1,0,0,0,510,95,1,0,0,0,511,509,
        1,0,0,0,512,513,5,27,0,0,513,514,3,74,37,0,514,97,1,0,0,0,515,516,
        5,50,0,0,516,517,3,170,85,0,517,518,3,72,36,0,518,99,1,0,0,0,519,
        521,3,102,51,0,520,519,1,0,0,0,521,522,1,0,0,0,522,520,1,0,0,0,522,
        523,1,0,0,0,523,101,1,0,0,0,524,525,7,3,0,0,525,103,1,0,0,0,526,
        527,3,106,53,0,527,105,1,0,0,0,528,533,3,108,54,0,529,530,5,46,0,
        0,530,532,3,108,54,0,531,529,1,0,0,0,532,535,1,0,0,0,533,531,1,0,
        0,0,533,534,1,0,0,0,534,107,1,0,0,0,535,533,1,0,0,0,536,539,3,136,
        68,0,537,538,5,51,0,0,538,540,3,170,85,0,539,537,1,0,0,0,539,540,
        1,0,0,0,540,109,1,0,0,0,541,543,5,19,0,0,542,541,1,0,0,0,542,543,
        1,0,0,0,543,544,1,0,0,0,544,546,5,1,0,0,545,547,3,52,26,0,546,545,
        1,0,0,0,546,547,1,0,0,0,547,548,1,0,0,0,548,549,5,32,0,0,549,550,
        3,112,56,0,550,551,5,35,0,0,551,111,1,0,0,0,552,553,3,114,57,0,553,
        113,1,0,0,0,554,559,3,116,58,0,555,556,5,46,0,0,556,558,3,116,58,
        0,557,555,1,0,0,0,558,561,1,0,0,0,559,557,1,0,0,0,559,560,1,0,0,
        0,560,115,1,0,0,0,561,559,1,0,0,0,562,564,3,118,59,0,563,565,3,126,
        63,0,564,563,1,0,0,0,564,565,1,0,0,0,565,568,1,0,0,0,566,568,1,0,
        0,0,567,562,1,0,0,0,567,566,1,0,0,0,568,117,1,0,0,0,569,571,3,120,
        60,0,570,569,1,0,0,0,571,572,1,0,0,0,572,570,1,0,0,0,572,573,1,0,
        0,0,573,576,1,0,0,0,574,576,1,0,0,0,575,570,1,0,0,0,575,574,1,0,
        0,0,576,119,1,0,0,0,577,579,3,122,61,0,578,580,3,146,73,0,579,578,
        1,0,0,0,579,580,1,0,0,0,580,594,1,0,0,0,581,583,3,148,74,0,582,584,
        3,146,73,0,583,582,1,0,0,0,583,584,1,0,0,0,584,594,1,0,0,0,585,587,
        3,124,62,0,586,588,3,146,73,0,587,586,1,0,0,0,587,588,1,0,0,0,588,
        594,1,0,0,0,589,591,3,72,36,0,590,592,5,42,0,0,591,590,1,0,0,0,591,
        592,1,0,0,0,592,594,1,0,0,0,593,577,1,0,0,0,593,581,1,0,0,0,593,
        585,1,0,0,0,593,589,1,0,0,0,594,121,1,0,0,0,595,596,3,170,85,0,596,
        599,7,2,0,0,597,600,3,148,74,0,598,600,3,124,62,0,599,597,1,0,0,
        0,599,598,1,0,0,0,600,123,1,0,0,0,601,602,5,36,0,0,602,603,3,114,
        57,0,603,604,5,37,0,0,604,125,1,0,0,0,605,606,5,38,0,0,606,611,3,
        128,64,0,607,608,5,34,0,0,608,610,3,128,64,0,609,607,1,0,0,0,610,
        613,1,0,0,0,611,609,1,0,0,0,611,612,1,0,0,0,612,127,1,0,0,0,613,
        611,1,0,0,0,614,615,3,130,65,0,615,616,5,36,0,0,616,617,3,132,66,
        0,617,618,5,37,0,0,618,621,1,0,0,0,619,621,3,130,65,0,620,614,1,
        0,0,0,620,619,1,0,0,0,621,129,1,0,0,0,622,625,3,170,85,0,623,625,
        5,31,0,0,624,622,1,0,0,0,624,623,1,0,0,0,625,131,1,0,0,0,626,629,
        3,170,85,0,627,629,5,10,0,0,628,626,1,0,0,0,628,627,1,0,0,0,629,
        133,1,0,0,0,630,635,3,136,68,0,631,632,5,46,0,0,632,634,3,136,68,
        0,633,631,1,0,0,0,634,637,1,0,0,0,635,633,1,0,0,0,635,636,1,0,0,
        0,636,135,1,0,0,0,637,635,1,0,0,0,638,640,3,166,83,0,639,638,1,0,
        0,0,639,640,1,0,0,0,640,642,1,0,0,0,641,643,3,138,69,0,642,641,1,
        0,0,0,643,644,1,0,0,0,644,642,1,0,0,0,644,645,1,0,0,0,645,648,1,
        0,0,0,646,648,1,0,0,0,647,639,1,0,0,0,647,646,1,0,0,0,648,137,1,
        0,0,0,649,652,3,140,70,0,650,653,3,146,73,0,651,653,1,0,0,0,652,
        650,1,0,0,0,652,651,1,0,0,0,653,665,1,0,0,0,654,657,3,150,75,0,655,
        658,3,146,73,0,656,658,1,0,0,0,657,655,1,0,0,0,657,656,1,0,0,0,658,
        665,1,0,0,0,659,665,3,142,71,0,660,662,3,72,36,0,661,663,5,42,0,
        0,662,661,1,0,0,0,662,663,1,0,0,0,663,665,1,0,0,0,664,649,1,0,0,
        0,664,654,1,0,0,0,664,659,1,0,0,0,664,660,1,0,0,0,665,139,1,0,0,
        0,666,667,3,170,85,0,667,670,7,2,0,0,668,671,3,150,75,0,669,671,
        3,158,79,0,670,668,1,0,0,0,670,669,1,0,0,0,671,141,1,0,0,0,672,674,
        3,158,79,0,673,675,3,144,72,0,674,673,1,0,0,0,674,675,1,0,0,0,675,
        143,1,0,0,0,676,677,3,146,73,0,677,145,1,0,0,0,678,680,5,42,0,0,
        679,681,5,42,0,0,680,679,1,0,0,0,680,681,1,0,0,0,681,691,1,0,0,0,
        682,684,5,43,0,0,683,685,5,42,0,0,684,683,1,0,0,0,684,685,1,0,0,
        0,685,691,1,0,0,0,686,688,5,45,0,0,687,689,5,42,0,0,688,687,1,0,
        0,0,688,689,1,0,0,0,689,691,1,0,0,0,690,678,1,0,0,0,690,682,1,0,
        0,0,690,686,1,0,0,0,691,147,1,0,0,0,692,701,3,162,81,0,693,701,3,
        164,82,0,694,701,3,152,76,0,695,701,5,3,0,0,696,698,5,49,0,0,697,
        699,3,166,83,0,698,697,1,0,0,0,698,699,1,0,0,0,699,701,1,0,0,0,700,
        692,1,0,0,0,700,693,1,0,0,0,700,694,1,0,0,0,700,695,1,0,0,0,700,
        696,1,0,0,0,701,149,1,0,0,0,702,710,3,164,82,0,703,710,3,160,80,
        0,704,710,3,152,76,0,705,707,5,49,0,0,706,708,3,166,83,0,707,706,
        1,0,0,0,707,708,1,0,0,0,708,710,1,0,0,0,709,702,1,0,0,0,709,703,
        1,0,0,0,709,704,1,0,0,0,709,705,1,0,0,0,710,151,1,0,0,0,711,712,
        5,52,0,0,712,716,3,156,78,0,713,714,5,52,0,0,714,716,3,154,77,0,
        715,711,1,0,0,0,715,713,1,0,0,0,716,153,1,0,0,0,717,718,5,36,0,0,
        718,723,3,156,78,0,719,720,5,46,0,0,720,722,3,156,78,0,721,719,1,
        0,0,0,722,725,1,0,0,0,723,721,1,0,0,0,723,724,1,0,0,0,724,726,1,
        0,0,0,725,723,1,0,0,0,726,727,5,37,0,0,727,155,1,0,0,0,728,730,5,
        1,0,0,729,731,3,166,83,0,730,729,1,0,0,0,730,731,1,0,0,0,731,739,
        1,0,0,0,732,734,5,11,0,0,733,735,3,166,83,0,734,733,1,0,0,0,734,
        735,1,0,0,0,735,739,1,0,0,0,736,739,3,162,81,0,737,739,5,3,0,0,738,
        728,1,0,0,0,738,732,1,0,0,0,738,736,1,0,0,0,738,737,1,0,0,0,739,
        157,1,0,0,0,740,751,5,36,0,0,741,743,3,52,26,0,742,741,1,0,0,0,742,
        743,1,0,0,0,743,747,1,0,0,0,744,746,3,98,49,0,745,744,1,0,0,0,746,
        749,1,0,0,0,747,745,1,0,0,0,747,748,1,0,0,0,748,750,1,0,0,0,749,
        747,1,0,0,0,750,752,5,32,0,0,751,742,1,0,0,0,751,752,1,0,0,0,752,
        753,1,0,0,0,753,754,3,134,67,0,754,755,5,37,0,0,755,159,1,0,0,0,
        756,758,5,2,0,0,757,759,3,74,37,0,758,757,1,0,0,0,758,759,1,0,0,
        0,759,761,1,0,0,0,760,762,3,166,83,0,761,760,1,0,0,0,761,762,1,0,
        0,0,762,161,1,0,0,0,763,764,5,11,0,0,764,765,5,48,0,0,765,766,5,
        11,0,0,766,163,1,0,0,0,767,769,5,1,0,0,768,770,3,166,83,0,769,768,
        1,0,0,0,769,770,1,0,0,0,770,776,1,0,0,0,771,773,5,11,0,0,772,774,
        3,166,83,0,773,772,1,0,0,0,773,774,1,0,0,0,774,776,1,0,0,0,775,767,
        1,0,0,0,775,771,1,0,0,0,776,165,1,0,0,0,777,778,5,39,0,0,778,783,
        3,168,84,0,779,780,5,34,0,0,780,782,3,168,84,0,781,779,1,0,0,0,782,
        785,1,0,0,0,783,781,1,0,0,0,783,784,1,0,0,0,784,786,1,0,0,0,785,
        783,1,0,0,0,786,787,5,40,0,0,787,167,1,0,0,0,788,796,3,170,85,0,
        789,790,3,170,85,0,790,793,5,41,0,0,791,794,3,170,85,0,792,794,5,
        11,0,0,793,791,1,0,0,0,793,792,1,0,0,0,794,796,1,0,0,0,795,788,1,
        0,0,0,795,789,1,0,0,0,796,169,1,0,0,0,797,798,7,0,0,0,798,171,1,
        0,0,0,106,174,176,183,190,196,203,213,221,227,231,236,239,243,248,
        255,259,263,272,276,279,283,288,303,310,324,331,339,353,359,367,
        377,381,387,396,400,406,414,420,429,440,446,451,454,458,461,464,
        467,472,483,487,498,509,522,533,539,542,546,559,564,567,572,575,
        579,583,587,591,593,599,611,620,624,628,635,639,644,647,652,657,
        662,664,670,674,680,684,688,690,698,700,707,709,715,723,730,734,
        738,742,747,751,758,761,769,773,775,783,793,795
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
    RULE_label = 20
    RULE_assign = 21
    RULE_grammarSpec = 22
    RULE_grammarDecl = 23
    RULE_grammarType = 24
    RULE_prequelConstruct = 25
    RULE_optionsSpec = 26
    RULE_option = 27
    RULE_optionValue = 28
    RULE_delegateGrammars = 29
    RULE_delegateGrammar = 30
    RULE_tokensSpec = 31
    RULE_channelsSpec = 32
    RULE_idList = 33
    RULE_action_ = 34
    RULE_actionScopeName = 35
    RULE_actionBlock = 36
    RULE_argActionBlock = 37
    RULE_modeSpec = 38
    RULE_rules = 39
    RULE_ruleSpec = 40
    RULE_parserRuleSpec = 41
    RULE_exceptionGroup = 42
    RULE_exceptionHandler = 43
    RULE_finallyClause = 44
    RULE_rulePrequel = 45
    RULE_ruleReturns = 46
    RULE_throwsSpec = 47
    RULE_localsSpec = 48
    RULE_ruleAction = 49
    RULE_ruleModifiers = 50
    RULE_ruleModifier = 51
    RULE_ruleBlock = 52
    RULE_ruleAltList = 53
    RULE_labeledAlt = 54
    RULE_lexerRuleSpec = 55
    RULE_lexerRuleBlock = 56
    RULE_lexerAltList = 57
    RULE_lexerAlt = 58
    RULE_lexerElements = 59
    RULE_lexerElement = 60
    RULE_labeledLexerElement = 61
    RULE_lexerBlock = 62
    RULE_lexerCommands = 63
    RULE_lexerCommand = 64
    RULE_lexerCommandName = 65
    RULE_lexerCommandExpr = 66
    RULE_altList = 67
    RULE_alternative = 68
    RULE_element = 69
    RULE_labeledElement = 70
    RULE_ebnf = 71
    RULE_blockSuffix = 72
    RULE_ebnfSuffix = 73
    RULE_lexerAtom = 74
    RULE_atom = 75
    RULE_notSet = 76
    RULE_blockSet = 77
    RULE_setElement = 78
    RULE_block = 79
    RULE_ruleref = 80
    RULE_characterRange = 81
    RULE_terminal = 82
    RULE_elementOptions = 83
    RULE_elementOption = 84
    RULE_identifier = 85

    ruleNames =  [ "program", "ruleDef", "tokenDef", "ruleSub", "tokenSub", 
                   "ruleAlts", "tokenAlts", "ruleAlt", "tokenAlt", "ruleAtom", 
                   "ruleEbnf", "ruleRef", "ruleLiteral", "expr", "call", 
                   "args", "tokenAtom", "tokenEbnf", "tokenRef", "tokenLiteral", 
                   "label", "assign", "grammarSpec", "grammarDecl", "grammarType", 
                   "prequelConstruct", "optionsSpec", "option", "optionValue", 
                   "delegateGrammars", "delegateGrammar", "tokensSpec", 
                   "channelsSpec", "idList", "action_", "actionScopeName", 
                   "actionBlock", "argActionBlock", "modeSpec", "rules", 
                   "ruleSpec", "parserRuleSpec", "exceptionGroup", "exceptionHandler", 
                   "finallyClause", "rulePrequel", "ruleReturns", "throwsSpec", 
                   "localsSpec", "ruleAction", "ruleModifiers", "ruleModifier", 
                   "ruleBlock", "ruleAltList", "labeledAlt", "lexerRuleSpec", 
                   "lexerRuleBlock", "lexerAltList", "lexerAlt", "lexerElements", 
                   "lexerElement", "labeledLexerElement", "lexerBlock", 
                   "lexerCommands", "lexerCommand", "lexerCommandName", 
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
            self.state = 174 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 174
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2]:
                    self.state = 172
                    self.ruleDef()
                    pass
                elif token in [1]:
                    self.state = 173
                    self.tokenDef()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 176 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==2):
                    break

            self.state = 178
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

        def ruleAlts(self):
            return self.getTypedRuleContext(ctx2lParser.RuleAltsContext,0)


        def OR(self):
            return self.getToken(ctx2lParser.OR, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(ctx2lParser.RULE_REF)
            self.state = 181
            self.match(ctx2lParser.COLON)
            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 182
                self.match(ctx2lParser.OR)


            self.state = 185
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

        def tokenAlts(self):
            return self.getTypedRuleContext(ctx2lParser.TokenAltsContext,0)


        def OR(self):
            return self.getToken(ctx2lParser.OR, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(ctx2lParser.TOKEN_REF)
            self.state = 188
            self.match(ctx2lParser.COLON)
            self.state = 190
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 189
                self.match(ctx2lParser.OR)


            self.state = 192
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
            self.state = 194
            self.match(ctx2lParser.LPAREN)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 195
                self.match(ctx2lParser.OR)


            self.state = 198
            self.ruleAlts()
            self.state = 199
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
            self.state = 201
            self.match(ctx2lParser.LPAREN)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 202
                self.match(ctx2lParser.OR)


            self.state = 205
            self.tokenAlts()
            self.state = 206
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
            self.state = 208
            self.ruleAlt()
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 209
                self.match(ctx2lParser.OR)
                self.state = 210
                self.ruleAlt()
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
            self.state = 216
            self.tokenAlt()
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 217
                self.match(ctx2lParser.OR)
                self.state = 218
                self.tokenAlt()
                self.state = 223
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
            self.state = 225 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 224
                    self.ruleAtom()

                else:
                    raise NoViableAltException(self)
                self.state = 227 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 229
                self.match(ctx2lParser.ARROW)
                self.state = 230
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
            self.state = 234 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 233
                    self.tokenAtom()

                else:
                    raise NoViableAltException(self)
                self.state = 236 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

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


        def label(self):
            return self.getTypedRuleContext(ctx2lParser.LabelContext,0)


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
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 238
                self.label()


            self.state = 241
            self.ruleEbnf()
            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 48378511622144) != 0):
                self.state = 242
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
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.ruleSub()
                pass
            elif token in [1, 2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 246
                self.ruleRef()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 247
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
            self.state = 250
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
            self.state = 252
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


        def DOLLAR(self):
            return self.getToken(ctx2lParser.DOLLAR, 0)

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
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47:
                self.state = 254
                self.match(ctx2lParser.DOLLAR)


            self.state = 257
            self.identifier()
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 258
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
            self.state = 261
            self.match(ctx2lParser.LPAREN)
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488355334) != 0):
                self.state = 262
                self.args()


            self.state = 265
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
            self.state = 267
            self.expr()
            self.state = 272
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 268
                    self.match(ctx2lParser.COMMA)
                    self.state = 269
                    self.expr() 
                self.state = 274
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

            self.state = 276
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 275
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


        def label(self):
            return self.getTypedRuleContext(ctx2lParser.LabelContext,0)


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
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 278
                self.label()


            self.state = 281
            self.tokenEbnf()
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 48378511622144) != 0):
                self.state = 282
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
            self.state = 288
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 285
                self.tokenSub()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 286
                self.tokenRef()
                pass
            elif token in [3, 11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 287
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
            self.state = 290
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
            self.state = 292
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


    class LabelContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def identifier(self):
            return self.getTypedRuleContext(ctx2lParser.IdentifierContext,0)


        def assign(self):
            return self.getTypedRuleContext(ctx2lParser.AssignContext,0)


        def getRuleIndex(self):
            return ctx2lParser.RULE_label

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLabel" ):
                return visitor.visitLabel(self)
            else:
                return visitor.visitChildren(self)




    def label(self):

        localctx = ctx2lParser.LabelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.identifier()
            self.state = 295
            self.assign()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(ctx2lParser.ASSIGN, 0)

        def PLUS_ASSIGN(self):
            return self.getToken(ctx2lParser.PLUS_ASSIGN, 0)

        def getRuleIndex(self):
            return ctx2lParser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = ctx2lParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            _la = self._input.LA(1)
            if not(_la==41 or _la==44):
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
        self.enterRule(localctx, 44, self.RULE_grammarSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.grammarDecl()
            self.state = 303
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1125899907334144) != 0):
                self.state = 300
                self.prequelConstruct()
                self.state = 305
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 306
            self.rules()
            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 307
                self.modeSpec()
                self.state = 312
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 313
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
        self.enterRule(localctx, 46, self.RULE_grammarDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.grammarType()
            self.state = 316
            self.identifier()
            self.state = 317
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
        self.enterRule(localctx, 48, self.RULE_grammarType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.state = 319
                self.match(ctx2lParser.LEXER)
                self.state = 320
                self.match(ctx2lParser.GRAMMAR)
                pass
            elif token in [21]:
                self.state = 321
                self.match(ctx2lParser.PARSER)
                self.state = 322
                self.match(ctx2lParser.GRAMMAR)
                pass
            elif token in [22]:
                self.state = 323
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
        self.enterRule(localctx, 50, self.RULE_prequelConstruct)
        try:
            self.state = 331
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 326
                self.optionsSpec()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
                self.delegateGrammars()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 328
                self.tokensSpec()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 4)
                self.state = 329
                self.channelsSpec()
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 5)
                self.state = 330
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
        self.enterRule(localctx, 52, self.RULE_optionsSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(ctx2lParser.OPTIONS)
            self.state = 339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==2:
                self.state = 334
                self.option()
                self.state = 335
                self.match(ctx2lParser.SEMI)
                self.state = 341
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 342
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
        self.enterRule(localctx, 54, self.RULE_option)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.identifier()
            self.state = 345
            self.match(ctx2lParser.ASSIGN)
            self.state = 346
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
        self.enterRule(localctx, 56, self.RULE_optionValue)
        self._la = 0 # Token type
        try:
            self.state = 359
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.identifier()
                self.state = 353
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==49:
                    self.state = 349
                    self.match(ctx2lParser.DOT)
                    self.state = 350
                    self.identifier()
                    self.state = 355
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 356
                self.match(ctx2lParser.STRING_LITERAL)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 357
                self.actionBlock()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 358
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
        self.enterRule(localctx, 58, self.RULE_delegateGrammars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(ctx2lParser.IMPORT)
            self.state = 362
            self.delegateGrammar()
            self.state = 367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 363
                self.match(ctx2lParser.COMMA)
                self.state = 364
                self.delegateGrammar()
                self.state = 369
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 370
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
        self.enterRule(localctx, 60, self.RULE_delegateGrammar)
        try:
            self.state = 377
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.identifier()
                self.state = 373
                self.match(ctx2lParser.ASSIGN)
                self.state = 374
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 376
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
        self.enterRule(localctx, 62, self.RULE_tokensSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.match(ctx2lParser.TOKENS)
            self.state = 381
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==2:
                self.state = 380
                self.idList()


            self.state = 383
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
        self.enterRule(localctx, 64, self.RULE_channelsSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(ctx2lParser.CHANNELS)
            self.state = 387
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==2:
                self.state = 386
                self.idList()


            self.state = 389
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
        self.enterRule(localctx, 66, self.RULE_idList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.identifier()
            self.state = 396
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 392
                    self.match(ctx2lParser.COMMA)
                    self.state = 393
                    self.identifier() 
                self.state = 398
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

            self.state = 400
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 399
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
        self.enterRule(localctx, 68, self.RULE_action_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 402
            self.match(ctx2lParser.AT)
            self.state = 406
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 403
                self.actionScopeName()
                self.state = 404
                self.match(ctx2lParser.COLONCOLON)


            self.state = 408
            self.identifier()
            self.state = 409
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
        self.enterRule(localctx, 70, self.RULE_actionScopeName)
        try:
            self.state = 414
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 411
                self.identifier()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
                self.match(ctx2lParser.LEXER)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 413
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
        self.enterRule(localctx, 72, self.RULE_actionBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(ctx2lParser.BEGIN_ACTION)
            self.state = 420
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==61:
                self.state = 417
                self.match(ctx2lParser.ACTION_CONTENT)
                self.state = 422
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 423
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
        self.enterRule(localctx, 74, self.RULE_argActionBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.match(ctx2lParser.BEGIN_ARGUMENT)
            self.state = 429
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==58:
                self.state = 426
                self.match(ctx2lParser.ARGUMENT_CONTENT)
                self.state = 431
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 432
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
        self.enterRule(localctx, 76, self.RULE_modeSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 434
            self.match(ctx2lParser.MODE)
            self.state = 435
            self.identifier()
            self.state = 436
            self.match(ctx2lParser.SEMI)
            self.state = 440
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==19:
                self.state = 437
                self.lexerRuleSpec()
                self.state = 442
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
        self.enterRule(localctx, 78, self.RULE_rules)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 59244550) != 0):
                self.state = 443
                self.ruleSpec()
                self.state = 448
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
        self.enterRule(localctx, 80, self.RULE_ruleSpec)
        try:
            self.state = 451
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 449
                self.parserRuleSpec()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 450
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
        self.enterRule(localctx, 82, self.RULE_parserRuleSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 59244544) != 0):
                self.state = 453
                self.ruleModifiers()


            self.state = 456
            self.match(ctx2lParser.RULE_REF)
            self.state = 458
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 457
                self.argActionBlock()


            self.state = 461
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 460
                self.ruleReturns()


            self.state = 464
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 463
                self.throwsSpec()


            self.state = 467
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 466
                self.localsSpec()


            self.state = 472
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15 or _la==50:
                self.state = 469
                self.rulePrequel()
                self.state = 474
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 475
            self.match(ctx2lParser.COLON)
            self.state = 476
            self.ruleBlock()
            self.state = 477
            self.match(ctx2lParser.SEMI)
            self.state = 478
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
        self.enterRule(localctx, 84, self.RULE_exceptionGroup)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 480
                self.exceptionHandler()
                self.state = 485
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 487
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 486
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
        self.enterRule(localctx, 86, self.RULE_exceptionHandler)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 489
            self.match(ctx2lParser.CATCH)
            self.state = 490
            self.argActionBlock()
            self.state = 491
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
        self.enterRule(localctx, 88, self.RULE_finallyClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 493
            self.match(ctx2lParser.FINALLY)
            self.state = 494
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
        self.enterRule(localctx, 90, self.RULE_rulePrequel)
        try:
            self.state = 498
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 496
                self.optionsSpec()
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 2)
                self.state = 497
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
        self.enterRule(localctx, 92, self.RULE_ruleReturns)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            self.match(ctx2lParser.RETURNS)
            self.state = 501
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
        self.enterRule(localctx, 94, self.RULE_throwsSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.match(ctx2lParser.THROWS)
            self.state = 504
            self.identifier()
            self.state = 509
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 505
                self.match(ctx2lParser.COMMA)
                self.state = 506
                self.identifier()
                self.state = 511
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
        self.enterRule(localctx, 96, self.RULE_localsSpec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
            self.match(ctx2lParser.LOCALS)
            self.state = 513
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
        self.enterRule(localctx, 98, self.RULE_ruleAction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.match(ctx2lParser.AT)
            self.state = 516
            self.identifier()
            self.state = 517
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
        self.enterRule(localctx, 100, self.RULE_ruleModifiers)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 519
                self.ruleModifier()
                self.state = 522 
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
        self.enterRule(localctx, 102, self.RULE_ruleModifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 524
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
        self.enterRule(localctx, 104, self.RULE_ruleBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
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
        self.enterRule(localctx, 106, self.RULE_ruleAltList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 528
            self.labeledAlt()
            self.state = 533
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 529
                self.match(ctx2lParser.OR)
                self.state = 530
                self.labeledAlt()
                self.state = 535
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
        self.enterRule(localctx, 108, self.RULE_labeledAlt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self.alternative()
            self.state = 539
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==51:
                self.state = 537
                self.match(ctx2lParser.POUND)
                self.state = 538
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
        self.enterRule(localctx, 110, self.RULE_lexerRuleSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 541
                self.match(ctx2lParser.FRAGMENT)


            self.state = 544
            self.match(ctx2lParser.TOKEN_REF)
            self.state = 546
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 545
                self.optionsSpec()


            self.state = 548
            self.match(ctx2lParser.COLON)
            self.state = 549
            self.lexerRuleBlock()
            self.state = 550
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
        self.enterRule(localctx, 112, self.RULE_lexerRuleBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 552
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
        self.enterRule(localctx, 114, self.RULE_lexerAltList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 554
            self.lexerAlt()
            self.state = 559
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 555
                self.match(ctx2lParser.OR)
                self.state = 556
                self.lexerAlt()
                self.state = 561
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
        self.enterRule(localctx, 116, self.RULE_lexerAlt)
        self._la = 0 # Token type
        try:
            self.state = 567
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 562
                self.lexerElements()
                self.state = 564
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==38:
                    self.state = 563
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
        self.enterRule(localctx, 118, self.RULE_lexerElements)
        self._la = 0 # Token type
        try:
            self.state = 575
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 11, 14, 36, 49, 52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 570 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 569
                    self.lexerElement()
                    self.state = 572 
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
        self.enterRule(localctx, 120, self.RULE_lexerElement)
        self._la = 0 # Token type
        try:
            self.state = 593
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 577
                self.labeledLexerElement()
                self.state = 579
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 48378511622144) != 0):
                    self.state = 578
                    self.ebnfSuffix()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 581
                self.lexerAtom()
                self.state = 583
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 48378511622144) != 0):
                    self.state = 582
                    self.ebnfSuffix()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 585
                self.lexerBlock()
                self.state = 587
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 48378511622144) != 0):
                    self.state = 586
                    self.ebnfSuffix()


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 589
                self.actionBlock()
                self.state = 591
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==42:
                    self.state = 590
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
        self.enterRule(localctx, 122, self.RULE_labeledLexerElement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 595
            self.identifier()
            self.state = 596
            _la = self._input.LA(1)
            if not(_la==41 or _la==44):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 599
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 11, 49, 52]:
                self.state = 597
                self.lexerAtom()
                pass
            elif token in [36]:
                self.state = 598
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
        self.enterRule(localctx, 124, self.RULE_lexerBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 601
            self.match(ctx2lParser.LPAREN)
            self.state = 602
            self.lexerAltList()
            self.state = 603
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
        self.enterRule(localctx, 126, self.RULE_lexerCommands)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 605
            self.match(ctx2lParser.RARROW)
            self.state = 606
            self.lexerCommand()
            self.state = 611
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 607
                self.match(ctx2lParser.COMMA)
                self.state = 608
                self.lexerCommand()
                self.state = 613
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
        self.enterRule(localctx, 128, self.RULE_lexerCommand)
        try:
            self.state = 620
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 614
                self.lexerCommandName()
                self.state = 615
                self.match(ctx2lParser.LPAREN)
                self.state = 616
                self.lexerCommandExpr()
                self.state = 617
                self.match(ctx2lParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 619
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
        self.enterRule(localctx, 130, self.RULE_lexerCommandName)
        try:
            self.state = 624
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 622
                self.identifier()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 623
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
        self.enterRule(localctx, 132, self.RULE_lexerCommandExpr)
        try:
            self.state = 628
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 626
                self.identifier()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 627
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
        self.enterRule(localctx, 134, self.RULE_altList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 630
            self.alternative()
            self.state = 635
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 631
                self.match(ctx2lParser.OR)
                self.state = 632
                self.alternative()
                self.state = 637
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
        self.enterRule(localctx, 136, self.RULE_alternative)
        self._la = 0 # Token type
        try:
            self.state = 647
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 11, 14, 36, 39, 49, 52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 639
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 638
                    self.elementOptions()


                self.state = 642 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 641
                    self.element()
                    self.state = 644 
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
        self.enterRule(localctx, 138, self.RULE_element)
        self._la = 0 # Token type
        try:
            self.state = 664
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 649
                self.labeledElement()
                self.state = 652
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [42, 43, 45]:
                    self.state = 650
                    self.ebnfSuffix()
                    pass
                elif token in [1, 2, 11, 14, 35, 36, 37, 46, 49, 51, 52]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 654
                self.atom()
                self.state = 657
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [42, 43, 45]:
                    self.state = 655
                    self.ebnfSuffix()
                    pass
                elif token in [1, 2, 11, 14, 35, 36, 37, 46, 49, 51, 52]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 659
                self.ebnf()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 660
                self.actionBlock()
                self.state = 662
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==42:
                    self.state = 661
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
        self.enterRule(localctx, 140, self.RULE_labeledElement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 666
            self.identifier()
            self.state = 667
            _la = self._input.LA(1)
            if not(_la==41 or _la==44):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 670
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 11, 49, 52]:
                self.state = 668
                self.atom()
                pass
            elif token in [36]:
                self.state = 669
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
        self.enterRule(localctx, 142, self.RULE_ebnf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 672
            self.block()
            self.state = 674
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 48378511622144) != 0):
                self.state = 673
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
        self.enterRule(localctx, 144, self.RULE_blockSuffix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 676
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
        self.enterRule(localctx, 146, self.RULE_ebnfSuffix)
        self._la = 0 # Token type
        try:
            self.state = 690
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 678
                self.match(ctx2lParser.QUESTION)
                self.state = 680
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==42:
                    self.state = 679
                    self.match(ctx2lParser.QUESTION)


                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 682
                self.match(ctx2lParser.STAR)
                self.state = 684
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==42:
                    self.state = 683
                    self.match(ctx2lParser.QUESTION)


                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 3)
                self.state = 686
                self.match(ctx2lParser.PLUS)
                self.state = 688
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==42:
                    self.state = 687
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
        self.enterRule(localctx, 148, self.RULE_lexerAtom)
        self._la = 0 # Token type
        try:
            self.state = 700
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,87,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 692
                self.characterRange()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 693
                self.terminal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 694
                self.notSet()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 695
                self.match(ctx2lParser.LEXER_CHAR_SET)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 696
                self.match(ctx2lParser.DOT)
                self.state = 698
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 697
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
        self.enterRule(localctx, 150, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 709
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 702
                self.terminal()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 703
                self.ruleref()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 3)
                self.state = 704
                self.notSet()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 4)
                self.state = 705
                self.match(ctx2lParser.DOT)
                self.state = 707
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 706
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
        self.enterRule(localctx, 152, self.RULE_notSet)
        try:
            self.state = 715
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,90,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 711
                self.match(ctx2lParser.NOT)
                self.state = 712
                self.setElement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 713
                self.match(ctx2lParser.NOT)
                self.state = 714
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
        self.enterRule(localctx, 154, self.RULE_blockSet)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 717
            self.match(ctx2lParser.LPAREN)
            self.state = 718
            self.setElement()
            self.state = 723
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 719
                self.match(ctx2lParser.OR)
                self.state = 720
                self.setElement()
                self.state = 725
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 726
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
        self.enterRule(localctx, 156, self.RULE_setElement)
        self._la = 0 # Token type
        try:
            self.state = 738
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,94,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 728
                self.match(ctx2lParser.TOKEN_REF)
                self.state = 730
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 729
                    self.elementOptions()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 732
                self.match(ctx2lParser.STRING_LITERAL)
                self.state = 734
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 733
                    self.elementOptions()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 736
                self.characterRange()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 737
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
        self.enterRule(localctx, 158, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 740
            self.match(ctx2lParser.LPAREN)
            self.state = 751
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1125904201842688) != 0):
                self.state = 742
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 741
                    self.optionsSpec()


                self.state = 747
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==50:
                    self.state = 744
                    self.ruleAction()
                    self.state = 749
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 750
                self.match(ctx2lParser.COLON)


            self.state = 753
            self.altList()
            self.state = 754
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
        self.enterRule(localctx, 160, self.RULE_ruleref)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 756
            self.match(ctx2lParser.RULE_REF)
            self.state = 758
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 757
                self.argActionBlock()


            self.state = 761
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 760
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
        self.enterRule(localctx, 162, self.RULE_characterRange)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 763
            self.match(ctx2lParser.STRING_LITERAL)
            self.state = 764
            self.match(ctx2lParser.RANGE)
            self.state = 765
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
        self.enterRule(localctx, 164, self.RULE_terminal)
        self._la = 0 # Token type
        try:
            self.state = 775
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 767
                self.match(ctx2lParser.TOKEN_REF)
                self.state = 769
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 768
                    self.elementOptions()


                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 771
                self.match(ctx2lParser.STRING_LITERAL)
                self.state = 773
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 772
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
        self.enterRule(localctx, 166, self.RULE_elementOptions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 777
            self.match(ctx2lParser.LT)
            self.state = 778
            self.elementOption()
            self.state = 783
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 779
                self.match(ctx2lParser.COMMA)
                self.state = 780
                self.elementOption()
                self.state = 785
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 786
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
        self.enterRule(localctx, 168, self.RULE_elementOption)
        try:
            self.state = 795
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,105,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 788
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 789
                self.identifier()
                self.state = 790
                self.match(ctx2lParser.ASSIGN)
                self.state = 793
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 2]:
                    self.state = 791
                    self.identifier()
                    pass
                elif token in [11]:
                    self.state = 792
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
        self.enterRule(localctx, 170, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 797
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





