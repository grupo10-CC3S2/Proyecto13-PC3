resource "null_resource" "server-1" {
  triggers = {
    version = "v1"
  }
  provisioner "local-exec" {
    command = "echo 'Creando server ${var.name} con network ${var.network_name}'"
  }
}
