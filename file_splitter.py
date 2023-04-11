
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

CHUNK_SIZE = 1024*1024*25
part_num = 1
print(f"Splitting file {sys.argv[1]} into parts of {CHUNK_SIZE/1024/1024}Mb")
with open(sys.argv[1], 'rb') as f:
    chunk = f.read(CHUNK_SIZE)
    while chunk:
        with open(f"{sys.argv[1]}_part{part_num}", 'wb') as chunk_file:
            chunk_file.write(chunk)
        part_num += 1
        chunk = f.read(CHUNK_SIZE)
