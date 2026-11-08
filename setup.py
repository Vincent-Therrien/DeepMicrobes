import setuptools
from setuptools.command.install import install
from io import open
import os

install_requires = ["tensorflow>=2.19.0", "tensorboard>=2.19.0", "absl-py>=0.3.0", "biopython>=1.70", "numpy>=1.19.0", "h5py>=2.10.0"]
setuptools.setup(
    name='DeepMicrobes',
    version='1.0.1',
    author='Qiaoxing Liang',
    author_email='liangqx7@mail2.sysu.edu.cn',
    url='https://github.com/MicrobeLab/DeepMicrobes/',
    packages = ['models', 'utils', 'scripts'],
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    entry_points={
        'console_scripts': [
            'DeepMicrobes.py = DeepMicrobes:main',
            'fna_label.py = scripts.fna_label:main',
            'random_trim.py = scripts.random_trim:main',
            'read_counter.py = scripts.read_counter:main',
            'seq2tfrec_kmer.py  = scripts.seq2tfrec_kmer:main',
            'seq2tfrec_onehot.py = scripts.seq2tfrec_onehot:main'
        ]
    },
    description="DeepMicrobes: taxonomic classification for metagenomics with deep learning",
    install_requires=install_requires
)
