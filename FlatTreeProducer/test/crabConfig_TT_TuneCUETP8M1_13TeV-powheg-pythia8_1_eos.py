from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.workArea = 'crab_projects'
config.General.transferOutputs=True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runFlatTreeMINIAOD_cfg.py'
config.JobType.inputFiles = ['conf.xml', 'Spring16_25nsV6_MC.db', 'Spring16_25nsV6_DATA.db', 'Spring16_25nsV3_DATA.db', 'Spring16_25nsV10All_DATA.db', 'Spring16_25nsV10_MC.db', 'Summer15_25nsV6_MC.db', 'Summer15_25nsV6_DATA.db']
config.JobType.disableAutomaticOutputCollection = False
config.JobType.outputFiles = [ 'output.root' ]

config.Data.inputDataset = '/TT_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16MiniAODv1-PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext4-v1/MINIAODSIM'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = 1
#config.Data.outLFNDirBase = '/store/caf/user/mdjordje/Cirkovic/FCNC2/TT_TuneCUETP8M1_13TeV-powheg-pythia8'

#config.Site.storageSite = 'T2_HU_Budapest'
#config.Site.storageSite = 'T2_UK_London_IC'
config.Site.storageSite = 'T2_CH_CERN'
#config.Data.outlfn = '/store/user/rkd123/DIRNAME'
config.Data.outLFNDirBase = '/store/caf/user/mdjordje/Cirkovic/FCNC2/TT_TuneCUETP8M1_13TeV-powheg-pythia8'
