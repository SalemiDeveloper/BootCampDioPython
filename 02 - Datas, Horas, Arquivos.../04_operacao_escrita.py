arquivo = open("/Users/Marcelo/Desktop/Estudos/BootCampPython/Codigos3/teste.txt", "w")

arquivo.write('Escrevendodados em um novo arquivo.')
arquivo.writelines(["\n", "escrevendo", "\n", "writelines"])
arquivo.close()
