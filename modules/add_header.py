import pandas as pd


def add_header(args):
    '''
    args.groups, args.samples, args.repeats, args.sep, args.index
    '''
    header = []
    for group in args.groups:
        for repeat in args.repeats:
            header.append(group + args.sep + repeat)

    if args.input == "-":
        input = sys.stdin
    else:
        input = args.input

    data = pd.read_csv(input, sep=args.sep, index_col=0, header=header)


    if args.output:
        output = args.output
    else:
        output = sys.stdout

    data.to_csv(output, index=True, sep="\t")
