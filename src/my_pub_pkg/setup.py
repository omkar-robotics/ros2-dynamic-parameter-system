from setuptools import setup

package_name = 'my_pub_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='omi',
    maintainer_email='omi@todo.todo',
    description='ROS2 Publisher Package',
    license='TODO',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "my_publisher = my_pub_pkg.my_publisher:main",
        ],
    },
)
