import pandas as pd
import sys
from modules.read_data import read_data, GeneExpressionData

def mean(args):
    data = read_data(args)
    geneexpressiondata = GeneExpressionData(data)
    data_mean =  geneexpressiondata.mean(sample_sep=args.sample_sep)

    if args.output:
        output = args.output
    else:
        output = sys.stdout

    try:
        data_mean.to_csv(output, index=False, sep="\t")
    except BrokenPipeError:
        pass
