import optparse

parser = optparse.OptionParser()

# An option taking an arg
parser.add_option('-o', action='store', dest='outfile')
parser.add_option('--output', action='store', dest='outfile')

# An option that sets a bool flag
parser.add_option('-d', action='store_true', dest='debug')
parser.add_option('--debug', action='store_true', dest='debug')

# Set default val for selected options
parser.set_defaults(debug=False)

# parse cmd line
opts, args = parser.parse_args()

# retrieve the option settings
outfile = opts.outfile
debug_mode = opts.debug

print(outfile)
print(debug_mode)
print(args)