def print_matches(match_text):
    print('Looking for ' + match_text)
    while True:
        line = (yield)
        if match_text in line:
            print(line)


matcher = print_matches('python')
matcher.next()  # advance to the first (yield)
matcher.send('Hello world!')
matcher.send('python is cool')
matcher.close()

##
matchers = [
    print_matches('python'),
    print_matches('guido'),
    print_matches('jython')
]

for m in matchers:
    m.next()

# say we read log lines from a file
logs = ['python is cool', 'guido designed python', 'jython is a dialect of python']

for log in logs:
    for m in matchers:
        m.send(log)

