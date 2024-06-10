# This file was automatically created by FeynRules 2.3.14
# Mathematica version: 10.3.0 for Linux x86 (64-bit) (October 9, 2015)
# Date: Fri 6 Mar 2020 14:41:35


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS1, L.SSSS2 ],
             couplings = {(0,0):C.GC_84,(0,1):C.GC_31})

V_2 = Vertex(name = 'V_2',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS2 ],
             couplings = {(0,0):C.GC_32})

V_3 = Vertex(name = 'V_3',
             particles = [ P.H, P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSSS2 ],
             couplings = {(0,0):C.GC_33})

V_4 = Vertex(name = 'V_4',
             particles = [ P.H, P.H, P.H ],
             color = [ '1' ],
             lorentz = [ L.SSS1 ],
             couplings = {(0,0):C.GC_412})

V_5 = Vertex(name = 'V_5',
             particles = [ P.ghG, P.ghG__tilde__, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.UUV1 ],
             couplings = {(0,0):C.GC_81})

V_6 = Vertex(name = 'V_6',
             particles = [ P.g, P.g, P.g ],
             color = [ 'f(1,2,3)' ],
             lorentz = [ L.VVV1 ],
             couplings = {(0,0):C.GC_81})

V_7 = Vertex(name = 'V_7',
             particles = [ P.g, P.g, P.g, P.g ],
             color = [ 'f(-1,1,2)*f(3,4,-1)', 'f(-1,1,3)*f(2,4,-1)', 'f(-1,1,4)*f(2,3,-1)' ],
             lorentz = [ L.VVVV12, L.VVVV13, L.VVVV3 ],
             couplings = {(1,0):C.GC_83,(0,2):C.GC_83,(2,1):C.GC_83})

V_8 = Vertex(name = 'V_8',
             particles = [ P.ta__plus__, P.ta__minus__, P.H ],
             color = [ '1' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_694})

V_9 = Vertex(name = 'V_9',
             particles = [ P.t__tilde__, P.t, P.H ],
             color = [ 'Identity(1,2)' ],
             lorentz = [ L.FFS1 ],
             couplings = {(0,0):C.GC_693})

V_10 = Vertex(name = 'V_10',
              particles = [ P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_4})

V_11 = Vertex(name = 'V_11',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS2, L.VVSS3, L.VVSS5, L.VVSS6 ],
              couplings = {(0,0):C.GC_541,(0,1):C.GC_138,(0,3):C.GC_10,(0,4):C.GC_6,(0,2):C.GC_542})

V_12 = Vertex(name = 'V_12',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS1, L.VVSS5 ],
              couplings = {(0,0):C.GC_543,(0,1):C.GC_24})

V_13 = Vertex(name = 'V_13',
              particles = [ P.W__minus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_433})

V_14 = Vertex(name = 'V_14',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV11, L.VVVV16, L.VVVV36, L.VVVV38, L.VVVV5, L.VVVV7 ],
              couplings = {(0,5):C.GC_67,(0,2):C.GC_72,(0,3):C.GC_61,(0,4):C.GC_488,(0,0):C.GC_5,(0,1):C.GC_487})

V_15 = Vertex(name = 'V_15',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV16, L.VVVV36, L.VVVV38, L.VVVV5, L.VVVV7 ],
              couplings = {(0,4):C.GC_309,(0,1):C.GC_313,(0,2):C.GC_305,(0,3):C.GC_495,(0,0):C.GC_527})

V_16 = Vertex(name = 'V_16',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV16, L.VVVV5 ],
              couplings = {(0,1):C.GC_528,(0,0):C.GC_549})

V_17 = Vertex(name = 'V_17',
              particles = [ P.a, P.a, P.W__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV5 ],
              couplings = {(0,0):C.GC_552})

V_18 = Vertex(name = 'V_18',
              particles = [ P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVV1 ],
              couplings = {(0,0):C.GC_200})

V_19 = Vertex(name = 'V_19',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV11, L.VVVV24, L.VVVV25, L.VVVV35, L.VVVV4, L.VVVV41, L.VVVV6, L.VVVV7, L.VVVV8 ],
              couplings = {(0,7):C.GC_34,(0,5):C.GC_43,(0,3):C.GC_52,(0,2):C.GC_523,(0,1):C.GC_535,(0,6):C.GC_519,(0,0):C.GC_139,(0,4):C.GC_572,(0,8):C.GC_571})

V_20 = Vertex(name = 'V_20',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.VVVV4 ],
              couplings = {(0,0):C.GC_573})

V_21 = Vertex(name = 'V_21',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV1, L.VVVV14, L.VVVV17, L.VVVV18, L.VVVV19, L.VVVV2, L.VVVV20, L.VVVV21, L.VVVV22, L.VVVV23, L.VVVV34, L.VVVV39 ],
              couplings = {(0,5):C.GC_268,(0,10):C.GC_276,(0,11):C.GC_272,(0,9):C.GC_493,(0,8):C.GC_532,(0,7):C.GC_554,(0,4):C.GC_562,(0,6):C.GC_545,(0,2):C.GC_491,(0,3):C.GC_529,(0,0):C.GC_544,(0,1):C.GC_201})

V_22 = Vertex(name = 'V_22',
              particles = [ P.a, P.W__minus__, P.W__plus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV1, L.VVVV2, L.VVVV20, L.VVVV34, L.VVVV39 ],
              couplings = {(0,1):C.GC_280,(0,3):C.GC_289,(0,4):C.GC_285,(0,2):C.GC_547,(0,0):C.GC_546})

V_23 = Vertex(name = 'V_23',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS2, L.VVSS3, L.VVSS4, L.VVSS5, L.VVSS6 ],
              couplings = {(0,2):C.GC_657,(0,0):C.GC_351,(0,3):C.GC_11,(0,4):C.GC_7,(0,1):C.GC_658})

V_24 = Vertex(name = 'V_24',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS3, L.VVSS5, L.VVSS6 ],
              couplings = {(0,1):C.GC_25,(0,2):C.GC_256,(0,0):C.GC_659})

V_25 = Vertex(name = 'V_25',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS5, L.VVSS6 ],
              couplings = {(0,0):C.GC_261,(0,1):C.GC_298})

V_26 = Vertex(name = 'V_26',
              particles = [ P.Z, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSS5 ],
              couplings = {(0,0):C.GC_299})

V_27 = Vertex(name = 'V_27',
              particles = [ P.Z, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVS1 ],
              couplings = {(0,0):C.GC_592})

V_28 = Vertex(name = 'V_28',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV10, L.VVVV11, L.VVVV16, L.VVVV25, L.VVVV26, L.VVVV27, L.VVVV28, L.VVVV30, L.VVVV31, L.VVVV32, L.VVVV36, L.VVVV38, L.VVVV4, L.VVVV5, L.VVVV6, L.VVVV7, L.VVVV8, L.VVVV9 ],
              couplings = {(0,15):C.GC_44,(0,10):C.GC_53,(0,11):C.GC_35,(0,13):C.GC_650,(0,6):C.GC_496,(0,0):C.GC_524,(0,4):C.GC_536,(0,5):C.GC_551,(0,3):C.GC_560,(0,7):C.GC_489,(0,9):C.GC_520,(0,8):C.GC_548,(0,14):C.GC_558,(0,17):C.GC_490,(0,1):C.GC_140,(0,12):C.GC_687,(0,2):C.GC_646,(0,16):C.GC_688})

