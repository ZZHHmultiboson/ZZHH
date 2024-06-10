# This file was automatically created by FeynRules 2.3.14
# Mathematica version: 10.3.0 for Linux x86 (64-bit) (October 9, 2015)
# Date: Fri 6 Mar 2020 14:41:35



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
FS0 = Parameter(name = 'FS0',
                nature = 'external',
                type = 'real',
                value = 1.e-8,
                texname = 'f_{\\text{S0}}',
                lhablock = 'ANOINPUTS',
                lhacode = [ 1 ])

FS1 = Parameter(name = 'FS1',
                nature = 'external',
                type = 'real',
                value = 1.e-8,
                texname = 'f_{\\text{S1}}',
                lhablock = 'ANOINPUTS',
                lhacode = [ 2 ])

FS2 = Parameter(name = 'FS2',
                nature = 'external',
                type = 'real',
                value = 1.e-8,
                texname = 'f_{\\text{S2}}',
                lhablock = 'ANOINPUTS',
                lhacode = [ 3 ])

FM0 = Parameter(name = 'FM0',
                nature = 'external',
                type = 'real',
                value = 1.e-8,
                texname = 'f_{\\text{M0}}',
                lhablock = 'ANOINPUTS',
                lhacode = [ 4 ])

FM1 = Parameter(name = 'FM1',
                nature = 'external',
                type = 'real',
                value = 1.e-8,
                texname = 'f_{\\text{M1}}',
                lhablock = 'ANOINPUTS',
                lhacode = [ 5 ])

FM2 = Parameter(name = 'FM2',
                nature = 'external',
                type = 'real',
                value = 1.e-8,
                texname = 'f_{\\text{M2}}',
                lhablock = 'ANOINPUTS',
                lhacode = [ 6 ])

FM3 = Parameter(name = 'FM3',
                nature = 'external',
                type = 'real',
                value = 1.e-8,
                texname = 'f_{\\text{M3}}',
                lhablock = 'ANOINPUTS',
                lhacode = [ 7 ])

FM4 = Parameter(name = 'FM4',
                nature = 'external',
                type = 'real',
                value = 1.e-8,
                texname = 'f_{\\text{M4}}',
                lhablock = 'ANOINPUTS',
                lhacode = [ 8 ])

FM5 = Parameter(name = 'FM5',
                nature = 'external',
                type = 'real',
                value = 1.e-8,
                texname = 'f_{\\text{M5}}',
                lhablock = 'ANOINPUTS',
                lhacode = [ 9 ])

FM6 = Parameter(name = 'FM6',
                nature = 'external',
                type = 'real',
                value = 1.e-8,
                texname = 'f_{\\text{M6}}',
                lhablock = 'ANOINPUTS',
                lhacode = [ 10 ])

FM7 = Parameter(name = 'FM7',
                nature = 'external',
                type = 'real',
                value = 1.e-8,
                texname = 'f_{\\text{M7}}',
                lhablock = 'ANOINPUTS',
                lhacode = [ 11 ])

FT0 = Parameter(name = 'FT0',
                nature = 'external',
                type = 'real',
                value = 1.e-8,
                texname = 'f_{\\text{T0}}',
                lhablock = 'ANOINPUTS',
                lhacode = [ 12 ])

FT1 = Parameter(name = 'FT1',
                nature = 'external',
                type = 'real',
                value = 1.e-8,
                texname = 'f_{\\text{T1}}',
                lhablock = 'ANOINPUTS',
                lhacode = [ 13 ])

FT2 = Parameter(name = 'FT2',
                nature = 'external',
                type = 'real',
                value = 1.e-8,
                texname = 'f_{\\text{T2}}',
                lhablock = 'ANOINPUTS',
                lhacode = [ 14 ])

FT3 = Parameter(name = 'FT3',
                nature = 'external',
                type = 'real',
                value = 1.e-8,
                texname = 'f_{\\text{T3}}',
                lhablock = 'ANOINPUTS',
                lhacode = [ 15 ])

FT4 = Parameter(name = 'FT4',
                nature = 'external',
                type = 'real',
                value = 1.e-8,
                texname = 'f_{\\text{T4}}',
                lhablock = 'ANOINPUTS',
                lhacode = [ 16 ])

FT5 = Parameter(name = 'FT5',
                nature = 'external',
                type = 'real',
                value = 1.e-8,
                texname = 'f_{\\text{T5}}',
                lhablock = 'ANOINPUTS',
                lhacode = [ 17 ])

FT6 = Parameter(name = 'FT6',
                nature = 'external',
                type = 'real',
                value = 1.e-8,
                texname = 'f_{\\text{T6}}',
                lhablock = 'ANOINPUTS',
                lhacode = [ 18 ])

FT7 = Parameter(name = 'FT7',
                nature = 'external',
                type = 'real',
                value = 1.e-8,
                texname = 'f_{\\text{T7}}',
                lhablock = 'ANOINPUTS',
                lhacode = [ 19 ])

FT8 = Parameter(name = 'FT8',
                nature = 'external',
                type = 'real',
                value = 1.e-8,
                texname = 'f_{\\text{T8}}',
                lhablock = 'ANOINPUTS',
                lhacode = [ 20 ])

FT9 = Parameter(name = 'FT9',
                nature = 'external',
                type = 'real',
                value = 1.e-8,
                texname = 'f_{\\text{T9}}',
                lhablock = 'ANOINPUTS',
                lhacode = [ 21 ])

cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

