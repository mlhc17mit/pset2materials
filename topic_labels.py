import pandas as pd 
import argparse, os

parser = argparse.ArgumentParser()
parser.add_argument("--topicdoc", required = True, help="directory and file containing topic word distributions from trained LLDA")
parser.add_argument("--labelcsv",required = True,  help="directory and file containing icd_label_ds.csv from pset2 git repo")
parser.add_argument("--outfile",required = True,  help="directory and file name you wish to store the cleaned up output in")
args = parser.parse_args()

output = pd.read_csv(args.topicdoc, sep='\t', header= None)
output.rename(index=str, columns={1: "icd"}, inplace = True)
output['icd'] = output['icd'].str.split('_').str[0]

dx_labels = pd.read_csv(args.labelcsv)
output2 = output.merge(dx_labels, on = 'icd')
assert output2.shape[0] ==output.shape[0]
assert len(output2.icd_desc.unique()) ==len(dx_labels.icd_desc.unique())
output2.columns = ['c1', 'icd', 'c2', 'c3', 'icd_desc']
output2 = output2[['c1', 'icd', 'icd_desc', 'c2', 'c3']]

output2.to_csv(args.outfile, sep='\t',  header=False, index = False) 