V_29 = Vertex(name = 'V_29',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z ],
              color = [ '1' ],
              lorentz = [ L.VVVV36, L.VVVV38, L.VVVV4, L.VVVV5, L.VVVV7 ],
              couplings = {(0,4):C.GC_322,(0,0):C.GC_327,(0,1):C.GC_317,(0,3):C.GC_566,(0,2):C.GC_689})

V_30 = Vertex(name = 'V_30',
              particles = [ P.e__plus__, P.ve, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_193})

V_31 = Vertex(name = 'V_31',
              particles = [ P.mu__plus__, P.vm, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_193})

V_32 = Vertex(name = 'V_32',
              particles = [ P.ta__plus__, P.vt, P.W__minus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_193})

V_33 = Vertex(name = 'V_33',
              particles = [ P.ve__tilde__, P.ve, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_344})

V_34 = Vertex(name = 'V_34',
              particles = [ P.vm__tilde__, P.vm, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_344})

V_35 = Vertex(name = 'V_35',
              particles = [ P.vt__tilde__, P.vt, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_344})

V_36 = Vertex(name = 'V_36',
              particles = [ P.e__plus__, P.e__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_3})

V_37 = Vertex(name = 'V_37',
              particles = [ P.mu__plus__, P.mu__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_3})

V_38 = Vertex(name = 'V_38',
              particles = [ P.ta__plus__, P.ta__minus__, P.a ],
              color = [ '1' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_3})

V_39 = Vertex(name = 'V_39',
              particles = [ P.ve__tilde__, P.e__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_193})

V_40 = Vertex(name = 'V_40',
              particles = [ P.vm__tilde__, P.mu__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_193})

V_41 = Vertex(name = 'V_41',
              particles = [ P.vt__tilde__, P.ta__minus__, P.W__plus__ ],
              color = [ '1' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_193})

V_42 = Vertex(name = 'V_42',
              particles = [ P.e__plus__, P.e__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV4 ],
              couplings = {(0,0):C.GC_198,(0,1):C.GC_251})

V_43 = Vertex(name = 'V_43',
              particles = [ P.mu__plus__, P.mu__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV4 ],
              couplings = {(0,0):C.GC_198,(0,1):C.GC_251})

V_44 = Vertex(name = 'V_44',
              particles = [ P.ta__plus__, P.ta__minus__, P.Z ],
              color = [ '1' ],
              lorentz = [ L.FFV2, L.FFV4 ],
              couplings = {(0,0):C.GC_198,(0,1):C.GC_251})

V_45 = Vertex(name = 'V_45',
              particles = [ P.c__tilde__, P.c, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_2})

V_46 = Vertex(name = 'V_46',
              particles = [ P.t__tilde__, P.t, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_2})

V_47 = Vertex(name = 'V_47',
              particles = [ P.u__tilde__, P.u, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_2})

V_48 = Vertex(name = 'V_48',
              particles = [ P.c__tilde__, P.c, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_82})

V_49 = Vertex(name = 'V_49',
              particles = [ P.t__tilde__, P.t, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_82})

V_50 = Vertex(name = 'V_50',
              particles = [ P.u__tilde__, P.u, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_82})

V_51 = Vertex(name = 'V_51',
              particles = [ P.d__tilde__, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_196})

V_52 = Vertex(name = 'V_52',
              particles = [ P.s__tilde__, P.c, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_197})

V_53 = Vertex(name = 'V_53',
              particles = [ P.b__tilde__, P.t, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_193})

V_54 = Vertex(name = 'V_54',
              particles = [ P.d__tilde__, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_194})

V_55 = Vertex(name = 'V_55',
              particles = [ P.s__tilde__, P.u, P.W__minus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_195})

V_56 = Vertex(name = 'V_56',
              particles = [ P.c__tilde__, P.c, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV5 ],
              couplings = {(0,0):C.GC_199,(0,1):C.GC_250})

V_57 = Vertex(name = 'V_57',
              particles = [ P.t__tilde__, P.t, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV5 ],
              couplings = {(0,0):C.GC_199,(0,1):C.GC_250})

V_58 = Vertex(name = 'V_58',
              particles = [ P.u__tilde__, P.u, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV5 ],
              couplings = {(0,0):C.GC_199,(0,1):C.GC_250})

V_59 = Vertex(name = 'V_59',
              particles = [ P.b__tilde__, P.b, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_60 = Vertex(name = 'V_60',
              particles = [ P.d__tilde__, P.d, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_61 = Vertex(name = 'V_61',
              particles = [ P.s__tilde__, P.s, P.a ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_1})

V_62 = Vertex(name = 'V_62',
              particles = [ P.b__tilde__, P.b, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_82})

V_63 = Vertex(name = 'V_63',
              particles = [ P.d__tilde__, P.d, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_82})

V_64 = Vertex(name = 'V_64',
              particles = [ P.s__tilde__, P.s, P.g ],
              color = [ 'T(3,2,1)' ],
              lorentz = [ L.FFV1 ],
              couplings = {(0,0):C.GC_82})

V_65 = Vertex(name = 'V_65',
              particles = [ P.t__tilde__, P.b, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_193})

V_66 = Vertex(name = 'V_66',
              particles = [ P.c__tilde__, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_697})

V_67 = Vertex(name = 'V_67',
              particles = [ P.u__tilde__, P.d, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_695})

V_68 = Vertex(name = 'V_68',
              particles = [ P.c__tilde__, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_698})

V_69 = Vertex(name = 'V_69',
              particles = [ P.u__tilde__, P.s, P.W__plus__ ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2 ],
              couplings = {(0,0):C.GC_696})

V_70 = Vertex(name = 'V_70',
              particles = [ P.b__tilde__, P.b, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_198,(0,1):C.GC_250})

V_71 = Vertex(name = 'V_71',
              particles = [ P.d__tilde__, P.d, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,0):C.GC_198,(0,1):C.GC_250})

V_72 = Vertex(name = 'V_72',
              particles = [ P.s__tilde__, P.s, P.Z ],
              color = [ 'Identity(1,2)' ],
              lorentz = [ L.FFV2, L.FFV3 ],
              couplings = {(0,1):C.GC_250,(0,0):C.GC_198})

V_73 = Vertex(name = 'V_73',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSSSS1, L.VVSSSS3 ],
              couplings = {(0,0):C.GC_163,(0,1):C.GC_164})

V_74 = Vertex(name = 'V_74',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSSSS1 ],
              couplings = {(0,0):C.GC_165})

V_75 = Vertex(name = 'V_75',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSSS1, L.VVSSS3 ],
              couplings = {(0,0):C.GC_456,(0,1):C.GC_457})

V_76 = Vertex(name = 'V_76',
              particles = [ P.W__minus__, P.W__plus__, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSSS1 ],
              couplings = {(0,0):C.GC_458})

V_77 = Vertex(name = 'V_77',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2 ],
              couplings = {(0,0):C.GC_104,(0,1):C.GC_103})

V_78 = Vertex(name = 'V_78',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVSSSS1 ],
              couplings = {(0,0):C.GC_105})

V_79 = Vertex(name = 'V_79',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVSSS1, L.VVVVSSS2 ],
              couplings = {(0,0):C.GC_420,(0,1):C.GC_419})

V_80 = Vertex(name = 'V_80',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVSSS1 ],
              couplings = {(0,0):C.GC_421})

V_81 = Vertex(name = 'V_81',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVSS19, L.VVVVSS2, L.VVVVSS32, L.VVVVSS37, L.VVVVSS5 ],
              couplings = {(0,0):C.GC_145,(0,2):C.GC_157,(0,3):C.GC_141,(0,1):C.GC_506,(0,4):C.GC_505})

