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

print('\n---------- PROGRAM FOR ANALYSING FRAT1 ----------')
print('SEQUENCE:', frat1, '\n')

# Create a dict ( base : number of that base in seq )
b_dict = {}
for i in 'ACGT':
    num_i = c.count(i)  # obtain num of base
    b_dict[i] = num_i  # add base + num

print(b_dict)


# 1.- Number of bases in gene
num_bases = 0
for i in b_dict:
    num_bases += b_dict[i]

print('· Total number of bases:', num_bases)

# 2.- Number of T bases in gene
print('· Total number of T bases:', b_dict['T'])

# 3.- Most popular base and percentage
max_num = max(b_dict.values())
max_base = []

print(max_base)

# 4.- Percentage of all bases in gene


