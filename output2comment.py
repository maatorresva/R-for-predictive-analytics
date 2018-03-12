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
                if 'text' in nb.cells[i].outputs[0].keys():

                    ##
                    ## obtiene la salida
                    ##
                    output = nb.cells[i].outputs[0]['text']

                    ##
                    ## comenta cada linea de la salida
                    ##
                    output = output.replace('\n', '\n## ')
                    output = '\n\n## ' + output
                    if len(nb.cells[i].source) != 0:
                        nb.cells[i].source += ''.join(output)
                    else:
                        nb.cells[i].source = ''.join(output)

                elif 'data' in nb.cells[i].outputs[0].keys():
                    if 'text/plain' in nb.cells[i].outputs[0]['data'].keys():

                        ##
                        ## obtiene la salida
                        ##
                        output = nb.cells[i].outputs[0]['data']['text/plain']

                        ##
                        ## comenta cada linea de la salida
                        ##
                        output = output.replace('\n', '\n## ')
                        output = '\n\n## ' + output
                        if len(nb.cells[i].source) != 0:
                            nb.cells[i].source += ''.join(output)
                        else:
                            nb.cells[i].source = ''.join(output)

                    else:
                        if len(nb.cells[i].source) != 0:
                            nb.cells[i].source += '\n\n## plot without title'
                        else:
                            nb.cells[i].source = '## plot without title'


                #if 'data' in nb.cells[i].outputs[0].keys():
                #    if 'text/plain' in nb.cells[i].outputs[0].data.keys():
                #        output = nb.cells[i].outputs[0]['data']['text/plain']


                ##
                ## agrega la salida al codigo
                ##
                    #print(type(nb.cells[i].source))
                # if len(nb.cells[i].source) != 0:
                #    # nb.cells[i].source += '\n'.join(output)
                #    if isinstance(output, str):
                #        nb.cells[i].source += '\n'.join(output)
                #    else:
                #        nb.cells[i].source += '\n'.join(output)
                #
                #else:
                #    nb.cells[i].source = output
                #    # nb.cells[i].source = '\n'.join(output)

    nbformat.write(nb, outfilename)

if __name__ == '__main__':
    ##
    nbgen(infilename = sys.argv[1], outfilename = sys.argv[2])
    ##
