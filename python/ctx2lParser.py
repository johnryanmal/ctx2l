# Generated from ./ctx2lParser.g4 by ANTLR 4.13.0
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
        4,1,62,814,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
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
        7,85,2,86,7,86,1,0,1,0,4,0,177,8,0,11,0,12,0,178,1,0,1,0,1,1,1,1,
        1,1,3,1,186,8,1,1,1,1,1,1,2,1,2,1,2,3,2,193,8,2,1,2,1,2,3,2,197,
        8,2,1,2,1,2,1,3,1,3,1,3,5,3,204,8,3,10,3,12,3,207,9,3,1,4,1,4,3,
        4,211,8,4,1,4,1,4,1,4,1,5,1,5,3,5,218,8,5,1,5,1,5,1,5,1,6,1,6,1,
        6,5,6,226,8,6,10,6,12,6,229,9,6,1,7,1,7,1,7,5,7,234,8,7,10,7,12,
        7,237,9,7,1,8,4,8,240,8,8,11,8,12,8,241,1,8,1,8,3,8,246,8,8,1,9,
        4,9,249,8,9,11,9,12,9,250,1,10,3,10,254,8,10,1,10,1,10,3,10,258,
        8,10,1,11,1,11,1,11,3,11,263,8,11,1,12,1,12,1,13,1,13,1,14,3,14,
        270,8,14,1,14,1,14,3,14,274,8,14,1,15,1,15,3,15,278,8,15,1,15,1,
        15,1,16,1,16,1,16,5,16,285,8,16,10,16,12,16,288,9,16,1,16,3,16,291,
        8,16,1,17,3,17,294,8,17,1,17,1,17,3,17,298,8,17,1,18,1,18,1,18,3,
        18,303,8,18,1,19,1,19,1,20,1,20,1,21,1,21,1,21,1,22,1,22,1,23,1,
        23,5,23,316,8,23,10,23,12,23,319,9,23,1,23,1,23,5,23,323,8,23,10,
        23,12,23,326,9,23,1,23,1,23,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,
        25,1,25,3,25,339,8,25,1,26,1,26,1,26,1,26,1,26,3,26,346,8,26,1,27,
        1,27,1,27,1,27,5,27,352,8,27,10,27,12,27,355,9,27,1,27,1,27,1,28,
        1,28,1,28,1,28,1,29,1,29,1,29,5,29,366,8,29,10,29,12,29,369,9,29,
        1,29,1,29,1,29,3,29,374,8,29,1,30,1,30,1,30,1,30,5,30,380,8,30,10,
        30,12,30,383,9,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,3,31,392,8,
        31,1,32,1,32,3,32,396,8,32,1,32,1,32,1,33,1,33,3,33,402,8,33,1,33,
        1,33,1,34,1,34,1,34,5,34,409,8,34,10,34,12,34,412,9,34,1,34,3,34,
        415,8,34,1,35,1,35,1,35,1,35,3,35,421,8,35,1,35,1,35,1,35,1,36,1,
        36,1,36,3,36,429,8,36,1,37,1,37,5,37,433,8,37,10,37,12,37,436,9,
        37,1,37,1,37,1,38,1,38,5,38,442,8,38,10,38,12,38,445,9,38,1,38,1,
        38,1,39,1,39,1,39,1,39,5,39,453,8,39,10,39,12,39,456,9,39,1,40,5,
        40,459,8,40,10,40,12,40,462,9,40,1,41,1,41,3,41,466,8,41,1,42,3,
        42,469,8,42,1,42,1,42,3,42,473,8,42,1,42,3,42,476,8,42,1,42,3,42,
        479,8,42,1,42,3,42,482,8,42,1,42,5,42,485,8,42,10,42,12,42,488,9,
        42,1,42,1,42,1,42,1,42,1,42,1,43,5,43,496,8,43,10,43,12,43,499,9,
        43,1,43,3,43,502,8,43,1,44,1,44,1,44,1,44,1,45,1,45,1,45,1,46,1,
        46,3,46,513,8,46,1,47,1,47,1,47,1,48,1,48,1,48,1,48,5,48,522,8,48,
        10,48,12,48,525,9,48,1,49,1,49,1,49,1,50,1,50,1,50,1,50,1,51,4,51,
        535,8,51,11,51,12,51,536,1,52,1,52,1,53,1,53,1,54,1,54,1,54,5,54,
        546,8,54,10,54,12,54,549,9,54,1,55,1,55,1,55,3,55,554,8,55,1,56,
        3,56,557,8,56,1,56,1,56,3,56,561,8,56,1,56,1,56,1,56,1,56,1,57,1,
        57,1,58,1,58,1,58,5,58,572,8,58,10,58,12,58,575,9,58,1,59,1,59,3,
        59,579,8,59,1,59,3,59,582,8,59,1,60,4,60,585,8,60,11,60,12,60,586,
        1,60,3,60,590,8,60,1,61,1,61,3,61,594,8,61,1,61,1,61,3,61,598,8,
        61,1,61,1,61,3,61,602,8,61,1,61,1,61,3,61,606,8,61,3,61,608,8,61,
        1,62,1,62,1,62,1,62,3,62,614,8,62,1,63,1,63,1,63,1,63,1,64,1,64,
        1,64,1,64,5,64,624,8,64,10,64,12,64,627,9,64,1,65,1,65,1,65,1,65,
        1,65,1,65,3,65,635,8,65,1,66,1,66,3,66,639,8,66,1,67,1,67,3,67,643,
        8,67,1,68,1,68,1,68,5,68,648,8,68,10,68,12,68,651,9,68,1,69,3,69,
        654,8,69,1,69,4,69,657,8,69,11,69,12,69,658,1,69,3,69,662,8,69,1,
        70,1,70,1,70,3,70,667,8,70,1,70,1,70,1,70,3,70,672,8,70,1,70,1,70,
        1,70,3,70,677,8,70,3,70,679,8,70,1,71,1,71,1,71,1,71,3,71,685,8,
        71,1,72,1,72,3,72,689,8,72,1,73,1,73,1,74,1,74,3,74,695,8,74,1,74,
        1,74,3,74,699,8,74,1,74,1,74,3,74,703,8,74,3,74,705,8,74,1,75,1,
        75,1,75,1,75,1,75,1,75,3,75,713,8,75,3,75,715,8,75,1,76,1,76,1,76,
        1,76,1,76,3,76,722,8,76,3,76,724,8,76,1,77,1,77,1,77,1,77,3,77,730,
        8,77,1,78,1,78,1,78,1,78,5,78,736,8,78,10,78,12,78,739,9,78,1,78,
        1,78,1,79,1,79,3,79,745,8,79,1,79,1,79,3,79,749,8,79,1,79,1,79,3,
        79,753,8,79,1,80,1,80,3,80,757,8,80,1,80,5,80,760,8,80,10,80,12,
        80,763,9,80,1,80,3,80,766,8,80,1,80,1,80,1,80,1,81,1,81,3,81,773,
        8,81,1,81,3,81,776,8,81,1,82,1,82,1,82,1,82,1,83,1,83,3,83,784,8,
        83,1,83,1,83,3,83,788,8,83,3,83,790,8,83,1,84,1,84,1,84,1,84,5,84,
        796,8,84,10,84,12,84,799,9,84,1,84,1,84,1,85,1,85,1,85,1,85,1,85,
        3,85,808,8,85,3,85,810,8,85,1,86,1,86,1,86,0,0,87,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,
        58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,
        102,104,106,108,110,112,114,116,118,120,122,124,126,128,130,132,
        134,136,138,140,142,144,146,148,150,152,154,156,158,160,162,164,
        166,168,170,172,0,4,1,0,1,2,2,0,3,3,11,11,2,0,41,41,44,44,2,0,19,
        19,23,25,855,0,176,1,0,0,0,2,182,1,0,0,0,4,189,1,0,0,0,6,200,1,0,
        0,0,8,208,1,0,0,0,10,215,1,0,0,0,12,222,1,0,0,0,14,230,1,0,0,0,16,
        239,1,0,0,0,18,248,1,0,0,0,20,253,1,0,0,0,22,262,1,0,0,0,24,264,
        1,0,0,0,26,266,1,0,0,0,28,269,1,0,0,0,30,275,1,0,0,0,32,281,1,0,
        0,0,34,293,1,0,0,0,36,302,1,0,0,0,38,304,1,0,0,0,40,306,1,0,0,0,
        42,308,1,0,0,0,44,311,1,0,0,0,46,313,1,0,0,0,48,329,1,0,0,0,50,338,
        1,0,0,0,52,345,1,0,0,0,54,347,1,0,0,0,56,358,1,0,0,0,58,373,1,0,
        0,0,60,375,1,0,0,0,62,391,1,0,0,0,64,393,1,0,0,0,66,399,1,0,0,0,
        68,405,1,0,0,0,70,416,1,0,0,0,72,428,1,0,0,0,74,430,1,0,0,0,76,439,
        1,0,0,0,78,448,1,0,0,0,80,460,1,0,0,0,82,465,1,0,0,0,84,468,1,0,
        0,0,86,497,1,0,0,0,88,503,1,0,0,0,90,507,1,0,0,0,92,512,1,0,0,0,
        94,514,1,0,0,0,96,517,1,0,0,0,98,526,1,0,0,0,100,529,1,0,0,0,102,
        534,1,0,0,0,104,538,1,0,0,0,106,540,1,0,0,0,108,542,1,0,0,0,110,
        550,1,0,0,0,112,556,1,0,0,0,114,566,1,0,0,0,116,568,1,0,0,0,118,
        581,1,0,0,0,120,589,1,0,0,0,122,607,1,0,0,0,124,609,1,0,0,0,126,
        615,1,0,0,0,128,619,1,0,0,0,130,634,1,0,0,0,132,638,1,0,0,0,134,
        642,1,0,0,0,136,644,1,0,0,0,138,661,1,0,0,0,140,678,1,0,0,0,142,
        680,1,0,0,0,144,686,1,0,0,0,146,690,1,0,0,0,148,704,1,0,0,0,150,
        714,1,0,0,0,152,723,1,0,0,0,154,729,1,0,0,0,156,731,1,0,0,0,158,
        752,1,0,0,0,160,754,1,0,0,0,162,770,1,0,0,0,164,777,1,0,0,0,166,
        789,1,0,0,0,168,791,1,0,0,0,170,809,1,0,0,0,172,811,1,0,0,0,174,
        177,3,2,1,0,175,177,3,4,2,0,176,174,1,0,0,0,176,175,1,0,0,0,177,
        178,1,0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,180,1,0,0,0,180,
        181,5,0,0,1,181,1,1,0,0,0,182,183,5,2,0,0,183,185,5,32,0,0,184,186,
        5,46,0,0,185,184,1,0,0,0,185,186,1,0,0,0,186,187,1,0,0,0,187,188,
        3,12,6,0,188,3,1,0,0,0,189,192,5,1,0,0,190,191,5,6,0,0,191,193,3,
        6,3,0,192,190,1,0,0,0,192,193,1,0,0,0,193,194,1,0,0,0,194,196,5,
        32,0,0,195,197,5,46,0,0,196,195,1,0,0,0,196,197,1,0,0,0,197,198,
        1,0,0,0,198,199,3,14,7,0,199,5,1,0,0,0,200,205,3,130,65,0,201,202,
        5,34,0,0,202,204,3,130,65,0,203,201,1,0,0,0,204,207,1,0,0,0,205,
        203,1,0,0,0,205,206,1,0,0,0,206,7,1,0,0,0,207,205,1,0,0,0,208,210,
        5,36,0,0,209,211,5,46,0,0,210,209,1,0,0,0,210,211,1,0,0,0,211,212,
        1,0,0,0,212,213,3,12,6,0,213,214,5,37,0,0,214,9,1,0,0,0,215,217,
        5,36,0,0,216,218,5,46,0,0,217,216,1,0,0,0,217,218,1,0,0,0,218,219,
        1,0,0,0,219,220,3,14,7,0,220,221,5,37,0,0,221,11,1,0,0,0,222,227,
        3,16,8,0,223,224,5,46,0,0,224,226,3,16,8,0,225,223,1,0,0,0,226,229,
        1,0,0,0,227,225,1,0,0,0,227,228,1,0,0,0,228,13,1,0,0,0,229,227,1,
        0,0,0,230,235,3,18,9,0,231,232,5,46,0,0,232,234,3,18,9,0,233,231,
        1,0,0,0,234,237,1,0,0,0,235,233,1,0,0,0,235,236,1,0,0,0,236,15,1,
        0,0,0,237,235,1,0,0,0,238,240,3,20,10,0,239,238,1,0,0,0,240,241,
        1,0,0,0,241,239,1,0,0,0,241,242,1,0,0,0,242,245,1,0,0,0,243,244,
        5,38,0,0,244,246,3,28,14,0,245,243,1,0,0,0,245,246,1,0,0,0,246,17,
        1,0,0,0,247,249,3,34,17,0,248,247,1,0,0,0,249,250,1,0,0,0,250,248,
        1,0,0,0,250,251,1,0,0,0,251,19,1,0,0,0,252,254,3,42,21,0,253,252,
        1,0,0,0,253,254,1,0,0,0,254,255,1,0,0,0,255,257,3,22,11,0,256,258,
        3,148,74,0,257,256,1,0,0,0,257,258,1,0,0,0,258,21,1,0,0,0,259,263,
        3,8,4,0,260,263,3,24,12,0,261,263,3,26,13,0,262,259,1,0,0,0,262,
        260,1,0,0,0,262,261,1,0,0,0,263,23,1,0,0,0,264,265,7,0,0,0,265,25,
        1,0,0,0,266,267,5,11,0,0,267,27,1,0,0,0,268,270,5,47,0,0,269,268,
        1,0,0,0,269,270,1,0,0,0,270,271,1,0,0,0,271,273,3,172,86,0,272,274,
        3,30,15,0,273,272,1,0,0,0,273,274,1,0,0,0,274,29,1,0,0,0,275,277,
        5,36,0,0,276,278,3,32,16,0,277,276,1,0,0,0,277,278,1,0,0,0,278,279,
        1,0,0,0,279,280,5,37,0,0,280,31,1,0,0,0,281,286,3,28,14,0,282,283,
        5,34,0,0,283,285,3,28,14,0,284,282,1,0,0,0,285,288,1,0,0,0,286,284,
        1,0,0,0,286,287,1,0,0,0,287,290,1,0,0,0,288,286,1,0,0,0,289,291,
        5,34,0,0,290,289,1,0,0,0,290,291,1,0,0,0,291,33,1,0,0,0,292,294,
        3,42,21,0,293,292,1,0,0,0,293,294,1,0,0,0,294,295,1,0,0,0,295,297,
        3,36,18,0,296,298,3,148,74,0,297,296,1,0,0,0,297,298,1,0,0,0,298,
        35,1,0,0,0,299,303,3,10,5,0,300,303,3,38,19,0,301,303,3,40,20,0,
        302,299,1,0,0,0,302,300,1,0,0,0,302,301,1,0,0,0,303,37,1,0,0,0,304,
        305,5,1,0,0,305,39,1,0,0,0,306,307,7,1,0,0,307,41,1,0,0,0,308,309,
        3,172,86,0,309,310,3,44,22,0,310,43,1,0,0,0,311,312,7,2,0,0,312,
        45,1,0,0,0,313,317,3,48,24,0,314,316,3,52,26,0,315,314,1,0,0,0,316,
        319,1,0,0,0,317,315,1,0,0,0,317,318,1,0,0,0,318,320,1,0,0,0,319,
        317,1,0,0,0,320,324,3,80,40,0,321,323,3,78,39,0,322,321,1,0,0,0,
        323,326,1,0,0,0,324,322,1,0,0,0,324,325,1,0,0,0,325,327,1,0,0,0,
        326,324,1,0,0,0,327,328,5,0,0,1,328,47,1,0,0,0,329,330,3,50,25,0,
        330,331,3,172,86,0,331,332,5,35,0,0,332,49,1,0,0,0,333,334,5,20,
        0,0,334,339,5,22,0,0,335,336,5,21,0,0,336,339,5,22,0,0,337,339,5,
        22,0,0,338,333,1,0,0,0,338,335,1,0,0,0,338,337,1,0,0,0,339,51,1,
        0,0,0,340,346,3,54,27,0,341,346,3,60,30,0,342,346,3,64,32,0,343,
        346,3,66,33,0,344,346,3,70,35,0,345,340,1,0,0,0,345,341,1,0,0,0,
        345,342,1,0,0,0,345,343,1,0,0,0,345,344,1,0,0,0,346,53,1,0,0,0,347,
        353,5,15,0,0,348,349,3,56,28,0,349,350,5,35,0,0,350,352,1,0,0,0,
        351,348,1,0,0,0,352,355,1,0,0,0,353,351,1,0,0,0,353,354,1,0,0,0,
        354,356,1,0,0,0,355,353,1,0,0,0,356,357,5,5,0,0,357,55,1,0,0,0,358,
        359,3,172,86,0,359,360,5,41,0,0,360,361,3,58,29,0,361,57,1,0,0,0,
        362,367,3,172,86,0,363,364,5,49,0,0,364,366,3,172,86,0,365,363,1,
        0,0,0,366,369,1,0,0,0,367,365,1,0,0,0,367,368,1,0,0,0,368,374,1,
        0,0,0,369,367,1,0,0,0,370,374,5,11,0,0,371,374,3,74,37,0,372,374,
        5,10,0,0,373,362,1,0,0,0,373,370,1,0,0,0,373,371,1,0,0,0,373,372,
        1,0,0,0,374,59,1,0,0,0,375,376,5,18,0,0,376,381,3,62,31,0,377,378,
        5,34,0,0,378,380,3,62,31,0,379,377,1,0,0,0,380,383,1,0,0,0,381,379,
        1,0,0,0,381,382,1,0,0,0,382,384,1,0,0,0,383,381,1,0,0,0,384,385,
        5,35,0,0,385,61,1,0,0,0,386,387,3,172,86,0,387,388,5,41,0,0,388,
        389,3,172,86,0,389,392,1,0,0,0,390,392,3,172,86,0,391,386,1,0,0,
        0,391,390,1,0,0,0,392,63,1,0,0,0,393,395,5,16,0,0,394,396,3,68,34,
        0,395,394,1,0,0,0,395,396,1,0,0,0,396,397,1,0,0,0,397,398,5,5,0,
        0,398,65,1,0,0,0,399,401,5,17,0,0,400,402,3,68,34,0,401,400,1,0,
        0,0,401,402,1,0,0,0,402,403,1,0,0,0,403,404,5,5,0,0,404,67,1,0,0,
        0,405,410,3,172,86,0,406,407,5,34,0,0,407,409,3,172,86,0,408,406,
        1,0,0,0,409,412,1,0,0,0,410,408,1,0,0,0,410,411,1,0,0,0,411,414,
        1,0,0,0,412,410,1,0,0,0,413,415,5,34,0,0,414,413,1,0,0,0,414,415,
        1,0,0,0,415,69,1,0,0,0,416,420,5,50,0,0,417,418,3,72,36,0,418,419,
        5,33,0,0,419,421,1,0,0,0,420,417,1,0,0,0,420,421,1,0,0,0,421,422,
        1,0,0,0,422,423,3,172,86,0,423,424,3,74,37,0,424,71,1,0,0,0,425,
        429,3,172,86,0,426,429,5,20,0,0,427,429,5,21,0,0,428,425,1,0,0,0,
        428,426,1,0,0,0,428,427,1,0,0,0,429,73,1,0,0,0,430,434,5,14,0,0,
        431,433,5,61,0,0,432,431,1,0,0,0,433,436,1,0,0,0,434,432,1,0,0,0,
        434,435,1,0,0,0,435,437,1,0,0,0,436,434,1,0,0,0,437,438,5,59,0,0,
        438,75,1,0,0,0,439,443,5,13,0,0,440,442,5,58,0,0,441,440,1,0,0,0,
        442,445,1,0,0,0,443,441,1,0,0,0,443,444,1,0,0,0,444,446,1,0,0,0,
        445,443,1,0,0,0,446,447,5,56,0,0,447,77,1,0,0,0,448,449,5,31,0,0,
        449,450,3,172,86,0,450,454,5,35,0,0,451,453,3,112,56,0,452,451,1,
        0,0,0,453,456,1,0,0,0,454,452,1,0,0,0,454,455,1,0,0,0,455,79,1,0,
        0,0,456,454,1,0,0,0,457,459,3,82,41,0,458,457,1,0,0,0,459,462,1,
        0,0,0,460,458,1,0,0,0,460,461,1,0,0,0,461,81,1,0,0,0,462,460,1,0,
        0,0,463,466,3,84,42,0,464,466,3,112,56,0,465,463,1,0,0,0,465,464,
        1,0,0,0,466,83,1,0,0,0,467,469,3,102,51,0,468,467,1,0,0,0,468,469,
        1,0,0,0,469,470,1,0,0,0,470,472,5,2,0,0,471,473,3,76,38,0,472,471,
        1,0,0,0,472,473,1,0,0,0,473,475,1,0,0,0,474,476,3,94,47,0,475,474,
        1,0,0,0,475,476,1,0,0,0,476,478,1,0,0,0,477,479,3,96,48,0,478,477,
        1,0,0,0,478,479,1,0,0,0,479,481,1,0,0,0,480,482,3,98,49,0,481,480,
        1,0,0,0,481,482,1,0,0,0,482,486,1,0,0,0,483,485,3,92,46,0,484,483,
        1,0,0,0,485,488,1,0,0,0,486,484,1,0,0,0,486,487,1,0,0,0,487,489,
        1,0,0,0,488,486,1,0,0,0,489,490,5,32,0,0,490,491,3,106,53,0,491,
        492,5,35,0,0,492,493,3,86,43,0,493,85,1,0,0,0,494,496,3,88,44,0,
        495,494,1,0,0,0,496,499,1,0,0,0,497,495,1,0,0,0,497,498,1,0,0,0,
        498,501,1,0,0,0,499,497,1,0,0,0,500,502,3,90,45,0,501,500,1,0,0,
        0,501,502,1,0,0,0,502,87,1,0,0,0,503,504,5,29,0,0,504,505,3,76,38,
        0,505,506,3,74,37,0,506,89,1,0,0,0,507,508,5,30,0,0,508,509,3,74,
        37,0,509,91,1,0,0,0,510,513,3,54,27,0,511,513,3,100,50,0,512,510,
        1,0,0,0,512,511,1,0,0,0,513,93,1,0,0,0,514,515,5,26,0,0,515,516,
        3,76,38,0,516,95,1,0,0,0,517,518,5,28,0,0,518,523,3,172,86,0,519,
        520,5,34,0,0,520,522,3,172,86,0,521,519,1,0,0,0,522,525,1,0,0,0,
        523,521,1,0,0,0,523,524,1,0,0,0,524,97,1,0,0,0,525,523,1,0,0,0,526,
        527,5,27,0,0,527,528,3,76,38,0,528,99,1,0,0,0,529,530,5,50,0,0,530,
        531,3,172,86,0,531,532,3,74,37,0,532,101,1,0,0,0,533,535,3,104,52,
        0,534,533,1,0,0,0,535,536,1,0,0,0,536,534,1,0,0,0,536,537,1,0,0,
        0,537,103,1,0,0,0,538,539,7,3,0,0,539,105,1,0,0,0,540,541,3,108,
        54,0,541,107,1,0,0,0,542,547,3,110,55,0,543,544,5,46,0,0,544,546,
        3,110,55,0,545,543,1,0,0,0,546,549,1,0,0,0,547,545,1,0,0,0,547,548,
        1,0,0,0,548,109,1,0,0,0,549,547,1,0,0,0,550,553,3,138,69,0,551,552,
        5,51,0,0,552,554,3,172,86,0,553,551,1,0,0,0,553,554,1,0,0,0,554,
        111,1,0,0,0,555,557,5,19,0,0,556,555,1,0,0,0,556,557,1,0,0,0,557,
        558,1,0,0,0,558,560,5,1,0,0,559,561,3,54,27,0,560,559,1,0,0,0,560,
        561,1,0,0,0,561,562,1,0,0,0,562,563,5,32,0,0,563,564,3,114,57,0,
        564,565,5,35,0,0,565,113,1,0,0,0,566,567,3,116,58,0,567,115,1,0,
        0,0,568,573,3,118,59,0,569,570,5,46,0,0,570,572,3,118,59,0,571,569,
        1,0,0,0,572,575,1,0,0,0,573,571,1,0,0,0,573,574,1,0,0,0,574,117,
        1,0,0,0,575,573,1,0,0,0,576,578,3,120,60,0,577,579,3,128,64,0,578,
        577,1,0,0,0,578,579,1,0,0,0,579,582,1,0,0,0,580,582,1,0,0,0,581,
        576,1,0,0,0,581,580,1,0,0,0,582,119,1,0,0,0,583,585,3,122,61,0,584,
        583,1,0,0,0,585,586,1,0,0,0,586,584,1,0,0,0,586,587,1,0,0,0,587,
        590,1,0,0,0,588,590,1,0,0,0,589,584,1,0,0,0,589,588,1,0,0,0,590,
        121,1,0,0,0,591,593,3,124,62,0,592,594,3,148,74,0,593,592,1,0,0,
        0,593,594,1,0,0,0,594,608,1,0,0,0,595,597,3,150,75,0,596,598,3,148,
        74,0,597,596,1,0,0,0,597,598,1,0,0,0,598,608,1,0,0,0,599,601,3,126,
        63,0,600,602,3,148,74,0,601,600,1,0,0,0,601,602,1,0,0,0,602,608,
        1,0,0,0,603,605,3,74,37,0,604,606,5,42,0,0,605,604,1,0,0,0,605,606,
        1,0,0,0,606,608,1,0,0,0,607,591,1,0,0,0,607,595,1,0,0,0,607,599,
        1,0,0,0,607,603,1,0,0,0,608,123,1,0,0,0,609,610,3,172,86,0,610,613,
        7,2,0,0,611,614,3,150,75,0,612,614,3,126,63,0,613,611,1,0,0,0,613,
        612,1,0,0,0,614,125,1,0,0,0,615,616,5,36,0,0,616,617,3,116,58,0,
        617,618,5,37,0,0,618,127,1,0,0,0,619,620,5,38,0,0,620,625,3,130,
        65,0,621,622,5,34,0,0,622,624,3,130,65,0,623,621,1,0,0,0,624,627,
        1,0,0,0,625,623,1,0,0,0,625,626,1,0,0,0,626,129,1,0,0,0,627,625,
        1,0,0,0,628,629,3,132,66,0,629,630,5,36,0,0,630,631,3,134,67,0,631,
        632,5,37,0,0,632,635,1,0,0,0,633,635,3,132,66,0,634,628,1,0,0,0,
        634,633,1,0,0,0,635,131,1,0,0,0,636,639,3,172,86,0,637,639,5,31,
        0,0,638,636,1,0,0,0,638,637,1,0,0,0,639,133,1,0,0,0,640,643,3,172,
        86,0,641,643,5,10,0,0,642,640,1,0,0,0,642,641,1,0,0,0,643,135,1,
        0,0,0,644,649,3,138,69,0,645,646,5,46,0,0,646,648,3,138,69,0,647,
        645,1,0,0,0,648,651,1,0,0,0,649,647,1,0,0,0,649,650,1,0,0,0,650,
        137,1,0,0,0,651,649,1,0,0,0,652,654,3,168,84,0,653,652,1,0,0,0,653,
        654,1,0,0,0,654,656,1,0,0,0,655,657,3,140,70,0,656,655,1,0,0,0,657,
        658,1,0,0,0,658,656,1,0,0,0,658,659,1,0,0,0,659,662,1,0,0,0,660,
        662,1,0,0,0,661,653,1,0,0,0,661,660,1,0,0,0,662,139,1,0,0,0,663,
        666,3,142,71,0,664,667,3,148,74,0,665,667,1,0,0,0,666,664,1,0,0,
        0,666,665,1,0,0,0,667,679,1,0,0,0,668,671,3,152,76,0,669,672,3,148,
        74,0,670,672,1,0,0,0,671,669,1,0,0,0,671,670,1,0,0,0,672,679,1,0,
        0,0,673,679,3,144,72,0,674,676,3,74,37,0,675,677,5,42,0,0,676,675,
        1,0,0,0,676,677,1,0,0,0,677,679,1,0,0,0,678,663,1,0,0,0,678,668,
        1,0,0,0,678,673,1,0,0,0,678,674,1,0,0,0,679,141,1,0,0,0,680,681,
        3,172,86,0,681,684,7,2,0,0,682,685,3,152,76,0,683,685,3,160,80,0,
        684,682,1,0,0,0,684,683,1,0,0,0,685,143,1,0,0,0,686,688,3,160,80,
        0,687,689,3,146,73,0,688,687,1,0,0,0,688,689,1,0,0,0,689,145,1,0,
        0,0,690,691,3,148,74,0,691,147,1,0,0,0,692,694,5,42,0,0,693,695,
        5,42,0,0,694,693,1,0,0,0,694,695,1,0,0,0,695,705,1,0,0,0,696,698,
        5,43,0,0,697,699,5,42,0,0,698,697,1,0,0,0,698,699,1,0,0,0,699,705,
        1,0,0,0,700,702,5,45,0,0,701,703,5,42,0,0,702,701,1,0,0,0,702,703,
        1,0,0,0,703,705,1,0,0,0,704,692,1,0,0,0,704,696,1,0,0,0,704,700,
        1,0,0,0,705,149,1,0,0,0,706,715,3,164,82,0,707,715,3,166,83,0,708,
        715,3,154,77,0,709,715,5,3,0,0,710,712,5,49,0,0,711,713,3,168,84,
        0,712,711,1,0,0,0,712,713,1,0,0,0,713,715,1,0,0,0,714,706,1,0,0,
        0,714,707,1,0,0,0,714,708,1,0,0,0,714,709,1,0,0,0,714,710,1,0,0,
        0,715,151,1,0,0,0,716,724,3,166,83,0,717,724,3,162,81,0,718,724,
        3,154,77,0,719,721,5,49,0,0,720,722,3,168,84,0,721,720,1,0,0,0,721,
        722,1,0,0,0,722,724,1,0,0,0,723,716,1,0,0,0,723,717,1,0,0,0,723,
        718,1,0,0,0,723,719,1,0,0,0,724,153,1,0,0,0,725,726,5,52,0,0,726,
        730,3,158,79,0,727,728,5,52,0,0,728,730,3,156,78,0,729,725,1,0,0,
        0,729,727,1,0,0,0,730,155,1,0,0,0,731,732,5,36,0,0,732,737,3,158,
        79,0,733,734,5,46,0,0,734,736,3,158,79,0,735,733,1,0,0,0,736,739,
        1,0,0,0,737,735,1,0,0,0,737,738,1,0,0,0,738,740,1,0,0,0,739,737,
        1,0,0,0,740,741,5,37,0,0,741,157,1,0,0,0,742,744,5,1,0,0,743,745,
        3,168,84,0,744,743,1,0,0,0,744,745,1,0,0,0,745,753,1,0,0,0,746,748,
        5,11,0,0,747,749,3,168,84,0,748,747,1,0,0,0,748,749,1,0,0,0,749,
        753,1,0,0,0,750,753,3,164,82,0,751,753,5,3,0,0,752,742,1,0,0,0,752,
        746,1,0,0,0,752,750,1,0,0,0,752,751,1,0,0,0,753,159,1,0,0,0,754,
        765,5,36,0,0,755,757,3,54,27,0,756,755,1,0,0,0,756,757,1,0,0,0,757,
        761,1,0,0,0,758,760,3,100,50,0,759,758,1,0,0,0,760,763,1,0,0,0,761,
        759,1,0,0,0,761,762,1,0,0,0,762,764,1,0,0,0,763,761,1,0,0,0,764,
        766,5,32,0,0,765,756,1,0,0,0,765,766,1,0,0,0,766,767,1,0,0,0,767,
        768,3,136,68,0,768,769,5,37,0,0,769,161,1,0,0,0,770,772,5,2,0,0,
        771,773,3,76,38,0,772,771,1,0,0,0,772,773,1,0,0,0,773,775,1,0,0,
        0,774,776,3,168,84,0,775,774,1,0,0,0,775,776,1,0,0,0,776,163,1,0,
        0,0,777,778,5,11,0,0,778,779,5,48,0,0,779,780,5,11,0,0,780,165,1,
        0,0,0,781,783,5,1,0,0,782,784,3,168,84,0,783,782,1,0,0,0,783,784,
        1,0,0,0,784,790,1,0,0,0,785,787,5,11,0,0,786,788,3,168,84,0,787,
        786,1,0,0,0,787,788,1,0,0,0,788,790,1,0,0,0,789,781,1,0,0,0,789,
        785,1,0,0,0,790,167,1,0,0,0,791,792,5,39,0,0,792,797,3,170,85,0,
        793,794,5,34,0,0,794,796,3,170,85,0,795,793,1,0,0,0,796,799,1,0,
        0,0,797,795,1,0,0,0,797,798,1,0,0,0,798,800,1,0,0,0,799,797,1,0,
        0,0,800,801,5,40,0,0,801,169,1,0,0,0,802,810,3,172,86,0,803,804,
        3,172,86,0,804,807,5,41,0,0,805,808,3,172,86,0,806,808,5,11,0,0,
        807,805,1,0,0,0,807,806,1,0,0,0,808,810,1,0,0,0,809,802,1,0,0,0,
        809,803,1,0,0,0,810,171,1,0,0,0,811,812,7,0,0,0,812,173,1,0,0,0,
        108,176,178,185,192,196,205,210,217,227,235,241,245,250,253,257,
        262,269,273,277,286,290,293,297,302,317,324,338,345,353,367,373,
        381,391,395,401,410,414,420,428,434,443,454,460,465,468,472,475,
        478,481,486,497,501,512,523,536,547,553,556,560,573,578,581,586,
        589,593,597,601,605,607,613,625,634,638,642,649,653,658,661,666,
        671,676,678,684,688,694,698,702,704,712,714,721,723,729,737,744,
        748,752,756,761,765,772,775,783,787,789,797,807,809
    ]