V_82 = Vertex(name = 'V_82',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVSS2 ],
              couplings = {(0,0):C.GC_507})

V_83 = Vertex(name = 'V_83',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVS16, L.VVVVS2, L.VVVVS30, L.VVVVS4, L.VVVVS5 ],
              couplings = {(0,0):C.GC_438,(0,2):C.GC_450,(0,3):C.GC_434,(0,1):C.GC_569,(0,4):C.GC_568})

V_84 = Vertex(name = 'V_84',
              particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVS2 ],
              couplings = {(0,0):C.GC_570})

V_85 = Vertex(name = 'V_85',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVSSSS1 ],
              couplings = {(0,0):C.GC_95})

V_86 = Vertex(name = 'V_86',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVSSSS1 ],
              couplings = {(0,0):C.GC_96})

V_87 = Vertex(name = 'V_87',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVSSS1 ],
              couplings = {(0,0):C.GC_584})

V_88 = Vertex(name = 'V_88',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVSSS1 ],
              couplings = {(0,0):C.GC_585})

V_89 = Vertex(name = 'V_89',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVSS10, L.VVVSS2, L.VVVSS3, L.VVVSS5, L.VVVSS6, L.VVVSS8, L.VVVSS9 ],
              couplings = {(0,5):C.GC_216,(0,2):C.GC_265,(0,3):C.GC_21,(0,0):C.GC_18,(0,4):C.GC_204,(0,1):C.GC_637,(0,6):C.GC_202})

V_90 = Vertex(name = 'V_90',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVSS2 ],
              couplings = {(0,0):C.GC_638})

V_91 = Vertex(name = 'V_91',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVS2, L.VVVS3, L.VVVS4, L.VVVS7, L.VVVS8 ],
              couplings = {(0,3):C.GC_471,(0,2):C.GC_480,(0,4):C.GC_404,(0,1):C.GC_401,(0,0):C.GC_682})

V_92 = Vertex(name = 'V_92',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVS2 ],
              couplings = {(0,0):C.GC_683})

V_93 = Vertex(name = 'V_93',
              particles = [ P.Z, P.Z, P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSSSS2, L.VVSSSS3 ],
              couplings = {(0,0):C.GC_366,(0,1):C.GC_367})

V_94 = Vertex(name = 'V_94',
              particles = [ P.Z, P.Z, P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSSSS3 ],
              couplings = {(0,0):C.GC_368})

V_95 = Vertex(name = 'V_95',
              particles = [ P.Z, P.Z, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSSS2, L.VVSSS3 ],
              couplings = {(0,0):C.GC_605,(0,1):C.GC_606})

V_96 = Vertex(name = 'V_96',
              particles = [ P.Z, P.Z, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVSSS3 ],
              couplings = {(0,0):C.GC_607})

V_97 = Vertex(name = 'V_97',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVSSSS1, L.VVVVSSSS2 ],
              couplings = {(0,0):C.GC_92,(0,1):C.GC_93})

V_98 = Vertex(name = 'V_98',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVSSSS1 ],
              couplings = {(0,0):C.GC_94})

V_99 = Vertex(name = 'V_99',
              particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H, P.H ],
              color = [ '1' ],
              lorentz = [ L.VVVVSSS1, L.VVVVSSS2 ],
              couplings = {(0,0):C.GC_581,(0,1):C.GC_582})

V_100 = Vertex(name = 'V_100',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS1 ],
               couplings = {(0,0):C.GC_583})

V_101 = Vertex(name = 'V_101',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS11, L.VVVVSS18, L.VVVVSS2, L.VVVVSS21, L.VVVVSS22, L.VVVVSS28, L.VVVVSS29, L.VVVVSS3, L.VVVVSS30, L.VVVVSS35, L.VVVVSS4, L.VVVVSS5, L.VVVVSS6, L.VVVVSS8 ],
               couplings = {(0,7):C.GC_357,(0,5):C.GC_28,(0,13):C.GC_146,(0,8):C.GC_158,(0,6):C.GC_213,(0,1):C.GC_262,(0,3):C.GC_15,(0,9):C.GC_142,(0,4):C.GC_210,(0,10):C.GC_258,(0,12):C.GC_17,(0,2):C.GC_634,(0,0):C.GC_353,(0,11):C.GC_635})

V_102 = Vertex(name = 'V_102',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS2, L.VVVVSS3 ],
               couplings = {(0,1):C.GC_303,(0,0):C.GC_636})

V_103 = Vertex(name = 'V_103',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS10, L.VVVVS16, L.VVVVS18, L.VVVVS19, L.VVVVS2, L.VVVVS20, L.VVVVS26, L.VVVVS27, L.VVVVS28, L.VVVVS3, L.VVVVS4, L.VVVVS5, L.VVVVS6, L.VVVVS7 ],
               couplings = {(0,9):C.GC_598,(0,6):C.GC_409,(0,13):C.GC_439,(0,8):C.GC_451,(0,7):C.GC_468,(0,1):C.GC_478,(0,2):C.GC_399,(0,5):C.GC_435,(0,3):C.GC_465,(0,10):C.GC_476,(0,12):C.GC_400,(0,4):C.GC_679,(0,0):C.GC_594,(0,11):C.GC_680})

V_104 = Vertex(name = 'V_104',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS2, L.VVVVS3 ],
               couplings = {(0,1):C.GC_485,(0,0):C.GC_681})

V_105 = Vertex(name = 'V_105',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSSS3 ],
               couplings = {(0,0):C.GC_391})

V_106 = Vertex(name = 'V_106',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSSS3 ],
               couplings = {(0,0):C.GC_392})

V_107 = Vertex(name = 'V_107',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.H, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSSS3 ],
               couplings = {(0,0):C.GC_393})

V_108 = Vertex(name = 'V_108',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS3 ],
               couplings = {(0,0):C.GC_624})

V_109 = Vertex(name = 'V_109',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS3 ],
               couplings = {(0,0):C.GC_625})

V_110 = Vertex(name = 'V_110',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.H, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSSS3 ],
               couplings = {(0,0):C.GC_626})

V_111 = Vertex(name = 'V_111',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS20, L.VVVVSS23, L.VVVVSS9 ],
               couplings = {(0,0):C.GC_356,(0,1):C.GC_352,(0,2):C.GC_676})

V_112 = Vertex(name = 'V_112',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS20, L.VVVVSS23, L.VVVVSS9 ],
               couplings = {(0,0):C.GC_387,(0,1):C.GC_386,(0,2):C.GC_677})

V_113 = Vertex(name = 'V_113',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS20, L.VVVVSS23, L.VVVVSS9 ],
               couplings = {(0,0):C.GC_364,(0,1):C.GC_374,(0,2):C.GC_678})

V_114 = Vertex(name = 'V_114',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS20 ],
               couplings = {(0,0):C.GC_375})

V_115 = Vertex(name = 'V_115',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS17, L.VVVVS21, L.VVVVS8 ],
               couplings = {(0,0):C.GC_597,(0,1):C.GC_593,(0,2):C.GC_684})

V_116 = Vertex(name = 'V_116',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS17, L.VVVVS21, L.VVVVS8 ],
               couplings = {(0,0):C.GC_620,(0,1):C.GC_619,(0,2):C.GC_685})

V_117 = Vertex(name = 'V_117',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS17, L.VVVVS21, L.VVVVS8 ],
               couplings = {(0,0):C.GC_603,(0,1):C.GC_613,(0,2):C.GC_686})

