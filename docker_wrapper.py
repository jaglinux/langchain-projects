import docker

client = docker.from_env()

images = client.images.list()

print("Number of Images in this node are ", len(images))
print("Images are ")
for i, image in enumerate(images):
    print(i, image)

containers = client.containers.list()
print("Number of containers running in this node are ", len(containers))
print("Containers are ")
for i, container in enumerate(containers):
    print(i, container, container.attrs['Config']['Image'])