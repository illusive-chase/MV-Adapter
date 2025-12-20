from setuptools import setup

setup(
    name="mvadapter",
    version="0.1.0",
    description="MV-Adapter: A Multi-View Adapter for 3D Generation",
    author="Zehuan Huang",
    packages=[
        "mvadapter",
        "mvadapter.loaders",
        "mvadapter.models",
        "mvadapter.pipelines",
        "mvadapter.schedulers",
        "mvadapter.utils",
        "mvadapter.utils.mesh_utils",
    ],
    install_requires=[
        "diffusers>=0.36.0",
        "cvcuda_cu12>=0.16.0",
        "spandrel==0.4.1",
        "pymeshlab>=2025.7",
        "gltflib>=1.0.13",
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/huanngzh/MV-Adapter",
    project_urls={
        "Project Page": "https://huanngzh.github.io/MV-Adapter-Page/",
        "Paper": "https://arxiv.org/abs/2412.03632",
        "Model Weights": "https://huggingface.co/huanngzh/mv-adapter",
    },
)
