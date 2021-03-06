# Python client that connects to the ensemble database (using JSON!)

# USEFUL DATA...
# Ensemble: http://rest.ensembl.org/
# Source for getting a sequence: sequence/id/

import http.client  # client connection
import requests  # request to ensemble
import sys  # system
import termcolor  # for easier analysis

PORT = 80  # every page listens to port 80
SERVER = "http://rest.ensembl.org"


# CONNECT TO ENSEMBLE
conn = http.client.HTTPConnection(SERVER, PORT)


# GET GENE (w/ REST API)
gene = "/sequence/id/ENSG00000165879?"  # FRAT1
r = requests.get(SERVER+gene, headers={"Content-Type": "application/json"})  # obtain seq

frat1_dict = r.json()  # all options
frat1 = frat1_dict['seq']  # only sequence
response = repr(frat1_dict)  # view

print()
termcolor.cprint("Response received: {} {} {response}".format(r.status_code, r.reason, response=response), 'green')

if not r.ok:  # close system when problems
    r.raise_for_status()
    sys.exit()


# -- main program
from P1.Seq import Seq
c = Seq(frat1)  # class w/ commands
bases = 'ACGT'

print('\n------------------- PROGRAM FOR ANALYSING FRAT1 -------------------')
print('SEQUENCE:', frat1, '\n')

# Create a dict ( base : number of that base in seq )
b_dict = {}
for i in bases:
    num_i = c.count(i)  # obtain num of base
    b_dict[i] = num_i  # add base + num


# 1.- NUMBER OF BASES IN GENE
num_bases = 0
for i in b_dict:
    num_bases += b_dict[i]

print('· Total number of bases:', num_bases)

# 2.- NUMBER OF T BASES IN GENE
print('· Total number of T bases:', b_dict['T'])

# 4.1.- CALCULATE PERCENTAGE OF ALL BASES IN GENE
perc_dict = {}
for a in bases:
    num_a = c.count(a)

    try:
        perc_a = int(round((num_a / num_bases) * 100, 0))
    except ZeroDivisionError:
        perc_a = 0

    perc_dict[a] = perc_a

# 3.- MOST POPULAR BASE AND PERCENTAGE
max_num = max(b_dict.values())

max_base = []  # Allow ALL bases that have the max number
for i in bases:
    if b_dict[i] == max_num:

        # Calculate percentage too
        perc_max = "({}%)".format(perc_dict[i])
        max_b_and_p = ' '.join([i, perc_max])
        max_base.append(max_b_and_p)

max_base_msg = ', '.join(max_base)

print('· Most popular base:', max_base_msg)

# 4.2.- PRINT ALL PERCENTAGES
perc_bases = []
for c in bases:
    perc_format = '({}%)'.format(perc_dict[c])
    b_and_p = ' '.join([c, perc_format])
    perc_bases.append(b_and_p)

perc_bases_msg = ', '.join(perc_bases)
print('· Percentages for all bases:', perc_bases_msg)
