import pandas as pd
import sys
from modules.read_data import read_data, GeneExpressionData

def wider(args):
    data = read_data(args)
    geneexpressiondata = GeneExpressionData(data)
    data_widered =  geneexpressiondata.wider()

    if args.output:
        output = args.output
    else:
        output = sys.stdout

    # data_longered.to_csv(output, index=False, sep="\t")
    try:
        data_widered.to_csv(output, index=False, sep="\t")
    except BrokenPipeError:
        pass
