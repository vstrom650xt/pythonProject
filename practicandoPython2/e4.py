# 2. Crea un programa que dado el PID de un proceso devuelva:
# - información relevante de dicho proceso
# - dónde se encuentra el archivo ejecutable
# (busca información y juega con subprocess.check_output() o con psutil.Process())


import subprocess
from subprocess import call

if __name__ == '__main__':
    # print(call('ps -aux | grep mariadb'))
    #     print(subprocess.run(['ps','-aux','|','grep','mariadb']))
     #   print (call('ps')) # no me cuadra
  #  print(subprocess.run['ps', '-aux'])

    # r  =subprocess.run(['grep','1203'])
    # print(r)

    result = subprocess.run(['grep', '1203'], stdout=subprocess.PIPE, text=True)
    print(result)

