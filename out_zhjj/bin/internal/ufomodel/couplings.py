# This file was automatically created by FeynRules 2.3.14
# Mathematica version: 10.3.0 for Linux x86 (64-bit) (October 9, 2015)
# Date: Fri 6 Mar 2020 14:41:43


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-(ee*complex(0,1))/3.',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '-2*FM0*complex(0,1)',
                order = {'M0':1})

GC_7 = Coupling(name = 'GC_7',
                value = '-2*cw**2*FM0*complex(0,1)',
                order = {'M0':1})

GC_8 = Coupling(name = 'GC_8',
                value = '2*ee*FM0*complex(0,1)',
                order = {'M0':1,'QED':1})

GC_9 = Coupling(name = 'GC_9',
                value = 'ee**2*FM0*complex(0,1)',
                order = {'M0':1,'QED':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '-(FM1*complex(0,1))/2.',
                 order = {'M1':1})

GC_11 = Coupling(name = 'GC_11',
                 value = '-(cw**2*FM1*complex(0,1))/2.',
                 order = {'M1':1})

GC_12 = Coupling(name = 'GC_12',
                 value = '-(ee*FM1*complex(0,1))/2.',
                 order = {'M1':1,'QED':1})

GC_13 = Coupling(name = 'GC_13',
                 value = '(ee**2*FM1*complex(0,1))/4.',
                 order = {'M1':1,'QED':2})

GC_14 = Coupling(name = 'GC_14',
                 value = '-4*cw**2*FM2*complex(0,1)',
                 order = {'M2':1})

GC_15 = Coupling(name = 'GC_15',
                 value = '2*ee**2*FM2*complex(0,1)',
                 order = {'M2':1,'QED':2})

GC_16 = Coupling(name = 'GC_16',
                 value = '-(cw**2*FM3*complex(0,1))',
                 order = {'M3':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '-(ee**2*FM3*complex(0,1))/2.',
                 order = {'M3':1,'QED':2})

GC_18 = Coupling(name = 'GC_18',
                 value = '-(ee*FM4*complex(0,1))/2.',
                 order = {'M4':1,'QED':1})

GC_19 = Coupling(name = 'GC_19',
                 value = '-(ee**2*FM4*complex(0,1))/2.',
                 order = {'M4':1,'QED':2})

GC_20 = Coupling(name = 'GC_20',
                 value = '-(ee**3*FM4*complex(0,1))/2.',
                 order = {'M4':1,'QED':3})

GC_21 = Coupling(name = 'GC_21',
                 value = '(ee*FM5*complex(0,1))/4.',
                 order = {'M5':1,'QED':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '(ee**2*FM5*complex(0,1))/4.',
                 order = {'M5':1,'QED':2})

GC_23 = Coupling(name = 'GC_23',
                 value = '(ee**3*FM5*complex(0,1))/2.',
                 order = {'M5':1,'QED':3})

GC_24 = Coupling(name = 'GC_24',
                 value = '(FM7*complex(0,1))/4.',
                 order = {'M7':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '(cw**2*FM7*complex(0,1))/4.',
                 order = {'M7':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '-(ee*FM7*complex(0,1))/8.',
                 order = {'M7':1,'QED':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '-(ee**2*FM7*complex(0,1))/8.',
                 order = {'M7':1,'QED':2})

GC_28 = Coupling(name = 'GC_28',
                 value = '-(ee**2*FM7*complex(0,1))/4.',
                 order = {'M7':1,'QED':2})

GC_29 = Coupling(name = 'GC_29',
                 value = '-(ee**3*FM7*complex(0,1))/4.',
                 order = {'M7':1,'QED':3})

GC_30 = Coupling(name = 'GC_30',
                 value = '-(ee**4*FM7*complex(0,1))/(4.*cw**2)',
                 order = {'M7':1,'QED':4})

GC_31 = Coupling(name = 'GC_31',
                 value = '2*complex(0,1)*FS0',
                 order = {'S0':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '2*complex(0,1)*FS1',
                 order = {'S1':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '2*complex(0,1)*FS2',
                 order = {'S2':1})

GC_34 = Coupling(name = 'GC_34',
                 value = '8*complex(0,1)*FT0',
                 order = {'T0':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '8*cw**2*complex(0,1)*FT0',
                 order = {'T0':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '8*cw**4*complex(0,1)*FT0',
                 order = {'T0':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '-8*ee*complex(0,1)*FT0',
                 order = {'QED':1,'T0':1})

GC_38 = Coupling(name = 'GC_38',
                 value = '-8*cw**2*ee*complex(0,1)*FT0',
                 order = {'QED':1,'T0':1})

GC_39 = Coupling(name = 'GC_39',
                 value = '8*ee**2*complex(0,1)*FT0',
                 order = {'QED':2,'T0':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '-8*cw**2*ee**2*complex(0,1)*FT0',
                 order = {'QED':2,'T0':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '8*ee**3*complex(0,1)*FT0',
                 order = {'QED':3,'T0':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '16*ee**4*complex(0,1)*FT0',
                 order = {'QED':4,'T0':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '4*complex(0,1)*FT1',
                 order = {'T1':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '4*cw**2*complex(0,1)*FT1',
                 order = {'T1':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '8*cw**4*complex(0,1)*FT1',
                 order = {'T1':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '4*ee*complex(0,1)*FT1',
                 order = {'QED':1,'T1':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '4*cw**2*ee*complex(0,1)*FT1',
                 order = {'QED':1,'T1':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '8*ee**2*complex(0,1)*FT1',
                 order = {'QED':2,'T1':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '-4*cw**2*ee**2*complex(0,1)*FT1',
                 order = {'QED':2,'T1':1})

GC_50 = Coupling(name = 'GC_50',
                 value = '-4*ee**3*complex(0,1)*FT1',
                 order = {'QED':3,'T1':1})

GC_51 = Coupling(name = 'GC_51',
                 value = '16*ee**4*complex(0,1)*FT1',
                 order = {'QED':4,'T1':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '2*complex(0,1)*FT2',
                 order = {'T2':1})

GC_53 = Coupling(name = 'GC_53',
                 value = 'cw**2*complex(0,1)*FT2',
                 order = {'T2':1})

GC_54 = Coupling(name = 'GC_54',
                 value = '2*cw**4*complex(0,1)*FT2',
                 order = {'T2':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '-(ee*complex(0,1)*FT2)',
                 order = {'QED':1,'T2':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '-(cw**2*ee*complex(0,1)*FT2)',
                 order = {'QED':1,'T2':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '2*ee**2*complex(0,1)*FT2',
                 order = {'QED':2,'T2':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '-(cw**2*ee**2*complex(0,1)*FT2)',
                 order = {'QED':2,'T2':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '2*ee**3*complex(0,1)*FT2',
                 order = {'QED':3,'T2':1})

GC_60 = Coupling(name = 'GC_60',
                 value = '8*ee**4*complex(0,1)*FT2',
                 order = {'QED':4,'T2':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '8*cw**2*complex(0,1)*FT5',
                 order = {'T5':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '-8*cw**2*ee*complex(0,1)*FT5',
                 order = {'QED':1,'T5':1})

GC_63 = Coupling(name = 'GC_63',
                 value = '8*cw**2*ee*complex(0,1)*FT5',
                 order = {'QED':1,'T5':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '8*ee**2*complex(0,1)*FT5',
                 order = {'QED':2,'T5':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '-8*cw**2*ee**2*complex(0,1)*FT5',
                 order = {'QED':2,'T5':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '-16*cw**2*ee**2*complex(0,1)*FT5',
                 order = {'QED':2,'T5':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '4*cw**2*complex(0,1)*FT6',
                 order = {'T6':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '-4*cw**2*ee*complex(0,1)*FT6',
                 order = {'QED':1,'T6':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '4*cw**2*ee*complex(0,1)*FT6',
                 order = {'QED':1,'T6':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '4*ee**2*complex(0,1)*FT6',
                 order = {'QED':2,'T6':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '-4*cw**2*ee**2*complex(0,1)*FT6',
                 order = {'QED':2,'T6':1})

GC_72 = Coupling(name = 'GC_72',
                 value = 'cw**2*complex(0,1)*FT7',
                 order = {'T7':1})

GC_73 = Coupling(name = 'GC_73',
                 value = 'cw**2*ee*complex(0,1)*FT7',
                 order = {'QED':1,'T7':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '-2*cw**2*ee*complex(0,1)*FT7',
                 order = {'QED':1,'T7':1})

GC_75 = Coupling(name = 'GC_75',
                 value = 'ee**2*complex(0,1)*FT7',
                 order = {'QED':2,'T7':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '-(cw**2*ee**2*complex(0,1)*FT7)',
                 order = {'QED':2,'T7':1})

GC_77 = Coupling(name = 'GC_77',
                 value = 'cw**2*ee**2*complex(0,1)*FT7',
                 order = {'QED':2,'T7':1})

GC_78 = Coupling(name = 'GC_78',
                 value = '-2*cw**2*ee**2*complex(0,1)*FT7',
                 order = {'QED':2,'T7':1})

GC_79 = Coupling(name = 'GC_79',
                 value = '32*cw**4*complex(0,1)*FT8',
                 order = {'T8':1})

GC_80 = Coupling(name = 'GC_80',
                 value = '8*cw**4*complex(0,1)*FT9',
                 order = {'T9':1})

GC_81 = Coupling(name = 'GC_81',
                 value = '-G',
                 order = {'QCD':1})

GC_82 = Coupling(name = 'GC_82',
                 value = 'complex(0,1)*G',
                 order = {'QCD':1})

GC_83 = Coupling(name = 'GC_83',
                 value = 'complex(0,1)*G**2',
                 order = {'QCD':2})

GC_84 = Coupling(name = 'GC_84',
                 value = '-6*complex(0,1)*lam',
                 order = {'QED':2})

GC_85 = Coupling(name = 'GC_85',
                 value = '(ee**4*FM0*complex(0,1))/cw**2 + (2*ee**4*FM0*complex(0,1))/sw**2',
                 order = {'M0':1,'QED':4})

GC_86 = Coupling(name = 'GC_86',
                 value = '-(ee**4*FM0*complex(0,1)) - (cw**4*ee**4*FM0*complex(0,1))/sw**4 - (2*cw**2*ee**4*FM0*complex(0,1))/sw**2',
                 order = {'M0':1,'QED':4})

GC_87 = Coupling(name = 'GC_87',
                 value = '(ee**4*FM1*complex(0,1))/(2.*cw**2) + (ee**4*FM1*complex(0,1))/sw**2',
                 order = {'M1':1,'QED':4})

GC_88 = Coupling(name = 'GC_88',
                 value = '(ee**4*FM1*complex(0,1))/2. + (cw**4*ee**4*FM1*complex(0,1))/(2.*sw**4) + (cw**2*ee**4*FM1*complex(0,1))/sw**2',
                 order = {'M1':1,'QED':4})

GC_89 = Coupling(name = 'GC_89',
                 value = '-(ee**3*FM4*complex(0,1))/2. - (cw**2*ee**3*FM4*complex(0,1))/(2.*sw**2)',
                 order = {'M4':1,'QED':3})

GC_90 = Coupling(name = 'GC_90',
                 value = '(ee**3*FM5*complex(0,1))/4. + (cw**2*ee**3*FM5*complex(0,1))/(4.*sw**2)',
                 order = {'M5':1,'QED':3})

GC_91 = Coupling(name = 'GC_91',
                 value = '-(ee**4*FM7*complex(0,1))/4. - (cw**4*ee**4*FM7*complex(0,1))/(4.*sw**4) - (cw**2*ee**4*FM7*complex(0,1))/(2.*sw**2)',
                 order = {'M7':1,'QED':4})

GC_92 = Coupling(name = 'GC_92',
                 value = '(3*ee**4*complex(0,1)*FS0)/(2.*cw**2) + (3*cw**2*ee**4*complex(0,1)*FS0)/(2.*sw**4) + (3*ee**4*complex(0,1)*FS0)/sw**2',
                 order = {'QED':4,'S0':1})

GC_93 = Coupling(name = 'GC_93',
                 value = '(3*ee**4*complex(0,1)*FS1)/cw**2 + (3*cw**2*ee**4*complex(0,1)*FS1)/sw**4 + (6*ee**4*complex(0,1)*FS1)/sw**2',
                 order = {'QED':4,'S1':1})

GC_94 = Coupling(name = 'GC_94',
                 value = '(3*ee**4*complex(0,1)*FS2)/(2.*cw**2) + (3*cw**2*ee**4*complex(0,1)*FS2)/(2.*sw**4) + (3*ee**4*complex(0,1)*FS2)/sw**2',
                 order = {'QED':4,'S2':1})

GC_95 = Coupling(name = 'GC_95',
                 value = '(-3*cw*ee**3*complex(0,1)*FS0)/(4.*sw**3) - (3*ee**3*complex(0,1)*FS0)/(4.*cw*sw)',
                 order = {'QED':3,'S0':1})

GC_96 = Coupling(name = 'GC_96',
                 value = '(3*cw*ee**3*complex(0,1)*FS2)/(4.*sw**3) + (3*ee**3*complex(0,1)*FS2)/(4.*cw*sw)',
                 order = {'QED':3,'S2':1})

GC_97 = Coupling(name = 'GC_97',
                 value = '(3*ee**4*FM0*complex(0,1))/sw**4',
                 order = {'M0':1,'QED':4})

GC_98 = Coupling(name = 'GC_98',
                 value = '-((cw**2*ee**4*FM0*complex(0,1))/sw**4)',
                 order = {'M0':1,'QED':4})

GC_99 = Coupling(name = 'GC_99',
                 value = '(-3*ee**4*FM1*complex(0,1))/(2.*sw**4)',
                 order = {'M1':1,'QED':4})

GC_100 = Coupling(name = 'GC_100',
                  value = '(3*cw**2*ee**4*FM1*complex(0,1))/(2.*sw**4)',
                  order = {'M1':1,'QED':4})

GC_101 = Coupling(name = 'GC_101',
                  value = '(3*ee**4*FM7*complex(0,1))/(4.*sw**4)',
                  order = {'M7':1,'QED':4})

GC_102 = Coupling(name = 'GC_102',
                  value = '(-9*cw**2*ee**4*FM7*complex(0,1))/(4.*sw**4)',
                  order = {'M7':1,'QED':4})

GC_103 = Coupling(name = 'GC_103',
                  value = '(6*ee**4*complex(0,1)*FS0)/sw**4',
                  order = {'QED':4,'S0':1})

GC_104 = Coupling(name = 'GC_104',
                  value = '(3*ee**4*complex(0,1)*FS1)/sw**4',
                  order = {'QED':4,'S1':1})

GC_105 = Coupling(name = 'GC_105',
                  value = '(3*ee**4*complex(0,1)*FS2)/sw**4',
                  order = {'QED':4,'S2':1})

GC_106 = Coupling(name = 'GC_106',
                  value = '(24*ee**4*complex(0,1)*FT0)/sw**4',
                  order = {'QED':4,'T0':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '(-8*cw**2*ee**4*complex(0,1)*FT0)/sw**4',
                  order = {'QED':4,'T0':1})

GC_108 = Coupling(name = 'GC_108',
                  value = '(16*cw**4*ee**4*complex(0,1)*FT0)/sw**4',
                  order = {'QED':4,'T0':1})

GC_109 = Coupling(name = 'GC_109',
                  value = '(24*ee**4*complex(0,1)*FT1)/sw**4',
                  order = {'QED':4,'T1':1})

GC_110 = Coupling(name = 'GC_110',
                  value = '(-16*cw**2*ee**4*complex(0,1)*FT1)/sw**4',
                  order = {'QED':4,'T1':1})

GC_111 = Coupling(name = 'GC_111',
                  value = '(16*cw**4*ee**4*complex(0,1)*FT1)/sw**4',
                  order = {'QED':4,'T1':1})

GC_112 = Coupling(name = 'GC_112',
                  value = '(12*ee**4*complex(0,1)*FT2)/sw**4',
                  order = {'QED':4,'T2':1})

GC_113 = Coupling(name = 'GC_113',
                  value = '(-4*cw**2*ee**4*complex(0,1)*FT2)/sw**4',
                  order = {'QED':4,'T2':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '(8*cw**4*ee**4*complex(0,1)*FT2)/sw**4',
                  order = {'QED':4,'T2':1})

GC_115 = Coupling(name = 'GC_115',
                  value = '-((cw*ee**3*FM0*complex(0,1))/sw**3)',
                  order = {'M0':1,'QED':3})

GC_116 = Coupling(name = 'GC_116',
                  value = '(4*cw*ee**4*FM0*complex(0,1))/sw**3',
                  order = {'M0':1,'QED':4})

GC_117 = Coupling(name = 'GC_117',
                  value = '(cw*ee**3*FM1*complex(0,1))/(4.*sw**3)',
                  order = {'M1':1,'QED':3})

GC_118 = Coupling(name = 'GC_118',
                  value = '-((cw*ee**4*FM1*complex(0,1))/sw**3)',
                  order = {'M1':1,'QED':4})

GC_119 = Coupling(name = 'GC_119',
                  value = '-(cw*ee**3*FM4*complex(0,1))/(2.*sw**3)',
                  order = {'M4':1,'QED':3})

GC_120 = Coupling(name = 'GC_120',
                  value = '(cw**3*ee**3*FM4*complex(0,1))/(2.*sw**3)',
                  order = {'M4':1,'QED':3})

GC_121 = Coupling(name = 'GC_121',
                  value = '-(cw*ee**3*FM5*complex(0,1))/(2.*sw**3)',
                  order = {'M5':1,'QED':3})

GC_122 = Coupling(name = 'GC_122',
                  value = '-(cw**3*ee**3*FM5*complex(0,1))/(4.*sw**3)',
                  order = {'M5':1,'QED':3})

GC_123 = Coupling(name = 'GC_123',
                  value = '(cw*ee**3*FM7*complex(0,1))/(8.*sw**3)',
                  order = {'M7':1,'QED':3})

GC_124 = Coupling(name = 'GC_124',
                  value = '(3*cw**3*ee**3*FM7*complex(0,1))/(8.*sw**3)',
                  order = {'M7':1,'QED':3})

GC_125 = Coupling(name = 'GC_125',
                  value = '-(cw*ee**4*FM7*complex(0,1))/(2.*sw**3)',
                  order = {'M7':1,'QED':4})

GC_126 = Coupling(name = 'GC_126',
                  value = '(-8*cw*ee**3*complex(0,1)*FT0)/sw**3',
                  order = {'QED':3,'T0':1})

GC_127 = Coupling(name = 'GC_127',
                  value = '(8*cw**3*ee**3*complex(0,1)*FT0)/sw**3',
                  order = {'QED':3,'T0':1})

GC_128 = Coupling(name = 'GC_128',
                  value = '(48*cw*ee**4*complex(0,1)*FT0)/sw**3',
                  order = {'QED':4,'T0':1})

GC_129 = Coupling(name = 'GC_129',
                  value = '(-16*cw**3*ee**4*complex(0,1)*FT0)/sw**3',
                  order = {'QED':4,'T0':1})

GC_130 = Coupling(name = 'GC_130',
                  value = '(4*cw*ee**3*complex(0,1)*FT1)/sw**3',
                  order = {'QED':3,'T1':1})

GC_131 = Coupling(name = 'GC_131',
                  value = '(-8*cw**3*ee**3*complex(0,1)*FT1)/sw**3',
                  order = {'QED':3,'T1':1})

GC_132 = Coupling(name = 'GC_132',
                  value = '(8*cw*ee**4*complex(0,1)*FT1)/sw**3',
                  order = {'QED':4,'T1':1})

GC_133 = Coupling(name = 'GC_133',
                  value = '(-16*cw**3*ee**4*complex(0,1)*FT1)/sw**3',
                  order = {'QED':4,'T1':1})

GC_134 = Coupling(name = 'GC_134',
                  value = '(-2*cw*ee**3*complex(0,1)*FT2)/sw**3',
                  order = {'QED':3,'T2':1})

GC_135 = Coupling(name = 'GC_135',
                  value = '(-2*cw**3*ee**3*complex(0,1)*FT2)/sw**3',
                  order = {'QED':3,'T2':1})

GC_136 = Coupling(name = 'GC_136',
                  value = '(12*cw*ee**4*complex(0,1)*FT2)/sw**3',
                  order = {'QED':4,'T2':1})

GC_137 = Coupling(name = 'GC_137',
                  value = '(-4*cw**3*ee**4*complex(0,1)*FT2)/sw**3',
                  order = {'QED':4,'T2':1})

GC_138 = Coupling(name = 'GC_138',
                  value = '(ee**2*complex(0,1))/(2.*sw**2)',
                  order = {'QED':2})

GC_139 = Coupling(name = 'GC_139',
                  value = '-((ee**2*complex(0,1))/sw**2)',
                  order = {'QED':2})

GC_140 = Coupling(name = 'GC_140',
                  value = '(cw**2*ee**2*complex(0,1))/sw**2',
                  order = {'QED':2})

GC_141 = Coupling(name = 'GC_141',
                  value = '(ee**2*FM0*complex(0,1))/sw**2',
                  order = {'M0':1,'QED':2})

GC_142 = Coupling(name = 'GC_142',
                  value = '(cw**2*ee**2*FM0*complex(0,1))/sw**2',
                  order = {'M0':1,'QED':2})

GC_143 = Coupling(name = 'GC_143',
                  value = '-((ee**3*FM0*complex(0,1))/sw**2)',
                  order = {'M0':1,'QED':3})

GC_144 = Coupling(name = 'GC_144',
                  value = '-((ee**4*FM0*complex(0,1))/sw**2)',
                  order = {'M0':1,'QED':4})

GC_145 = Coupling(name = 'GC_145',
                  value = '-(ee**2*FM1*complex(0,1))/(4.*sw**2)',
                  order = {'M1':1,'QED':2})

GC_146 = Coupling(name = 'GC_146',
                  value = '(cw**2*ee**2*FM1*complex(0,1))/(4.*sw**2)',
                  order = {'M1':1,'QED':2})

GC_147 = Coupling(name = 'GC_147',
                  value = '-(ee**3*FM1*complex(0,1))/(4.*sw**2)',
                  order = {'M1':1,'QED':3})

GC_148 = Coupling(name = 'GC_148',
                  value = '(ee**4*FM1*complex(0,1))/sw**2',
                  order = {'M1':1,'QED':4})

GC_149 = Coupling(name = 'GC_149',
                  value = '(2*cw**2*ee**2*FM2*complex(0,1))/sw**2',
                  order = {'M2':1,'QED':2})

GC_150 = Coupling(name = 'GC_150',
                  value = '(cw**2*ee**2*FM3*complex(0,1))/(2.*sw**2)',
                  order = {'M3':1,'QED':2})

GC_151 = Coupling(name = 'GC_151',
                  value = '-(cw**2*ee**2*FM4*complex(0,1))/(2.*sw**2)',
                  order = {'M4':1,'QED':2})

GC_152 = Coupling(name = 'GC_152',
                  value = '(ee**3*FM4*complex(0,1))/(2.*sw**2)',
                  order = {'M4':1,'QED':3})

GC_153 = Coupling(name = 'GC_153',
                  value = '-(cw**2*ee**3*FM4*complex(0,1))/(2.*sw**2)',
                  order = {'M4':1,'QED':3})

GC_154 = Coupling(name = 'GC_154',
                  value = '(cw**2*ee**2*FM5*complex(0,1))/(4.*sw**2)',
                  order = {'M5':1,'QED':2})

GC_155 = Coupling(name = 'GC_155',
                  value = '(ee**3*FM5*complex(0,1))/(2.*sw**2)',
                  order = {'M5':1,'QED':3})

GC_156 = Coupling(name = 'GC_156',
                  value = '(cw**2*ee**3*FM5*complex(0,1))/(4.*sw**2)',
                  order = {'M5':1,'QED':3})

GC_157 = Coupling(name = 'GC_157',
                  value = '(ee**2*FM7*complex(0,1))/(4.*sw**2)',
                  order = {'M7':1,'QED':2})

GC_158 = Coupling(name = 'GC_158',
                  value = '-(cw**2*ee**2*FM7*complex(0,1))/(8.*sw**2)',
                  order = {'M7':1,'QED':2})

GC_159 = Coupling(name = 'GC_159',
                  value = '(ee**3*FM7*complex(0,1))/(4.*sw**2)',
                  order = {'M7':1,'QED':3})

GC_160 = Coupling(name = 'GC_160',
                  value = '-(cw**2*ee**3*FM7*complex(0,1))/(8.*sw**2)',
                  order = {'M7':1,'QED':3})

GC_161 = Coupling(name = 'GC_161',
                  value = '-((ee**4*FM7*complex(0,1))/sw**2)',
                  order = {'M7':1,'QED':4})

GC_162 = Coupling(name = 'GC_162',
                  value = '(-3*ee**4*FM7*complex(0,1))/(2.*sw**2)',
                  order = {'M7':1,'QED':4})

GC_163 = Coupling(name = 'GC_163',
                  value = '-(ee**2*complex(0,1)*FS0)/(2.*sw**2)',
                  order = {'QED':2,'S0':1})

GC_164 = Coupling(name = 'GC_164',
                  value = '-((ee**2*complex(0,1)*FS1)/sw**2)',
                  order = {'QED':2,'S1':1})

GC_165 = Coupling(name = 'GC_165',
                  value = '-(ee**2*complex(0,1)*FS2)/(2.*sw**2)',
                  order = {'QED':2,'S2':1})

GC_166 = Coupling(name = 'GC_166',
                  value = '(8*ee**2*complex(0,1)*FT0)/sw**2',
                  order = {'QED':2,'T0':1})

GC_167 = Coupling(name = 'GC_167',
                  value = '(8*cw**2*ee**2*complex(0,1)*FT0)/sw**2',
                  order = {'QED':2,'T0':1})

GC_168 = Coupling(name = 'GC_168',
                  value = '(-8*cw**4*ee**2*complex(0,1)*FT0)/sw**2',
                  order = {'QED':2,'T0':1})

GC_169 = Coupling(name = 'GC_169',
                  value = '(-8*ee**3*complex(0,1)*FT0)/sw**2',
                  order = {'QED':3,'T0':1})

GC_170 = Coupling(name = 'GC_170',
                  value = '(-16*cw**2*ee**3*complex(0,1)*FT0)/sw**2',
                  order = {'QED':3,'T0':1})

GC_171 = Coupling(name = 'GC_171',
                  value = '(-8*ee**4*complex(0,1)*FT0)/sw**2',
                  order = {'QED':4,'T0':1})

GC_172 = Coupling(name = 'GC_172',
                  value = '(64*cw**2*ee**4*complex(0,1)*FT0)/sw**2',
                  order = {'QED':4,'T0':1})

GC_173 = Coupling(name = 'GC_173',
                  value = '(4*ee**2*complex(0,1)*FT1)/sw**2',
                  order = {'QED':2,'T1':1})

GC_174 = Coupling(name = 'GC_174',
                  value = '(4*cw**2*ee**2*complex(0,1)*FT1)/sw**2',
                  order = {'QED':2,'T1':1})

GC_175 = Coupling(name = 'GC_175',
                  value = '(-4*cw**4*ee**2*complex(0,1)*FT1)/sw**2',
                  order = {'QED':2,'T1':1})

GC_176 = Coupling(name = 'GC_176',
                  value = '(4*ee**3*complex(0,1)*FT1)/sw**2',
                  order = {'QED':3,'T1':1})

GC_177 = Coupling(name = 'GC_177',
                  value = '(-8*cw**2*ee**3*complex(0,1)*FT1)/sw**2',
                  order = {'QED':3,'T1':1})

GC_178 = Coupling(name = 'GC_178',
                  value = '(-16*ee**4*complex(0,1)*FT1)/sw**2',
                  order = {'QED':4,'T1':1})

GC_179 = Coupling(name = 'GC_179',
                  value = '(32*cw**2*ee**4*complex(0,1)*FT1)/sw**2',
                  order = {'QED':4,'T1':1})

GC_180 = Coupling(name = 'GC_180',
                  value = '(2*ee**2*complex(0,1)*FT2)/sw**2',
                  order = {'QED':2,'T2':1})

GC_181 = Coupling(name = 'GC_181',
                  value = '(2*cw**2*ee**2*complex(0,1)*FT2)/sw**2',
                  order = {'QED':2,'T2':1})

GC_182 = Coupling(name = 'GC_182',
                  value = '-((cw**4*ee**2*complex(0,1)*FT2)/sw**2)',
                  order = {'QED':2,'T2':1})

GC_183 = Coupling(name = 'GC_183',
                  value = '(ee**3*complex(0,1)*FT2)/sw**2',
                  order = {'QED':3,'T2':1})

GC_184 = Coupling(name = 'GC_184',
                  value = '(-6*cw**2*ee**3*complex(0,1)*FT2)/sw**2',
                  order = {'QED':3,'T2':1})

GC_185 = Coupling(name = 'GC_185',
                  value = '(-4*ee**4*complex(0,1)*FT2)/sw**2',
                  order = {'QED':4,'T2':1})

GC_186 = Coupling(name = 'GC_186',
                  value = '(24*cw**2*ee**4*complex(0,1)*FT2)/sw**2',
                  order = {'QED':4,'T2':1})

GC_187 = Coupling(name = 'GC_187',
                  value = '(8*cw**2*ee**2*complex(0,1)*FT5)/sw**2',
                  order = {'QED':2,'T5':1})

GC_188 = Coupling(name = 'GC_188',
                  value = '(-8*cw**4*ee**2*complex(0,1)*FT5)/sw**2',
                  order = {'QED':2,'T5':1})

GC_189 = Coupling(name = 'GC_189',
                  value = '(4*cw**2*ee**2*complex(0,1)*FT6)/sw**2',
                  order = {'QED':2,'T6':1})

GC_190 = Coupling(name = 'GC_190',
                  value = '(-4*cw**4*ee**2*complex(0,1)*FT6)/sw**2',
                  order = {'QED':2,'T6':1})

GC_191 = Coupling(name = 'GC_191',
                  value = '(2*cw**2*ee**2*complex(0,1)*FT7)/sw**2',
                  order = {'QED':2,'T7':1})

GC_192 = Coupling(name = 'GC_192',
                  value = '(-2*cw**4*ee**2*complex(0,1)*FT7)/sw**2',
                  order = {'QED':2,'T7':1})

GC_193 = Coupling(name = 'GC_193',
                  value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_194 = Coupling(name = 'GC_194',
                  value = '(CKM1x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_195 = Coupling(name = 'GC_195',
                  value = '(CKM1x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_196 = Coupling(name = 'GC_196',
                  value = '(CKM2x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_197 = Coupling(name = 'GC_197',
                  value = '(CKM2x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_198 = Coupling(name = 'GC_198',
                  value = '-(cw*ee*complex(0,1))/(2.*sw)',
                  order = {'QED':1})

GC_199 = Coupling(name = 'GC_199',
                  value = '(cw*ee*complex(0,1))/(2.*sw)',
                  order = {'QED':1})

GC_200 = Coupling(name = 'GC_200',
                  value = '(cw*ee*complex(0,1))/sw',
                  order = {'QED':1})

GC_201 = Coupling(name = 'GC_201',
                  value = '(-2*cw*ee**2*complex(0,1))/sw',
                  order = {'QED':2})

GC_202 = Coupling(name = 'GC_202',
                  value = '(2*cw*ee*FM0*complex(0,1))/sw',
                  order = {'M0':1,'QED':1})

GC_203 = Coupling(name = 'GC_203',
                  value = '(cw*ee**2*FM0*complex(0,1))/sw',
                  order = {'M0':1,'QED':2})

GC_204 = Coupling(name = 'GC_204',
                  value = '-(cw*ee*FM1*complex(0,1))/(2.*sw)',
                  order = {'M1':1,'QED':1})

GC_205 = Coupling(name = 'GC_205',
                  value = '-(cw*ee**2*FM1*complex(0,1))/(4.*sw)',
                  order = {'M1':1,'QED':2})

GC_206 = Coupling(name = 'GC_206',
                  value = '(-2*cw*ee**2*FM2*complex(0,1))/sw',
                  order = {'M2':1,'QED':2})

GC_207 = Coupling(name = 'GC_207',
                  value = '(cw*ee**2*FM3*complex(0,1))/(2.*sw)',
                  order = {'M3':1,'QED':2})

GC_208 = Coupling(name = 'GC_208',
                  value = '(cw*ee*FM4*complex(0,1))/(2.*sw)',
                  order = {'M4':1,'QED':1})

GC_209 = Coupling(name = 'GC_209',
                  value = '(cw*ee**2*FM4*complex(0,1))/(2.*sw)',
                  order = {'M4':1,'QED':2})

GC_210 = Coupling(name = 'GC_210',
                  value = '-((cw*ee**2*FM4*complex(0,1))/sw)',
                  order = {'M4':1,'QED':2})

GC_211 = Coupling(name = 'GC_211',
                  value = '(cw*ee**3*FM4*complex(0,1))/(2.*sw)',
                  order = {'M4':1,'QED':3})

GC_212 = Coupling(name = 'GC_212',
                  value = '-(cw*ee*FM5*complex(0,1))/(4.*sw)',
                  order = {'M5':1,'QED':1})

GC_213 = Coupling(name = 'GC_213',
                  value = '(cw*ee**2*FM5*complex(0,1))/(4.*sw)',
                  order = {'M5':1,'QED':2})

GC_214 = Coupling(name = 'GC_214',
                  value = '-(cw*ee**2*FM5*complex(0,1))/(2.*sw)',
                  order = {'M5':1,'QED':2})

GC_215 = Coupling(name = 'GC_215',
                  value = '-(cw*ee**3*FM5*complex(0,1))/(2.*sw)',
                  order = {'M5':1,'QED':3})

GC_216 = Coupling(name = 'GC_216',
                  value = '-(cw*ee*FM7*complex(0,1))/(8.*sw)',
                  order = {'M7':1,'QED':1})

GC_217 = Coupling(name = 'GC_217',
                  value = '(cw*ee**2*FM7*complex(0,1))/(8.*sw)',
                  order = {'M7':1,'QED':2})

GC_218 = Coupling(name = 'GC_218',
                  value = '(ee**3*FM7*complex(0,1))/(8.*cw*sw)',
                  order = {'M7':1,'QED':3})

GC_219 = Coupling(name = 'GC_219',
                  value = '(cw*ee**3*FM7*complex(0,1))/(2.*sw)',
                  order = {'M7':1,'QED':3})

GC_220 = Coupling(name = 'GC_220',
                  value = '-(ee**4*FM7*complex(0,1))/(2.*cw*sw)',
                  order = {'M7':1,'QED':4})

GC_221 = Coupling(name = 'GC_221',
                  value = '(-8*cw*ee*complex(0,1)*FT0)/sw',
                  order = {'QED':1,'T0':1})

GC_222 = Coupling(name = 'GC_222',
                  value = '(-8*cw**3*ee*complex(0,1)*FT0)/sw',
                  order = {'QED':1,'T0':1})

GC_223 = Coupling(name = 'GC_223',
                  value = '(8*cw*ee**2*complex(0,1)*FT0)/sw',
                  order = {'QED':2,'T0':1})

GC_224 = Coupling(name = 'GC_224',
                  value = '(16*cw**3*ee**2*complex(0,1)*FT0)/sw',
                  order = {'QED':2,'T0':1})

GC_225 = Coupling(name = 'GC_225',
                  value = '(8*cw*ee**3*complex(0,1)*FT0)/sw',
                  order = {'QED':3,'T0':1})

GC_226 = Coupling(name = 'GC_226',
                  value = '(-16*cw*ee**4*complex(0,1)*FT0)/sw',
                  order = {'QED':4,'T0':1})

GC_227 = Coupling(name = 'GC_227',
                  value = '(8*cw*ee*complex(0,1)*FT1)/sw',
                  order = {'QED':1,'T1':1})

GC_228 = Coupling(name = 'GC_228',
                  value = '(4*cw**3*ee*complex(0,1)*FT1)/sw',
                  order = {'QED':1,'T1':1})

GC_229 = Coupling(name = 'GC_229',
                  value = '(4*cw*ee**2*complex(0,1)*FT1)/sw',
                  order = {'QED':2,'T1':1})

GC_230 = Coupling(name = 'GC_230',
                  value = '(-4*cw**3*ee**2*complex(0,1)*FT1)/sw',
                  order = {'QED':2,'T1':1})

GC_231 = Coupling(name = 'GC_231',
                  value = '(-8*cw*ee**3*complex(0,1)*FT1)/sw',
                  order = {'QED':3,'T1':1})

GC_232 = Coupling(name = 'GC_232',
                  value = '(-16*cw*ee**4*complex(0,1)*FT1)/sw',
                  order = {'QED':4,'T1':1})

GC_233 = Coupling(name = 'GC_233',
                  value = '-((cw*ee*complex(0,1)*FT2)/sw)',
                  order = {'QED':1,'T2':1})

GC_234 = Coupling(name = 'GC_234',
                  value = '-((cw**3*ee*complex(0,1)*FT2)/sw)',
                  order = {'QED':1,'T2':1})

GC_235 = Coupling(name = 'GC_235',
                  value = '(cw*ee**2*complex(0,1)*FT2)/sw',
                  order = {'QED':2,'T2':1})

GC_236 = Coupling(name = 'GC_236',
                  value = '(-2*cw**3*ee**2*complex(0,1)*FT2)/sw',
                  order = {'QED':2,'T2':1})

GC_237 = Coupling(name = 'GC_237',
                  value = '(-2*cw*ee**3*complex(0,1)*FT2)/sw',
                  order = {'QED':3,'T2':1})

GC_238 = Coupling(name = 'GC_238',
                  value = '(-4*cw*ee**4*complex(0,1)*FT2)/sw',
                  order = {'QED':4,'T2':1})

GC_239 = Coupling(name = 'GC_239',
                  value = '(-8*cw**3*ee*complex(0,1)*FT5)/sw',
                  order = {'QED':1,'T5':1})

GC_240 = Coupling(name = 'GC_240',
                  value = '(-8*cw*ee**2*complex(0,1)*FT5)/sw',
                  order = {'QED':2,'T5':1})

GC_241 = Coupling(name = 'GC_241',
                  value = '(8*cw**3*ee**2*complex(0,1)*FT5)/sw',
                  order = {'QED':2,'T5':1})

GC_242 = Coupling(name = 'GC_242',
                  value = '(16*cw**3*ee**2*complex(0,1)*FT5)/sw',
                  order = {'QED':2,'T5':1})

GC_243 = Coupling(name = 'GC_243',
                  value = '(4*cw**3*ee*complex(0,1)*FT6)/sw',
                  order = {'QED':1,'T6':1})

GC_244 = Coupling(name = 'GC_244',
                  value = '(-4*cw*ee**2*complex(0,1)*FT6)/sw',
                  order = {'QED':2,'T6':1})

GC_245 = Coupling(name = 'GC_245',
                  value = '(4*cw**3*ee**2*complex(0,1)*FT6)/sw',
                  order = {'QED':2,'T6':1})

GC_246 = Coupling(name = 'GC_246',
                  value = '-((cw**3*ee*complex(0,1)*FT7)/sw)',
                  order = {'QED':1,'T7':1})

GC_247 = Coupling(name = 'GC_247',
                  value = '(2*cw*ee**2*complex(0,1)*FT7)/sw',
                  order = {'QED':2,'T7':1})

GC_248 = Coupling(name = 'GC_248',
                  value = '(cw**3*ee**2*complex(0,1)*FT7)/sw',
                  order = {'QED':2,'T7':1})

GC_249 = Coupling(name = 'GC_249',
                  value = '(2*cw**3*ee**2*complex(0,1)*FT7)/sw',
                  order = {'QED':2,'T7':1})

GC_250 = Coupling(name = 'GC_250',
                  value = '-(ee*complex(0,1)*sw)/(6.*cw)',
                  order = {'QED':1})

GC_251 = Coupling(name = 'GC_251',
                  value = '(ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_252 = Coupling(name = 'GC_252',
                  value = '-2*cw*FM0*complex(0,1)*sw',
                  order = {'M0':1})

GC_253 = Coupling(name = 'GC_253',
                  value = '-(cw*FM1*complex(0,1)*sw)/2.',
                  order = {'M1':1})

GC_254 = Coupling(name = 'GC_254',
                  value = '4*cw*FM2*complex(0,1)*sw',
                  order = {'M2':1})

GC_255 = Coupling(name = 'GC_255',
                  value = 'cw*FM3*complex(0,1)*sw',
                  order = {'M3':1})

GC_256 = Coupling(name = 'GC_256',
                  value = '-2*cw*FM4*complex(0,1)*sw',
                  order = {'M4':1})

GC_257 = Coupling(name = 'GC_257',
                  value = '2*cw*FM4*complex(0,1)*sw',
                  order = {'M4':1})

GC_258 = Coupling(name = 'GC_258',
                  value = '(ee**2*FM4*complex(0,1)*sw)/(2.*cw)',
                  order = {'M4':1,'QED':2})

GC_259 = Coupling(name = 'GC_259',
                  value = '(ee**3*FM4*complex(0,1)*sw)/(2.*cw)',
                  order = {'M4':1,'QED':3})

GC_260 = Coupling(name = 'GC_260',
                  value = '-(cw*FM5*complex(0,1)*sw)',
                  order = {'M5':1})

GC_261 = Coupling(name = 'GC_261',
                  value = 'cw*FM5*complex(0,1)*sw',
                  order = {'M5':1})

GC_262 = Coupling(name = 'GC_262',
                  value = '(ee**2*FM5*complex(0,1)*sw)/(4.*cw)',
                  order = {'M5':1,'QED':2})

GC_263 = Coupling(name = 'GC_263',
                  value = '-(ee**3*FM5*complex(0,1)*sw)/(4.*cw)',
                  order = {'M5':1,'QED':3})

GC_264 = Coupling(name = 'GC_264',
                  value = '(cw*FM7*complex(0,1)*sw)/4.',
                  order = {'M7':1})

GC_265 = Coupling(name = 'GC_265',
                  value = '-(ee*FM7*complex(0,1)*sw)/(8.*cw)',
                  order = {'M7':1,'QED':1})

GC_266 = Coupling(name = 'GC_266',
                  value = '(ee**2*FM7*complex(0,1)*sw)/(8.*cw)',
                  order = {'M7':1,'QED':2})

GC_267 = Coupling(name = 'GC_267',
                  value = '(ee**3*FM7*complex(0,1)*sw)/(8.*cw)',
                  order = {'M7':1,'QED':3})

GC_268 = Coupling(name = 'GC_268',
                  value = '8*cw*complex(0,1)*FT0*sw',
                  order = {'T0':1})

GC_269 = Coupling(name = 'GC_269',
                  value = '8*cw**3*complex(0,1)*FT0*sw',
                  order = {'T0':1})

GC_270 = Coupling(name = 'GC_270',
                  value = '-8*cw*ee*complex(0,1)*FT0*sw',
                  order = {'QED':1,'T0':1})

GC_271 = Coupling(name = 'GC_271',
                  value = '-8*cw*ee**2*complex(0,1)*FT0*sw',
                  order = {'QED':2,'T0':1})

GC_272 = Coupling(name = 'GC_272',
                  value = '4*cw*complex(0,1)*FT1*sw',
                  order = {'T1':1})

GC_273 = Coupling(name = 'GC_273',
                  value = '8*cw**3*complex(0,1)*FT1*sw',
                  order = {'T1':1})

GC_274 = Coupling(name = 'GC_274',
                  value = '4*cw*ee*complex(0,1)*FT1*sw',
                  order = {'QED':1,'T1':1})

GC_275 = Coupling(name = 'GC_275',
                  value = '4*cw*ee**2*complex(0,1)*FT1*sw',
                  order = {'QED':2,'T1':1})

GC_276 = Coupling(name = 'GC_276',
                  value = 'cw*complex(0,1)*FT2*sw',
                  order = {'T2':1})

GC_277 = Coupling(name = 'GC_277',
                  value = '2*cw**3*complex(0,1)*FT2*sw',
                  order = {'T2':1})

GC_278 = Coupling(name = 'GC_278',
                  value = '-(cw*ee*complex(0,1)*FT2*sw)',
                  order = {'QED':1,'T2':1})

GC_279 = Coupling(name = 'GC_279',
                  value = 'cw*ee**2*complex(0,1)*FT2*sw',
                  order = {'QED':2,'T2':1})

GC_280 = Coupling(name = 'GC_280',
                  value = '-8*cw*complex(0,1)*FT5*sw',
                  order = {'T5':1})

GC_281 = Coupling(name = 'GC_281',
                  value = '-8*cw*ee*complex(0,1)*FT5*sw',
                  order = {'QED':1,'T5':1})

GC_282 = Coupling(name = 'GC_282',
                  value = '8*cw*ee*complex(0,1)*FT5*sw',
                  order = {'QED':1,'T5':1})

GC_283 = Coupling(name = 'GC_283',
                  value = '8*cw*ee**2*complex(0,1)*FT5*sw',
                  order = {'QED':2,'T5':1})

GC_284 = Coupling(name = 'GC_284',
                  value = '16*cw*ee**2*complex(0,1)*FT5*sw',
                  order = {'QED':2,'T5':1})

GC_285 = Coupling(name = 'GC_285',
                  value = '-4*cw*complex(0,1)*FT6*sw',
                  order = {'T6':1})

GC_286 = Coupling(name = 'GC_286',
                  value = '-4*cw*ee*complex(0,1)*FT6*sw',
                  order = {'QED':1,'T6':1})

GC_287 = Coupling(name = 'GC_287',
                  value = '4*cw*ee*complex(0,1)*FT6*sw',
                  order = {'QED':1,'T6':1})

GC_288 = Coupling(name = 'GC_288',
                  value = '4*cw*ee**2*complex(0,1)*FT6*sw',
                  order = {'QED':2,'T6':1})

GC_289 = Coupling(name = 'GC_289',
                  value = '-(cw*complex(0,1)*FT7*sw)',
                  order = {'T7':1})

GC_290 = Coupling(name = 'GC_290',
                  value = '-(cw*ee*complex(0,1)*FT7*sw)',
                  order = {'QED':1,'T7':1})

GC_291 = Coupling(name = 'GC_291',
                  value = 'cw*ee*complex(0,1)*FT7*sw',
                  order = {'QED':1,'T7':1})

GC_292 = Coupling(name = 'GC_292',
                  value = '-2*cw*ee**2*complex(0,1)*FT7*sw',
                  order = {'QED':2,'T7':1})

GC_293 = Coupling(name = 'GC_293',
                  value = '2*cw*ee**2*complex(0,1)*FT7*sw',
                  order = {'QED':2,'T7':1})

GC_294 = Coupling(name = 'GC_294',
                  value = '-32*cw**3*complex(0,1)*FT8*sw',
                  order = {'T8':1})

GC_295 = Coupling(name = 'GC_295',
                  value = '-8*cw**3*complex(0,1)*FT9*sw',
                  order = {'T9':1})

GC_296 = Coupling(name = 'GC_296',
                  value = '-2*FM0*complex(0,1)*sw**2',
                  order = {'M0':1})

GC_297 = Coupling(name = 'GC_297',
                  value = '-(FM1*complex(0,1)*sw**2)/2.',
                  order = {'M1':1})

GC_298 = Coupling(name = 'GC_298',
                  value = '-4*FM2*complex(0,1)*sw**2',
                  order = {'M2':1})

GC_299 = Coupling(name = 'GC_299',
                  value = '-(FM3*complex(0,1)*sw**2)',
                  order = {'M3':1})

GC_300 = Coupling(name = 'GC_300',
                  value = '-(ee**3*FM4*complex(0,1)*sw**2)/(2.*cw**2)',
                  order = {'M4':1,'QED':3})

GC_301 = Coupling(name = 'GC_301',
                  value = '(ee**3*FM5*complex(0,1)*sw**2)/(4.*cw**2)',
                  order = {'M5':1,'QED':3})

GC_302 = Coupling(name = 'GC_302',
                  value = '(FM7*complex(0,1)*sw**2)/4.',
                  order = {'M7':1})

GC_303 = Coupling(name = 'GC_303',
                  value = '-(ee**2*FM7*complex(0,1)*sw**2)/(8.*cw**2)',
                  order = {'M7':1,'QED':2})

GC_304 = Coupling(name = 'GC_304',
                  value = '-(ee**3*FM7*complex(0,1)*sw**2)/(8.*cw**2)',
                  order = {'M7':1,'QED':3})

GC_305 = Coupling(name = 'GC_305',
                  value = '8*complex(0,1)*FT0*sw**2',
                  order = {'T0':1})

GC_306 = Coupling(name = 'GC_306',
                  value = '8*cw**2*complex(0,1)*FT0*sw**2',
                  order = {'T0':1})

GC_307 = Coupling(name = 'GC_307',
                  value = '-8*ee*complex(0,1)*FT0*sw**2',
                  order = {'QED':1,'T0':1})

GC_308 = Coupling(name = 'GC_308',
                  value = '-8*ee**2*complex(0,1)*FT0*sw**2',
                  order = {'QED':2,'T0':1})

GC_309 = Coupling(name = 'GC_309',
                  value = '4*complex(0,1)*FT1*sw**2',
                  order = {'T1':1})

GC_310 = Coupling(name = 'GC_310',
                  value = '8*cw**2*complex(0,1)*FT1*sw**2',
                  order = {'T1':1})

GC_311 = Coupling(name = 'GC_311',
                  value = '4*ee*complex(0,1)*FT1*sw**2',
                  order = {'QED':1,'T1':1})

GC_312 = Coupling(name = 'GC_312',
                  value = '-4*ee**2*complex(0,1)*FT1*sw**2',
                  order = {'QED':2,'T1':1})

GC_313 = Coupling(name = 'GC_313',
                  value = 'complex(0,1)*FT2*sw**2',
                  order = {'T2':1})

GC_314 = Coupling(name = 'GC_314',
                  value = '2*cw**2*complex(0,1)*FT2*sw**2',
                  order = {'T2':1})

GC_315 = Coupling(name = 'GC_315',
                  value = '-2*ee*complex(0,1)*FT2*sw**2',
                  order = {'QED':1,'T2':1})

GC_316 = Coupling(name = 'GC_316',
                  value = '-2*ee**2*complex(0,1)*FT2*sw**2',
                  order = {'QED':2,'T2':1})

GC_317 = Coupling(name = 'GC_317',
                  value = '8*complex(0,1)*FT5*sw**2',
                  order = {'T5':1})

GC_318 = Coupling(name = 'GC_318',
                  value = '-16*cw**2*complex(0,1)*FT5*sw**2',
                  order = {'T5':1})

GC_319 = Coupling(name = 'GC_319',
                  value = '16*cw**2*complex(0,1)*FT5*sw**2',
                  order = {'T5':1})

GC_320 = Coupling(name = 'GC_320',
                  value = '-8*ee*complex(0,1)*FT5*sw**2',
                  order = {'QED':1,'T5':1})

GC_321 = Coupling(name = 'GC_321',
                  value = '-8*ee**2*complex(0,1)*FT5*sw**2',
                  order = {'QED':2,'T5':1})

GC_322 = Coupling(name = 'GC_322',
                  value = '4*complex(0,1)*FT6*sw**2',
                  order = {'T6':1})

GC_323 = Coupling(name = 'GC_323',
                  value = '-8*cw**2*complex(0,1)*FT6*sw**2',
                  order = {'T6':1})

GC_324 = Coupling(name = 'GC_324',
                  value = '16*cw**2*complex(0,1)*FT6*sw**2',
                  order = {'T6':1})

GC_325 = Coupling(name = 'GC_325',
                  value = '4*ee*complex(0,1)*FT6*sw**2',
                  order = {'QED':1,'T6':1})

GC_326 = Coupling(name = 'GC_326',
                  value = '-4*ee**2*complex(0,1)*FT6*sw**2',
                  order = {'QED':2,'T6':1})

GC_327 = Coupling(name = 'GC_327',
                  value = 'complex(0,1)*FT7*sw**2',
                  order = {'T7':1})

GC_328 = Coupling(name = 'GC_328',
                  value = '-4*cw**2*complex(0,1)*FT7*sw**2',
                  order = {'T7':1})

GC_329 = Coupling(name = 'GC_329',
                  value = '4*cw**2*complex(0,1)*FT7*sw**2',
                  order = {'T7':1})

GC_330 = Coupling(name = 'GC_330',
                  value = '-(ee*complex(0,1)*FT7*sw**2)',
                  order = {'QED':1,'T7':1})

GC_331 = Coupling(name = 'GC_331',
                  value = '-(ee**2*complex(0,1)*FT7*sw**2)',
                  order = {'QED':2,'T7':1})

GC_332 = Coupling(name = 'GC_332',
                  value = '32*cw**2*complex(0,1)*FT8*sw**2',
                  order = {'T8':1})

GC_333 = Coupling(name = 'GC_333',
                  value = '8*cw**2*complex(0,1)*FT9*sw**2',
                  order = {'T9':1})

GC_334 = Coupling(name = 'GC_334',
                  value = '8*cw*complex(0,1)*FT0*sw**3',
                  order = {'T0':1})

GC_335 = Coupling(name = 'GC_335',
                  value = '8*cw*complex(0,1)*FT1*sw**3',
                  order = {'T1':1})

GC_336 = Coupling(name = 'GC_336',
                  value = '2*cw*complex(0,1)*FT2*sw**3',
                  order = {'T2':1})

GC_337 = Coupling(name = 'GC_337',
                  value = '-32*cw*complex(0,1)*FT8*sw**3',
                  order = {'T8':1})

GC_338 = Coupling(name = 'GC_338',
                  value = '-8*cw*complex(0,1)*FT9*sw**3',
                  order = {'T9':1})

GC_339 = Coupling(name = 'GC_339',
                  value = '8*complex(0,1)*FT0*sw**4',
                  order = {'T0':1})

GC_340 = Coupling(name = 'GC_340',
                  value = '8*complex(0,1)*FT1*sw**4',
                  order = {'T1':1})

GC_341 = Coupling(name = 'GC_341',
                  value = '2*complex(0,1)*FT2*sw**4',
                  order = {'T2':1})

GC_342 = Coupling(name = 'GC_342',
                  value = '32*complex(0,1)*FT8*sw**4',
                  order = {'T8':1})

GC_343 = Coupling(name = 'GC_343',
                  value = '8*complex(0,1)*FT9*sw**4',
                  order = {'T9':1})

GC_344 = Coupling(name = 'GC_344',
                  value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_345 = Coupling(name = 'GC_345',
                  value = '-((cw**3*ee**3*FM0*complex(0,1))/sw**3) - (2*cw*ee**3*FM0*complex(0,1))/sw - (ee**3*FM0*complex(0,1)*sw)/cw',
                  order = {'M0':1,'QED':3})

GC_346 = Coupling(name = 'GC_346',
                  value = '(2*cw**3*ee**4*FM0*complex(0,1))/sw**3 + (4*cw*ee**4*FM0*complex(0,1))/sw + (2*ee**4*FM0*complex(0,1)*sw)/cw',
                  order = {'M0':1,'QED':4})

GC_347 = Coupling(name = 'GC_347',
                  value = '-(cw**3*ee**3*FM1*complex(0,1))/(4.*sw**3) - (cw*ee**3*FM1*complex(0,1))/(2.*sw) - (ee**3*FM1*complex(0,1)*sw)/(4.*cw)',
                  order = {'M1':1,'QED':3})

GC_348 = Coupling(name = 'GC_348',
                  value = '-((cw**3*ee**4*FM1*complex(0,1))/sw**3) - (2*cw*ee**4*FM1*complex(0,1))/sw - (ee**4*FM1*complex(0,1)*sw)/cw',
                  order = {'M1':1,'QED':4})

GC_349 = Coupling(name = 'GC_349',
                  value = '(cw*ee**3*FM7*complex(0,1))/(8.*sw) + (ee**3*FM7*complex(0,1)*sw)/(8.*cw)',
                  order = {'M7':1,'QED':3})

GC_350 = Coupling(name = 'GC_350',
                  value = '(cw**3*ee**4*FM7*complex(0,1))/(2.*sw**3) + (cw*ee**4*FM7*complex(0,1))/sw + (ee**4*FM7*complex(0,1)*sw)/(2.*cw)',
                  order = {'M7':1,'QED':4})

GC_351 = Coupling(name = 'GC_351',
                  value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_352 = Coupling(name = 'GC_352',
                  value = '2*cw**2*ee**2*FM0*complex(0,1) + (cw**4*ee**2*FM0*complex(0,1))/sw**2 + ee**2*FM0*complex(0,1)*sw**2',
                  order = {'M0':1,'QED':2})

GC_353 = Coupling(name = 'GC_353',
                  value = '2*ee**2*FM0*complex(0,1) + (ee**2*FM0*complex(0,1)*sw**2)/cw**2',
                  order = {'M0':1,'QED':2})

GC_354 = Coupling(name = 'GC_354',
                  value = '-2*ee**3*FM0*complex(0,1) - (cw**2*ee**3*FM0*complex(0,1))/sw**2 - (ee**3*FM0*complex(0,1)*sw**2)/cw**2',
                  order = {'M0':1,'QED':3})

GC_355 = Coupling(name = 'GC_355',
                  value = '-2*ee**4*FM0*complex(0,1) - (cw**2*ee**4*FM0*complex(0,1))/sw**2 - (ee**4*FM0*complex(0,1)*sw**2)/cw**2',
                  order = {'M0':1,'QED':4})

GC_356 = Coupling(name = 'GC_356',
                  value = '(cw**2*ee**2*FM1*complex(0,1))/2. + (cw**4*ee**2*FM1*complex(0,1))/(4.*sw**2) + (ee**2*FM1*complex(0,1)*sw**2)/4.',
                  order = {'M1':1,'QED':2})

GC_357 = Coupling(name = 'GC_357',
                  value = '(ee**2*FM1*complex(0,1))/2. + (ee**2*FM1*complex(0,1)*sw**2)/(4.*cw**2)',
                  order = {'M1':1,'QED':2})

GC_358 = Coupling(name = 'GC_358',
                  value = '(ee**3*FM1*complex(0,1))/2. + (cw**2*ee**3*FM1*complex(0,1))/(4.*sw**2) + (ee**3*FM1*complex(0,1)*sw**2)/(4.*cw**2)',
                  order = {'M1':1,'QED':3})

GC_359 = Coupling(name = 'GC_359',
                  value = '-(ee**4*FM1*complex(0,1)) - (cw**2*ee**4*FM1*complex(0,1))/(2.*sw**2) - (ee**4*FM1*complex(0,1)*sw**2)/(2.*cw**2)',
                  order = {'M1':1,'QED':4})

GC_360 = Coupling(name = 'GC_360',
                  value = '4*cw**2*ee**2*FM2*complex(0,1) + (2*cw**4*ee**2*FM2*complex(0,1))/sw**2 + 2*ee**2*FM2*complex(0,1)*sw**2',
                  order = {'M2':1,'QED':2})

GC_361 = Coupling(name = 'GC_361',
                  value = 'cw**2*ee**2*FM3*complex(0,1) + (cw**4*ee**2*FM3*complex(0,1))/(2.*sw**2) + (ee**2*FM3*complex(0,1)*sw**2)/2.',
                  order = {'M3':1,'QED':2})

GC_362 = Coupling(name = 'GC_362',
                  value = 'cw**2*FM4*complex(0,1) - FM4*complex(0,1)*sw**2',
                  order = {'M4':1})

GC_363 = Coupling(name = 'GC_363',
                  value = '-(cw**2*FM5*complex(0,1))/2. + (FM5*complex(0,1)*sw**2)/2.',
                  order = {'M5':1})

GC_364 = Coupling(name = 'GC_364',
                  value = '-(cw**2*ee**2*FM7*complex(0,1))/4. - (cw**4*ee**2*FM7*complex(0,1))/(8.*sw**2) - (ee**2*FM7*complex(0,1)*sw**2)/8.',
                  order = {'M7':1,'QED':2})

GC_365 = Coupling(name = 'GC_365',
                  value = '(ee**4*FM7*complex(0,1))/2. + (cw**2*ee**4*FM7*complex(0,1))/(4.*sw**2) + (ee**4*FM7*complex(0,1)*sw**2)/(4.*cw**2)',
                  order = {'M7':1,'QED':4})

GC_366 = Coupling(name = 'GC_366',
                  value = '-2*ee**2*complex(0,1)*FS0 - (cw**2*ee**2*complex(0,1)*FS0)/sw**2 - (ee**2*complex(0,1)*FS0*sw**2)/cw**2',
                  order = {'QED':2,'S0':1})

GC_367 = Coupling(name = 'GC_367',
                  value = '-2*ee**2*complex(0,1)*FS1 - (cw**2*ee**2*complex(0,1)*FS1)/sw**2 - (ee**2*complex(0,1)*FS1*sw**2)/cw**2',
                  order = {'QED':2,'S1':1})

GC_368 = Coupling(name = 'GC_368',
                  value = '-2*ee**2*complex(0,1)*FS2 - (cw**2*ee**2*complex(0,1)*FS2)/sw**2 - (ee**2*complex(0,1)*FS2*sw**2)/cw**2',
                  order = {'QED':2,'S2':1})

GC_369 = Coupling(name = 'GC_369',
                  value = '(cw**3*ee**2*FM0*complex(0,1))/sw + 2*cw*ee**2*FM0*complex(0,1)*sw + (ee**2*FM0*complex(0,1)*sw**3)/cw',
                  order = {'M0':1,'QED':2})

GC_370 = Coupling(name = 'GC_370',
                  value = '(cw**3*ee**2*FM1*complex(0,1))/(4.*sw) + (cw*ee**2*FM1*complex(0,1)*sw)/2. + (ee**2*FM1*complex(0,1)*sw**3)/(4.*cw)',
                  order = {'M1':1,'QED':2})

GC_371 = Coupling(name = 'GC_371',
                  value = '(-2*cw**3*ee**2*FM2*complex(0,1))/sw - 4*cw*ee**2*FM2*complex(0,1)*sw - (2*ee**2*FM2*complex(0,1)*sw**3)/cw',
                  order = {'M2':1,'QED':2})

GC_372 = Coupling(name = 'GC_372',
                  value = '-(cw**3*ee**2*FM3*complex(0,1))/(2.*sw) - cw*ee**2*FM3*complex(0,1)*sw - (ee**2*FM3*complex(0,1)*sw**3)/(2.*cw)',
                  order = {'M3':1,'QED':2})

GC_373 = Coupling(name = 'GC_373',
                  value = '-((cw**3*ee**2*FM4*complex(0,1))/sw) - 2*cw*ee**2*FM4*complex(0,1)*sw - (ee**2*FM4*complex(0,1)*sw**3)/cw',
                  order = {'M4':1,'QED':2})

GC_374 = Coupling(name = 'GC_374',
                  value = '(cw**3*ee**2*FM4*complex(0,1))/sw + 2*cw*ee**2*FM4*complex(0,1)*sw + (ee**2*FM4*complex(0,1)*sw**3)/cw',
                  order = {'M4':1,'QED':2})

GC_375 = Coupling(name = 'GC_375',
                  value = '-(cw**3*ee**2*FM5*complex(0,1))/(2.*sw) - cw*ee**2*FM5*complex(0,1)*sw - (ee**2*FM5*complex(0,1)*sw**3)/(2.*cw)',
                  order = {'M5':1,'QED':2})

GC_376 = Coupling(name = 'GC_376',
                  value = '(cw**3*ee**2*FM5*complex(0,1))/(2.*sw) + cw*ee**2*FM5*complex(0,1)*sw + (ee**2*FM5*complex(0,1)*sw**3)/(2.*cw)',
                  order = {'M5':1,'QED':2})

GC_377 = Coupling(name = 'GC_377',
                  value = '-(cw**3*ee**2*FM7*complex(0,1))/(8.*sw) - (cw*ee**2*FM7*complex(0,1)*sw)/4. - (ee**2*FM7*complex(0,1)*sw**3)/(8.*cw)',
                  order = {'M7':1,'QED':2})

GC_378 = Coupling(name = 'GC_378',
                  value = '8*cw**3*complex(0,1)*FT5*sw - 8*cw*complex(0,1)*FT5*sw**3',
                  order = {'T5':1})

GC_379 = Coupling(name = 'GC_379',
                  value = '-8*cw**3*complex(0,1)*FT5*sw + 8*cw*complex(0,1)*FT5*sw**3',
                  order = {'T5':1})

GC_380 = Coupling(name = 'GC_380',
                  value = '8*cw**3*complex(0,1)*FT6*sw - 8*cw*complex(0,1)*FT6*sw**3',
                  order = {'T6':1})

GC_381 = Coupling(name = 'GC_381',
                  value = '-8*cw**3*complex(0,1)*FT6*sw + 8*cw*complex(0,1)*FT6*sw**3',
                  order = {'T6':1})

GC_382 = Coupling(name = 'GC_382',
                  value = '2*cw**3*complex(0,1)*FT7*sw - 2*cw*complex(0,1)*FT7*sw**3',
                  order = {'T7':1})

GC_383 = Coupling(name = 'GC_383',
                  value = '-2*cw**3*complex(0,1)*FT7*sw + 2*cw*complex(0,1)*FT7*sw**3',
                  order = {'T7':1})

GC_384 = Coupling(name = 'GC_384',
                  value = 'cw**2*ee**2*FM0*complex(0,1) + 2*ee**2*FM0*complex(0,1)*sw**2 + (ee**2*FM0*complex(0,1)*sw**4)/cw**2',
                  order = {'M0':1,'QED':2})

GC_385 = Coupling(name = 'GC_385',
                  value = '(cw**2*ee**2*FM1*complex(0,1))/4. + (ee**2*FM1*complex(0,1)*sw**2)/2. + (ee**2*FM1*complex(0,1)*sw**4)/(4.*cw**2)',
                  order = {'M1':1,'QED':2})

GC_386 = Coupling(name = 'GC_386',
                  value = '2*cw**2*ee**2*FM2*complex(0,1) + 4*ee**2*FM2*complex(0,1)*sw**2 + (2*ee**2*FM2*complex(0,1)*sw**4)/cw**2',
                  order = {'M2':1,'QED':2})

GC_387 = Coupling(name = 'GC_387',
                  value = '(cw**2*ee**2*FM3*complex(0,1))/2. + ee**2*FM3*complex(0,1)*sw**2 + (ee**2*FM3*complex(0,1)*sw**4)/(2.*cw**2)',
                  order = {'M3':1,'QED':2})

GC_388 = Coupling(name = 'GC_388',
                  value = '-(cw**2*ee**2*FM4*complex(0,1))/2. - (cw**4*ee**2*FM4*complex(0,1))/(2.*sw**2) + (ee**2*FM4*complex(0,1)*sw**2)/2. + (ee**2*FM4*complex(0,1)*sw**4)/(2.*cw**2)',
                  order = {'M4':1,'QED':2})

GC_389 = Coupling(name = 'GC_389',
                  value = '(cw**2*ee**2*FM5*complex(0,1))/4. + (cw**4*ee**2*FM5*complex(0,1))/(4.*sw**2) - (ee**2*FM5*complex(0,1)*sw**2)/4. - (ee**2*FM5*complex(0,1)*sw**4)/(4.*cw**2)',
                  order = {'M5':1,'QED':2})

GC_390 = Coupling(name = 'GC_390',
                  value = '-(cw**2*ee**2*FM7*complex(0,1))/8. - (ee**2*FM7*complex(0,1)*sw**2)/4. - (ee**2*FM7*complex(0,1)*sw**4)/(8.*cw**2)',
                  order = {'M7':1,'QED':2})

GC_391 = Coupling(name = 'GC_391',
                  value = '18*ee**4*complex(0,1)*FS0 + (3*cw**4*ee**4*complex(0,1)*FS0)/sw**4 + (12*cw**2*ee**4*complex(0,1)*FS0)/sw**2 + (12*ee**4*complex(0,1)*FS0*sw**2)/cw**2 + (3*ee**4*complex(0,1)*FS0*sw**4)/cw**4',
                  order = {'QED':4,'S0':1})

GC_392 = Coupling(name = 'GC_392',
                  value = '18*ee**4*complex(0,1)*FS1 + (3*cw**4*ee**4*complex(0,1)*FS1)/sw**4 + (12*cw**2*ee**4*complex(0,1)*FS1)/sw**2 + (12*ee**4*complex(0,1)*FS1*sw**2)/cw**2 + (3*ee**4*complex(0,1)*FS1*sw**4)/cw**4',
                  order = {'QED':4,'S1':1})

GC_393 = Coupling(name = 'GC_393',
                  value = '18*ee**4*complex(0,1)*FS2 + (3*cw**4*ee**4*complex(0,1)*FS2)/sw**4 + (12*cw**2*ee**4*complex(0,1)*FS2)/sw**2 + (12*ee**4*complex(0,1)*FS2*sw**2)/cw**2 + (3*ee**4*complex(0,1)*FS2*sw**4)/cw**4',
                  order = {'QED':4,'S2':1})

GC_394 = Coupling(name = 'GC_394',
                  value = '8*cw**4*complex(0,1)*FT5 + 8*complex(0,1)*FT5*sw**4',
                  order = {'T5':1})

GC_395 = Coupling(name = 'GC_395',
                  value = '4*cw**4*complex(0,1)*FT6 + 4*complex(0,1)*FT6*sw**4',
                  order = {'T6':1})

GC_396 = Coupling(name = 'GC_396',
                  value = 'cw**4*complex(0,1)*FT7 + complex(0,1)*FT7*sw**4',
                  order = {'T7':1})

GC_397 = Coupling(name = 'GC_397',
                  value = 'ee**2*FM0*complex(0,1)*vev',
                  order = {'M0':1,'QED':1})

GC_398 = Coupling(name = 'GC_398',
                  value = '(ee**2*FM1*complex(0,1)*vev)/4.',
                  order = {'M1':1,'QED':1})

GC_399 = Coupling(name = 'GC_399',
                  value = '2*ee**2*FM2*complex(0,1)*vev',
                  order = {'M2':1,'QED':1})

GC_400 = Coupling(name = 'GC_400',
                  value = '-(ee**2*FM3*complex(0,1)*vev)/2.',
                  order = {'M3':1,'QED':1})

GC_401 = Coupling(name = 'GC_401',
                  value = '-(ee*FM4*complex(0,1)*vev)/2.',
                  order = {'M4':1})

GC_402 = Coupling(name = 'GC_402',
                  value = '-(ee**2*FM4*complex(0,1)*vev)/2.',
                  order = {'M4':1,'QED':1})

GC_403 = Coupling(name = 'GC_403',
                  value = '-(ee**3*FM4*complex(0,1)*vev)/2.',
                  order = {'M4':1,'QED':2})

GC_404 = Coupling(name = 'GC_404',
                  value = '(ee*FM5*complex(0,1)*vev)/4.',
                  order = {'M5':1})

GC_405 = Coupling(name = 'GC_405',
                  value = '(ee**2*FM5*complex(0,1)*vev)/4.',
                  order = {'M5':1,'QED':1})

GC_406 = Coupling(name = 'GC_406',
                  value = '(ee**3*FM5*complex(0,1)*vev)/2.',
                  order = {'M5':1,'QED':2})

GC_407 = Coupling(name = 'GC_407',
                  value = '-(ee*FM7*complex(0,1)*vev)/8.',
                  order = {'M7':1})

GC_408 = Coupling(name = 'GC_408',
                  value = '-(ee**2*FM7*complex(0,1)*vev)/8.',
                  order = {'M7':1,'QED':1})

GC_409 = Coupling(name = 'GC_409',
                  value = '-(ee**2*FM7*complex(0,1)*vev)/4.',
                  order = {'M7':1,'QED':1})

GC_410 = Coupling(name = 'GC_410',
                  value = '-(ee**3*FM7*complex(0,1)*vev)/4.',
                  order = {'M7':1,'QED':2})

GC_411 = Coupling(name = 'GC_411',
                  value = '-(ee**4*FM7*complex(0,1)*vev)/(4.*cw**2)',
                  order = {'M7':1,'QED':3})

GC_412 = Coupling(name = 'GC_412',
                  value = '-6*complex(0,1)*lam*vev',
                  order = {'QED':1})

GC_413 = Coupling(name = 'GC_413',
                  value = '(3*ee**4*FM0*complex(0,1)*vev)/sw**4',
                  order = {'M0':1,'QED':3})

GC_414 = Coupling(name = 'GC_414',
                  value = '-((cw**2*ee**4*FM0*complex(0,1)*vev)/sw**4)',
                  order = {'M0':1,'QED':3})

GC_415 = Coupling(name = 'GC_415',
                  value = '(-3*ee**4*FM1*complex(0,1)*vev)/(2.*sw**4)',
                  order = {'M1':1,'QED':3})

GC_416 = Coupling(name = 'GC_416',
                  value = '(3*cw**2*ee**4*FM1*complex(0,1)*vev)/(2.*sw**4)',
                  order = {'M1':1,'QED':3})

GC_417 = Coupling(name = 'GC_417',
                  value = '(3*ee**4*FM7*complex(0,1)*vev)/(4.*sw**4)',
                  order = {'M7':1,'QED':3})

GC_418 = Coupling(name = 'GC_418',
                  value = '(-9*cw**2*ee**4*FM7*complex(0,1)*vev)/(4.*sw**4)',
                  order = {'M7':1,'QED':3})

GC_419 = Coupling(name = 'GC_419',
                  value = '(6*ee**4*complex(0,1)*FS0*vev)/sw**4',
                  order = {'QED':3,'S0':1})

GC_420 = Coupling(name = 'GC_420',
                  value = '(3*ee**4*complex(0,1)*FS1*vev)/sw**4',
                  order = {'QED':3,'S1':1})

GC_421 = Coupling(name = 'GC_421',
                  value = '(3*ee**4*complex(0,1)*FS2*vev)/sw**4',
                  order = {'QED':3,'S2':1})

GC_422 = Coupling(name = 'GC_422',
                  value = '-((cw*ee**3*FM0*complex(0,1)*vev)/sw**3)',
                  order = {'M0':1,'QED':2})

GC_423 = Coupling(name = 'GC_423',
                  value = '(4*cw*ee**4*FM0*complex(0,1)*vev)/sw**3',
                  order = {'M0':1,'QED':3})

GC_424 = Coupling(name = 'GC_424',
                  value = '(cw*ee**3*FM1*complex(0,1)*vev)/(4.*sw**3)',
                  order = {'M1':1,'QED':2})

GC_425 = Coupling(name = 'GC_425',
                  value = '-((cw*ee**4*FM1*complex(0,1)*vev)/sw**3)',
                  order = {'M1':1,'QED':3})

GC_426 = Coupling(name = 'GC_426',
                  value = '-(cw*ee**3*FM4*complex(0,1)*vev)/(2.*sw**3)',
                  order = {'M4':1,'QED':2})

GC_427 = Coupling(name = 'GC_427',
                  value = '(cw**3*ee**3*FM4*complex(0,1)*vev)/(2.*sw**3)',
                  order = {'M4':1,'QED':2})

GC_428 = Coupling(name = 'GC_428',
                  value = '-(cw*ee**3*FM5*complex(0,1)*vev)/(2.*sw**3)',
                  order = {'M5':1,'QED':2})

GC_429 = Coupling(name = 'GC_429',
                  value = '-(cw**3*ee**3*FM5*complex(0,1)*vev)/(4.*sw**3)',
                  order = {'M5':1,'QED':2})

GC_430 = Coupling(name = 'GC_430',
                  value = '(cw*ee**3*FM7*complex(0,1)*vev)/(8.*sw**3)',
                  order = {'M7':1,'QED':2})

GC_431 = Coupling(name = 'GC_431',
                  value = '(3*cw**3*ee**3*FM7*complex(0,1)*vev)/(8.*sw**3)',
                  order = {'M7':1,'QED':2})

GC_432 = Coupling(name = 'GC_432',
                  value = '-(cw*ee**4*FM7*complex(0,1)*vev)/(2.*sw**3)',
                  order = {'M7':1,'QED':3})

GC_433 = Coupling(name = 'GC_433',
                  value = '(ee**2*complex(0,1)*vev)/(2.*sw**2)',
                  order = {'QED':1})

GC_434 = Coupling(name = 'GC_434',
                  value = '(ee**2*FM0*complex(0,1)*vev)/sw**2',
                  order = {'M0':1,'QED':1})

GC_435 = Coupling(name = 'GC_435',
                  value = '(cw**2*ee**2*FM0*complex(0,1)*vev)/sw**2',
                  order = {'M0':1,'QED':1})

GC_436 = Coupling(name = 'GC_436',
                  value = '-((ee**3*FM0*complex(0,1)*vev)/sw**2)',
                  order = {'M0':1,'QED':2})

GC_437 = Coupling(name = 'GC_437',
                  value = '-((ee**4*FM0*complex(0,1)*vev)/sw**2)',
                  order = {'M0':1,'QED':3})

GC_438 = Coupling(name = 'GC_438',
                  value = '-(ee**2*FM1*complex(0,1)*vev)/(4.*sw**2)',
                  order = {'M1':1,'QED':1})

GC_439 = Coupling(name = 'GC_439',
                  value = '(cw**2*ee**2*FM1*complex(0,1)*vev)/(4.*sw**2)',
                  order = {'M1':1,'QED':1})

GC_440 = Coupling(name = 'GC_440',
                  value = '-(ee**3*FM1*complex(0,1)*vev)/(4.*sw**2)',
                  order = {'M1':1,'QED':2})

GC_441 = Coupling(name = 'GC_441',
                  value = '(ee**4*FM1*complex(0,1)*vev)/sw**2',
                  order = {'M1':1,'QED':3})

GC_442 = Coupling(name = 'GC_442',
                  value = '(2*cw**2*ee**2*FM2*complex(0,1)*vev)/sw**2',
                  order = {'M2':1,'QED':1})

GC_443 = Coupling(name = 'GC_443',
                  value = '(cw**2*ee**2*FM3*complex(0,1)*vev)/(2.*sw**2)',
                  order = {'M3':1,'QED':1})

GC_444 = Coupling(name = 'GC_444',
                  value = '-(cw**2*ee**2*FM4*complex(0,1)*vev)/(2.*sw**2)',
                  order = {'M4':1,'QED':1})

GC_445 = Coupling(name = 'GC_445',
                  value = '(ee**3*FM4*complex(0,1)*vev)/(2.*sw**2)',
                  order = {'M4':1,'QED':2})

GC_446 = Coupling(name = 'GC_446',
                  value = '-(cw**2*ee**3*FM4*complex(0,1)*vev)/(2.*sw**2)',
                  order = {'M4':1,'QED':2})

GC_447 = Coupling(name = 'GC_447',
                  value = '(cw**2*ee**2*FM5*complex(0,1)*vev)/(4.*sw**2)',
                  order = {'M5':1,'QED':1})

GC_448 = Coupling(name = 'GC_448',
                  value = '(ee**3*FM5*complex(0,1)*vev)/(2.*sw**2)',
                  order = {'M5':1,'QED':2})

GC_449 = Coupling(name = 'GC_449',
                  value = '(cw**2*ee**3*FM5*complex(0,1)*vev)/(4.*sw**2)',
                  order = {'M5':1,'QED':2})

GC_450 = Coupling(name = 'GC_450',
                  value = '(ee**2*FM7*complex(0,1)*vev)/(4.*sw**2)',
                  order = {'M7':1,'QED':1})

GC_451 = Coupling(name = 'GC_451',
                  value = '-(cw**2*ee**2*FM7*complex(0,1)*vev)/(8.*sw**2)',
                  order = {'M7':1,'QED':1})

GC_452 = Coupling(name = 'GC_452',
                  value = '(ee**3*FM7*complex(0,1)*vev)/(4.*sw**2)',
                  order = {'M7':1,'QED':2})

GC_453 = Coupling(name = 'GC_453',
                  value = '-(cw**2*ee**3*FM7*complex(0,1)*vev)/(8.*sw**2)',
                  order = {'M7':1,'QED':2})

GC_454 = Coupling(name = 'GC_454',
                  value = '-((ee**4*FM7*complex(0,1)*vev)/sw**2)',
                  order = {'M7':1,'QED':3})

GC_455 = Coupling(name = 'GC_455',
                  value = '(-3*ee**4*FM7*complex(0,1)*vev)/(2.*sw**2)',
                  order = {'M7':1,'QED':3})

GC_456 = Coupling(name = 'GC_456',
                  value = '-(ee**2*complex(0,1)*FS0*vev)/(2.*sw**2)',
                  order = {'QED':1,'S0':1})

GC_457 = Coupling(name = 'GC_457',
                  value = '-((ee**2*complex(0,1)*FS1*vev)/sw**2)',
                  order = {'QED':1,'S1':1})

GC_458 = Coupling(name = 'GC_458',
                  value = '-(ee**2*complex(0,1)*FS2*vev)/(2.*sw**2)',
                  order = {'QED':1,'S2':1})

GC_459 = Coupling(name = 'GC_459',
                  value = '(cw*ee**2*FM0*complex(0,1)*vev)/sw',
                  order = {'M0':1,'QED':1})

GC_460 = Coupling(name = 'GC_460',
                  value = '-(cw*ee**2*FM1*complex(0,1)*vev)/(4.*sw)',
                  order = {'M1':1,'QED':1})

GC_461 = Coupling(name = 'GC_461',
                  value = '(-2*cw*ee**2*FM2*complex(0,1)*vev)/sw',
                  order = {'M2':1,'QED':1})

GC_462 = Coupling(name = 'GC_462',
                  value = '(cw*ee**2*FM3*complex(0,1)*vev)/(2.*sw)',
                  order = {'M3':1,'QED':1})

GC_463 = Coupling(name = 'GC_463',
                  value = '(cw*ee*FM4*complex(0,1)*vev)/(2.*sw)',
                  order = {'M4':1})

GC_464 = Coupling(name = 'GC_464',
                  value = '(cw*ee**2*FM4*complex(0,1)*vev)/(2.*sw)',
                  order = {'M4':1,'QED':1})

GC_465 = Coupling(name = 'GC_465',
                  value = '-((cw*ee**2*FM4*complex(0,1)*vev)/sw)',
                  order = {'M4':1,'QED':1})

GC_466 = Coupling(name = 'GC_466',
                  value = '(cw*ee**3*FM4*complex(0,1)*vev)/(2.*sw)',
                  order = {'M4':1,'QED':2})

GC_467 = Coupling(name = 'GC_467',
                  value = '-(cw*ee*FM5*complex(0,1)*vev)/(4.*sw)',
                  order = {'M5':1})

GC_468 = Coupling(name = 'GC_468',
                  value = '(cw*ee**2*FM5*complex(0,1)*vev)/(4.*sw)',
                  order = {'M5':1,'QED':1})

GC_469 = Coupling(name = 'GC_469',
                  value = '-(cw*ee**2*FM5*complex(0,1)*vev)/(2.*sw)',
                  order = {'M5':1,'QED':1})

GC_470 = Coupling(name = 'GC_470',
                  value = '-(cw*ee**3*FM5*complex(0,1)*vev)/(2.*sw)',
                  order = {'M5':1,'QED':2})

GC_471 = Coupling(name = 'GC_471',
                  value = '-(cw*ee*FM7*complex(0,1)*vev)/(8.*sw)',
                  order = {'M7':1})

GC_472 = Coupling(name = 'GC_472',
                  value = '(cw*ee**2*FM7*complex(0,1)*vev)/(8.*sw)',
                  order = {'M7':1,'QED':1})

GC_473 = Coupling(name = 'GC_473',
                  value = '(ee**3*FM7*complex(0,1)*vev)/(8.*cw*sw)',
                  order = {'M7':1,'QED':2})

GC_474 = Coupling(name = 'GC_474',
                  value = '(cw*ee**3*FM7*complex(0,1)*vev)/(2.*sw)',
                  order = {'M7':1,'QED':2})

GC_475 = Coupling(name = 'GC_475',
                  value = '-(ee**4*FM7*complex(0,1)*vev)/(2.*cw*sw)',
                  order = {'M7':1,'QED':3})

GC_476 = Coupling(name = 'GC_476',
                  value = '(ee**2*FM4*complex(0,1)*sw*vev)/(2.*cw)',
                  order = {'M4':1,'QED':1})

GC_477 = Coupling(name = 'GC_477',
                  value = '(ee**3*FM4*complex(0,1)*sw*vev)/(2.*cw)',
                  order = {'M4':1,'QED':2})

GC_478 = Coupling(name = 'GC_478',
                  value = '(ee**2*FM5*complex(0,1)*sw*vev)/(4.*cw)',
                  order = {'M5':1,'QED':1})

GC_479 = Coupling(name = 'GC_479',
                  value = '-(ee**3*FM5*complex(0,1)*sw*vev)/(4.*cw)',
                  order = {'M5':1,'QED':2})

GC_480 = Coupling(name = 'GC_480',
                  value = '-(ee*FM7*complex(0,1)*sw*vev)/(8.*cw)',
                  order = {'M7':1})

GC_481 = Coupling(name = 'GC_481',
                  value = '(ee**2*FM7*complex(0,1)*sw*vev)/(8.*cw)',
                  order = {'M7':1,'QED':1})

GC_482 = Coupling(name = 'GC_482',
                  value = '(ee**3*FM7*complex(0,1)*sw*vev)/(8.*cw)',
                  order = {'M7':1,'QED':2})

GC_483 = Coupling(name = 'GC_483',
                  value = '-(ee**3*FM4*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                  order = {'M4':1,'QED':2})

GC_484 = Coupling(name = 'GC_484',
                  value = '(ee**3*FM5*complex(0,1)*sw**2*vev)/(4.*cw**2)',
                  order = {'M5':1,'QED':2})

GC_485 = Coupling(name = 'GC_485',
                  value = '-(ee**2*FM7*complex(0,1)*sw**2*vev)/(8.*cw**2)',
                  order = {'M7':1,'QED':1})

GC_486 = Coupling(name = 'GC_486',
                  value = '-(ee**3*FM7*complex(0,1)*sw**2*vev)/(8.*cw**2)',
                  order = {'M7':1,'QED':2})

GC_487 = Coupling(name = 'GC_487',
                  value = '(ee**2*FM0*complex(0,1)*vev**2)/2.',
                  order = {'M0':1})

GC_488 = Coupling(name = 'GC_488',
                  value = '(ee**2*FM1*complex(0,1)*vev**2)/8.',
                  order = {'M1':1})

GC_489 = Coupling(name = 'GC_489',
                  value = 'ee**2*FM2*complex(0,1)*vev**2',
                  order = {'M2':1})

GC_490 = Coupling(name = 'GC_490',
                  value = '-(ee**2*FM3*complex(0,1)*vev**2)/4.',
                  order = {'M3':1})

GC_491 = Coupling(name = 'GC_491',
                  value = '-(ee**2*FM4*complex(0,1)*vev**2)/4.',
                  order = {'M4':1})

GC_492 = Coupling(name = 'GC_492',
                  value = '-(ee**3*FM4*complex(0,1)*vev**2)/4.',
                  order = {'M4':1,'QED':1})

GC_493 = Coupling(name = 'GC_493',
                  value = '(ee**2*FM5*complex(0,1)*vev**2)/8.',
                  order = {'M5':1})

GC_494 = Coupling(name = 'GC_494',
                  value = '(ee**3*FM5*complex(0,1)*vev**2)/4.',
                  order = {'M5':1,'QED':1})

GC_495 = Coupling(name = 'GC_495',
                  value = '-(ee**2*FM7*complex(0,1)*vev**2)/16.',
                  order = {'M7':1})

GC_496 = Coupling(name = 'GC_496',
                  value = '-(ee**2*FM7*complex(0,1)*vev**2)/8.',
                  order = {'M7':1})

GC_497 = Coupling(name = 'GC_497',
                  value = '-(ee**3*FM7*complex(0,1)*vev**2)/8.',
                  order = {'M7':1,'QED':1})

GC_498 = Coupling(name = 'GC_498',
                  value = '-(ee**4*FM7*complex(0,1)*vev**2)/(8.*cw**2)',
                  order = {'M7':1,'QED':2})

GC_499 = Coupling(name = 'GC_499',
                  value = '(3*ee**4*FM0*complex(0,1)*vev**2)/(2.*sw**4)',
                  order = {'M0':1,'QED':2})

GC_500 = Coupling(name = 'GC_500',
                  value = '-(cw**2*ee**4*FM0*complex(0,1)*vev**2)/(2.*sw**4)',
                  order = {'M0':1,'QED':2})

GC_501 = Coupling(name = 'GC_501',
                  value = '(-3*ee**4*FM1*complex(0,1)*vev**2)/(4.*sw**4)',
                  order = {'M1':1,'QED':2})

GC_502 = Coupling(name = 'GC_502',
                  value = '(3*cw**2*ee**4*FM1*complex(0,1)*vev**2)/(4.*sw**4)',
                  order = {'M1':1,'QED':2})

GC_503 = Coupling(name = 'GC_503',
                  value = '(3*ee**4*FM7*complex(0,1)*vev**2)/(8.*sw**4)',
                  order = {'M7':1,'QED':2})

GC_504 = Coupling(name = 'GC_504',
                  value = '(-9*cw**2*ee**4*FM7*complex(0,1)*vev**2)/(8.*sw**4)',
                  order = {'M7':1,'QED':2})

GC_505 = Coupling(name = 'GC_505',
                  value = '(3*ee**4*complex(0,1)*FS0*vev**2)/sw**4',
                  order = {'QED':2,'S0':1})

GC_506 = Coupling(name = 'GC_506',
                  value = '(3*ee**4*complex(0,1)*FS1*vev**2)/(2.*sw**4)',
                  order = {'QED':2,'S1':1})

GC_507 = Coupling(name = 'GC_507',
                  value = '(3*ee**4*complex(0,1)*FS2*vev**2)/(2.*sw**4)',
                  order = {'QED':2,'S2':1})

GC_508 = Coupling(name = 'GC_508',
                  value = '-(cw*ee**3*FM0*complex(0,1)*vev**2)/(2.*sw**3)',
                  order = {'M0':1,'QED':1})

GC_509 = Coupling(name = 'GC_509',
                  value = '(2*cw*ee**4*FM0*complex(0,1)*vev**2)/sw**3',
                  order = {'M0':1,'QED':2})

GC_510 = Coupling(name = 'GC_510',
                  value = '(cw*ee**3*FM1*complex(0,1)*vev**2)/(8.*sw**3)',
                  order = {'M1':1,'QED':1})

GC_511 = Coupling(name = 'GC_511',
                  value = '-(cw*ee**4*FM1*complex(0,1)*vev**2)/(2.*sw**3)',
                  order = {'M1':1,'QED':2})

GC_512 = Coupling(name = 'GC_512',
                  value = '-(cw*ee**3*FM4*complex(0,1)*vev**2)/(4.*sw**3)',
                  order = {'M4':1,'QED':1})

GC_513 = Coupling(name = 'GC_513',
                  value = '(cw**3*ee**3*FM4*complex(0,1)*vev**2)/(4.*sw**3)',
                  order = {'M4':1,'QED':1})

GC_514 = Coupling(name = 'GC_514',
                  value = '-(cw*ee**3*FM5*complex(0,1)*vev**2)/(4.*sw**3)',
                  order = {'M5':1,'QED':1})

GC_515 = Coupling(name = 'GC_515',
                  value = '-(cw**3*ee**3*FM5*complex(0,1)*vev**2)/(8.*sw**3)',
                  order = {'M5':1,'QED':1})

GC_516 = Coupling(name = 'GC_516',
                  value = '(cw*ee**3*FM7*complex(0,1)*vev**2)/(16.*sw**3)',
                  order = {'M7':1,'QED':1})

GC_517 = Coupling(name = 'GC_517',
                  value = '(3*cw**3*ee**3*FM7*complex(0,1)*vev**2)/(16.*sw**3)',
                  order = {'M7':1,'QED':1})

GC_518 = Coupling(name = 'GC_518',
                  value = '-(cw*ee**4*FM7*complex(0,1)*vev**2)/(4.*sw**3)',
                  order = {'M7':1,'QED':2})

GC_519 = Coupling(name = 'GC_519',
                  value = '(ee**2*FM0*complex(0,1)*vev**2)/(2.*sw**2)',
                  order = {'M0':1})

GC_520 = Coupling(name = 'GC_520',
                  value = '(cw**2*ee**2*FM0*complex(0,1)*vev**2)/(2.*sw**2)',
                  order = {'M0':1})

GC_521 = Coupling(name = 'GC_521',
                  value = '-(ee**3*FM0*complex(0,1)*vev**2)/(2.*sw**2)',
                  order = {'M0':1,'QED':1})

GC_522 = Coupling(name = 'GC_522',
                  value = '-(ee**4*FM0*complex(0,1)*vev**2)/(2.*sw**2)',
                  order = {'M0':1,'QED':2})

GC_523 = Coupling(name = 'GC_523',
                  value = '-(ee**2*FM1*complex(0,1)*vev**2)/(8.*sw**2)',
                  order = {'M1':1})

GC_524 = Coupling(name = 'GC_524',
                  value = '(cw**2*ee**2*FM1*complex(0,1)*vev**2)/(8.*sw**2)',
                  order = {'M1':1})

GC_525 = Coupling(name = 'GC_525',
                  value = '-(ee**3*FM1*complex(0,1)*vev**2)/(8.*sw**2)',
                  order = {'M1':1,'QED':1})

GC_526 = Coupling(name = 'GC_526',
                  value = '(ee**4*FM1*complex(0,1)*vev**2)/(2.*sw**2)',
                  order = {'M1':1,'QED':2})

GC_527 = Coupling(name = 'GC_527',
                  value = '(cw**2*ee**2*FM2*complex(0,1)*vev**2)/sw**2',
                  order = {'M2':1})

GC_528 = Coupling(name = 'GC_528',
                  value = '(cw**2*ee**2*FM3*complex(0,1)*vev**2)/(4.*sw**2)',
                  order = {'M3':1})

GC_529 = Coupling(name = 'GC_529',
                  value = '(cw**2*ee**2*FM4*complex(0,1)*vev**2)/(4.*sw**2)',
                  order = {'M4':1})

GC_530 = Coupling(name = 'GC_530',
                  value = '(ee**3*FM4*complex(0,1)*vev**2)/(4.*sw**2)',
                  order = {'M4':1,'QED':1})

GC_531 = Coupling(name = 'GC_531',
                  value = '-(cw**2*ee**3*FM4*complex(0,1)*vev**2)/(4.*sw**2)',
                  order = {'M4':1,'QED':1})

GC_532 = Coupling(name = 'GC_532',
                  value = '(cw**2*ee**2*FM5*complex(0,1)*vev**2)/(8.*sw**2)',
                  order = {'M5':1})

GC_533 = Coupling(name = 'GC_533',
                  value = '(ee**3*FM5*complex(0,1)*vev**2)/(4.*sw**2)',
                  order = {'M5':1,'QED':1})

GC_534 = Coupling(name = 'GC_534',
                  value = '(cw**2*ee**3*FM5*complex(0,1)*vev**2)/(8.*sw**2)',
                  order = {'M5':1,'QED':1})

GC_535 = Coupling(name = 'GC_535',
                  value = '(ee**2*FM7*complex(0,1)*vev**2)/(8.*sw**2)',
                  order = {'M7':1})

GC_536 = Coupling(name = 'GC_536',
                  value = '-(cw**2*ee**2*FM7*complex(0,1)*vev**2)/(16.*sw**2)',
                  order = {'M7':1})

GC_537 = Coupling(name = 'GC_537',
                  value = '(ee**3*FM7*complex(0,1)*vev**2)/(8.*sw**2)',
                  order = {'M7':1,'QED':1})

GC_538 = Coupling(name = 'GC_538',
                  value = '-(cw**2*ee**3*FM7*complex(0,1)*vev**2)/(16.*sw**2)',
                  order = {'M7':1,'QED':1})

GC_539 = Coupling(name = 'GC_539',
                  value = '-(ee**4*FM7*complex(0,1)*vev**2)/(2.*sw**2)',
                  order = {'M7':1,'QED':2})

GC_540 = Coupling(name = 'GC_540',
                  value = '(-3*ee**4*FM7*complex(0,1)*vev**2)/(4.*sw**2)',
                  order = {'M7':1,'QED':2})

GC_541 = Coupling(name = 'GC_541',
                  value = '-(ee**2*complex(0,1)*FS0*vev**2)/(4.*sw**2)',
                  order = {'S0':1})

GC_542 = Coupling(name = 'GC_542',
                  value = '-(ee**2*complex(0,1)*FS1*vev**2)/(2.*sw**2)',
                  order = {'S1':1})

GC_543 = Coupling(name = 'GC_543',
                  value = '-(ee**2*complex(0,1)*FS2*vev**2)/(4.*sw**2)',
                  order = {'S2':1})

GC_544 = Coupling(name = 'GC_544',
                  value = '(cw*ee**2*FM0*complex(0,1)*vev**2)/(2.*sw)',
                  order = {'M0':1})

GC_545 = Coupling(name = 'GC_545',
                  value = '-(cw*ee**2*FM1*complex(0,1)*vev**2)/(8.*sw)',
                  order = {'M1':1})

GC_546 = Coupling(name = 'GC_546',
                  value = '-((cw*ee**2*FM2*complex(0,1)*vev**2)/sw)',
                  order = {'M2':1})

GC_547 = Coupling(name = 'GC_547',
                  value = '(cw*ee**2*FM3*complex(0,1)*vev**2)/(4.*sw)',
                  order = {'M3':1})

GC_548 = Coupling(name = 'GC_548',
                  value = '-(cw*ee**2*FM4*complex(0,1)*vev**2)/(2.*sw)',
                  order = {'M4':1})

GC_549 = Coupling(name = 'GC_549',
                  value = '(cw*ee**2*FM4*complex(0,1)*vev**2)/(2.*sw)',
                  order = {'M4':1})

GC_550 = Coupling(name = 'GC_550',
                  value = '(cw*ee**3*FM4*complex(0,1)*vev**2)/(4.*sw)',
                  order = {'M4':1,'QED':1})

GC_551 = Coupling(name = 'GC_551',
                  value = '(cw*ee**2*FM5*complex(0,1)*vev**2)/(8.*sw)',
                  order = {'M5':1})

GC_552 = Coupling(name = 'GC_552',
                  value = '-(cw*ee**2*FM5*complex(0,1)*vev**2)/(4.*sw)',
                  order = {'M5':1})

GC_553 = Coupling(name = 'GC_553',
                  value = '-(cw*ee**3*FM5*complex(0,1)*vev**2)/(4.*sw)',
                  order = {'M5':1,'QED':1})

GC_554 = Coupling(name = 'GC_554',
                  value = '(cw*ee**2*FM7*complex(0,1)*vev**2)/(16.*sw)',
                  order = {'M7':1})

GC_555 = Coupling(name = 'GC_555',
                  value = '(ee**3*FM7*complex(0,1)*vev**2)/(16.*cw*sw)',
                  order = {'M7':1,'QED':1})

GC_556 = Coupling(name = 'GC_556',
                  value = '(cw*ee**3*FM7*complex(0,1)*vev**2)/(4.*sw)',
                  order = {'M7':1,'QED':1})

GC_557 = Coupling(name = 'GC_557',
                  value = '-(ee**4*FM7*complex(0,1)*vev**2)/(4.*cw*sw)',
                  order = {'M7':1,'QED':2})

GC_558 = Coupling(name = 'GC_558',
                  value = '(ee**2*FM4*complex(0,1)*sw*vev**2)/(4.*cw)',
                  order = {'M4':1})

GC_559 = Coupling(name = 'GC_559',
                  value = '(ee**3*FM4*complex(0,1)*sw*vev**2)/(4.*cw)',
                  order = {'M4':1,'QED':1})

GC_560 = Coupling(name = 'GC_560',
                  value = '(ee**2*FM5*complex(0,1)*sw*vev**2)/(8.*cw)',
                  order = {'M5':1})

GC_561 = Coupling(name = 'GC_561',
                  value = '-(ee**3*FM5*complex(0,1)*sw*vev**2)/(8.*cw)',
                  order = {'M5':1,'QED':1})

GC_562 = Coupling(name = 'GC_562',
                  value = '(ee**2*FM7*complex(0,1)*sw*vev**2)/(16.*cw)',
                  order = {'M7':1})

GC_563 = Coupling(name = 'GC_563',
                  value = '(ee**3*FM7*complex(0,1)*sw*vev**2)/(16.*cw)',
                  order = {'M7':1,'QED':1})

GC_564 = Coupling(name = 'GC_564',
                  value = '-(ee**3*FM4*complex(0,1)*sw**2*vev**2)/(4.*cw**2)',
                  order = {'M4':1,'QED':1})

GC_565 = Coupling(name = 'GC_565',
                  value = '(ee**3*FM5*complex(0,1)*sw**2*vev**2)/(8.*cw**2)',
                  order = {'M5':1,'QED':1})

GC_566 = Coupling(name = 'GC_566',
                  value = '-(ee**2*FM7*complex(0,1)*sw**2*vev**2)/(16.*cw**2)',
                  order = {'M7':1})

GC_567 = Coupling(name = 'GC_567',
                  value = '-(ee**3*FM7*complex(0,1)*sw**2*vev**2)/(16.*cw**2)',
                  order = {'M7':1,'QED':1})

GC_568 = Coupling(name = 'GC_568',
                  value = '(ee**4*complex(0,1)*FS0*vev**3)/sw**4',
                  order = {'QED':1,'S0':1})

GC_569 = Coupling(name = 'GC_569',
                  value = '(ee**4*complex(0,1)*FS1*vev**3)/(2.*sw**4)',
                  order = {'QED':1,'S1':1})

GC_570 = Coupling(name = 'GC_570',
                  value = '(ee**4*complex(0,1)*FS2*vev**3)/(2.*sw**4)',
                  order = {'QED':1,'S2':1})

GC_571 = Coupling(name = 'GC_571',
                  value = '(ee**4*complex(0,1)*FS0*vev**4)/(4.*sw**4)',
                  order = {'S0':1})

GC_572 = Coupling(name = 'GC_572',
                  value = '(ee**4*complex(0,1)*FS1*vev**4)/(8.*sw**4)',
                  order = {'S1':1})

GC_573 = Coupling(name = 'GC_573',
                  value = '(ee**4*complex(0,1)*FS2*vev**4)/(8.*sw**4)',
                  order = {'S2':1})

GC_574 = Coupling(name = 'GC_574',
                  value = '(ee**4*FM0*complex(0,1)*vev)/cw**2 + (2*ee**4*FM0*complex(0,1)*vev)/sw**2',
                  order = {'M0':1,'QED':3})

GC_575 = Coupling(name = 'GC_575',
                  value = '-(ee**4*FM0*complex(0,1)*vev) - (cw**4*ee**4*FM0*complex(0,1)*vev)/sw**4 - (2*cw**2*ee**4*FM0*complex(0,1)*vev)/sw**2',
                  order = {'M0':1,'QED':3})

GC_576 = Coupling(name = 'GC_576',
                  value = '(ee**4*FM1*complex(0,1)*vev)/(2.*cw**2) + (ee**4*FM1*complex(0,1)*vev)/sw**2',
                  order = {'M1':1,'QED':3})

GC_577 = Coupling(name = 'GC_577',
                  value = '(ee**4*FM1*complex(0,1)*vev)/2. + (cw**4*ee**4*FM1*complex(0,1)*vev)/(2.*sw**4) + (cw**2*ee**4*FM1*complex(0,1)*vev)/sw**2',
                  order = {'M1':1,'QED':3})

GC_578 = Coupling(name = 'GC_578',
                  value = '-(ee**3*FM4*complex(0,1)*vev)/2. - (cw**2*ee**3*FM4*complex(0,1)*vev)/(2.*sw**2)',
                  order = {'M4':1,'QED':2})

GC_579 = Coupling(name = 'GC_579',
                  value = '(ee**3*FM5*complex(0,1)*vev)/4. + (cw**2*ee**3*FM5*complex(0,1)*vev)/(4.*sw**2)',
                  order = {'M5':1,'QED':2})

GC_580 = Coupling(name = 'GC_580',
                  value = '-(ee**4*FM7*complex(0,1)*vev)/4. - (cw**4*ee**4*FM7*complex(0,1)*vev)/(4.*sw**4) - (cw**2*ee**4*FM7*complex(0,1)*vev)/(2.*sw**2)',
                  order = {'M7':1,'QED':3})

GC_581 = Coupling(name = 'GC_581',
                  value = '(3*ee**4*complex(0,1)*FS0*vev)/(2.*cw**2) + (3*cw**2*ee**4*complex(0,1)*FS0*vev)/(2.*sw**4) + (3*ee**4*complex(0,1)*FS0*vev)/sw**2',
                  order = {'QED':3,'S0':1})

GC_582 = Coupling(name = 'GC_582',
                  value = '(3*ee**4*complex(0,1)*FS1*vev)/cw**2 + (3*cw**2*ee**4*complex(0,1)*FS1*vev)/sw**4 + (6*ee**4*complex(0,1)*FS1*vev)/sw**2',
                  order = {'QED':3,'S1':1})

GC_583 = Coupling(name = 'GC_583',
                  value = '(3*ee**4*complex(0,1)*FS2*vev)/(2.*cw**2) + (3*cw**2*ee**4*complex(0,1)*FS2*vev)/(2.*sw**4) + (3*ee**4*complex(0,1)*FS2*vev)/sw**2',
                  order = {'QED':3,'S2':1})

GC_584 = Coupling(name = 'GC_584',
                  value = '(-3*cw*ee**3*complex(0,1)*FS0*vev)/(4.*sw**3) - (3*ee**3*complex(0,1)*FS0*vev)/(4.*cw*sw)',
                  order = {'QED':2,'S0':1})

GC_585 = Coupling(name = 'GC_585',
                  value = '(3*cw*ee**3*complex(0,1)*FS2*vev)/(4.*sw**3) + (3*ee**3*complex(0,1)*FS2*vev)/(4.*cw*sw)',
                  order = {'QED':2,'S2':1})

GC_586 = Coupling(name = 'GC_586',
                  value = '-((cw**3*ee**3*FM0*complex(0,1)*vev)/sw**3) - (2*cw*ee**3*FM0*complex(0,1)*vev)/sw - (ee**3*FM0*complex(0,1)*sw*vev)/cw',
                  order = {'M0':1,'QED':2})

GC_587 = Coupling(name = 'GC_587',
                  value = '(2*cw**3*ee**4*FM0*complex(0,1)*vev)/sw**3 + (4*cw*ee**4*FM0*complex(0,1)*vev)/sw + (2*ee**4*FM0*complex(0,1)*sw*vev)/cw',
                  order = {'M0':1,'QED':3})

GC_588 = Coupling(name = 'GC_588',
                  value = '-(cw**3*ee**3*FM1*complex(0,1)*vev)/(4.*sw**3) - (cw*ee**3*FM1*complex(0,1)*vev)/(2.*sw) - (ee**3*FM1*complex(0,1)*sw*vev)/(4.*cw)',
                  order = {'M1':1,'QED':2})

GC_589 = Coupling(name = 'GC_589',
                  value = '-((cw**3*ee**4*FM1*complex(0,1)*vev)/sw**3) - (2*cw*ee**4*FM1*complex(0,1)*vev)/sw - (ee**4*FM1*complex(0,1)*sw*vev)/cw',
                  order = {'M1':1,'QED':3})

GC_590 = Coupling(name = 'GC_590',
                  value = '(cw*ee**3*FM7*complex(0,1)*vev)/(8.*sw) + (ee**3*FM7*complex(0,1)*sw*vev)/(8.*cw)',
                  order = {'M7':1,'QED':2})

GC_591 = Coupling(name = 'GC_591',
                  value = '(cw**3*ee**4*FM7*complex(0,1)*vev)/(2.*sw**3) + (cw*ee**4*FM7*complex(0,1)*vev)/sw + (ee**4*FM7*complex(0,1)*sw*vev)/(2.*cw)',
                  order = {'M7':1,'QED':3})

GC_592 = Coupling(name = 'GC_592',
                  value = 'ee**2*complex(0,1)*vev + (cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                  order = {'QED':1})

GC_593 = Coupling(name = 'GC_593',
                  value = '2*cw**2*ee**2*FM0*complex(0,1)*vev + (cw**4*ee**2*FM0*complex(0,1)*vev)/sw**2 + ee**2*FM0*complex(0,1)*sw**2*vev',
                  order = {'M0':1,'QED':1})

GC_594 = Coupling(name = 'GC_594',
                  value = '2*ee**2*FM0*complex(0,1)*vev + (ee**2*FM0*complex(0,1)*sw**2*vev)/cw**2',
                  order = {'M0':1,'QED':1})

GC_595 = Coupling(name = 'GC_595',
                  value = '-2*ee**3*FM0*complex(0,1)*vev - (cw**2*ee**3*FM0*complex(0,1)*vev)/sw**2 - (ee**3*FM0*complex(0,1)*sw**2*vev)/cw**2',
                  order = {'M0':1,'QED':2})

GC_596 = Coupling(name = 'GC_596',
                  value = '-2*ee**4*FM0*complex(0,1)*vev - (cw**2*ee**4*FM0*complex(0,1)*vev)/sw**2 - (ee**4*FM0*complex(0,1)*sw**2*vev)/cw**2',
                  order = {'M0':1,'QED':3})

GC_597 = Coupling(name = 'GC_597',
                  value = '(cw**2*ee**2*FM1*complex(0,1)*vev)/2. + (cw**4*ee**2*FM1*complex(0,1)*vev)/(4.*sw**2) + (ee**2*FM1*complex(0,1)*sw**2*vev)/4.',
                  order = {'M1':1,'QED':1})

GC_598 = Coupling(name = 'GC_598',
                  value = '(ee**2*FM1*complex(0,1)*vev)/2. + (ee**2*FM1*complex(0,1)*sw**2*vev)/(4.*cw**2)',
                  order = {'M1':1,'QED':1})

GC_599 = Coupling(name = 'GC_599',
                  value = '(ee**3*FM1*complex(0,1)*vev)/2. + (cw**2*ee**3*FM1*complex(0,1)*vev)/(4.*sw**2) + (ee**3*FM1*complex(0,1)*sw**2*vev)/(4.*cw**2)',
                  order = {'M1':1,'QED':2})

GC_600 = Coupling(name = 'GC_600',
                  value = '-(ee**4*FM1*complex(0,1)*vev) - (cw**2*ee**4*FM1*complex(0,1)*vev)/(2.*sw**2) - (ee**4*FM1*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                  order = {'M1':1,'QED':3})

GC_601 = Coupling(name = 'GC_601',
                  value = '4*cw**2*ee**2*FM2*complex(0,1)*vev + (2*cw**4*ee**2*FM2*complex(0,1)*vev)/sw**2 + 2*ee**2*FM2*complex(0,1)*sw**2*vev',
                  order = {'M2':1,'QED':1})

GC_602 = Coupling(name = 'GC_602',
                  value = 'cw**2*ee**2*FM3*complex(0,1)*vev + (cw**4*ee**2*FM3*complex(0,1)*vev)/(2.*sw**2) + (ee**2*FM3*complex(0,1)*sw**2*vev)/2.',
                  order = {'M3':1,'QED':1})

GC_603 = Coupling(name = 'GC_603',
                  value = '-(cw**2*ee**2*FM7*complex(0,1)*vev)/4. - (cw**4*ee**2*FM7*complex(0,1)*vev)/(8.*sw**2) - (ee**2*FM7*complex(0,1)*sw**2*vev)/8.',
                  order = {'M7':1,'QED':1})

GC_604 = Coupling(name = 'GC_604',
                  value = '(ee**4*FM7*complex(0,1)*vev)/2. + (cw**2*ee**4*FM7*complex(0,1)*vev)/(4.*sw**2) + (ee**4*FM7*complex(0,1)*sw**2*vev)/(4.*cw**2)',
                  order = {'M7':1,'QED':3})

GC_605 = Coupling(name = 'GC_605',
                  value = '-2*ee**2*complex(0,1)*FS0*vev - (cw**2*ee**2*complex(0,1)*FS0*vev)/sw**2 - (ee**2*complex(0,1)*FS0*sw**2*vev)/cw**2',
                  order = {'QED':1,'S0':1})

GC_606 = Coupling(name = 'GC_606',
                  value = '-2*ee**2*complex(0,1)*FS1*vev - (cw**2*ee**2*complex(0,1)*FS1*vev)/sw**2 - (ee**2*complex(0,1)*FS1*sw**2*vev)/cw**2',
                  order = {'QED':1,'S1':1})

GC_607 = Coupling(name = 'GC_607',
                  value = '-2*ee**2*complex(0,1)*FS2*vev - (cw**2*ee**2*complex(0,1)*FS2*vev)/sw**2 - (ee**2*complex(0,1)*FS2*sw**2*vev)/cw**2',
                  order = {'QED':1,'S2':1})

GC_608 = Coupling(name = 'GC_608',
                  value = '(cw**3*ee**2*FM0*complex(0,1)*vev)/sw + 2*cw*ee**2*FM0*complex(0,1)*sw*vev + (ee**2*FM0*complex(0,1)*sw**3*vev)/cw',
                  order = {'M0':1,'QED':1})

GC_609 = Coupling(name = 'GC_609',
                  value = '(cw**3*ee**2*FM1*complex(0,1)*vev)/(4.*sw) + (cw*ee**2*FM1*complex(0,1)*sw*vev)/2. + (ee**2*FM1*complex(0,1)*sw**3*vev)/(4.*cw)',
                  order = {'M1':1,'QED':1})

GC_610 = Coupling(name = 'GC_610',
                  value = '(-2*cw**3*ee**2*FM2*complex(0,1)*vev)/sw - 4*cw*ee**2*FM2*complex(0,1)*sw*vev - (2*ee**2*FM2*complex(0,1)*sw**3*vev)/cw',
                  order = {'M2':1,'QED':1})

GC_611 = Coupling(name = 'GC_611',
                  value = '-(cw**3*ee**2*FM3*complex(0,1)*vev)/(2.*sw) - cw*ee**2*FM3*complex(0,1)*sw*vev - (ee**2*FM3*complex(0,1)*sw**3*vev)/(2.*cw)',
                  order = {'M3':1,'QED':1})

GC_612 = Coupling(name = 'GC_612',
                  value = '-((cw**3*ee**2*FM4*complex(0,1)*vev)/sw) - 2*cw*ee**2*FM4*complex(0,1)*sw*vev - (ee**2*FM4*complex(0,1)*sw**3*vev)/cw',
                  order = {'M4':1,'QED':1})

GC_613 = Coupling(name = 'GC_613',
                  value = '(cw**3*ee**2*FM4*complex(0,1)*vev)/sw + 2*cw*ee**2*FM4*complex(0,1)*sw*vev + (ee**2*FM4*complex(0,1)*sw**3*vev)/cw',
                  order = {'M4':1,'QED':1})

GC_614 = Coupling(name = 'GC_614',
                  value = '-(cw**3*ee**2*FM5*complex(0,1)*vev)/(2.*sw) - cw*ee**2*FM5*complex(0,1)*sw*vev - (ee**2*FM5*complex(0,1)*sw**3*vev)/(2.*cw)',
                  order = {'M5':1,'QED':1})

GC_615 = Coupling(name = 'GC_615',
                  value = '(cw**3*ee**2*FM5*complex(0,1)*vev)/(2.*sw) + cw*ee**2*FM5*complex(0,1)*sw*vev + (ee**2*FM5*complex(0,1)*sw**3*vev)/(2.*cw)',
                  order = {'M5':1,'QED':1})

GC_616 = Coupling(name = 'GC_616',
                  value = '-(cw**3*ee**2*FM7*complex(0,1)*vev)/(8.*sw) - (cw*ee**2*FM7*complex(0,1)*sw*vev)/4. - (ee**2*FM7*complex(0,1)*sw**3*vev)/(8.*cw)',
                  order = {'M7':1,'QED':1})

GC_617 = Coupling(name = 'GC_617',
                  value = 'cw**2*ee**2*FM0*complex(0,1)*vev + 2*ee**2*FM0*complex(0,1)*sw**2*vev + (ee**2*FM0*complex(0,1)*sw**4*vev)/cw**2',
                  order = {'M0':1,'QED':1})

GC_618 = Coupling(name = 'GC_618',
                  value = '(cw**2*ee**2*FM1*complex(0,1)*vev)/4. + (ee**2*FM1*complex(0,1)*sw**2*vev)/2. + (ee**2*FM1*complex(0,1)*sw**4*vev)/(4.*cw**2)',
                  order = {'M1':1,'QED':1})

GC_619 = Coupling(name = 'GC_619',
                  value = '2*cw**2*ee**2*FM2*complex(0,1)*vev + 4*ee**2*FM2*complex(0,1)*sw**2*vev + (2*ee**2*FM2*complex(0,1)*sw**4*vev)/cw**2',
                  order = {'M2':1,'QED':1})

GC_620 = Coupling(name = 'GC_620',
                  value = '(cw**2*ee**2*FM3*complex(0,1)*vev)/2. + ee**2*FM3*complex(0,1)*sw**2*vev + (ee**2*FM3*complex(0,1)*sw**4*vev)/(2.*cw**2)',
                  order = {'M3':1,'QED':1})

GC_621 = Coupling(name = 'GC_621',
                  value = '-(cw**2*ee**2*FM4*complex(0,1)*vev)/2. - (cw**4*ee**2*FM4*complex(0,1)*vev)/(2.*sw**2) + (ee**2*FM4*complex(0,1)*sw**2*vev)/2. + (ee**2*FM4*complex(0,1)*sw**4*vev)/(2.*cw**2)',
                  order = {'M4':1,'QED':1})

GC_622 = Coupling(name = 'GC_622',
                  value = '(cw**2*ee**2*FM5*complex(0,1)*vev)/4. + (cw**4*ee**2*FM5*complex(0,1)*vev)/(4.*sw**2) - (ee**2*FM5*complex(0,1)*sw**2*vev)/4. - (ee**2*FM5*complex(0,1)*sw**4*vev)/(4.*cw**2)',
                  order = {'M5':1,'QED':1})

GC_623 = Coupling(name = 'GC_623',
                  value = '-(cw**2*ee**2*FM7*complex(0,1)*vev)/8. - (ee**2*FM7*complex(0,1)*sw**2*vev)/4. - (ee**2*FM7*complex(0,1)*sw**4*vev)/(8.*cw**2)',
                  order = {'M7':1,'QED':1})

GC_624 = Coupling(name = 'GC_624',
                  value = '18*ee**4*complex(0,1)*FS0*vev + (3*cw**4*ee**4*complex(0,1)*FS0*vev)/sw**4 + (12*cw**2*ee**4*complex(0,1)*FS0*vev)/sw**2 + (12*ee**4*complex(0,1)*FS0*sw**2*vev)/cw**2 + (3*ee**4*complex(0,1)*FS0*sw**4*vev)/cw**4',
                  order = {'QED':3,'S0':1})

GC_625 = Coupling(name = 'GC_625',
                  value = '18*ee**4*complex(0,1)*FS1*vev + (3*cw**4*ee**4*complex(0,1)*FS1*vev)/sw**4 + (12*cw**2*ee**4*complex(0,1)*FS1*vev)/sw**2 + (12*ee**4*complex(0,1)*FS1*sw**2*vev)/cw**2 + (3*ee**4*complex(0,1)*FS1*sw**4*vev)/cw**4',
                  order = {'QED':3,'S1':1})

GC_626 = Coupling(name = 'GC_626',
                  value = '18*ee**4*complex(0,1)*FS2*vev + (3*cw**4*ee**4*complex(0,1)*FS2*vev)/sw**4 + (12*cw**2*ee**4*complex(0,1)*FS2*vev)/sw**2 + (12*ee**4*complex(0,1)*FS2*sw**2*vev)/cw**2 + (3*ee**4*complex(0,1)*FS2*sw**4*vev)/cw**4',
                  order = {'QED':3,'S2':1})

GC_627 = Coupling(name = 'GC_627',
                  value = '(ee**4*FM0*complex(0,1)*vev**2)/(2.*cw**2) + (ee**4*FM0*complex(0,1)*vev**2)/sw**2',
                  order = {'M0':1,'QED':2})

GC_628 = Coupling(name = 'GC_628',
                  value = '-(ee**4*FM0*complex(0,1)*vev**2)/2. - (cw**4*ee**4*FM0*complex(0,1)*vev**2)/(2.*sw**4) - (cw**2*ee**4*FM0*complex(0,1)*vev**2)/sw**2',
                  order = {'M0':1,'QED':2})

GC_629 = Coupling(name = 'GC_629',
                  value = '(ee**4*FM1*complex(0,1)*vev**2)/(4.*cw**2) + (ee**4*FM1*complex(0,1)*vev**2)/(2.*sw**2)',
                  order = {'M1':1,'QED':2})

GC_630 = Coupling(name = 'GC_630',
                  value = '(ee**4*FM1*complex(0,1)*vev**2)/4. + (cw**4*ee**4*FM1*complex(0,1)*vev**2)/(4.*sw**4) + (cw**2*ee**4*FM1*complex(0,1)*vev**2)/(2.*sw**2)',
                  order = {'M1':1,'QED':2})

GC_631 = Coupling(name = 'GC_631',
                  value = '-(ee**3*FM4*complex(0,1)*vev**2)/4. - (cw**2*ee**3*FM4*complex(0,1)*vev**2)/(4.*sw**2)',
                  order = {'M4':1,'QED':1})

GC_632 = Coupling(name = 'GC_632',
                  value = '(ee**3*FM5*complex(0,1)*vev**2)/8. + (cw**2*ee**3*FM5*complex(0,1)*vev**2)/(8.*sw**2)',
                  order = {'M5':1,'QED':1})

GC_633 = Coupling(name = 'GC_633',
                  value = '-(ee**4*FM7*complex(0,1)*vev**2)/8. - (cw**4*ee**4*FM7*complex(0,1)*vev**2)/(8.*sw**4) - (cw**2*ee**4*FM7*complex(0,1)*vev**2)/(4.*sw**2)',
                  order = {'M7':1,'QED':2})

GC_634 = Coupling(name = 'GC_634',
                  value = '(3*ee**4*complex(0,1)*FS0*vev**2)/(4.*cw**2) + (3*cw**2*ee**4*complex(0,1)*FS0*vev**2)/(4.*sw**4) + (3*ee**4*complex(0,1)*FS0*vev**2)/(2.*sw**2)',
                  order = {'QED':2,'S0':1})

GC_635 = Coupling(name = 'GC_635',
                  value = '(3*ee**4*complex(0,1)*FS1*vev**2)/(2.*cw**2) + (3*cw**2*ee**4*complex(0,1)*FS1*vev**2)/(2.*sw**4) + (3*ee**4*complex(0,1)*FS1*vev**2)/sw**2',
                  order = {'QED':2,'S1':1})

GC_636 = Coupling(name = 'GC_636',
                  value = '(3*ee**4*complex(0,1)*FS2*vev**2)/(4.*cw**2) + (3*cw**2*ee**4*complex(0,1)*FS2*vev**2)/(4.*sw**4) + (3*ee**4*complex(0,1)*FS2*vev**2)/(2.*sw**2)',
                  order = {'QED':2,'S2':1})

GC_637 = Coupling(name = 'GC_637',
                  value = '(-3*cw*ee**3*complex(0,1)*FS0*vev**2)/(8.*sw**3) - (3*ee**3*complex(0,1)*FS0*vev**2)/(8.*cw*sw)',
                  order = {'QED':1,'S0':1})

GC_638 = Coupling(name = 'GC_638',
                  value = '(3*cw*ee**3*complex(0,1)*FS2*vev**2)/(8.*sw**3) + (3*ee**3*complex(0,1)*FS2*vev**2)/(8.*cw*sw)',
                  order = {'QED':1,'S2':1})

GC_639 = Coupling(name = 'GC_639',
                  value = '-(cw**3*ee**3*FM0*complex(0,1)*vev**2)/(2.*sw**3) - (cw*ee**3*FM0*complex(0,1)*vev**2)/sw - (ee**3*FM0*complex(0,1)*sw*vev**2)/(2.*cw)',
                  order = {'M0':1,'QED':1})

GC_640 = Coupling(name = 'GC_640',
                  value = '(cw**3*ee**4*FM0*complex(0,1)*vev**2)/sw**3 + (2*cw*ee**4*FM0*complex(0,1)*vev**2)/sw + (ee**4*FM0*complex(0,1)*sw*vev**2)/cw',
                  order = {'M0':1,'QED':2})

GC_641 = Coupling(name = 'GC_641',
                  value = '-(cw**3*ee**3*FM1*complex(0,1)*vev**2)/(8.*sw**3) - (cw*ee**3*FM1*complex(0,1)*vev**2)/(4.*sw) - (ee**3*FM1*complex(0,1)*sw*vev**2)/(8.*cw)',
                  order = {'M1':1,'QED':1})

GC_642 = Coupling(name = 'GC_642',
                  value = '-(cw**3*ee**4*FM1*complex(0,1)*vev**2)/(2.*sw**3) - (cw*ee**4*FM1*complex(0,1)*vev**2)/sw - (ee**4*FM1*complex(0,1)*sw*vev**2)/(2.*cw)',
                  order = {'M1':1,'QED':2})

GC_643 = Coupling(name = 'GC_643',
                  value = '(cw*ee**3*FM7*complex(0,1)*vev**2)/(16.*sw) + (ee**3*FM7*complex(0,1)*sw*vev**2)/(16.*cw)',
                  order = {'M7':1,'QED':1})

GC_644 = Coupling(name = 'GC_644',
                  value = '(cw**3*ee**4*FM7*complex(0,1)*vev**2)/(4.*sw**3) + (cw*ee**4*FM7*complex(0,1)*vev**2)/(2.*sw) + (ee**4*FM7*complex(0,1)*sw*vev**2)/(4.*cw)',
                  order = {'M7':1,'QED':2})

GC_645 = Coupling(name = 'GC_645',
                  value = 'cw**2*ee**2*FM0*complex(0,1)*vev**2 + (cw**4*ee**2*FM0*complex(0,1)*vev**2)/(2.*sw**2) + (ee**2*FM0*complex(0,1)*sw**2*vev**2)/2.',
                  order = {'M0':1})

GC_646 = Coupling(name = 'GC_646',
                  value = 'ee**2*FM0*complex(0,1)*vev**2 + (ee**2*FM0*complex(0,1)*sw**2*vev**2)/(2.*cw**2)',
                  order = {'M0':1})

GC_647 = Coupling(name = 'GC_647',
                  value = '-(ee**3*FM0*complex(0,1)*vev**2) - (cw**2*ee**3*FM0*complex(0,1)*vev**2)/(2.*sw**2) - (ee**3*FM0*complex(0,1)*sw**2*vev**2)/(2.*cw**2)',
                  order = {'M0':1,'QED':1})

GC_648 = Coupling(name = 'GC_648',
                  value = '-(ee**4*FM0*complex(0,1)*vev**2) - (cw**2*ee**4*FM0*complex(0,1)*vev**2)/(2.*sw**2) - (ee**4*FM0*complex(0,1)*sw**2*vev**2)/(2.*cw**2)',
                  order = {'M0':1,'QED':2})

GC_649 = Coupling(name = 'GC_649',
                  value = '(cw**2*ee**2*FM1*complex(0,1)*vev**2)/4. + (cw**4*ee**2*FM1*complex(0,1)*vev**2)/(8.*sw**2) + (ee**2*FM1*complex(0,1)*sw**2*vev**2)/8.',
                  order = {'M1':1})

GC_650 = Coupling(name = 'GC_650',
                  value = '(ee**2*FM1*complex(0,1)*vev**2)/4. + (ee**2*FM1*complex(0,1)*sw**2*vev**2)/(8.*cw**2)',
                  order = {'M1':1})

GC_651 = Coupling(name = 'GC_651',
                  value = '(ee**3*FM1*complex(0,1)*vev**2)/4. + (cw**2*ee**3*FM1*complex(0,1)*vev**2)/(8.*sw**2) + (ee**3*FM1*complex(0,1)*sw**2*vev**2)/(8.*cw**2)',
                  order = {'M1':1,'QED':1})

GC_652 = Coupling(name = 'GC_652',
                  value = '-(ee**4*FM1*complex(0,1)*vev**2)/2. - (cw**2*ee**4*FM1*complex(0,1)*vev**2)/(4.*sw**2) - (ee**4*FM1*complex(0,1)*sw**2*vev**2)/(4.*cw**2)',
                  order = {'M1':1,'QED':2})

GC_653 = Coupling(name = 'GC_653',
                  value = '2*cw**2*ee**2*FM2*complex(0,1)*vev**2 + (cw**4*ee**2*FM2*complex(0,1)*vev**2)/sw**2 + ee**2*FM2*complex(0,1)*sw**2*vev**2',
                  order = {'M2':1})

GC_654 = Coupling(name = 'GC_654',
                  value = '(cw**2*ee**2*FM3*complex(0,1)*vev**2)/2. + (cw**4*ee**2*FM3*complex(0,1)*vev**2)/(4.*sw**2) + (ee**2*FM3*complex(0,1)*sw**2*vev**2)/4.',
                  order = {'M3':1})

GC_655 = Coupling(name = 'GC_655',
                  value = '-(cw**2*ee**2*FM7*complex(0,1)*vev**2)/8. - (cw**4*ee**2*FM7*complex(0,1)*vev**2)/(16.*sw**2) - (ee**2*FM7*complex(0,1)*sw**2*vev**2)/16.',
                  order = {'M7':1})

GC_656 = Coupling(name = 'GC_656',
                  value = '(ee**4*FM7*complex(0,1)*vev**2)/4. + (cw**2*ee**4*FM7*complex(0,1)*vev**2)/(8.*sw**2) + (ee**4*FM7*complex(0,1)*sw**2*vev**2)/(8.*cw**2)',
                  order = {'M7':1,'QED':2})

GC_657 = Coupling(name = 'GC_657',
                  value = '-(ee**2*complex(0,1)*FS0*vev**2) - (cw**2*ee**2*complex(0,1)*FS0*vev**2)/(2.*sw**2) - (ee**2*complex(0,1)*FS0*sw**2*vev**2)/(2.*cw**2)',
                  order = {'S0':1})

GC_658 = Coupling(name = 'GC_658',
                  value = '-(ee**2*complex(0,1)*FS1*vev**2) - (cw**2*ee**2*complex(0,1)*FS1*vev**2)/(2.*sw**2) - (ee**2*complex(0,1)*FS1*sw**2*vev**2)/(2.*cw**2)',
                  order = {'S1':1})

GC_659 = Coupling(name = 'GC_659',
                  value = '-(ee**2*complex(0,1)*FS2*vev**2) - (cw**2*ee**2*complex(0,1)*FS2*vev**2)/(2.*sw**2) - (ee**2*complex(0,1)*FS2*sw**2*vev**2)/(2.*cw**2)',
                  order = {'S2':1})

GC_660 = Coupling(name = 'GC_660',
                  value = '(cw**3*ee**2*FM0*complex(0,1)*vev**2)/(2.*sw) + cw*ee**2*FM0*complex(0,1)*sw*vev**2 + (ee**2*FM0*complex(0,1)*sw**3*vev**2)/(2.*cw)',
                  order = {'M0':1})

GC_661 = Coupling(name = 'GC_661',
                  value = '(cw**3*ee**2*FM1*complex(0,1)*vev**2)/(8.*sw) + (cw*ee**2*FM1*complex(0,1)*sw*vev**2)/4. + (ee**2*FM1*complex(0,1)*sw**3*vev**2)/(8.*cw)',
                  order = {'M1':1})

GC_662 = Coupling(name = 'GC_662',
                  value = '-((cw**3*ee**2*FM2*complex(0,1)*vev**2)/sw) - 2*cw*ee**2*FM2*complex(0,1)*sw*vev**2 - (ee**2*FM2*complex(0,1)*sw**3*vev**2)/cw',
                  order = {'M2':1})

GC_663 = Coupling(name = 'GC_663',
                  value = '-(cw**3*ee**2*FM3*complex(0,1)*vev**2)/(4.*sw) - (cw*ee**2*FM3*complex(0,1)*sw*vev**2)/2. - (ee**2*FM3*complex(0,1)*sw**3*vev**2)/(4.*cw)',
                  order = {'M3':1})

GC_664 = Coupling(name = 'GC_664',
                  value = '-(cw**3*ee**2*FM4*complex(0,1)*vev**2)/(2.*sw) - cw*ee**2*FM4*complex(0,1)*sw*vev**2 - (ee**2*FM4*complex(0,1)*sw**3*vev**2)/(2.*cw)',
                  order = {'M4':1})

GC_665 = Coupling(name = 'GC_665',
                  value = '(cw**3*ee**2*FM4*complex(0,1)*vev**2)/(2.*sw) + cw*ee**2*FM4*complex(0,1)*sw*vev**2 + (ee**2*FM4*complex(0,1)*sw**3*vev**2)/(2.*cw)',
                  order = {'M4':1})

GC_666 = Coupling(name = 'GC_666',
                  value = '-(cw**3*ee**2*FM5*complex(0,1)*vev**2)/(4.*sw) - (cw*ee**2*FM5*complex(0,1)*sw*vev**2)/2. - (ee**2*FM5*complex(0,1)*sw**3*vev**2)/(4.*cw)',
                  order = {'M5':1})

GC_667 = Coupling(name = 'GC_667',
                  value = '(cw**3*ee**2*FM5*complex(0,1)*vev**2)/(4.*sw) + (cw*ee**2*FM5*complex(0,1)*sw*vev**2)/2. + (ee**2*FM5*complex(0,1)*sw**3*vev**2)/(4.*cw)',
                  order = {'M5':1})

GC_668 = Coupling(name = 'GC_668',
                  value = '-(cw**3*ee**2*FM7*complex(0,1)*vev**2)/(16.*sw) - (cw*ee**2*FM7*complex(0,1)*sw*vev**2)/8. - (ee**2*FM7*complex(0,1)*sw**3*vev**2)/(16.*cw)',
                  order = {'M7':1})

GC_669 = Coupling(name = 'GC_669',
                  value = '(cw**2*ee**2*FM0*complex(0,1)*vev**2)/2. + ee**2*FM0*complex(0,1)*sw**2*vev**2 + (ee**2*FM0*complex(0,1)*sw**4*vev**2)/(2.*cw**2)',
                  order = {'M0':1})

GC_670 = Coupling(name = 'GC_670',
                  value = '(cw**2*ee**2*FM1*complex(0,1)*vev**2)/8. + (ee**2*FM1*complex(0,1)*sw**2*vev**2)/4. + (ee**2*FM1*complex(0,1)*sw**4*vev**2)/(8.*cw**2)',
                  order = {'M1':1})

GC_671 = Coupling(name = 'GC_671',
                  value = 'cw**2*ee**2*FM2*complex(0,1)*vev**2 + 2*ee**2*FM2*complex(0,1)*sw**2*vev**2 + (ee**2*FM2*complex(0,1)*sw**4*vev**2)/cw**2',
                  order = {'M2':1})

GC_672 = Coupling(name = 'GC_672',
                  value = '(cw**2*ee**2*FM3*complex(0,1)*vev**2)/4. + (ee**2*FM3*complex(0,1)*sw**2*vev**2)/2. + (ee**2*FM3*complex(0,1)*sw**4*vev**2)/(4.*cw**2)',
                  order = {'M3':1})

GC_673 = Coupling(name = 'GC_673',
                  value = '-(cw**2*ee**2*FM4*complex(0,1)*vev**2)/4. - (cw**4*ee**2*FM4*complex(0,1)*vev**2)/(4.*sw**2) + (ee**2*FM4*complex(0,1)*sw**2*vev**2)/4. + (ee**2*FM4*complex(0,1)*sw**4*vev**2)/(4.*cw**2)',
                  order = {'M4':1})

GC_674 = Coupling(name = 'GC_674',
                  value = '(cw**2*ee**2*FM5*complex(0,1)*vev**2)/8. + (cw**4*ee**2*FM5*complex(0,1)*vev**2)/(8.*sw**2) - (ee**2*FM5*complex(0,1)*sw**2*vev**2)/8. - (ee**2*FM5*complex(0,1)*sw**4*vev**2)/(8.*cw**2)',
                  order = {'M5':1})

GC_675 = Coupling(name = 'GC_675',
                  value = '-(cw**2*ee**2*FM7*complex(0,1)*vev**2)/16. - (ee**2*FM7*complex(0,1)*sw**2*vev**2)/8. - (ee**2*FM7*complex(0,1)*sw**4*vev**2)/(16.*cw**2)',
                  order = {'M7':1})

GC_676 = Coupling(name = 'GC_676',
                  value = '9*ee**4*complex(0,1)*FS0*vev**2 + (3*cw**4*ee**4*complex(0,1)*FS0*vev**2)/(2.*sw**4) + (6*cw**2*ee**4*complex(0,1)*FS0*vev**2)/sw**2 + (6*ee**4*complex(0,1)*FS0*sw**2*vev**2)/cw**2 + (3*ee**4*complex(0,1)*FS0*sw**4*vev**2)/(2.*cw**4)',
                  order = {'QED':2,'S0':1})

GC_677 = Coupling(name = 'GC_677',
                  value = '9*ee**4*complex(0,1)*FS1*vev**2 + (3*cw**4*ee**4*complex(0,1)*FS1*vev**2)/(2.*sw**4) + (6*cw**2*ee**4*complex(0,1)*FS1*vev**2)/sw**2 + (6*ee**4*complex(0,1)*FS1*sw**2*vev**2)/cw**2 + (3*ee**4*complex(0,1)*FS1*sw**4*vev**2)/(2.*cw**4)',
                  order = {'QED':2,'S1':1})

GC_678 = Coupling(name = 'GC_678',
                  value = '9*ee**4*complex(0,1)*FS2*vev**2 + (3*cw**4*ee**4*complex(0,1)*FS2*vev**2)/(2.*sw**4) + (6*cw**2*ee**4*complex(0,1)*FS2*vev**2)/sw**2 + (6*ee**4*complex(0,1)*FS2*sw**2*vev**2)/cw**2 + (3*ee**4*complex(0,1)*FS2*sw**4*vev**2)/(2.*cw**4)',
                  order = {'QED':2,'S2':1})

GC_679 = Coupling(name = 'GC_679',
                  value = '(ee**4*complex(0,1)*FS0*vev**3)/(4.*cw**2) + (cw**2*ee**4*complex(0,1)*FS0*vev**3)/(4.*sw**4) + (ee**4*complex(0,1)*FS0*vev**3)/(2.*sw**2)',
                  order = {'QED':1,'S0':1})

GC_680 = Coupling(name = 'GC_680',
                  value = '(ee**4*complex(0,1)*FS1*vev**3)/(2.*cw**2) + (cw**2*ee**4*complex(0,1)*FS1*vev**3)/(2.*sw**4) + (ee**4*complex(0,1)*FS1*vev**3)/sw**2',
                  order = {'QED':1,'S1':1})

GC_681 = Coupling(name = 'GC_681',
                  value = '(ee**4*complex(0,1)*FS2*vev**3)/(4.*cw**2) + (cw**2*ee**4*complex(0,1)*FS2*vev**3)/(4.*sw**4) + (ee**4*complex(0,1)*FS2*vev**3)/(2.*sw**2)',
                  order = {'QED':1,'S2':1})

GC_682 = Coupling(name = 'GC_682',
                  value = '-(cw*ee**3*complex(0,1)*FS0*vev**3)/(8.*sw**3) - (ee**3*complex(0,1)*FS0*vev**3)/(8.*cw*sw)',
                  order = {'S0':1})

GC_683 = Coupling(name = 'GC_683',
                  value = '(cw*ee**3*complex(0,1)*FS2*vev**3)/(8.*sw**3) + (ee**3*complex(0,1)*FS2*vev**3)/(8.*cw*sw)',
                  order = {'S2':1})

GC_684 = Coupling(name = 'GC_684',
                  value = '3*ee**4*complex(0,1)*FS0*vev**3 + (cw**4*ee**4*complex(0,1)*FS0*vev**3)/(2.*sw**4) + (2*cw**2*ee**4*complex(0,1)*FS0*vev**3)/sw**2 + (2*ee**4*complex(0,1)*FS0*sw**2*vev**3)/cw**2 + (ee**4*complex(0,1)*FS0*sw**4*vev**3)/(2.*cw**4)',
                  order = {'QED':1,'S0':1})

GC_685 = Coupling(name = 'GC_685',
                  value = '3*ee**4*complex(0,1)*FS1*vev**3 + (cw**4*ee**4*complex(0,1)*FS1*vev**3)/(2.*sw**4) + (2*cw**2*ee**4*complex(0,1)*FS1*vev**3)/sw**2 + (2*ee**4*complex(0,1)*FS1*sw**2*vev**3)/cw**2 + (ee**4*complex(0,1)*FS1*sw**4*vev**3)/(2.*cw**4)',
                  order = {'QED':1,'S1':1})

GC_686 = Coupling(name = 'GC_686',
                  value = '3*ee**4*complex(0,1)*FS2*vev**3 + (cw**4*ee**4*complex(0,1)*FS2*vev**3)/(2.*sw**4) + (2*cw**2*ee**4*complex(0,1)*FS2*vev**3)/sw**2 + (2*ee**4*complex(0,1)*FS2*sw**2*vev**3)/cw**2 + (ee**4*complex(0,1)*FS2*sw**4*vev**3)/(2.*cw**4)',
                  order = {'QED':1,'S2':1})

GC_687 = Coupling(name = 'GC_687',
                  value = '(ee**4*complex(0,1)*FS0*vev**4)/(16.*cw**2) + (cw**2*ee**4*complex(0,1)*FS0*vev**4)/(16.*sw**4) + (ee**4*complex(0,1)*FS0*vev**4)/(8.*sw**2)',
                  order = {'S0':1})

GC_688 = Coupling(name = 'GC_688',
                  value = '(ee**4*complex(0,1)*FS1*vev**4)/(8.*cw**2) + (cw**2*ee**4*complex(0,1)*FS1*vev**4)/(8.*sw**4) + (ee**4*complex(0,1)*FS1*vev**4)/(4.*sw**2)',
                  order = {'S1':1})

GC_689 = Coupling(name = 'GC_689',
                  value = '(ee**4*complex(0,1)*FS2*vev**4)/(16.*cw**2) + (cw**2*ee**4*complex(0,1)*FS2*vev**4)/(16.*sw**4) + (ee**4*complex(0,1)*FS2*vev**4)/(8.*sw**2)',
                  order = {'S2':1})

GC_690 = Coupling(name = 'GC_690',
                  value = '(3*ee**4*complex(0,1)*FS0*vev**4)/4. + (cw**4*ee**4*complex(0,1)*FS0*vev**4)/(8.*sw**4) + (cw**2*ee**4*complex(0,1)*FS0*vev**4)/(2.*sw**2) + (ee**4*complex(0,1)*FS0*sw**2*vev**4)/(2.*cw**2) + (ee**4*complex(0,1)*FS0*sw**4*vev**4)/(8.*cw**4)',
                  order = {'S0':1})

GC_691 = Coupling(name = 'GC_691',
                  value = '(3*ee**4*complex(0,1)*FS1*vev**4)/4. + (cw**4*ee**4*complex(0,1)*FS1*vev**4)/(8.*sw**4) + (cw**2*ee**4*complex(0,1)*FS1*vev**4)/(2.*sw**2) + (ee**4*complex(0,1)*FS1*sw**2*vev**4)/(2.*cw**2) + (ee**4*complex(0,1)*FS1*sw**4*vev**4)/(8.*cw**4)',
                  order = {'S1':1})

GC_692 = Coupling(name = 'GC_692',
                  value = '(3*ee**4*complex(0,1)*FS2*vev**4)/4. + (cw**4*ee**4*complex(0,1)*FS2*vev**4)/(8.*sw**4) + (cw**2*ee**4*complex(0,1)*FS2*vev**4)/(2.*sw**2) + (ee**4*complex(0,1)*FS2*sw**2*vev**4)/(2.*cw**2) + (ee**4*complex(0,1)*FS2*sw**4*vev**4)/(8.*cw**4)',
                  order = {'S2':1})

GC_693 = Coupling(name = 'GC_693',
                  value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_694 = Coupling(name = 'GC_694',
                  value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_695 = Coupling(name = 'GC_695',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_696 = Coupling(name = 'GC_696',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_697 = Coupling(name = 'GC_697',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_698 = Coupling(name = 'GC_698',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

