import os, os.path

#
inputPath = 'midi'
outputPath = 'txt'

inputExtension = '.mid'
outputExtension = '.txt'

command = 'midicsv'

files = list(map(lambda s: s.split('.')[0], os.listdir(inputPath)))
#print(files)

# os.system(command)
for f in files:
    os.system('{0} {2}/{1}{3} {4}/{1}{5}'.format(command, f, inputPath, inputExtension, outputPath, outputExtension))
    #print('{0} {2}/{1}{3} {4}/{1}{5}'.format(command, f, inputPath, inputExtension, outputPath, outputExtension))
