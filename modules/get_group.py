import pandas as pd
import sys
from modules.read_data import GeneExpressionData

def get_group(args):
    if args.input == "-":
        input = sys.stdin
    else:
        input = args.input

    data = pd.read_csv(input, sep=args.sep, index_col=0, header=0)

    geneexpressiondata = GeneExpressionData(data)
    # print(data.columns)
    samples = geneexpressiondata.get_samples()
    groups,repeats = geneexpressiondata.get_groups(sample_sep=args.sample_sep)
    # samples = data.columns.tolist()
    # groups = [re.split(args.sample_sep, sample, 1)[0] for sample in samples]

    group_info = pd.DataFrame({"Samples":samples, "Groups":groups, "Repeats":repeats})

    if args.output:
        output = args.output
    else:
        output = sys.stdout

    group_info.to_csv(output, index=False, sep="\t")
