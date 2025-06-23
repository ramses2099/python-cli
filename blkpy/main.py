from util import run_lsblk
import click

@click.command()
@click.option("--verbose", "-v", is_flag=True)
@click.argument('device')
def main(device, verbose):
    """
    Mian Entrypoint
    """
    print(f"Device: {device}")
    print(f"Verbose: {verbose}")
    print(f"{run_lsblk(device)}")


if __name__ == "__main__":
    import sys

    main(sys.argv[-1])