V_118 = Vertex(name = 'V_118',
               particles = [ P.Z, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS17 ],
               couplings = {(0,0):C.GC_614})

V_119 = Vertex(name = 'V_119',
               particles = [ P.Z, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV15, L.VVVV29, L.VVVV33, L.VVVV37, L.VVVV40 ],
               couplings = {(0,4):C.GC_36,(0,3):C.GC_54,(0,1):C.GC_649,(0,2):C.GC_645,(0,0):C.GC_690})

V_120 = Vertex(name = 'V_120',
               particles = [ P.Z, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV15, L.VVVV29, L.VVVV33, L.VVVV37, L.VVVV40 ],
               couplings = {(0,4):C.GC_45,(0,3):C.GC_329,(0,1):C.GC_672,(0,2):C.GC_671,(0,0):C.GC_691})

V_121 = Vertex(name = 'V_121',
               particles = [ P.Z, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV15, L.VVVV29, L.VVVV33, L.VVVV37, L.VVVV40 ],
               couplings = {(0,4):C.GC_319,(0,3):C.GC_343,(0,1):C.GC_655,(0,2):C.GC_665,(0,0):C.GC_692})

V_122 = Vertex(name = 'V_122',
               particles = [ P.Z, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV29, L.VVVV40 ],
               couplings = {(0,1):C.GC_324,(0,0):C.GC_666})

V_123 = Vertex(name = 'V_123',
               particles = [ P.Z, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV40 ],
               couplings = {(0,0):C.GC_342})

V_124 = Vertex(name = 'V_124',
               particles = [ P.a, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS5, L.VVSS6 ],
               couplings = {(0,0):C.GC_16,(0,1):C.GC_14})

V_125 = Vertex(name = 'V_125',
               particles = [ P.a, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS5, L.VVSS6 ],
               couplings = {(0,0):C.GC_260,(0,1):C.GC_257})

V_126 = Vertex(name = 'V_126',
               particles = [ P.a, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS5, L.VVSS6 ],
               couplings = {(0,0):C.GC_297,(0,1):C.GC_296})

V_127 = Vertex(name = 'V_127',
               particles = [ P.a, P.a, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS5 ],
               couplings = {(0,0):C.GC_302})

V_128 = Vertex(name = 'V_128',
               particles = [ P.a, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS5, L.VVSS6 ],
               couplings = {(0,0):C.GC_363,(0,1):C.GC_362})

V_129 = Vertex(name = 'V_129',
               particles = [ P.a, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS5, L.VVSS6 ],
               couplings = {(0,0):C.GC_253,(0,1):C.GC_252})

V_130 = Vertex(name = 'V_130',
               particles = [ P.a, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS5, L.VVSS6 ],
               couplings = {(0,0):C.GC_255,(0,1):C.GC_254})

V_131 = Vertex(name = 'V_131',
               particles = [ P.a, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVSS5 ],
               couplings = {(0,0):C.GC_264})

V_132 = Vertex(name = 'V_132',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVSS1, L.VVVSS4, L.VVVSS6, L.VVVSS7, L.VVVSS9 ],
               couplings = {(0,3):C.GC_26,(0,1):C.GC_212,(0,0):C.GC_208,(0,2):C.GC_12,(0,4):C.GC_8})

V_133 = Vertex(name = 'V_133',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS10, L.VVVVSS11, L.VVVVSS25, L.VVVVSS27, L.VVVVSS3, L.VVVVSS34, L.VVVVSS7 ],
               couplings = {(0,6):C.GC_13,(0,2):C.GC_27,(0,4):C.GC_150,(0,3):C.GC_214,(0,0):C.GC_209,(0,5):C.GC_9,(0,1):C.GC_149})

V_134 = Vertex(name = 'V_134',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS10, L.VVVVS23, L.VVVVS25, L.VVVVS3, L.VVVVS9 ],
               couplings = {(0,3):C.GC_398,(0,1):C.GC_408,(0,2):C.GC_469,(0,4):C.GC_464,(0,0):C.GC_397})

V_135 = Vertex(name = 'V_135',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS10, L.VVVVS3 ],
               couplings = {(0,1):C.GC_443,(0,0):C.GC_442})

V_136 = Vertex(name = 'V_136',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS1, L.VVVVSS13, L.VVVVSS14, L.VVVVSS15, L.VVVVSS16, L.VVVVSS24, L.VVVVSS26, L.VVVVSS31, L.VVVVSS33, L.VVVVSS36 ],
               couplings = {(0,8):C.GC_22,(0,5):C.GC_154,(0,7):C.GC_217,(0,6):C.GC_266,(0,4):C.GC_205,(0,3):C.GC_207,(0,1):C.GC_151,(0,2):C.GC_19,(0,9):C.GC_203,(0,0):C.GC_206})

V_137 = Vertex(name = 'V_137',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS1, L.VVVVS12, L.VVVVS13, L.VVVVS14, L.VVVVS22, L.VVVVS24, L.VVVVS29, L.VVVVS31 ],
               couplings = {(0,7):C.GC_405,(0,4):C.GC_447,(0,6):C.GC_472,(0,5):C.GC_481,(0,3):C.GC_460,(0,1):C.GC_444,(0,2):C.GC_402,(0,0):C.GC_459})

V_138 = Vertex(name = 'V_138',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS1, L.VVVVS14 ],
               couplings = {(0,1):C.GC_462,(0,0):C.GC_461})

V_139 = Vertex(name = 'V_139',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVSS1, L.VVVVVSS29, L.VVVVVSS3, L.VVVVVSS30 ],
               couplings = {(0,3):C.GC_147,(0,1):C.GC_159,(0,0):C.GC_119,(0,2):C.GC_143})

V_140 = Vertex(name = 'V_140',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVSS1 ],
               couplings = {(0,0):C.GC_121})

V_141 = Vertex(name = 'V_141',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS1, L.VVVVVS29, L.VVVVVS3, L.VVVVVS30 ],
               couplings = {(0,3):C.GC_440,(0,1):C.GC_452,(0,0):C.GC_426,(0,2):C.GC_436})

V_142 = Vertex(name = 'V_142',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS1 ],
               couplings = {(0,0):C.GC_428})

V_143 = Vertex(name = 'V_143',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVV3, L.VVVVV40, L.VVVVV41, L.VVVVV52, L.VVVVV58, L.VVVVV6, L.VVVVV9 ],
               couplings = {(0,3):C.GC_55,(0,6):C.GC_37,(0,4):C.GC_46,(0,2):C.GC_525,(0,1):C.GC_537,(0,0):C.GC_512,(0,5):C.GC_521})

V_144 = Vertex(name = 'V_144',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVV3 ],
               couplings = {(0,0):C.GC_514})

V_145 = Vertex(name = 'V_145',
               particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVSS1, L.VVVVVVSS6, L.VVVVVVSS7 ],
               couplings = {(0,2):C.GC_148,(0,1):C.GC_161,(0,0):C.GC_144})

V_146 = Vertex(name = 'V_146',
               particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVS1, L.VVVVVVS6, L.VVVVVVS7 ],
               couplings = {(0,2):C.GC_441,(0,1):C.GC_454,(0,0):C.GC_437})

