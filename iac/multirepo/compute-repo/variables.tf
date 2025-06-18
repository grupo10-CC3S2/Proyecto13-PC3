variable "name" {
  type    = string
  default = "server-1-us-east"
}

variable "network_name" {
  type        = string
}

# Agregando instance_count
variable "instance_count" {
  description = "Number of instaces"
  type    = number
  default = 2
}