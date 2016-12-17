from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'crab_projects'
config.section_('JobType')
config.JobType.psetName = 'runFlatTreeMINIAOD_cfg.py'
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles = ['output.root']
config.section_('Data')
config.Data.inputDataset = '/TT_TuneCUETP8M1_13TeV-powheg-pythia8/RunIISpring16MiniAODv1-PUSpring16_80X_mcRun2_asymptotic_2016_v3_ext4-v1/MINIAODSIM'
config.Data.unitsPerJob = 1000
config.Data.inputDBS = 'global'
config.Data.splitting = 'EventBased'
config.section_('User')
config.section_('Site')
config.Site.storageSite = 'srm-eoscms.cern.ch'
