from setuptools import setup, find_packages

setup(
    name="aws-sync",
    packages=find_packages(),
    version="0.3",
    description="Sync AWS secrets across multiple accounts",
    long_description="
    Python package which easily syncs specifc or all secrets between multiple AWS accounts. Missing secrets are automatically created and existing secrets are updated in-place. Supports filtering to replicate specific pattern matching secrets. Defaults to replicate all secrets. Supports using custom KMS Encryption key. Defaults to default AWS secrets manager encryption key.
",
    author="Udhav Pawar",
    author_email="upawar78@gmail.com",
    url="https://github.com/UdhavPawar/aws_sync",
    keywords=["aws","secrets","aws-secrets-manager","aws-sync","replicate","credentials","automation"],
    license="MIT",
    include_package_data = True,
    install_requires=["boto3"],
)
