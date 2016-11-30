from FlatTree.FlatTreeProducer.ConfFile_MINIAOD_cfg import *
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(5000) )
process.source = cms.Source ("PoolSource",
                        fileNames=cms.untracked.vstring('/store/mc/RunIISpring16MiniAODv2/TT_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14_ext3-v1/00000/0064B539-803A-E611-BDEA-002590D0B060.root'),
                        skipEvents=cms.untracked.uint32(5000)
)

process.TFileService = cms.Service("TFileService", fileName = cms.string("output_1.root"))
