__author__ = "Pablo Martin Ruiz Diaz"
__version__ = "2.0"

from configparser import ConfigParser
import os

def config(section, filename='config.ini'):
    '''
    Config
    ---------------------------
    Este programa fue creado para leer archivos de configuracion "config.ini".
    Fue modificado para ser mas versatil en donde se guarda, solamante importando
    el archivo y llamando a la funcion config() con parametro el nombre de la 
    base de datos a la cual se quiere llamar. Se puede trabajar con mas de un 
    archivo .ini como 2do parametro debe nombrarse el mismo que se desea abrir.
        config(section,filename="config.ini")
    '''
    
    # Read config file
    script_path = os.path.dirname(os.path.realpath(__file__))
    config_path_name = os.path.join(script_path, filename)

    parser = ConfigParser()
    parser.read(config_path_name)

    # Read section
    config_param = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config_param[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, config_path_name))

    return config_param
