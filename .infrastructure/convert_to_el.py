def make_elisp_commands(rootname):
    fr = open(rootname + ".txt", "r")
    fw = open(rootname + ".el", "w")
    for line in fr.readlines()[::-1]:
        newline = '(kill-new "' + line.strip() + '")\n'
        fw.write(newline)

make_elisp_commands("commands")