V_147 = Vertex(name = 'V_147',
               particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV1, L.VVVVVV16, L.VVVVVV26, L.VVVVVV27, L.VVVVVV39, L.VVVVVV40, L.VVVVVV54, L.VVVVVV66, L.VVVVVV8 ],
               couplings = {(0,5):C.GC_39,(0,7):C.GC_48,(0,6):C.GC_57,(0,0):C.GC_189,(0,1):C.GC_191,(0,3):C.GC_526,(0,2):C.GC_539,(0,8):C.GC_522,(0,4):C.GC_187})

V_148 = Vertex(name = 'V_148',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVSS17, L.VVVVVSS18, L.VVVVVSS19, L.VVVVVSS20, L.VVVVVSS28 ],
               couplings = {(0,3):C.GC_115,(0,1):C.GC_117,(0,4):C.GC_123,(0,0):C.GC_218,(0,2):C.GC_152})

V_149 = Vertex(name = 'V_149',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVSS19 ],
               couplings = {(0,0):C.GC_155})

V_150 = Vertex(name = 'V_150',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS17, L.VVVVVS18, L.VVVVVS19, L.VVVVVS20, L.VVVVVS28 ],
               couplings = {(0,3):C.GC_422,(0,1):C.GC_424,(0,4):C.GC_430,(0,0):C.GC_473,(0,2):C.GC_445})

V_151 = Vertex(name = 'V_151',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS19 ],
               couplings = {(0,0):C.GC_448})

V_152 = Vertex(name = 'V_152',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV28, L.VVVVV29, L.VVVVV30, L.VVVVV31, L.VVVVV39, L.VVVVV42, L.VVVVV47, L.VVVVV56 ],
               couplings = {(0,6):C.GC_233,(0,7):C.GC_227,(0,5):C.GC_221,(0,3):C.GC_508,(0,1):C.GC_510,(0,4):C.GC_516,(0,0):C.GC_555,(0,2):C.GC_530})

V_153 = Vertex(name = 'V_153',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV30 ],
               couplings = {(0,0):C.GC_533})

V_154 = Vertex(name = 'V_154',
               particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVSS12 ],
               couplings = {(0,0):C.GC_97})

V_155 = Vertex(name = 'V_155',
               particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVSS12 ],
               couplings = {(0,0):C.GC_99})

V_156 = Vertex(name = 'V_156',
               particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVSS12 ],
               couplings = {(0,0):C.GC_101})

V_157 = Vertex(name = 'V_157',
               particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVS12 ],
               couplings = {(0,0):C.GC_413})

V_158 = Vertex(name = 'V_158',
               particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVS12 ],
               couplings = {(0,0):C.GC_415})

V_159 = Vertex(name = 'V_159',
               particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVS12 ],
               couplings = {(0,0):C.GC_417})

V_160 = Vertex(name = 'V_160',
               particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV19, L.VVVVVV32, L.VVVVVV45, L.VVVVVV53 ],
               couplings = {(0,3):C.GC_180,(0,0):C.GC_173,(0,2):C.GC_166,(0,1):C.GC_499})

V_161 = Vertex(name = 'V_161',
               particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV32 ],
               couplings = {(0,0):C.GC_501})

V_162 = Vertex(name = 'V_162',
               particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV32 ],
               couplings = {(0,0):C.GC_503})

V_163 = Vertex(name = 'V_163',
               particles = [ P.a, P.a, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS11, L.VVVVSS3 ],
               couplings = {(0,1):C.GC_385,(0,0):C.GC_384})

V_164 = Vertex(name = 'V_164',
               particles = [ P.a, P.a, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS11, L.VVVVSS3 ],
               couplings = {(0,1):C.GC_361,(0,0):C.GC_360})

V_165 = Vertex(name = 'V_165',
               particles = [ P.a, P.a, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS11, L.VVVVSS3 ],
               couplings = {(0,1):C.GC_390,(0,0):C.GC_373})

V_166 = Vertex(name = 'V_166',
               particles = [ P.a, P.a, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS3 ],
               couplings = {(0,0):C.GC_376})

V_167 = Vertex(name = 'V_167',
               particles = [ P.a, P.a, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS10, L.VVVVS3 ],
               couplings = {(0,1):C.GC_618,(0,0):C.GC_617})

V_168 = Vertex(name = 'V_168',
               particles = [ P.a, P.a, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS10, L.VVVVS3 ],
               couplings = {(0,1):C.GC_602,(0,0):C.GC_601})

V_169 = Vertex(name = 'V_169',
               particles = [ P.a, P.a, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS10, L.VVVVS3 ],
               couplings = {(0,1):C.GC_623,(0,0):C.GC_612})

V_170 = Vertex(name = 'V_170',
               particles = [ P.a, P.a, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS3 ],
               couplings = {(0,0):C.GC_615})

V_171 = Vertex(name = 'V_171',
               particles = [ P.a, P.a, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV16, L.VVVV35, L.VVVV36, L.VVVV37, L.VVVV38, L.VVVV40, L.VVVV41, L.VVVV5, L.VVVV7 ],
               couplings = {(0,8):C.GC_395,(0,5):C.GC_306,(0,6):C.GC_323,(0,3):C.GC_314,(0,1):C.GC_328,(0,2):C.GC_396,(0,4):C.GC_394,(0,7):C.GC_670,(0,0):C.GC_669})

V_172 = Vertex(name = 'V_172',
               particles = [ P.a, P.a, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV16, L.VVVV37, L.VVVV40, L.VVVV5, L.VVVV7 ],
               couplings = {(0,4):C.GC_318,(0,2):C.GC_310,(0,1):C.GC_333,(0,3):C.GC_654,(0,0):C.GC_653})

V_173 = Vertex(name = 'V_173',
               particles = [ P.a, P.a, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV16, L.VVVV40, L.VVVV5 ],
               couplings = {(0,1):C.GC_332,(0,2):C.GC_675,(0,0):C.GC_664})

V_174 = Vertex(name = 'V_174',
               particles = [ P.a, P.a, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV5 ],
               couplings = {(0,0):C.GC_667})

V_175 = Vertex(name = 'V_175',
               particles = [ P.a, P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS12, L.VVVVSS17 ],
               couplings = {(0,1):C.GC_389,(0,0):C.GC_388})

V_176 = Vertex(name = 'V_176',
               particles = [ P.a, P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS12, L.VVVVSS17 ],
               couplings = {(0,1):C.GC_370,(0,0):C.GC_369})

V_177 = Vertex(name = 'V_177',
               particles = [ P.a, P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS12, L.VVVVSS17 ],
               couplings = {(0,1):C.GC_372,(0,0):C.GC_371})

V_178 = Vertex(name = 'V_178',
               particles = [ P.a, P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVSS17 ],
               couplings = {(0,0):C.GC_377})

V_179 = Vertex(name = 'V_179',
               particles = [ P.a, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS11, L.VVVVS15 ],
               couplings = {(0,1):C.GC_622,(0,0):C.GC_621})

V_180 = Vertex(name = 'V_180',
               particles = [ P.a, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS11, L.VVVVS15 ],
               couplings = {(0,1):C.GC_609,(0,0):C.GC_608})

V_181 = Vertex(name = 'V_181',
               particles = [ P.a, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS11, L.VVVVS15 ],
               couplings = {(0,1):C.GC_611,(0,0):C.GC_610})

V_182 = Vertex(name = 'V_182',
               particles = [ P.a, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVS15 ],
               couplings = {(0,0):C.GC_616})

V_183 = Vertex(name = 'V_183',
               particles = [ P.a, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV17, L.VVVV23, L.VVVV37, L.VVVV40 ],
               couplings = {(0,3):C.GC_269,(0,2):C.GC_277,(0,1):C.GC_674,(0,0):C.GC_673})

