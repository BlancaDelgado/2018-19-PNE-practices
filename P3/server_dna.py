# Server for performing operations on a sequence: total length, number and percentage of a base.





# --MESSAGE FROM SERVER

# FIRST LINE
# - ALIVE: request is blank
# - ERROR: sequence is not valid (!= A,C,G,T, BUT they can be lower)
# - OK: the sequence is valid

# FOLLOWING LINES
# Corresponding to the lines in the client

# 127.0.0.1