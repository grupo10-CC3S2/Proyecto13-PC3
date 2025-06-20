resource "null_resource" "network-1" {
  triggers = {
    version = "v1"
  }
  provisioner "local-exec" {
    command = "echo 'Creando network ${var.name} con puerto ${var.port}'"
  }
}
