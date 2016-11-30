from FlatTree.FlatTreeProducer.ConfFile_MINIAOD_Data_cfg import *
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(1000) )
#process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10000) )
process.source = cms.Source ("PoolSource",
                        fileNames=cms.untracked.vstring('/store/data/Run2016D/SingleElectron/MINIAOD/PromptReco-v2/000/276/315/00000/10BB1858-0045-E611-83A5-02163E01456D.root'),
                        skipEvents=cms.untracked.uint32(50000)
)

process.TFileService = cms.Service("TFileService", fileName = cms.string("output_5.root"))
