import aws-sync 

# source defintions
sourceAccountProfile = ""
sourceSecretsRegion = ""
sourceSecretsEnvFilter = ""

# destination definitions
destinationAccountProfile = ""
destinationSecretsRegion = ""
destinationAccountKMS = ""

response = aws-sync.sync(sourceAccountProfile, sourceSecretsRegion, sourceSecretsEnvFilter, destinationAccountProfile, destinationSecretsRegion, destinationAccountKMS)
print(response)
