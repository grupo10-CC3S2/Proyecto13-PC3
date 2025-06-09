import json
from network_module.network import NetworkFactoryModule

if __name__ == "__main__":
    network_name = "network-1"
    port = 8080
    network_factory = NetworkFactoryModule(network_name, port)
    network_build = network_factory.build()
    resources = {"resource": network_build}

    with open("main.tf.json", "w") as f:
        json.dump(resources, f, indent=4)
