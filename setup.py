from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required_packages = f.read().splitlines()

setup(
    name='Analizador_de_cometas',  # Nombre del paquete
    version='1.0.0',            # Versión del paquete
    author='Santiago Pérez Puerta',         # Autor del paquete
    author_email='sperezp23@gmail.com',  # Email del autor
    description='Descripción breve del paquete',
    long_description=open('README.md').read(),  # Descripción más extensa (opcional)
    long_description_content_type='text/markdown',  # Formato del README
    url='https://github.com/sperezp23/Analizador_de_cometas',  # URL del proyecto
    packages=find_packages(),    # Encuentra automáticamente los paquetes en el directorio
    classifiers=[                # Clasificadores para categorizar el paquete
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',     # Versión mínima de Python requerida

    install_requires= required_packages
)
