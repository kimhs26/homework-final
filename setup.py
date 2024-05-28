from setuptools import find_packages, setup

package_name = 'kim_hyun_sung_homework1_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kim_hyun_sung',
    maintainer_email='kimhstim@naver.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
      'kim_hyun_sung_publisher = kim_hyun_sung_homework1_pkg.kim_hyun_sung_publisher:main',
      'kim_hyun_sung_subscriber = kim_hyun_sung_homework1_pkg.kim_hyun_sung_subscriber:main',
        ],
    },
)
