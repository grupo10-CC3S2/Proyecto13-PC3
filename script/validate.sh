#!/bin/bash

set -e

echo  "Validación de módulos de Terraform"

validate_terraform_dir() {
  local dir="$1"
  echo "Validando directorio: $dir"
  
  cd "$dir" 
  
  echo "Verifica formato"
  terraform fmt -check -diff

  echo "Valida sintaxis"
  terraform init -backend=false > /dev/null
  terraform validate

  cd - > /dev/null
}

# Validar cada modulo de Terraform

echo "Validando Monorepo"
for module in network-module compute-module storage-module; do
    if [ -d "iac/monorepo/$module" ]; then
        validate_terraform_dir "iac/monorepo/$module"
    else
        echo "Módulo $module no encontrado en iac/monorepo/"
    fi
done

echo "Validando Multirepo"
for repo in compute-repo network-repo storage-repo; do
    if [ -d "iac/multirepo/$repo" ]; then
        validate_terraform_dir "iac/multirepo/$repo"
    else
        echo "Repo $repo no encontrado en iac/multirepo/"
    fi
done

echo "Validación completada exitosa."