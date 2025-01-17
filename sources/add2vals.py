'''
adjustment the pipeline script : 
    -limitations to the Test stage only .
    - move the script "checkout scm" above of all the stages
    - fixing script exporting the report of stage Test
    - Testing the effectiveness of the CRON expression  on the first minute
    - Testing the effetiveness of the CRON expression on the second time, with a-2 minute interval during source code management checking with scm.
'''

import sys
import calc

argnumbers = len(sys.argv) - 1

if argnumbers == 2 :
    print("")
    print("The result is " + str(calc.add2(str(sys.argv[1]), str(sys.argv[2]))))
    print("")
    sys.exit(0)

if argnumbers != 2 :
    print("")
    print("You entered " + str(argnumbers) + " value/s.")
    print("")
    print("Usage: 'add2vals X Y' where X and Y are individual values.")
    print("       If add2vals is not in your path, usage is './add2vals X Y'.")
    print("       If unbundled, usage is 'python add2vals.py X Y'.")
    print("")
    sys.exit(1)
