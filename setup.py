from setuptools import setup, find_packages

setup(
    name="manim-algorithm-video",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "manim>=0.18.0",
        "numpy>=1.19.0",
        "pillow>=7.2.0",
        "scipy>=1.5.0",
        "tqdm>=4.48.0",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="Algorithm visualization using Manim",
    keywords="manim, algorithms, visualization",
    python_requires=">=3.7",
)
