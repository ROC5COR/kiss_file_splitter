
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <phk@FreeBSD.ORG> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return
# ----------------------------------------------------------------------------

####################### KISS File Splitter #######################
#                         .;&&=.      .;&&s,                                        
#                        ::%%&&&~;   ;::%% ';                                  
#                      _:::%%%  '*\ ;::%%%  ';                               
#                    _;:::%%%%;   *;::%%%%;  ';                              
#                 _;:::::%%%%%;   *:::%%%%%.   '                              
#               _;::::::%%%%%;    *;::%%%%%%%.  '._                           
#             _;:::::%%%%%%;    _*; \::%%%%%%.=~:'                                     
#          _::::::%%%%%%%'   _**:'   '=:=~::%%;~                               
#       .::::%%%%%%%%%%%===***~'    _.-::::%;~                                     
#           ~~_--===--~~~~~~~==+._.+:::%' %:                                                  
#              =;::::::%%%%%%,   *;:::%' .;                                  
#                =;::::::%%%%%%   |::%' .;                                 
#                    ~;::::%%%%% *;::% .'                                  
#                       ~'+%%%P=' '~%P~                                               

import sys
import argparse
import re

parser = argparse.ArgumentParser(description='File splitter')
parser.add_argument('--split', metavar='FILE', type=str,
                    help='File to split')
parser.add_argument('--group', metavar='FILES', type=str,
                    help='List of file to group', nargs='+')

CHUNK_SIZE = 1024*1024*25
args = parser.parse_args()

if args.split:
    part_num = 1
    print(f"Splitting file {args.split} into parts of {CHUNK_SIZE/1024/1024}Mb")
    with open(args.split, 'rb') as f:
        chunk = f.read(CHUNK_SIZE)
        while chunk:
            with open(f"{args.split}_part{part_num}", 'wb') as chunk_file:
                chunk_file.write(chunk)
            part_num += 1
            chunk = f.read(CHUNK_SIZE)

elif args.group:
    n_files = len(args.group)
    output_name = args.group[0] if n_files > 0 else None
    if output_name is None:
        print("No file to group")
        sys.exit(1)
    output_name = re.sub(r'_part[0-9]+$', '',output_name)

    print(f"Grouping files {n_files} into one single file named {output_name}")
    with open(output_name, 'wb') as f:
        for part_file in args.group:
            with open(part_file, 'rb') as part_file:
                f.write(part_file.read())
else:
    print("You have to specify an argument either --split to split file or --group to group part of files together")
print("Have a nice day!")
