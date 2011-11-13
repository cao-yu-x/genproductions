import FWCore.ParameterSet.Config as cms

#source = cms.Source("LHESource",
#    fileNames = cms.untracked.vstring(
#    'file:/nasdata/cmsdata/lhe/fromAlexis/7TeV_tptpbar_550_5.5_run20964_unweighted_events_mgPost.lhe'
#    ),
#    skipEvents=cms.untracked.uint32(0)
#)

from Configuration.Generator.PythiaUEZ2Settings_cfi import *
generator = cms.EDFilter("Pythia6HadronizerFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(0),
    comEnergy = cms.double(7000.0),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring(
            'MSTP(1) = 4',
            'MSEL=8         ! fourth generation (t4) fermions',
			'MWID(8)=2',
            'MSTJ(1)=1       ! Fragmentation/hadronization on or off',
            'MSTP(61)=1      ! Parton showering on or off',
            'PMAS(5,1)=4.8   ! b quark mass', #from Spring11 4000040
            'PMAS(6,1)=172.5 ! t quark mass', #from Spring11 4000040
            'PMAS(25,1)=120.0! h0 masss',
            'PMAS(8,1) = 550.0D0  ! tprime quarks mass',
            'PMAS(8,2) = 5.5D0',
            'PMAS(8,3) = 55.0D0',
 'VCKM(1,1) = 0.97414000D0',
 'VCKM(1,2) = 0.22450000D0',
 'VCKM(1,3) = 0.00420000D0',
 'VCKM(1,4) = 0.02500000D0',
 'VCKM(2,1) = 0.22560000D0',
 'VCKM(2,2) = 0.97170000D0',
 'VCKM(2,3) = 0.04109000D0',
 'VCKM(2,4) = 0.05700000D0',
 'VCKM(3,1) = 0.00100000D0',
 'VCKM(3,2) = 0.06200000D0',
 'VCKM(3,3) = 0.91000000D0',
 'VCKM(3,4) = 0.41000000D0',
 'VCKM(4,1) = 0.01300000D0',
 'VCKM(4,2) = 0.04000000D0',
 'VCKM(4,3) = 0.41000000D0',
 'VCKM(4,4) = 0.91000000D0',
            'MDME(66,1)=0     ! g t4',
            'MDME(67,1)=0     ! gamma t4',
			'MDME(68,1)=0     ! Z0 t4'
			'MDME(69,1)=0     ! W d',
            'MDME(70,1)=0     ! W s',
            'MDME(71,1)=0     ! W b',
            'MDME(72,1)=0     ! W b4',
            'KFDP(73,2)=6     ! defines h0 t (replace t4-default with t)',
            'MDME(73,1)=1     ! h0 t ', 		
            'MDME(74,1)=-1    ! H+ b',
            'MDME(75,1)=-1    ! H+ b4',
            'BRAT(66)  = 0.0D0',
            'BRAT(67)  = 0.0D0',
            'BRAT(68)  = 0.0D0',
            'BRAT(69)  = 0.0D0',
            'BRAT(70)  = 0.0D0',
            'BRAT(71)  = 0.0D0',
            'BRAT(72)  = 0.0D0',
            'BRAT(73)  = 1.0D0',
            'BRAT(74)  = 0.0D0',
            'BRAT(75)  = 0.0D0',
            'MDME(210,1)=1     !H decay into d dbar',
            'MDME(211,1)=1     !H decay into u ubar',
            'MDME(212,1)=1     !H decay into s sbar',
            'MDME(213,1)=1     !H decay into c cbar',
            'MDME(214,1)=1     !H decay into b bbar',
            'MDME(215,1)=1     !H decay into t tbar',
            'MDME(216,1)=-1    !Z decay into b4 b4bar',
            'MDME(217,1)=-1    !Z decay into t4 t4bar',
            'MDME(218,1)=1     !Z decay into e- e+',
            'MDME(219,1)=1     !Z decay into mu- mu+',
            'MDME(220,1)=1     !Z decay into tau- tau+',
            'MDME(221,1)=-1    !Z decay into tau4 tau4bar',
            'MDME(222,1)=1     !H decay into g g',
            'MDME(223,1)=1     !H decay into gamma gamma',
            'MDME(224,1)=1     !H decay into gamma Z0',
            'MDME(225,1)=1     !H decay into Z0 Z0',
            'MDME(226,1)=1     !H decay into W+ W-',									
            'MDME(190,1)=1     !W decay into u dbar',
            'MDME(191,1)=1     !W decay into c dbar',
            'MDME(192,1)=1     !W decay into t dbar',
            'MDME(193,1)=-1    !W decay into t4 dbar',
            'MDME(194,1)=1     !W decay into u sbar',
            'MDME(195,1)=1     !W decay into c sbar',
            'MDME(196,1)=1     !W decay into t sbar',
            'MDME(197,1)=-1    !W decay into t4 sbar',
            'MDME(198,1)=1     !W decay into u bbar',
            'MDME(199,1)=1     !W decay into c bbar',
            'MDME(200,1)=1     !W decay into t bbar',
            'MDME(201,1)=-1    !W decay into t4 bbar',
            'MDME(202,1)=-1    !W decay into u b4bar',
            'MDME(203,1)=-1    !W decay into c b4bar',
            'MDME(204,1)=-1    !W decay into t b4bar',
            'MDME(205,1)=-1    !W decay into t4 b4bar',
            'MDME(206,1)=1     !W decay into e- nu_e',
            'MDME(207,1)=1     !W decay into mu nu_mu',
            'MDME(208,1)=1     !W decay into tau nu_tau',
            'MDME(209,1)=-1    !W decay into tau4 nu_tau4'),
        # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring('pythiaUESettings',
            'processParameters')
    ),
    jetMatching = cms.untracked.PSet(
       scheme = cms.string("Madgraph"),
       mode = cms.string("auto"),       # soup, or "inclusive" / "exclusive"
       MEMAIN_etaclmax = cms.double(5.0),
       MEMAIN_qcut = cms.double(-1),
       MEMAIN_nqmatch = cms.int32(5),
       MEMAIN_minjets = cms.int32(0),
       MEMAIN_maxjets = cms.int32(2),
       MEMAIN_showerkt = cms.double(0),
       MEMAIN_excres = cms.string(''),
       outTree_flag = cms.int32(0)
    )
)

ProductionFilterSequence = cms.Sequence(generator)

