import FWCore.ParameterSet.Config as cms

# Input source
#source = cms.Source("LHESource",
#    fileNames = cms.untracked.vstring('file:./Output/MYPROCESS/xsec/Events/run_ISSIGNAL_0_cuts/unweighted_events.lhe') 
#)

generator = cms.EDFilter("Pythia8ConcurrentHadronizerFilter",
    PythiaParameters = cms.PSet(
        parameterSets = cms.vstring(
            'pythia8CommonSettings', 
            'processParameters'
        ),
        processParameters = cms.vstring(
            '24:onMode = off', 
            '24:onIfAny = 13 14', 
            '23:onMode = off', 
            '23:onIfAny = 13 13', 
            '25:onMode = off', 
            '25:onIfAny = 5 5'
        ),
        pythia8CommonSettings = cms.vstring(
            'Tune:preferLHAPDF = 2', 
            'Main:timesAllowErrors = 10000', 
            'Check:epTolErr = 0.01', 
            'Beams:setProductionScalesFromLHEF = off', 
            'SLHA:minMassSM = 1000.', 
            'ParticleDecays:limitTau0 = on', 
            'ParticleDecays:tau0Max = 10', 
            'ParticleDecays:allowPhotonRadiation = on'
        )
    ),
    comEnergy = cms.double(13600.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)

bfilter = cms.EDFilter("MCMultiParticleFilter",
    AcceptMore = cms.bool(True),
    EtaMax = cms.vdouble(2.5),
    NumRequired = cms.int32(MYBJ),
    ParticleID = cms.vint32(5),
    PtMin = cms.vdouble(30.0),
    Status = cms.vint32(0)
)


mufilter = cms.EDFilter("MCMultiParticleFilter",
    AcceptMore = cms.bool(True),
    EtaMax = cms.vdouble(2.5),
    NumRequired = cms.int32(MYLEPT),
    ParticleID = cms.vint32(13),
    PtMin = cms.vdouble(15.0),
    Status = cms.vint32(0)
)

ProductionFilterSequence = cms.Sequence(generator+mufilter+bfilter)