V_184 = Vertex(name = 'V_184',
               particles = [ P.a, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV17, L.VVVV23, L.VVVV37, L.VVVV40 ],
               couplings = {(0,3):C.GC_273,(0,2):C.GC_383,(0,1):C.GC_661,(0,0):C.GC_660})

V_185 = Vertex(name = 'V_185',
               particles = [ P.a, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV17, L.VVVV23, L.VVVV37, L.VVVV40 ],
               couplings = {(0,3):C.GC_379,(0,2):C.GC_338,(0,1):C.GC_663,(0,0):C.GC_662})

V_186 = Vertex(name = 'V_186',
               particles = [ P.a, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV23, L.VVVV40 ],
               couplings = {(0,1):C.GC_381,(0,0):C.GC_668})

V_187 = Vertex(name = 'V_187',
               particles = [ P.a, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV40 ],
               couplings = {(0,0):C.GC_337})

V_188 = Vertex(name = 'V_188',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVSS10, L.VVVVVSS11, L.VVVVVSS15, L.VVVVVSS2, L.VVVVVSS4, L.VVVVVSS5, L.VVVVVSS6, L.VVVVVSS7, L.VVVVVSS8, L.VVVVVSS9 ],
               couplings = {(0,3):C.GC_358,(0,1):C.GC_29,(0,0):C.GC_160,(0,6):C.GC_120,(0,4):C.GC_122,(0,5):C.GC_211,(0,8):C.GC_215,(0,9):C.GC_263,(0,7):C.GC_259,(0,2):C.GC_354})

V_189 = Vertex(name = 'V_189',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVSS2 ],
               couplings = {(0,0):C.GC_304})

V_190 = Vertex(name = 'V_190',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS10, L.VVVVVS11, L.VVVVVS15, L.VVVVVS2, L.VVVVVS4, L.VVVVVS5, L.VVVVVS6, L.VVVVVS7, L.VVVVVS8, L.VVVVVS9 ],
               couplings = {(0,3):C.GC_599,(0,1):C.GC_410,(0,0):C.GC_453,(0,6):C.GC_427,(0,4):C.GC_429,(0,5):C.GC_466,(0,8):C.GC_470,(0,9):C.GC_479,(0,7):C.GC_477,(0,2):C.GC_595})

V_191 = Vertex(name = 'V_191',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS2 ],
               couplings = {(0,0):C.GC_486})

V_192 = Vertex(name = 'V_192',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV12, L.VVVVV13, L.VVVVV14, L.VVVVV15, L.VVVVV16, L.VVVVV17, L.VVVVV18, L.VVVVV19, L.VVVVV20, L.VVVVV21, L.VVVVV26, L.VVVVV4, L.VVVVV45, L.VVVVV5, L.VVVVV50, L.VVVVV51, L.VVVVV59, L.VVVVV60, L.VVVVV8 ],
               couplings = {(0,15):C.GC_56,(0,12):C.GC_73,(0,9):C.GC_47,(0,8):C.GC_68,(0,14):C.GC_330,(0,17):C.GC_38,(0,16):C.GC_320,(0,18):C.GC_325,(0,11):C.GC_63,(0,13):C.GC_651,(0,5):C.GC_497,(0,4):C.GC_538,(0,2):C.GC_513,(0,0):C.GC_515,(0,1):C.GC_550,(0,6):C.GC_553,(0,7):C.GC_561,(0,3):C.GC_559,(0,10):C.GC_647})

V_193 = Vertex(name = 'V_193',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV5 ],
               couplings = {(0,0):C.GC_567})

V_194 = Vertex(name = 'V_194',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVSS2, L.VVVVVVSS5 ],
               couplings = {(0,0):C.GC_359,(0,1):C.GC_355})

V_195 = Vertex(name = 'V_195',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVSS2 ],
               couplings = {(0,0):C.GC_365})

V_196 = Vertex(name = 'V_196',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVS2, L.VVVVVVS5 ],
               couplings = {(0,0):C.GC_600,(0,1):C.GC_596})

V_197 = Vertex(name = 'V_197',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVS2 ],
               couplings = {(0,0):C.GC_604})

V_198 = Vertex(name = 'V_198',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV1, L.VVVVVV14, L.VVVVVV15, L.VVVVVV16, L.VVVVVV23, L.VVVVVV25, L.VVVVVV39, L.VVVVVV49, L.VVVVVV5, L.VVVVVV50, L.VVVVVV62, L.VVVVVV64, L.VVVVVV7, L.VVVVVV9 ],
               couplings = {(0,1):C.GC_49,(0,0):C.GC_190,(0,9):C.GC_58,(0,7):C.GC_77,(0,11):C.GC_40,(0,10):C.GC_321,(0,2):C.GC_71,(0,4):C.GC_331,(0,12):C.GC_326,(0,3):C.GC_192,(0,8):C.GC_66,(0,13):C.GC_652,(0,6):C.GC_188,(0,5):C.GC_648})

V_199 = Vertex(name = 'V_199',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV9 ],
               couplings = {(0,0):C.GC_656})

V_200 = Vertex(name = 'V_200',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVSS14, L.VVVVVSS16, L.VVVVVSS21, L.VVVVVSS22, L.VVVVVSS23, L.VVVVVSS24, L.VVVVVSS25, L.VVVVVSS26, L.VVVVVSS27 ],
               couplings = {(0,5):C.GC_20,(0,3):C.GC_347,(0,6):C.GC_124,(0,7):C.GC_153,(0,4):C.GC_156,(0,8):C.GC_219,(0,2):C.GC_301,(0,1):C.GC_345,(0,0):C.GC_300})

V_201 = Vertex(name = 'V_201',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVSS22, L.VVVVVSS24 ],
               couplings = {(0,1):C.GC_23,(0,0):C.GC_267})

V_202 = Vertex(name = 'V_202',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS14, L.VVVVVS16, L.VVVVVS21, L.VVVVVS22, L.VVVVVS23, L.VVVVVS24, L.VVVVVS25, L.VVVVVS26, L.VVVVVS27 ],
               couplings = {(0,5):C.GC_403,(0,3):C.GC_588,(0,6):C.GC_431,(0,7):C.GC_446,(0,4):C.GC_449,(0,8):C.GC_474,(0,2):C.GC_484,(0,1):C.GC_586,(0,0):C.GC_483})

V_203 = Vertex(name = 'V_203',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS22, L.VVVVVS24 ],
               couplings = {(0,1):C.GC_406,(0,0):C.GC_482})

V_204 = Vertex(name = 'V_204',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV25, L.VVVVV27, L.VVVVV32, L.VVVVV33, L.VVVVV34, L.VVVVV35, L.VVVVV36, L.VVVVV37, L.VVVVV38, L.VVVVV53, L.VVVVV57, L.VVVVV61 ],
               couplings = {(0,11):C.GC_222,(0,9):C.GC_234,(0,10):C.GC_228,(0,5):C.GC_492,(0,3):C.GC_641,(0,6):C.GC_517,(0,7):C.GC_531,(0,4):C.GC_534,(0,8):C.GC_556,(0,2):C.GC_565,(0,1):C.GC_639,(0,0):C.GC_564})

V_205 = Vertex(name = 'V_205',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV33, L.VVVVV35, L.VVVVV53, L.VVVVV57, L.VVVVV61 ],
               couplings = {(0,4):C.GC_281,(0,2):C.GC_290,(0,3):C.GC_287,(0,1):C.GC_494,(0,0):C.GC_563})

