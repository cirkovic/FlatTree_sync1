from FlatTree.FlatTreeProducer.ConfFile_MINIAOD_Data_cfg import *
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10000) )
process.source = cms.Source ("PoolSource",
                        fileNames=cms.untracked.vstring('/store/data/Run2016D/SingleMuon/MINIAOD/PromptReco-v2/000/276/315/00000/168C3DE5-F444-E611-A012-02163E014230.root'),
                        skipEvents=cms.untracked.uint32(30000)
)

process.TFileService = cms.Service("TFileService", fileName = cms.string("output_3.root"))
