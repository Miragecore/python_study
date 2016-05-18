from setuptools import setup

setup(name="test_camera",
      description="py2app test application",
      version="0.0.1",
      setup_requires=["py2app"],
      app=["hello.py"]
      )