V_206 = Vertex(name = 'V_206',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVSS10, L.VVVVVVSS16, L.VVVVVVSS2, L.VVVVVVSS5, L.VVVVVVSS8, L.VVVVVVSS9 ],
               couplings = {(0,2):C.GC_87,(0,5):C.GC_100,(0,4):C.GC_102,(0,0):C.GC_162,(0,1):C.GC_98,(0,3):C.GC_85})

V_207 = Vertex(name = 'V_207',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVSS2 ],
               couplings = {(0,0):C.GC_30})

V_208 = Vertex(name = 'V_208',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVS10, L.VVVVVVS16, L.VVVVVVS2, L.VVVVVVS5, L.VVVVVVS8, L.VVVVVVS9 ],
               couplings = {(0,2):C.GC_576,(0,5):C.GC_416,(0,4):C.GC_418,(0,0):C.GC_455,(0,1):C.GC_414,(0,3):C.GC_574})

V_209 = Vertex(name = 'V_209',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVS2 ],
               couplings = {(0,0):C.GC_411})

V_210 = Vertex(name = 'V_210',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV23, L.VVVVVV25, L.VVVVVV28, L.VVVVVV29, L.VVVVVV30, L.VVVVVV36, L.VVVVVV42, L.VVVVVV62, L.VVVVVV63, L.VVVVVV67, L.VVVVVV7, L.VVVVVV9 ],
               couplings = {(0,8):C.GC_167,(0,9):C.GC_174,(0,6):C.GC_181,(0,7):C.GC_64,(0,0):C.GC_75,(0,10):C.GC_70,(0,11):C.GC_629,(0,3):C.GC_502,(0,2):C.GC_504,(0,4):C.GC_540,(0,5):C.GC_500,(0,1):C.GC_627})

V_211 = Vertex(name = 'V_211',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV9 ],
               couplings = {(0,0):C.GC_498})

V_212 = Vertex(name = 'V_212',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVSS11, L.VVVVVVSS14, L.VVVVVVSS15, L.VVVVVVSS3 ],
               couplings = {(0,2):C.GC_116,(0,3):C.GC_118,(0,0):C.GC_125,(0,1):C.GC_220})

V_213 = Vertex(name = 'V_213',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVS11, L.VVVVVVS14, L.VVVVVVS15, L.VVVVVVS3 ],
               couplings = {(0,2):C.GC_423,(0,3):C.GC_425,(0,0):C.GC_432,(0,1):C.GC_475})

V_214 = Vertex(name = 'V_214',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV10, L.VVVVVV12, L.VVVVVV3, L.VVVVVV31, L.VVVVVV34, L.VVVVVV35, L.VVVVVV44, L.VVVVVV48, L.VVVVVV57, L.VVVVVV61 ],
               couplings = {(0,9):C.GC_229,(0,8):C.GC_235,(0,7):C.GC_247,(0,6):C.GC_223,(0,0):C.GC_244,(0,2):C.GC_240,(0,5):C.GC_509,(0,1):C.GC_511,(0,3):C.GC_518,(0,4):C.GC_557})

V_215 = Vertex(name = 'V_215',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVSS13 ],
               couplings = {(0,0):C.GC_346})

V_216 = Vertex(name = 'V_216',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVSS13 ],
               couplings = {(0,0):C.GC_348})

V_217 = Vertex(name = 'V_217',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVSS13 ],
               couplings = {(0,0):C.GC_350})

V_218 = Vertex(name = 'V_218',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVS13 ],
               couplings = {(0,0):C.GC_587})

V_219 = Vertex(name = 'V_219',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVS13 ],
               couplings = {(0,0):C.GC_589})

V_220 = Vertex(name = 'V_220',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVS13 ],
               couplings = {(0,0):C.GC_591})

V_221 = Vertex(name = 'V_221',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV11, L.VVVVVV13, L.VVVVVV20, L.VVVVVV21, L.VVVVVV33, L.VVVVVV47, L.VVVVVV55, L.VVVVVV56, L.VVVVVV59, L.VVVVVV60 ],
               couplings = {(0,6):C.GC_236,(0,5):C.GC_249,(0,7):C.GC_293,(0,9):C.GC_224,(0,8):C.GC_284,(0,2):C.GC_230,(0,0):C.GC_245,(0,3):C.GC_288,(0,1):C.GC_241,(0,4):C.GC_640})

V_222 = Vertex(name = 'V_222',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV33 ],
               couplings = {(0,0):C.GC_642})

V_223 = Vertex(name = 'V_223',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV33 ],
               couplings = {(0,0):C.GC_644})

V_224 = Vertex(name = 'V_224',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVSS4 ],
               couplings = {(0,0):C.GC_86})

V_225 = Vertex(name = 'V_225',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVSS4 ],
               couplings = {(0,0):C.GC_88})

V_226 = Vertex(name = 'V_226',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVSS4 ],
               couplings = {(0,0):C.GC_91})

V_227 = Vertex(name = 'V_227',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVS4 ],
               couplings = {(0,0):C.GC_575})

V_228 = Vertex(name = 'V_228',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVS4 ],
               couplings = {(0,0):C.GC_577})

V_229 = Vertex(name = 'V_229',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVS4 ],
               couplings = {(0,0):C.GC_580})

V_230 = Vertex(name = 'V_230',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV22, L.VVVVVV24, L.VVVVVV58, L.VVVVVV65 ],
               couplings = {(0,0):C.GC_71,(0,2):C.GC_76,(0,3):C.GC_65,(0,1):C.GC_628})

V_231 = Vertex(name = 'V_231',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV22, L.VVVVVV24, L.VVVVVV58, L.VVVVVV65 ],
               couplings = {(0,0):C.GC_175,(0,2):C.GC_182,(0,3):C.GC_168,(0,1):C.GC_630})

V_232 = Vertex(name = 'V_232',
               particles = [ P.W__minus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV24 ],
               couplings = {(0,0):C.GC_633})

V_233 = Vertex(name = 'V_233',
               particles = [ P.a, P.W__minus__, P.W__plus__, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVS1, L.VVVS5, L.VVVS6 ],
               couplings = {(0,1):C.GC_407,(0,2):C.GC_467,(0,0):C.GC_463})

V_234 = Vertex(name = 'V_234',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.H, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVSS12, L.VVVVVSS13, L.VVVVVSS31 ],
               couplings = {(0,1):C.GC_90,(0,2):C.GC_349,(0,0):C.GC_89})

V_235 = Vertex(name = 'V_235',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z, P.H ],
               color = [ '1' ],
               lorentz = [ L.VVVVVS12, L.VVVVVS13, L.VVVVVS31 ],
               couplings = {(0,1):C.GC_579,(0,2):C.GC_590,(0,0):C.GC_578})

V_236 = Vertex(name = 'V_236',
               particles = [ P.a, P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVV1, L.VVVVV10, L.VVVVV11, L.VVVVV2, L.VVVVV22, L.VVVVV23, L.VVVVV24, L.VVVVV44, L.VVVVV48, L.VVVVV49, L.VVVVV54, L.VVVVV55 ],
               couplings = {(0,7):C.GC_246,(0,8):C.GC_278,(0,9):C.GC_291,(0,10):C.GC_274,(0,11):C.GC_286,(0,0):C.GC_243,(0,2):C.GC_270,(0,3):C.GC_282,(0,6):C.GC_632,(0,4):C.GC_643,(0,1):C.GC_239,(0,5):C.GC_631})

