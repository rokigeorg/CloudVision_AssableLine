import argparse

parser = argparse.ArgumentParser(description='Firmware CloudVision:')

parser.add_argument('-d', action='store_const', const=True,
                    help="start software in DEBUG or PRODUCTION mode. Set [-p] for PRODUCTION mode. Fefault is DEBUG mode. ")

args = parser.parse_args()
runMode = args.d

runMode = False if runMode is None else True
print(runMode)
# print(args.accumulate(args.productionMode))
