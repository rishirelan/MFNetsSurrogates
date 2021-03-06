import setuptools

setuptools.setup(
    name="mfnets_surrogates",
    version="1.0.0",
    author="Alex A. Gorodetsky",
    author_email="goroda@umich.edu",
    description="A set of routines to enable construction of completely unstructured multifidelity surrogate models for fusing multiple information sources",
    url="https://github.com/goroda/MFNetsSurrogates",
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    setup_requires=[],
    install_requires=['numpy >= 1.14','networkx'],
    license='MIT',
)
