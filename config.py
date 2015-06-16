SNPEFF='java -Xmx24g -jar /usr/local/apps/snpEff/4.1c/snpEff.jar'
SNPSIFT= 'java -Xmx24g -jar /usr/local/apps/snpEff/4.1c/SnpSift.jar'
GENOME= "GRCh37.75"
SNPEFF_CONFIG= '/usr/local/apps/snpEff/4.1c/snpEff.config'
FIRSTANNO= '/data/CCBR/projects/ccbr519/Pipeline/gvcf/vcfAnnFirst_snpEff.py'
FILTERSIFT= "(FILTER='PASS') & ( QUAL >= 20 )"
SELECTDB="SIFT_score,SIFT_pred,Polyphen2_HVAR_score,Polyphen2_HVAR_pred,LRT_score,LRT_pred,GERP++_RS,MutationAssessor_score,MutationAssessor_pred,1000Gp1_AF,1000Gp1_EUR_AF,ESP6500_EA_AF,ESP6500_AA_AF"
DB29= '/data/CCBR/local/lib/snpEff_db/dbNSFP2.9.txt.gz'

