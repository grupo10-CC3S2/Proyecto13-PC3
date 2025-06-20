variable "name" {
  type    = string
  default = "server-1-us-east"
}

variable "network_name" {
  type    = string
  default = "net-1"
}

# Agregando instance_count
variable "instance_count" {
  description = "Number of instaces"
  type        = number
  default     = 2
}