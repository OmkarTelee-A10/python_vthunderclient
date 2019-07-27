import sys
import argparse
import argparse_actions
from a10_octavia.controller.worker.tasks.a10_vthunder_db import VThunderDB

def main():
    #defining parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()
 
    #create parser
    create_parser = subparsers.add_parser("create")
    create_parser.add_argument("--project_id", required=True)
    create_parser.add_argument("--device_name", default="")
    create_parser.add_argument("--ip_address", required=True, action=argparse_actions.ProperIpFormatAction)
    create_parser.add_argument("--username", required=True)
    create_parser.add_argument("--password", required=True)
    create_parser.add_argument("--axapi_version", type=float, choices=[2.1, 3.0], required=True)
    create_parser.add_argument("--undercloud", choices=['True', 'False'], default='True')
    create_parser.set_defaults(func=create)
   
    #update parser
    update_parser = subparsers.add_parser("update")
    update_parser.add_argument("--id", required=True)
    update_parser.add_argument("--project_id", required=True)
    update_parser.add_argument("--device_name")
    update_parser.add_argument("--ip_address", required=True, action=argparse_actions.ProperIpFormatAction)
    update_parser.add_argument("--username", required=True)
    update_parser.add_argument("--password", required=True)
    update_parser.add_argument("--axapi_version", type=float, choices=[2.1, 3.0], required=True)
    update_parser.add_argument("--undercloud", choices=['True', 'False'], default='True')
    update_parser.set_defaults(func=update)
    
    #delete parser
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--id", required=True)
    delete_parser.set_defaults(func=delete)
    

    try: 
        args = parser.parse_args()
        args.func(args)
    except argparse_actions.InvalidIp as e:
        print("Invalid IP address range.")


def create(args):
    vthunderdb = VThunderDB()
    vthunderdb.create_vthunder(args.project_id, args.device_name, args.username, args.password, 
                               args.ip_address, args.undercloud, args.axapi_version)

def update(args):
    vthunderdb = VThunderDB()
    vthunderdb.update_vthunder(args.id, args.project_id, args.device_name, args.username, args.password,
                               args.ip_address, args.undercloud, args.axapi_version)

def delete(args):
    vthunderdb = VThunderDB()
    vthunderdb.delete_vthunder(args.id)
