#!/usr/bin/env python2

from argparse import ArgumentParser
from pyfiglet import figlet_format
from os import system
from time import sleep
import sys


defaultSecs = .5

######################################################
######################################################
##################### ARG PARSER #####################
######################################################
######################################################


class ParseArgument(ArgumentParser):
    
    
    def parse_error(self, message):
        os.stderr.write("Error:  %s\n" % message)
        self.print_help()
        exit(2)
        
        
def parse_arguments():
    '''
        Input - None
        Output - Command line argument list from ParseArgument object
    '''
    # Parser object
    parser = ParseArgument()
    
    # Command line arguments
    parser.add_argument("-m", "--message", required = True, action = "store", help = "Print this message to the screen")
    parser.add_argument("-d", "--delay", required = False, action = "store", help = "Number of milliseconds to delay between letters (default: {})".format(defaultSecs))
    
    # List of arguments from the command line
    args = parser.parse_args()
    
    return args


######################################################
######################################################
################## HELPER FUNCTIONS ##################
######################################################
######################################################


######################################################
######################################################
######################## MAIN ########################
######################################################
######################################################


def main():
    ### PARSE XRANDO ARGUMENTS ###
    args = parse_arguments()
    # print("Args:\t{}".format(args))  # DEBUGGING

    ### LOCAL VARIABLES ###
    secs = 0.0  # Number of milliseconds to delay between letters

    ### INPUT VALIDATION ###
    if not isinstance(args.message, str):
        raise TypeError("-m argument was not a string")
    elif args.message.__len__() == 0:
        raise ValueError("-m argument was empty")
    else:
        if args.delay:
            try:
                secs = float(args.delay)
            except ValueError as err:
                print("Error converting -d argument:\t{}".format(err))
                raise err
            except Exception as err:
                print("Unknown error while converting -d argument:\t{}".format(err))
                raise err
            else:
                # print("secs:\t{}".format(secs))  # DEBUGGING
                pass
        else:
            secs = defaultSecs
            # print("Using default secs value:\t{}".format(secs))

    # print("\nMessage:\t{}\nDelay:\t\t{}\n".format(args.message, secs))  # DEBUGGING
    # print(figlet_format(args.message, "banner3"))  # DEBUGGING
    
    system("clear")  # Clear the screen
    try:
        input("Press Enter to continue...")
    except:
        pass

    for char in args.message:
        system("clear")  # Clear the screen
        print(figlet_format(char, "banner3", justify="center"))
        sleep(secs)  # Sleep

    system("clear")  # Clear the screen
    try:
        input("Press Enter to end...")
    except:
        pass
    finally:
        system("clear")  # Clear the screen

    return


if __name__ == "__main__":
    if sys.version_info[0] != 2 or (sys.version_info[0] == 2 and sys.version_info[1] < 7):
        print("This script requires Python 2.7 to run as written.")
    else:
        main()

