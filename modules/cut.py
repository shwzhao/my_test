import pandas as pd
import sys
from modules.read_data import read_data, GeneExpressionData

def cut(args):
    data = read_data(args)
    geneexpressiondata = GeneExpressionData(data)
    data_cutted =  geneexpressiondata.cut(cols=args.fields, others=args.others)

    if args.output:
        output = args.output
    else:
        output = sys.stdout

    try:
        data_cutted.to_csv(output, index=False, sep="\t")
    except BrokenPipeError:
        pass
