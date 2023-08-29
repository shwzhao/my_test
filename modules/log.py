import pandas as pd
import sys
from modules.read_data import read_data, GeneExpressionData

def log(args):
    data = read_data(args)
    geneexpressiondata = GeneExpressionData(data)
    data_logged =  geneexpressiondata.log(base=args.base)

    if args.output:
        output = args.output
    else:
        output = sys.stdout

    try:
        data_logged.to_csv(output, index=False, sep="\t")
    except BrokenPipeError:
        pass
