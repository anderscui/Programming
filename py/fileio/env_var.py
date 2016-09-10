import os

# Sys var + User var
for p in os.environ['PATH'].split(';'):
    print(p)

print(os.environ['OS'])