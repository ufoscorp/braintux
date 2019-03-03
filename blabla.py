import subprocess

p= subprocess.Popen("python3 /opt/braintux-master/braintux-core.py ping terminal", stdout=subprocess.PIPE,shell=True)

output = p.communicate()[0].decode('utf-8')

print("saida do comando:",output=="On\n")
