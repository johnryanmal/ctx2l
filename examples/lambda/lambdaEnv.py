# === combinators ===

# -- math --

B = r'\a.\b.\c.a(b c)'
B1 = r'\a.\b.\c.\d.a (b c d)'
B2 = r'\a.\b.\c.\d.\e.a (b c d e)'
B3 = r'\a.\b.\c.\d.a (b c d)'
C = r'\a.\b.\c.a c b'
C_prime = r'\a.\b.\c.\d.a (b d) c'
D = B_prime = r'\a.\b.\c.\d.a b (c d)'
D1 = r'\a.\b.c\d.\e.a b c (d e)'
D2 = r'\a.\b.\c.\d.\e.a (b c) (d e)'
E = r'\a.\b.\c.\d.\e.a b (c d e)'
E_hat = r'\a.\b.\c.\d.\e.\f.\g.a (b c d) (e f g)'
F = r'\a.\b.\c.c b a'
G = r'\a.\b.\c.\d.a d (b c)'
H = r'\a.\b.\c.a b c b'
I = r'\a.a'
J = r'\a.\b.\c.\d.a b (a d c)'
J_alt = r'\a.\b.\c.a b'
J_alt_prime = r'\a.\b.\c.\d.a b c'
K = r'\a.\b.a'
KI = r'\a.\b.b'
L = r'\a.\b.a (b b)'
M = r'\a.a a'
M2 = r'\a.\b.a b (a b)'
O = r'\a.\b.b (a b)'
P = psi = r'\a.\b.\c.\d.a (b c) (b d)'
Q = r'\a.\b.\c.b (a c)'
Q1 = r'\a.\b.\c.a (c b)'
Q2 = r'\a.\b.\c.b (c a)'
Q3 = r'\a.\c.\b.c (a b)'
Q4 = r'\a.\b.\c.c (b a)'
R = r'\a.\b.\c.b c a'
S = r'\a.\b.\c.a c (b c)'
S_prime = r'\a.\b.\c.\d.a (b d) (c d)'
T = r'\a.\b.b a'
U = r'\a.\b.b (a a b)'
V = r'\a.\b.\c.c a b'
W = r'\a.\b.a b b'
W1 = r'\a.\b.b a a'
# Y = r'\a.(\b.a (b b)) (\b.a (b b))'
Z = r'\a.(\b.a (\c.b b c)) (\b.a (\c.b b c))'
KM = r'\a.\b.b b'

# MM = omega = r'(\a.a a) (\a.a a)'
# YO = theta = r'(\a.\b.b (a a b)) (\a.\b.b (a a b))'

I_star = r'\a.\b.a b'
W_star = r'\a.\b.\c.a b c c'
C_star = r'\a.\b.\c.\d.a b d c'
R_star = r'\a.\b.\c.\d.a c d b'
F_star = r'\a.\b.\c.\d.a d c b'
V_star = r'\a.\b.\c.\d.a c b d'

I_star_star = r'\a.\b.\c.a b c'
W_star_star = r'\a.\b.\c.\d.a b c d d'
C_star_star = r'\a.\b.\c.\d.\e.a b c e d'
R_star_star = r'\a.\b.\c.\d.\e.a b d e c'
F_star_star = r'\a.\b.\c.\d.\e.a b e d c'
V_star_star = r'\a.\b.\c.\d.\e.a b e c d'

A = r'I_star'

turing = U

# -- birds --

bluebird = r'B'
bluebird_prime = r'B_prime'
blackbird = r'B1'
bunting = r'B2'
becard = r'B3'
cardinal = r'C'
cardinal_prime = r'C_prime'
dove = r'D'
dickcissel = r'D1'
dovekie = r'D2'
eagle = r'E'
bald_eagle = r'E_hat'
finch = r'F'
goldfinch = r'G'
hummingbird = r'H'
idiot = identity_bird = r'I'
jay = r'J'
kestrel = r'K'
kite = r'KI'
lark = r'L'
mockingbird = r'M'
double_mockingbird = r'M2'
owl = r'O'
queer_bird = queer = r'Q'
quixotic_bird = quixotic = r'Q1'
quizzical_bird = quizzical = r'Q2'
quirky_bird = quirky = r'Q3'
quacky_bird = quacky = r'Q4'
robin = r'R'
starling = r'S'
starling_prime = phoenix = 'S_prime'
thrush = r'T'
vireo = r'V'
warbler = r'W'
converse_warbler = warbler1 = r'W1'
# why = sage = r'Y'


# -- stdlib --

identity = id = r'I'
constant = const = always = locals()['return'] = lift = r'K'
map = compose = comp = r'B'
apply = call = r'A'
apply_to = r'T'
flip = r'C'
join = duplicate = dup = unnest = r'W'
pair = r'V'
ap = substitute = sub = S
on = r'P'
fix = rec = r'Z'
bind = flatmap = r'\a.\b.\c.b (a c) c'
chain = r'flip bind'
converge = lift2 = r'S_prime'

# === church ===

# -- boolean --

true = r'K'
false = r'KI'
