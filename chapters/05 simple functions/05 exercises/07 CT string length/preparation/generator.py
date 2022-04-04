import os
import random
import subprocess

# set fixed seed for generating test cases
random.seed(123456789)

# locate evaldir
evaldir = os.path.join('..', 'evaluation')
if not os.path.exists(evaldir):
    os.makedirs(evaldir)

# locate solutiondir
solutiondir = os.path.join('..', 'solution')
if not os.path.exists(solutiondir):
    os.makedirs(solutiondir)

# configuration settings
tab_name = 'Length'
tab_name_translations = {'nl': 'Lengte'}
settings = f'''
tab name: {tab_name}
python input without prompt: true
block count: multi
input block size: 1
output block size: 1
comparison: exact match
'''
for language, translation in tab_name_translations.items():
    settings += f'''<LANGUAGE code="{language}">
    <fixed from="{tab_name}" to="{translation}" detect="false" />
</LANGUAGE>
'''

# generate test data
cases = [
    'And now for something completely different.',
    'My brain hurts!',
    "It's just a flesh wound.",
]

# configure test files
infile = open(os.path.join(evaldir, '0.in'), 'w')
outfile = open(os.path.join(evaldir, '0.out'), 'w')

# generate unit tests
for stdin in cases:

    # add input to input file
    print(stdin, file=infile)

    # generate output to output file
    script = os.path.join(solutiondir, 'solution.en.py')
    process= subprocess.run(
        ['python', script],
        input=stdin,
        encoding='utf-8',
        capture_output=True, shell=True, check=True
    )
    stdout = process.stdout

    # remove prompt from stdout
    stdout = '\n'.join(
        line.split(':', maxsplit=1)[1].lstrip(' ') if ':' in line else line
        for line in stdout.splitlines(keepends=False)
    )

    # add stdout to output file
    print(stdout, file=outfile)

# add settings to output file
print('-' * 60 + settings, file=outfile)