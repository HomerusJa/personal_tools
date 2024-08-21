import socket

import click


@click.command()
@click.option("-h", "--host", type=str, default="0.0.0.0")
@click.option("-p", "--port", type=int, default=514)
@click.option("-t", "--timeout", type=float, default=1.0)
def cli(host: str, port: int, timeout: float):
    """Your tool description here"""
    click.echo(f"Listening on {host}:{port}")
    click.echo("Press Ctrl+C to exit")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    sock.settimeout(timeout)  # Set a timeout of 1 second

    try:
        while True:
            try:
                data, addr = sock.recvfrom(1024)
                click.echo(f"Received data from {addr}: {data}")
            except socket.timeout:
                continue  # If no data is received, continue the loop
    except KeyboardInterrupt:
        click.echo("Shutting down...")
    finally:
        sock.close()


if __name__ == "__main__":
    cli()
