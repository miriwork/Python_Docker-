import docker
from docker.errors import DockerException

try:
    print("Connecting to Docker...")
    client = docker.from_env()
    print("Creating and starting a BusyBox container...")
    container = client.containers.run(
        "busybox",
        "sleep 3600",  
        detach=True
    )
    print("Executing command in the container to retrieve hostname...")
    exec_result = container.exec_run("hostname")
    hostname = exec_result.output.decode("utf-8").strip()
    print(f"The hostname of the container is: {hostname}")
except DockerException as e:
    print(f"An error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
