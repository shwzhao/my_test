#!/usr/bin/env python3

import argparse
import numpy as np
import pandas as pd

from modules.get_group import get_group
from modules.add_header import add_header
from modules.transpose import transpose
from modules.longer import longer
from modules.wider import wider
from modules.mean import mean
from modules.round import round
from modules.log import log
from modules.cut import cut

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--version", action="version", version="0.0.1")
    parser.add_argument("-i", "--input", help="导入表达矩阵")
    parser.add_argument("-o", "--output", help="输出文件，没设置时，标准输出")
    parser.add_argument("-s", "--sep", default="\t", help="设置分隔符")
    parser.add_argument("-S", "--sample_sep", default="_", help="设置表头中的分隔符")
    # sub_get_group.add_argument("-H", "--header", help="默认有表头")
    parser.add_argument("-r", "--regex", action='store_false', help="表头分隔符是否有正则表达式")

    sub_parser = parser.add_subparsers()

    sub_get_group = sub_parser.add_parser("get_group", parents=[parser], add_help=False)
    sub_get_group.set_defaults(func=get_group)

    sub_add_header = sub_parser.add_parser("add_header")
    sub_add_header.add_argument("-G", "--groups", help="设置分组")
    sub_add_header.add_argument("-R", "--repeats", help="设置分组中的重复")
    sub_add_header.set_defaults(func=add_header)

    sub_transponse = sub_parser.add_parser("T", parents=[parser], add_help=False)
    sub_transponse.set_defaults(func=transpose)

    sub_longer = sub_parser.add_parser("longer", parents=[parser], add_help=False)
    sub_longer.set_defaults(func=longer)

    sub_wider = sub_parser.add_parser("wider", parents=[parser], add_help=False)
    sub_wider.set_defaults(func=wider)

    sub_mean = sub_parser.add_parser("mean", parents=[parser], add_help=False)
    sub_mean.set_defaults(func=mean)

    sub_round = sub_parser.add_parser("round", parents=[parser], add_help=False)
    sub_round.add_argument("-d", "--digit", default=2, help="保留位数")
    sub_round.set_defaults(func=round)

    sub_log = sub_parser.add_parser("log", parents=[parser], add_help=False)
    sub_log.add_argument("-b", "--base", default=np.e, help="底数")
    sub_log.set_defaults(func=log)

    sub_cut = sub_parser.add_parser("cut", parents=[parser], add_help=False)
    sub_cut.add_argument("-f", "--fields", help="输出的列")
    sub_cut.add_argument("--others", action='store_true', help="剩下的列")
    sub_cut.set_defaults(func=cut)

    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    args.func(args)
    # modules_dir = os.path.join(os.path.dirname(__file__), 'modules')
    # sys.path.append(modules_dir)


if __name__ == "__main__":
    main()
