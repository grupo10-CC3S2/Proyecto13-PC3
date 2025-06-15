import os
import shutil
import sys

def check_command(cmd):
    if shutil.which(cmd) is None:
        print(f"Error: '{cmd}' no está instalado o no está en el PATH.")
        sys.exit(1)

def generar_diagrama(path, output):
    
    try:
        os.chdir(path)
        os.system('terraform init')
        result = os.system(f'terraform graph | dot -Tpng > {output}')
        if result != 0:
            print(f"Error generando el diagrama en {path}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

check_command('terraform')
check_command('dot')

generar_diagrama('../iac/monorepo', 'graph-monorepo.png')
generar_diagrama('../iac/multirepo/umbrella-repo', 'graph-multirepo.png') 