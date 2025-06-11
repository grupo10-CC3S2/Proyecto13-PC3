class ServerFatoryModule:
    def __init__(self, name, network):
        self.name = name
        self.network = network
        self.server_type = "web"

    def build(self):
        command = f"echo 'Creando server {self.name} con network {self.network.name}'"

        return [
            {
                "null_resource": {
                    self.name: {
                        "provisioner": {"local-exec": {"command": command}},
                    },
                }
            }
        ]
