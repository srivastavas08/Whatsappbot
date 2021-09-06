import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="whatsappchatbot-kc",
    version="0.0.1",
    author="Kiran Chandra",
    author_email="srivastavas08@gmail.com",
    description="Its an whatsapp chatbot that can receive and send message to user",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/srivastavas08/WhatsappBOT",
    project_urls={
        "Bug Tracker": "https://github.com/srivastavas08/WhatsappBOT/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)