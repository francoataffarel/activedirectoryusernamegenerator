# !/usr/bin/ python3

import argparse
arg_parser = argparse.ArgumentParser( description = "Gerador de usernames por nome com dois campos" )
arg_parser.add_argument("Arquivo com uma lista de nomes" )
arguments = arg_parser.parse_args()
source = arguments.source_file

usernames = []
count = 0

for line in open(source):
    name = line.lower().split()
    usernames.append(name[0])
    usernames.append(name[0][0] + name[-1])
    usernames.append(name[1] + name[0][0])
    usernames.append(name[-1][0] + name[0])
    usernames.append(name[1])
    usernames.append(name[0]+name[1])
    usernames.append(name[0]+'.'+name[1])
    usernames.append(name[0][0]+'.'+name[1]) 
    rev= (name[0]+name[1]).strip()
    usernames.append(rev[::-1])
    count += 1

for entry in usernames:
    print(entry)
print()
print("Lista de usuários criada em users.txt") 
print()
with open('users.txt', 'w') as f:
    for entry in usernames:
        f.write("%s\n" % entry)
  
