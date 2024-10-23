from setuptools import find_packages, setup

setup(
    name="rabbit-helper",
    version="1.0.0",
    packages=find_packages(include=["rabbit_helper", "rabbit_helper.*"]),
    install_requires=["pika"],
    python_requires=">=3.8",
    description="RabbitMQ helper for publishing and consuming messages for MealMasterMind project",
    author="Arshia Rezagholi",
    author_email="arshiarezagholi1212@gmail.com"

)
