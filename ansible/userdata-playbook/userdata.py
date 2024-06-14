#!/usr/bin/python
import json
from ansible.module_utils.basic import AnsibleModule
import sys
def main():
    module = AnsibleModule(
        argument_spec = dict(
            name = dict(required=True, type='str'),
            surname  = dict(required=True, type='str'),
        )
    )

    name = module.params['name']
    surname = module.params['surname']


    data = dict(
        output="your data has stored successfully :-) ",
    )
    try:
        file = open("/var/www/html/index.nginx-debian.html","w")
        file.write("\n"+ name+ "," + surname + "\n")
        module.exit_json(changed=True, success=data,msg=data)
    except Exception as e:
        module.fail_json(msg='something went wrong. :-(')


if __name__ == '__main__':
    main()