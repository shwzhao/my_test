import pandas as pd
import sys
from modules.read_data import read_data, GeneExpressionData

def transpose(args):
    data = read_data(args)
    geneexpressiondata = GeneExpressionData(data)
    data_transposed =  geneexpressiondata.transpose()

    if args.output:
        output = args.output
    else:
        output = sys.stdout

    data_transposed.to_csv(output, index=False, sep="\t")
