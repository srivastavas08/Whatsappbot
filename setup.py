from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
    name = 'whatsappAutomation',
    version = '1.00',
    packages = ['whatsapp'],
    url = '',
    license = '',
    author = 'KIRAN CHANDRA',
    author_email = 'srivastavas08@gmail.com',
    long_description = 'long_description',
    long_description_content_type = 'text/markdown'
)



