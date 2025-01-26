# my_sample_project/setup.py
from setuptools import setup, find_packages

setup(
    name='Code_01',
    version='0.1.0',
    package_dir={'': 'src'},  # 소스 코드가 있는 디렉토리 설정
    packages=find_packages(where='src'), # src 디렉토리에서 패키지 찾기
    description='A sample Python package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your_email@example.com',
    license='MIT',
    url='https://github.com/yourusername/my_sample_project',  # 실제 repository 주소로 변경
    install_requires=[],
    tests_require=['unittest'],
    python_requires='>=3.6',
)