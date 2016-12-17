from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

#config.General.requestName = 'FCNC_MC_analysis_TTbar_Hct_1'
config.General.workArea = 'crab_projects'
#config.General.transferOutputs = True
#config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
#config.JobType.psetName = 'runFlatTreeMINIAOD_cfg.py'
config.JobType.psetName = 'runFlatTreeMINIAOD_data_cfg.py'
config.JobType.inputFiles = ['conf.xml', 'Spring16_25nsV10_MC.db', 'Spring16_25nsV10All_DATA.db']
#config.JobType.pyCfgParams = ['isData=True']

config.Data.inputDataset = '/SingleElectron/Run2016G-23Sep2016-v1/MINIAOD'
#config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 16
#config.Data.totalUnits = 1
#config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
#config.Data.publication = True
#config.Data.outputDatasetTag = 'CRAB3_tutorial_May2015_MC_analysis'

config.Site.storageSite = 'T2_HU_Budapest'
