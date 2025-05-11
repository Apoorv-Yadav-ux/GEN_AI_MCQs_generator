from setuptools import setup, find_packages

setup(
    name="mcq_generator",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "streamlit",
        "openai",
        "langchain"
    ],
    include_package_data=True,
    description="MCQ Generator using Streamlit and OpenAI",
    author="Apoorv Yadav",
    author_email="apoorvyadav2022@vitbhopal.ac.in",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
