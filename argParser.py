import argparse

def process_cmd_arguments(debug_on):
    parser = argparse.ArgumentParser(
                        prog='Scanex v0.1',
                        description='Program for scanning given targets.',
                        epilog='Usage of this tool for attacking targets without prior mutual consent is illegal. It is the user\'s responsibility to obey all applicable local, state and federal laws.')
    '''
    parser.add_argument('-t', '--type', help="Type of the attack. Default = 1", choices=range(1,3), default=1)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--file', help="Text file containing list of target. Each target on a new line.")
    group.add_argument('-s', '--single', help="Single target specified. Either an IP or a web address.")

    args = parser.parse_args()
    

    print("-----------------------")
    print(args.type)
    print(group.file)
    '''
    parser.add_argument('-t', '--type', help="Type of scan. Default=1", choices=['1', '2'], default=1)
    sp = parser.add_subparsers()

    target_as_list = sp.add_parser('LIST', help="Scanning list of target in the given file.")
    target_as_single = sp.add_parser('SINGLE', help="Scanning just one single target specified in the command line.")

   # target_as_list.add_argument('-f', '--file', help="Location of the file", required=True)
    target_as_list.add_argument('file', help="Location of the file")
    target_as_single.add_argument('address', help="Target address")



   # sp_target_as_single_address = sp.add_parser('-s', '--single', help="Single target specified. Either an IP or a web address.")
    #sp_target_as_list = sp.add_parser('-f', '--file', help="Text file containing list of target. Each target on a new line.")

    args = parser.parse_args()
    if debug_on: print(args.type)

    arg_list =  True if 'file' in vars(args)  else False
   
    if debug_on: print("arg_list: " + str(arg_list))
    
    
    if arg_list:
        with open(args.file, 'r') as f:
            targetS = f.read().split()
    else:
        targetS = [args.address]

    if debug_on: print(targetS)
    return args.type, targetS