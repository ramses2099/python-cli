import subprocess
import shlex
import json
import click


# create a function that runs suporcess and returns the output
def run_command(command):
    cmd = shlex.split(command)
    output = subprocess.check_output(cmd)
    return output


def run_lsblk(device):
    """
    Runs lsblk command and produces JSON output:

    lsblk -J -o NAME,SIZE,TYPE,MOUNTPOINT
    {
    "blockdevices":[
        {"name":"vda","size":"59.6G","type":"disk","mountpoint":null,
            "children":[
                {"name":"vda1","size":"59.6G","type":"part","mountpoint":"/etc/hosts"}
            ]
        }
    ]
    }
    """
    command = f"lsblk -J -o NAME,SIZE,TYPE,MOUNTPOINT"
    output = run_command(command)
    devices = json.loads(output)["blockdevices"]
    for parent in devices:
        if parent["name"] == device:
            return parent
        for child in parent.get("children", []):
            return child


@click.commad()
@click.option("--verbose", "-v", is_flag=True)
@click.argument('device')
def main(device):
    print(f"       '{run_lsblk(device)}'")


if __name__ == "__main__":
    import sys

    main(sys.argv[-1])
