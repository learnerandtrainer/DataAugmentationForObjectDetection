from setuptools import setup,find_packages

setup(name="data_aug",
      version='1.0.0',
      description='test',
      url="https://github.com/Paperspace/DataAugmentationForObjectDetection",
      author='ayooshkathuria and dkobran',
      author_email='dkobran@gmail.com',
      license='MIT',
      packages= find_packages(),
      install_requires=['numpy','scipy','pillow',"matplotlib", "h5py"],
      zip_safe=False

      )
