import pandas as pd
import sys
from modules.read_data import read_data, GeneExpressionData

def round(args):
    data = read_data(args)
    geneexpressiondata = GeneExpressionData(data)
    data_rounded =  geneexpressiondata.round(digit=args.digit)

    if args.output:
        output = args.output
    else:
        output = sys.stdout

    try:
        data_rounded.to_csv(output, index=False, sep="\t")
    except BrokenPipeError:
        pass
