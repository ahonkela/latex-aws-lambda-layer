import tempfile
import subprocess
import base64
import codecs
import boto3

def lambda_handler(event, context):
    
    with tempfile.TemporaryDirectory() as dname:
        fname = dname + '/' + 'hello.tex'
        with codecs.open(fname, 'w', 'utf-8') as f:
            f.write("""% AUTOMATICALLY GENERATED, DO NOT EDIT!
\\documentclass[a4paper,10pt]{article}
\\usepackage[utf8]{inputenc}

\\begin{document}
\\LARGE Hello, AWS!
\\end{document}
    """)
    
        # Run pdflatex...
        r = subprocess.run(["pdflatex",
                        "-output-directory=%s" % (dname,),
                        fname],
                       stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT)
        print(r.stdout.decode('utf_8'))
        # Read "hello.pdf"...
        with open(dname + '/' + "hello.pdf", "rb") as f:
            pdf = f.read()

    # Return base64 encoded pdf and stdout log from pdflaxex...
    return {
        "output": base64.b64encode(pdf).decode('ascii'),
        "stdout": r.stdout.decode('utf_8')
    }