class ctx2lParser ( Parser ):

    grammarFileName = "ctx2lParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'>>'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'import'", "'fragment'", "'lexer'", "'parser'", 
                     "'grammar'", "'protected'", "'public'", "'private'", 
                     "'returns'", "'locals'", "'throws'", "'catch'", "'finally'", 
                     "'mode'" ]

    symbolicNames = [ "<INVALID>", "TOKEN_REF", "RULE_REF", "LEXER_CHAR_SET", 
                      "LBRACE", "RBRACE", "DIRECT", "DOC_COMMENT", "BLOCK_COMMENT", 
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
    RULE_tokenCommands = 3
    RULE_ruleSub = 4
    RULE_tokenSub = 5
    RULE_ruleAlts = 6
    RULE_tokenAlts = 7
    RULE_ruleAlt = 8
    RULE_tokenAlt = 9
    RULE_ruleAtom = 10
    RULE_ruleTerm = 11
    RULE_ruleRef = 12
    RULE_ruleLiteral = 13
    RULE_expr = 14
    RULE_call = 15
    RULE_args = 16
    RULE_tokenAtom = 17
    RULE_tokenTerm = 18
    RULE_tokenRef = 19
    RULE_tokenLiteral = 20
    RULE_label = 21
    RULE_assign = 22
    RULE_grammarSpec = 23
    RULE_grammarDecl = 24
    RULE_grammarType = 25
    RULE_prequelConstruct = 26
    RULE_optionsSpec = 27
    RULE_option = 28
    RULE_optionValue = 29
    RULE_delegateGrammars = 30
    RULE_delegateGrammar = 31
    RULE_tokensSpec = 32
    RULE_channelsSpec = 33
    RULE_idList = 34
    RULE_action_ = 35
    RULE_actionScopeName = 36
    RULE_actionBlock = 37
    RULE_argActionBlock = 38
    RULE_modeSpec = 39
    RULE_rules = 40
    RULE_ruleSpec = 41
    RULE_parserRuleSpec = 42
    RULE_exceptionGroup = 43
    RULE_exceptionHandler = 44
    RULE_finallyClause = 45
    RULE_rulePrequel = 46
    RULE_ruleReturns = 47
    RULE_throwsSpec = 48
    RULE_localsSpec = 49
    RULE_ruleAction = 50
    RULE_ruleModifiers = 51
    RULE_ruleModifier = 52
    RULE_ruleBlock = 53
    RULE_ruleAltList = 54
    RULE_labeledAlt = 55
    RULE_lexerRuleSpec = 56
    RULE_lexerRuleBlock = 57
    RULE_lexerAltList = 58
    RULE_lexerAlt = 59
    RULE_lexerElements = 60
    RULE_lexerElement = 61
    RULE_labeledLexerElement = 62
    RULE_lexerBlock = 63
    RULE_lexerCommands = 64
    RULE_lexerCommand = 65
    RULE_lexerCommandName = 66
    RULE_lexerCommandExpr = 67
    RULE_altList = 68
    RULE_alternative = 69
    RULE_element = 70
    RULE_labeledElement = 71
    RULE_ebnf = 72
    RULE_blockSuffix = 73
    RULE_ebnfSuffix = 74
    RULE_lexerAtom = 75
    RULE_atom = 76
    RULE_notSet = 77
    RULE_blockSet = 78
    RULE_setElement = 79
    RULE_block = 80
    RULE_ruleref = 81
    RULE_characterRange = 82
    RULE_terminal = 83
    RULE_elementOptions = 84
    RULE_elementOption = 85
    RULE_identifier = 86

    ruleNames =  [ "program", "ruleDef", "tokenDef", "tokenCommands", "ruleSub", 
                   "tokenSub", "ruleAlts", "tokenAlts", "ruleAlt", "tokenAlt", 
                   "ruleAtom", "ruleTerm", "ruleRef", "ruleLiteral", "expr", 
                   "call", "args", "tokenAtom", "tokenTerm", "tokenRef", 
                   "tokenLiteral", "label", "assign", "grammarSpec", "grammarDecl", 
                   "grammarType", "prequelConstruct", "optionsSpec", "option", 
                   "optionValue", "delegateGrammars", "delegateGrammar", 
                   "tokensSpec", "channelsSpec", "idList", "action_", "actionScopeName", 
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
    DIRECT=6
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
        self.checkVersion("4.13.0")
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
            self.state = 176 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 176
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [2]:
                    self.state = 174
                    self.ruleDef()
                    pass
                elif token in [1]:
                    self.state = 175
                    self.tokenDef()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 178 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==2):
                    break

            self.state = 180
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
            self.state = 182
            self.match(ctx2lParser.RULE_REF)
            self.state = 183
            self.match(ctx2lParser.COLON)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 184
                self.match(ctx2lParser.OR)


            self.state = 187
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


        def DIRECT(self):
            return self.getToken(ctx2lParser.DIRECT, 0)

        def tokenCommands(self):
            return self.getTypedRuleContext(ctx2lParser.TokenCommandsContext,0)


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
            self.state = 189
            self.match(ctx2lParser.TOKEN_REF)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 190
                self.match(ctx2lParser.DIRECT)
                self.state = 191
                self.tokenCommands()


            self.state = 194
            self.match(ctx2lParser.COLON)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 195
                self.match(ctx2lParser.OR)


            self.state = 198
            self.tokenAlts()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TokenCommandsContext(RuleContextWithAltNum):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
            return ctx2lParser.RULE_tokenCommands

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTokenCommands" ):
                return visitor.visitTokenCommands(self)
            else:
                return visitor.visitChildren(self)




    def tokenCommands(self):

        localctx = ctx2lParser.TokenCommandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tokenCommands)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.lexerCommand()
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 201
                self.match(ctx2lParser.COMMA)
                self.state = 202
                self.lexerCommand()
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
        self.enterRule(localctx, 8, self.RULE_ruleSub)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(ctx2lParser.LPAREN)
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 209
                self.match(ctx2lParser.OR)


            self.state = 212
            self.ruleAlts()
            self.state = 213
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
        self.enterRule(localctx, 10, self.RULE_tokenSub)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(ctx2lParser.LPAREN)
            self.state = 217
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 216
                self.match(ctx2lParser.OR)


            self.state = 219
            self.tokenAlts()
            self.state = 220
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
        self.enterRule(localctx, 12, self.RULE_ruleAlts)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.ruleAlt()
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 223
                self.match(ctx2lParser.OR)
                self.state = 224
                self.ruleAlt()
                self.state = 229
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
        self.enterRule(localctx, 14, self.RULE_tokenAlts)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.tokenAlt()
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 231
                self.match(ctx2lParser.OR)
                self.state = 232
                self.tokenAlt()
                self.state = 237
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


        def RARROW(self):
            return self.getToken(ctx2lParser.RARROW, 0)

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
        self.enterRule(localctx, 16, self.RULE_ruleAlt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 238
                    self.ruleAtom()

                else:
                    raise NoViableAltException(self)
                self.state = 241 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 243
                self.match(ctx2lParser.RARROW)
                self.state = 244
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
        self.enterRule(localctx, 18, self.RULE_tokenAlt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 247
                    self.tokenAtom()

                else:
                    raise NoViableAltException(self)
                self.state = 250 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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

        def ruleTerm(self):
            return self.getTypedRuleContext(ctx2lParser.RuleTermContext,0)


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
        self.enterRule(localctx, 20, self.RULE_ruleAtom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 252
                self.label()


            self.state = 255
            self.ruleTerm()
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 48378511622144) != 0):
                self.state = 256
                self.ebnfSuffix()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleTermContext(RuleContextWithAltNum):
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
            return ctx2lParser.RULE_ruleTerm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRuleTerm" ):
                return visitor.visitRuleTerm(self)
            else:
                return visitor.visitChildren(self)




    def ruleTerm(self):

        localctx = ctx2lParser.RuleTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ruleTerm)
        try:
            self.state = 262
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.ruleSub()
                pass
            elif token in [1, 2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.ruleRef()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 261
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
        self.enterRule(localctx, 24, self.RULE_ruleRef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
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
        self.enterRule(localctx, 26, self.RULE_ruleLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
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
        self.enterRule(localctx, 28, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47:
                self.state = 268
                self.match(ctx2lParser.DOLLAR)


            self.state = 271
            self.identifier()
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 272
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
        self.enterRule(localctx, 30, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(ctx2lParser.LPAREN)
            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 140737488355334) != 0):
                self.state = 276
                self.args()


            self.state = 279
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
        self.enterRule(localctx, 32, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.expr()
            self.state = 286
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 282
                    self.match(ctx2lParser.COMMA)
                    self.state = 283
                    self.expr() 
                self.state = 288
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 289
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

        def tokenTerm(self):
            return self.getTypedRuleContext(ctx2lParser.TokenTermContext,0)


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
        self.enterRule(localctx, 34, self.RULE_tokenAtom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 292
                self.label()


            self.state = 295
            self.tokenTerm()
            self.state = 297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 48378511622144) != 0):
                self.state = 296
                self.ebnfSuffix()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TokenTermContext(RuleContextWithAltNum):
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
            return ctx2lParser.RULE_tokenTerm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTokenTerm" ):
                return visitor.visitTokenTerm(self)
            else:
                return visitor.visitChildren(self)




    def tokenTerm(self):

        localctx = ctx2lParser.TokenTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_tokenTerm)
        try:
            self.state = 302
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 299
                self.tokenSub()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 300
                self.tokenRef()
                pass
            elif token in [3, 11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 301
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
        self.enterRule(localctx, 38, self.RULE_tokenRef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
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
        self.enterRule(localctx, 40, self.RULE_tokenLiteral)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
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
        self.enterRule(localctx, 42, self.RULE_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.identifier()
            self.state = 309
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
        self.enterRule(localctx, 44, self.RULE_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 311
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
        self.enterRule(localctx, 46, self.RULE_grammarSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.grammarDecl()
            self.state = 317
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1125899907334144) != 0):
                self.state = 314
                self.prequelConstruct()
                self.state = 319
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 320
            self.rules()
            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31:
                self.state = 321
                self.modeSpec()
                self.state = 326
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 327
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
        self.enterRule(localctx, 48, self.RULE_grammarDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.grammarType()
            self.state = 330
            self.identifier()
            self.state = 331
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
        self.enterRule(localctx, 50, self.RULE_grammarType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                self.state = 333
                self.match(ctx2lParser.LEXER)
                self.state = 334
                self.match(ctx2lParser.GRAMMAR)
                pass
            elif token in [21]:
                self.state = 335
                self.match(ctx2lParser.PARSER)
                self.state = 336
                self.match(ctx2lParser.GRAMMAR)
                pass
            elif token in [22]:
                self.state = 337
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
        self.enterRule(localctx, 52, self.RULE_prequelConstruct)
        try:
            self.state = 345
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 340
                self.optionsSpec()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.delegateGrammars()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 342
                self.tokensSpec()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 4)
                self.state = 343
                self.channelsSpec()
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 5)
                self.state = 344
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
        self.enterRule(localctx, 54, self.RULE_optionsSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.match(ctx2lParser.OPTIONS)
            self.state = 353
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==2:
                self.state = 348
                self.option()
                self.state = 349
                self.match(ctx2lParser.SEMI)
                self.state = 355
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 356
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
        self.enterRule(localctx, 56, self.RULE_option)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.identifier()
            self.state = 359
            self.match(ctx2lParser.ASSIGN)
            self.state = 360
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
        self.enterRule(localctx, 58, self.RULE_optionValue)
        self._la = 0 # Token type
        try:
            self.state = 373
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.identifier()
                self.state = 367
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==49:
                    self.state = 363
                    self.match(ctx2lParser.DOT)
                    self.state = 364
                    self.identifier()
                    self.state = 369
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.match(ctx2lParser.STRING_LITERAL)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 371
                self.actionBlock()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 372
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
        self.enterRule(localctx, 60, self.RULE_delegateGrammars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(ctx2lParser.IMPORT)
            self.state = 376
            self.delegateGrammar()
            self.state = 381
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 377
                self.match(ctx2lParser.COMMA)
                self.state = 378
                self.delegateGrammar()
                self.state = 383
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 384
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
        self.enterRule(localctx, 62, self.RULE_delegateGrammar)
        try:
            self.state = 391
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 386
                self.identifier()
                self.state = 387
                self.match(ctx2lParser.ASSIGN)
                self.state = 388
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 390
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
        self.enterRule(localctx, 64, self.RULE_tokensSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 393
            self.match(ctx2lParser.TOKENS)
            self.state = 395
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==2:
                self.state = 394
                self.idList()


            self.state = 397
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
        self.enterRule(localctx, 66, self.RULE_channelsSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 399
            self.match(ctx2lParser.CHANNELS)
            self.state = 401
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==2:
                self.state = 400
                self.idList()


            self.state = 403
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
        self.enterRule(localctx, 68, self.RULE_idList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 405
            self.identifier()
            self.state = 410
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 406
                    self.match(ctx2lParser.COMMA)
                    self.state = 407
                    self.identifier() 
                self.state = 412
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

            self.state = 414
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 413
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
        self.enterRule(localctx, 70, self.RULE_action_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 416
            self.match(ctx2lParser.AT)
            self.state = 420
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 417
                self.actionScopeName()
                self.state = 418
                self.match(ctx2lParser.COLONCOLON)


            self.state = 422
            self.identifier()
            self.state = 423
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
        self.enterRule(localctx, 72, self.RULE_actionScopeName)
        try:
            self.state = 428
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 425
                self.identifier()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 426
                self.match(ctx2lParser.LEXER)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 427
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
        self.enterRule(localctx, 74, self.RULE_actionBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            self.match(ctx2lParser.BEGIN_ACTION)
            self.state = 434
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==61:
                self.state = 431
                self.match(ctx2lParser.ACTION_CONTENT)
                self.state = 436
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 437
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
        self.enterRule(localctx, 76, self.RULE_argActionBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 439
            self.match(ctx2lParser.BEGIN_ARGUMENT)
            self.state = 443
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==58:
                self.state = 440
                self.match(ctx2lParser.ARGUMENT_CONTENT)
                self.state = 445
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 446
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
        self.enterRule(localctx, 78, self.RULE_modeSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 448
            self.match(ctx2lParser.MODE)
            self.state = 449
            self.identifier()
            self.state = 450
            self.match(ctx2lParser.SEMI)
            self.state = 454
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==19:
                self.state = 451
                self.lexerRuleSpec()
                self.state = 456
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
        self.enterRule(localctx, 80, self.RULE_rules)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 59244550) != 0):
                self.state = 457
                self.ruleSpec()
                self.state = 462
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
        self.enterRule(localctx, 82, self.RULE_ruleSpec)
        try:
            self.state = 465
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 463
                self.parserRuleSpec()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 464
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
        self.enterRule(localctx, 84, self.RULE_parserRuleSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 59244544) != 0):
                self.state = 467
                self.ruleModifiers()


            self.state = 470
            self.match(ctx2lParser.RULE_REF)
            self.state = 472
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 471
                self.argActionBlock()


            self.state = 475
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 474
                self.ruleReturns()


            self.state = 478
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==28:
                self.state = 477
                self.throwsSpec()


            self.state = 481
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 480
                self.localsSpec()


            self.state = 486
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==15 or _la==50:
                self.state = 483
                self.rulePrequel()
                self.state = 488
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 489
            self.match(ctx2lParser.COLON)
            self.state = 490
            self.ruleBlock()
            self.state = 491
            self.match(ctx2lParser.SEMI)
            self.state = 492
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
        self.enterRule(localctx, 86, self.RULE_exceptionGroup)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 494
                self.exceptionHandler()
                self.state = 499
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 501
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 500
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
        self.enterRule(localctx, 88, self.RULE_exceptionHandler)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            self.match(ctx2lParser.CATCH)
            self.state = 504
            self.argActionBlock()
            self.state = 505
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
        self.enterRule(localctx, 90, self.RULE_finallyClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self.match(ctx2lParser.FINALLY)
            self.state = 508
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
        self.enterRule(localctx, 92, self.RULE_rulePrequel)
        try:
            self.state = 512
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 510
                self.optionsSpec()
                pass
            elif token in [50]:
                self.enterOuterAlt(localctx, 2)
                self.state = 511
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
        self.enterRule(localctx, 94, self.RULE_ruleReturns)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self.match(ctx2lParser.RETURNS)
            self.state = 515
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
        self.enterRule(localctx, 96, self.RULE_throwsSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self.match(ctx2lParser.THROWS)
            self.state = 518
            self.identifier()
            self.state = 523
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 519
                self.match(ctx2lParser.COMMA)
                self.state = 520
                self.identifier()
                self.state = 525
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
        self.enterRule(localctx, 98, self.RULE_localsSpec)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            self.match(ctx2lParser.LOCALS)
            self.state = 527
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
        self.enterRule(localctx, 100, self.RULE_ruleAction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
            self.match(ctx2lParser.AT)
            self.state = 530
            self.identifier()
            self.state = 531
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
        self.enterRule(localctx, 102, self.RULE_ruleModifiers)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 533
                self.ruleModifier()
                self.state = 536 
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
        self.enterRule(localctx, 104, self.RULE_ruleModifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
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
        self.enterRule(localctx, 106, self.RULE_ruleBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 540
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
        self.enterRule(localctx, 108, self.RULE_ruleAltList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.labeledAlt()
            self.state = 547
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 543
                self.match(ctx2lParser.OR)
                self.state = 544
                self.labeledAlt()
                self.state = 549
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
        self.enterRule(localctx, 110, self.RULE_labeledAlt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550
            self.alternative()
            self.state = 553
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==51:
                self.state = 551
                self.match(ctx2lParser.POUND)
                self.state = 552
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
        self.enterRule(localctx, 112, self.RULE_lexerRuleSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 555
                self.match(ctx2lParser.FRAGMENT)


            self.state = 558
            self.match(ctx2lParser.TOKEN_REF)
            self.state = 560
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 559
                self.optionsSpec()


            self.state = 562
            self.match(ctx2lParser.COLON)
            self.state = 563
            self.lexerRuleBlock()
            self.state = 564
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
        self.enterRule(localctx, 114, self.RULE_lexerRuleBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 566
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
        self.enterRule(localctx, 116, self.RULE_lexerAltList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568
            self.lexerAlt()
            self.state = 573
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 569
                self.match(ctx2lParser.OR)
                self.state = 570
                self.lexerAlt()
                self.state = 575
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
        self.enterRule(localctx, 118, self.RULE_lexerAlt)
        self._la = 0 # Token type
        try:
            self.state = 581
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 576
                self.lexerElements()
                self.state = 578
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==38:
                    self.state = 577
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
        self.enterRule(localctx, 120, self.RULE_lexerElements)
        self._la = 0 # Token type
        try:
            self.state = 589
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 11, 14, 36, 49, 52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 584 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 583
                    self.lexerElement()
                    self.state = 586 
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
        self.enterRule(localctx, 122, self.RULE_lexerElement)
        self._la = 0 # Token type
        try:
            self.state = 607
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 591
                self.labeledLexerElement()
                self.state = 593
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 48378511622144) != 0):
                    self.state = 592
                    self.ebnfSuffix()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 595
                self.lexerAtom()
                self.state = 597
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 48378511622144) != 0):
                    self.state = 596
                    self.ebnfSuffix()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 599
                self.lexerBlock()
                self.state = 601
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 48378511622144) != 0):
                    self.state = 600
                    self.ebnfSuffix()


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 603
                self.actionBlock()
                self.state = 605
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==42:
                    self.state = 604
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
        self.enterRule(localctx, 124, self.RULE_labeledLexerElement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 609
            self.identifier()
            self.state = 610
            _la = self._input.LA(1)
            if not(_la==41 or _la==44):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 613
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 3, 11, 49, 52]:
                self.state = 611
                self.lexerAtom()
                pass
            elif token in [36]:
                self.state = 612
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
        self.enterRule(localctx, 126, self.RULE_lexerBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 615
            self.match(ctx2lParser.LPAREN)
            self.state = 616
            self.lexerAltList()
            self.state = 617
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
        self.enterRule(localctx, 128, self.RULE_lexerCommands)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 619
            self.match(ctx2lParser.RARROW)
            self.state = 620
            self.lexerCommand()
            self.state = 625
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 621
                self.match(ctx2lParser.COMMA)
                self.state = 622
                self.lexerCommand()
                self.state = 627
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
        self.enterRule(localctx, 130, self.RULE_lexerCommand)
        try:
            self.state = 634
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 628
                self.lexerCommandName()
                self.state = 629
                self.match(ctx2lParser.LPAREN)
                self.state = 630
                self.lexerCommandExpr()
                self.state = 631
                self.match(ctx2lParser.RPAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 633
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
        self.enterRule(localctx, 132, self.RULE_lexerCommandName)
        try:
            self.state = 638
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 636
                self.identifier()
                pass
            elif token in [31]:
                self.enterOuterAlt(localctx, 2)
                self.state = 637
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
        self.enterRule(localctx, 134, self.RULE_lexerCommandExpr)
        try:
            self.state = 642
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 640
                self.identifier()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 641
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
        self.enterRule(localctx, 136, self.RULE_altList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 644
            self.alternative()
            self.state = 649
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 645
                self.match(ctx2lParser.OR)
                self.state = 646
                self.alternative()
                self.state = 651
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
        self.enterRule(localctx, 138, self.RULE_alternative)
        self._la = 0 # Token type
        try:
            self.state = 661
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 11, 14, 36, 39, 49, 52]:
                self.enterOuterAlt(localctx, 1)
                self.state = 653
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 652
                    self.elementOptions()


                self.state = 656 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 655
                    self.element()
                    self.state = 658 
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
        self.enterRule(localctx, 140, self.RULE_element)
        self._la = 0 # Token type
        try:
            self.state = 678
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,81,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 663
                self.labeledElement()
                self.state = 666
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [42, 43, 45]:
                    self.state = 664
                    self.ebnfSuffix()
                    pass
                elif token in [1, 2, 11, 14, 35, 36, 37, 46, 49, 51, 52]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 668
                self.atom()
                self.state = 671
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [42, 43, 45]:
                    self.state = 669
                    self.ebnfSuffix()
                    pass
                elif token in [1, 2, 11, 14, 35, 36, 37, 46, 49, 51, 52]:
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 673
                self.ebnf()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 674
                self.actionBlock()
                self.state = 676
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==42:
                    self.state = 675
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
        self.enterRule(localctx, 142, self.RULE_labeledElement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 680
            self.identifier()
            self.state = 681
            _la = self._input.LA(1)
            if not(_la==41 or _la==44):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 684
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 11, 49, 52]:
                self.state = 682
                self.atom()
                pass
            elif token in [36]:
                self.state = 683
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
        self.enterRule(localctx, 144, self.RULE_ebnf)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 686
            self.block()
            self.state = 688
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 48378511622144) != 0):
                self.state = 687
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
        self.enterRule(localctx, 146, self.RULE_blockSuffix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 690
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
        self.enterRule(localctx, 148, self.RULE_ebnfSuffix)
        self._la = 0 # Token type
        try:
            self.state = 704
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 692
                self.match(ctx2lParser.QUESTION)
                self.state = 694
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==42:
                    self.state = 693
                    self.match(ctx2lParser.QUESTION)


                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 696
                self.match(ctx2lParser.STAR)
                self.state = 698
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==42:
                    self.state = 697
                    self.match(ctx2lParser.QUESTION)


                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 3)
                self.state = 700
                self.match(ctx2lParser.PLUS)
                self.state = 702
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==42:
                    self.state = 701
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
        self.enterRule(localctx, 150, self.RULE_lexerAtom)
        self._la = 0 # Token type
        try:
            self.state = 714
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,89,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 706
                self.characterRange()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 707
                self.terminal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 708
                self.notSet()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 709
                self.match(ctx2lParser.LEXER_CHAR_SET)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 710
                self.match(ctx2lParser.DOT)
                self.state = 712
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 711
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
        self.enterRule(localctx, 152, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 723
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 716
                self.terminal()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 717
                self.ruleref()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 3)
                self.state = 718
                self.notSet()
                pass
            elif token in [49]:
                self.enterOuterAlt(localctx, 4)
                self.state = 719
                self.match(ctx2lParser.DOT)
                self.state = 721
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 720
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
        self.enterRule(localctx, 154, self.RULE_notSet)
        try:
            self.state = 729
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,92,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 725
                self.match(ctx2lParser.NOT)
                self.state = 726
                self.setElement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 727
                self.match(ctx2lParser.NOT)
                self.state = 728
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
        self.enterRule(localctx, 156, self.RULE_blockSet)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 731
            self.match(ctx2lParser.LPAREN)
            self.state = 732
            self.setElement()
            self.state = 737
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 733
                self.match(ctx2lParser.OR)
                self.state = 734
                self.setElement()
                self.state = 739
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 740
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
        self.enterRule(localctx, 158, self.RULE_setElement)
        self._la = 0 # Token type
        try:
            self.state = 752
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,96,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 742
                self.match(ctx2lParser.TOKEN_REF)
                self.state = 744
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 743
                    self.elementOptions()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 746
                self.match(ctx2lParser.STRING_LITERAL)
                self.state = 748
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 747
                    self.elementOptions()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 750
                self.characterRange()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 751
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
        self.enterRule(localctx, 160, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 754
            self.match(ctx2lParser.LPAREN)
            self.state = 765
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1125904201842688) != 0):
                self.state = 756
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==15:
                    self.state = 755
                    self.optionsSpec()


                self.state = 761
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==50:
                    self.state = 758
                    self.ruleAction()
                    self.state = 763
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 764
                self.match(ctx2lParser.COLON)


            self.state = 767
            self.altList()
            self.state = 768
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
        self.enterRule(localctx, 162, self.RULE_ruleref)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 770
            self.match(ctx2lParser.RULE_REF)
            self.state = 772
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 771
                self.argActionBlock()


            self.state = 775
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 774
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
        self.enterRule(localctx, 164, self.RULE_characterRange)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 777
            self.match(ctx2lParser.STRING_LITERAL)
            self.state = 778
            self.match(ctx2lParser.RANGE)
            self.state = 779
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
        self.enterRule(localctx, 166, self.RULE_terminal)
        self._la = 0 # Token type
        try:
            self.state = 789
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 781
                self.match(ctx2lParser.TOKEN_REF)
                self.state = 783
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 782
                    self.elementOptions()


                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 785
                self.match(ctx2lParser.STRING_LITERAL)
                self.state = 787
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==39:
                    self.state = 786
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
        self.enterRule(localctx, 168, self.RULE_elementOptions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 791
            self.match(ctx2lParser.LT)
            self.state = 792
            self.elementOption()
            self.state = 797
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==34:
                self.state = 793
                self.match(ctx2lParser.COMMA)
                self.state = 794
                self.elementOption()
                self.state = 799
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 800
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
        self.enterRule(localctx, 170, self.RULE_elementOption)
        try:
            self.state = 809
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,107,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 802
                self.identifier()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 803
                self.identifier()
                self.state = 804
                self.match(ctx2lParser.ASSIGN)
                self.state = 807
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 2]:
                    self.state = 805
                    self.identifier()
                    pass
                elif token in [11]:
                    self.state = 806
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
        self.enterRule(localctx, 172, self.RULE_identifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 811
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





