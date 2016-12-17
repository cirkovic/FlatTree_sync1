from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'runFlatTreeMINIAOD_cfg.py'
config.JobType.inputFiles = ['conf.xml', 'Spring16_25nsV6_MC.db', 'Spring16_25nsV6_DATA.db', 'Spring16_25nsV3_DATA.db', 'Spring16_25nsV10All_DATA.db', 'Spring16_25nsV10_MC.db', 'Summer15_25nsV6_MC.db', 'Summer15_25nsV6_DATA.db']

config.Data.inputDataset = '/TT_AntitopLeptonicDecay_TH_1L3B_Eta_Hct/kskovpen-crab_TT_AntitopLeptonicDecay_TH_1L3B_Eta_Hct_-945eeaf2bbc1c170dee4cc02592a5272/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1

config.Site.storageSite = 'T2_HU_Budapest'