V_237 = Vertex(name = 'V_237',
               particles = [ P.a, P.a, P.a, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV37, L.VVVV40 ],
               couplings = {(0,1):C.GC_79,(0,0):C.GC_80})

V_238 = Vertex(name = 'V_238',
               particles = [ P.a, P.a, P.a, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV37, L.VVVV40 ],
               couplings = {(0,1):C.GC_319,(0,0):C.GC_329})

V_239 = Vertex(name = 'V_239',
               particles = [ P.a, P.a, P.a, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV37, L.VVVV40 ],
               couplings = {(0,1):C.GC_324,(0,0):C.GC_341})

V_240 = Vertex(name = 'V_240',
               particles = [ P.a, P.a, P.a, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV40 ],
               couplings = {(0,0):C.GC_339})

V_241 = Vertex(name = 'V_241',
               particles = [ P.a, P.a, P.a, P.a ],
               color = [ '1' ],
               lorentz = [ L.VVVV40 ],
               couplings = {(0,0):C.GC_340})

V_242 = Vertex(name = 'V_242',
               particles = [ P.a, P.a, P.a, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV37, L.VVVV40 ],
               couplings = {(0,1):C.GC_378,(0,0):C.GC_382})

V_243 = Vertex(name = 'V_243',
               particles = [ P.a, P.a, P.a, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV37, L.VVVV40 ],
               couplings = {(0,1):C.GC_380,(0,0):C.GC_295})

V_244 = Vertex(name = 'V_244',
               particles = [ P.a, P.a, P.a, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV37, L.VVVV40 ],
               couplings = {(0,1):C.GC_294,(0,0):C.GC_336})

V_245 = Vertex(name = 'V_245',
               particles = [ P.a, P.a, P.a, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV40 ],
               couplings = {(0,0):C.GC_334})

V_246 = Vertex(name = 'V_246',
               particles = [ P.a, P.a, P.a, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVV40 ],
               couplings = {(0,0):C.GC_335})

V_247 = Vertex(name = 'V_247',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVV43, L.VVVVV46, L.VVVVV7 ],
               couplings = {(0,1):C.GC_74,(0,2):C.GC_69,(0,0):C.GC_62})

V_248 = Vertex(name = 'V_248',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVV43, L.VVVVV46, L.VVVVV7 ],
               couplings = {(0,1):C.GC_315,(0,2):C.GC_311,(0,0):C.GC_307})

V_249 = Vertex(name = 'V_249',
               particles = [ P.a, P.a, P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV43, L.VVVVVV46, L.VVVVVV6 ],
               couplings = {(0,2):C.GC_71,(0,0):C.GC_78,(0,1):C.GC_65})

V_250 = Vertex(name = 'V_250',
               particles = [ P.a, P.a, P.a, P.a, P.W__minus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV43, L.VVVVVV46, L.VVVVVV6 ],
               couplings = {(0,2):C.GC_312,(0,0):C.GC_316,(0,1):C.GC_308})

V_251 = Vertex(name = 'V_251',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVV17, L.VVVVVV18, L.VVVVVV2, L.VVVVVV37, L.VVVVVV38, L.VVVVVV4, L.VVVVVV41, L.VVVVVV51, L.VVVVVV52 ],
               couplings = {(0,2):C.GC_245,(0,0):C.GC_275,(0,6):C.GC_248,(0,7):C.GC_279,(0,8):C.GC_292,(0,1):C.GC_288,(0,3):C.GC_271,(0,5):C.GC_283,(0,4):C.GC_242})

V_252 = Vertex(name = 'V_252',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVV1, L.VVVVVVV11, L.VVVVVVV17 ],
               couplings = {(0,0):C.GC_41,(0,2):C.GC_59,(0,1):C.GC_50})

V_253 = Vertex(name = 'V_253',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVV3, L.VVVVVVV4, L.VVVVVVV8 ],
               couplings = {(0,0):C.GC_176,(0,1):C.GC_183,(0,2):C.GC_169})

V_254 = Vertex(name = 'V_254',
               particles = [ P.a, P.a, P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVVV17, L.VVVVVVVV2, L.VVVVVVVV24 ],
               couplings = {(0,1):C.GC_42,(0,2):C.GC_51,(0,0):C.GC_60})

V_255 = Vertex(name = 'V_255',
               particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVV12, L.VVVVVVV13, L.VVVVVVV6 ],
               couplings = {(0,0):C.GC_231,(0,1):C.GC_237,(0,2):C.GC_225})

V_256 = Vertex(name = 'V_256',
               particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVVV16, L.VVVVVVVV22, L.VVVVVVVV4 ],
               couplings = {(0,2):C.GC_178,(0,0):C.GC_185,(0,1):C.GC_171})

V_257 = Vertex(name = 'V_257',
               particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVV10, L.VVVVVVV16, L.VVVVVVV18 ],
               couplings = {(0,1):C.GC_126,(0,2):C.GC_134,(0,0):C.GC_130})

V_258 = Vertex(name = 'V_258',
               particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVVV21 ],
               couplings = {(0,0):C.GC_106})

V_259 = Vertex(name = 'V_259',
               particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVVV21 ],
               couplings = {(0,0):C.GC_109})

V_260 = Vertex(name = 'V_260',
               particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.W__plus__ ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVVV21 ],
               couplings = {(0,0):C.GC_112})

V_261 = Vertex(name = 'V_261',
               particles = [ P.a, P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVVV12, L.VVVVVVVV14, L.VVVVVVVV7 ],
               couplings = {(0,2):C.GC_232,(0,1):C.GC_238,(0,0):C.GC_226})

V_262 = Vertex(name = 'V_262',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVV2, L.VVVVVVV5, L.VVVVVVV7 ],
               couplings = {(0,0):C.GC_170,(0,1):C.GC_177,(0,2):C.GC_184})

V_263 = Vertex(name = 'V_263',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVVV10, L.VVVVVVVV18, L.VVVVVVVV6 ],
               couplings = {(0,2):C.GC_128,(0,0):C.GC_136,(0,1):C.GC_132})

V_264 = Vertex(name = 'V_264',
               particles = [ P.a, P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVVV15, L.VVVVVVVV3, L.VVVVVVVV9 ],
               couplings = {(0,1):C.GC_172,(0,0):C.GC_179,(0,2):C.GC_186})

V_265 = Vertex(name = 'V_265',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVV14, L.VVVVVVV15, L.VVVVVVV9 ],
               couplings = {(0,0):C.GC_131,(0,1):C.GC_135,(0,2):C.GC_127})

V_266 = Vertex(name = 'V_266',
               particles = [ P.W__minus__, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.W__plus__, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVVV1, L.VVVVVVVV19, L.VVVVVVVV25 ],
               couplings = {(0,0):C.GC_110,(0,1):C.GC_113,(0,2):C.GC_107})

V_267 = Vertex(name = 'V_267',
               particles = [ P.a, P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVVV11, L.VVVVVVVV13, L.VVVVVVVV8 ],
               couplings = {(0,2):C.GC_133,(0,1):C.GC_137,(0,0):C.GC_129})

V_268 = Vertex(name = 'V_268',
               particles = [ P.W__minus__, P.W__minus__, P.W__plus__, P.W__plus__, P.Z, P.Z, P.Z, P.Z ],
               color = [ '1' ],
               lorentz = [ L.VVVVVVVV20, L.VVVVVVVV23, L.VVVVVVVV5 ],
               couplings = {(0,2):C.GC_108,(0,1):C.GC_111,(0,0):C.GC_114})

