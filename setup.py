from setuptools import setup, find_packages

setup(
    name='geocrowdai',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'geopandas',
        'pandas',
        'scikit-learn',
        'matplotlib',
    ],
    author='Srijon Kumar Shill',
    author_email='your-email@example.com',
    description='Real-time crowdsourced geospatial data analysis using AI.',
    license='MIT',
    keywords='geospatial crowdsourcing AI',
    url='https://github.com/example/GeoCrowdAI',
)