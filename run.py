import aws_sync 

# source defintions
sourceAccountProfile = "accountA"
sourceSecretsRegion = "us-east-1"
sourceSecretsEnvFilter = "" # if not specified then all secrets will be replicated.

# destination definitions
destinationAccountProfile = "accountB"
destinationSecretsRegion = "us-west-2"
destinationAccountKMS = "" # if not specifed then "DefaultEncryptionKey" will be used.

aws-sync.sync(sourceAccountProfile, sourceSecretsRegion, sourceSecretsEnvFilter, destinationAccountProfile, destinationSecretsRegion, destinationAccountKMS)
