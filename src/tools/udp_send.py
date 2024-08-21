import socket

import click


@click.command()
@click.option("-h", "--host", type=str, default="255.255.255.255")
@click.option("-p", "--port", type=int, default=514)
@click.option("-m", "--message", type=str, default="Hello, world!")
def cli(host: str, port: int, message: str):
    """Send a UDP message to a host and port"""
    click.echo(f"Sending message to {host}:{port}")
    click.echo(f"Message: {message}")

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Enable broadcast

    sock.sendto(message.encode(), (host, port))
    sock.close()


if __name__ == "__main__":
    cli()
