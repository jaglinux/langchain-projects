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

def run_container(image="ubuntu", command="echo hello", detach=False):
    if detach is False:
        out = client.containers.run(image, command)
        print(out)

if __name__ == "__main__":
    print("enter main")
    #run_container("jaglinuxdocker/ubuntu-plus:latest", command="lspci -d 1002:")
