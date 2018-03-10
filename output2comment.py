#
# Este programa convierte en comentarios dentro
# del codigo las salidas de las celdas
#
# import io
# import os
import sys
import nbformat

def nbgen(infilename, outfilename):

    nb = nbformat.read(infilename,  as_version=4)

    for i in range(len(nb.cells)):

        if nb.cells[i].cell_type == 'code':

            ##
            ## borra la numeración
            ##
            nb.cells[i].execution_count = None

            ##
            ## comenta el codigo fuente
            ##
            if len(nb.cells[i].source) != 0:
                source = nb.cells[i].source.splitlines()
                source_out = []
                for line in source:
                    if len(line) > 0:
                        if line[0] != '#':
                            line = "## " + line
                    source_out.append(line)
                nb.cells[i].source = '\n'.join(source_out)

            ##
            ## copia la salida como comentarios al
            ## codigo fuente
            ##
            if len(nb.cells[i].outputs) != 0:

                ##
                ## parte en lineas la salida
                ##
                if nb.cells[i].outputs[0]['output_type'] == 'stream':
                    output = nb.cells[i].outputs[0]['text'].splitlines()
                elif nb.cells[i].outputs[0]['output_type'] == 'display_data':
                    output = nb.cells[i].outputs[0]['data']['text/plain'].splitlines()
                ##
                ## comenta cada linea de la salida
                ##
                output = ['## ' + line for line in output]
                output = ['\n##'] + output + ['##']

                ##
                ## agrega la salida al codigo
                ##
                if len(nb.cells[i].source) != 0:
                    nb.cells[i].source += '\n'.join(output)
                else:
                    nb.cells[i].source = '\n'.join(output)

    nbformat.write(nb, outfilename)

if __name__ == '__main__':
    ##
    nbgen(infilename = sys.argv[1], outfilename = sys.argv[2])
    ##
