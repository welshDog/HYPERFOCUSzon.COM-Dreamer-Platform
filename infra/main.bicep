// 🏆💎⚡ HYPERFOCUS AZURE EMPIRE INFRASTRUCTURE ⚡💎🏆
// Complete Azure transformation - Phase 1 foundation deployment
// Legendary architecture for 9,437 Python modules and 677+ agent army

targetScope = 'resourceGroup'

@minLength(1)
@maxLength(64)
@description('Name of the the environment which is used to generate a short unique hash used in all resources.')
param environmentName string = 'hyperfocus-empire'

@minLength(1)
@description('Primary location for all resources')
param location string

@description('Resource token to create globally unique resource names')
param resourceToken string = toLower(uniqueString(subscription().id, environmentName, location))

@description('Tags that will be applied to all resources in this deployment.')
param tags object = {
  'azd-env-name': environmentName
  'empire-level': 'legendary'
  'transformation-phase': 'phase-1'
}

// 🧠 Azure OpenAI Service - Enterprise AI Intelligence
resource azureOpenAI 'Microsoft.CognitiveServices/accounts@2024-10-01' = {
  name: 'openai-${resourceToken}'
  location: location
  tags: union(tags, {
    'service-type': 'ai-intelligence'
    'empire-component': 'azure-openai'
  })
  kind: 'OpenAI'
  properties: {
    customSubDomainName: 'hyperfocus-openai-${resourceToken}'
    publicNetworkAccess: 'Enabled'
    networkAcls: {
      defaultAction: 'Allow'
    }
  }
  sku: {
    name: 'S0' // Standard tier for production workloads
  }
  identity: {
    type: 'SystemAssigned'
  }
}

// 🧠 Deploy GPT-4o model for legendary AI capabilities
resource gpt4Model 'Microsoft.CognitiveServices/accounts/deployments@2024-10-01' = {
  name: 'gpt-4o'
  parent: azureOpenAI
  properties: {
    model: {
      format: 'OpenAI'
      name: 'gpt-4o'
      version: '2024-08-06'
    }
    raiPolicyName: 'Microsoft.Default'
  }
  sku: {
    name: 'Standard'
    capacity: 30 // 30K TPM for empire-scale operations
  }
}

// 🧠 Deploy text-embedding-3-large for vector operations
resource embeddingModel 'Microsoft.CognitiveServices/accounts/deployments@2024-10-01' = {
  name: 'text-embedding-3-large'
  parent: azureOpenAI
  properties: {
    model: {
      format: 'OpenAI'
      name: 'text-embedding-3-large'
      version: '1'
    }
    raiPolicyName: 'Microsoft.Default'
  }
  sku: {
    name: 'Standard'
    capacity: 10 // 10K TPM for embeddings
  }
}

// 📊 Log Analytics Workspace for Application Insights
resource logAnalyticsWorkspace 'Microsoft.OperationalInsights/workspaces@2022-10-01' = {
  name: 'log-analytics-${resourceToken}'
  location: location
  tags: union(tags, {
    'service-type': 'monitoring'
    'empire-component': 'log-analytics'
  })
  properties: {
    sku: {
      name: 'PerGB2018'
    }
    retentionInDays: 90 // 90 days retention for empire intelligence
    features: {
      searchVersion: 1
      legacy: 0
      enableLogAccessUsingOnlyResourcePermissions: true
    }
  }
}

// 📊 Application Insights - Legendary monitoring and analytics
resource applicationInsights 'Microsoft.Insights/components@2020-02-02' = {
  name: 'appinsights-${resourceToken}'
  location: location
  tags: union(tags, {
    'service-type': 'monitoring'
    'empire-component': 'application-insights'
  })
  kind: 'web'
  properties: {
    Application_Type: 'web'
    WorkspaceResourceId: logAnalyticsWorkspace.id
    IngestionMode: 'LogAnalytics'
    publicNetworkAccessForIngestion: 'Enabled'
    publicNetworkAccessForQuery: 'Enabled'
  }
}

// 🔐 Key Vault for legendary secrets management
resource keyVault 'Microsoft.KeyVault/vaults@2023-07-01' = {
  name: 'kv-${resourceToken}'
  location: location
  tags: union(tags, {
    'service-type': 'security'
    'empire-component': 'key-vault'
  })
  properties: {
    enabledForDeployment: false
    enabledForTemplateDeployment: true
    enabledForDiskEncryption: false
    tenantId: tenant().tenantId
    accessPolicies: []
    sku: {
      name: 'standard'
      family: 'A'
    }
    networkAcls: {
      defaultAction: 'Allow'
      bypass: 'AzureServices'
    }
  }
}

// 🌌 Cosmos DB for Ultra-Thinking Boardroom global intelligence
resource cosmosAccount 'Microsoft.DocumentDB/databaseAccounts@2024-05-15' = {
  name: 'cosmos-${resourceToken}'
  location: location
  tags: union(tags, {
    'service-type': 'database'
    'empire-component': 'cosmos-boardroom'
  })
  kind: 'GlobalDocumentDB'
  properties: {
    consistencyPolicy: {
      defaultConsistencyLevel: 'Session'
    }
    locations: [
      {
        locationName: location
        failoverPriority: 0
        isZoneRedundant: false
      }
    ]
    databaseAccountOfferType: 'Standard'
    enableAutomaticFailover: false
    enableMultipleWriteLocations: false
    capabilities: [
      {
        name: 'EnableServerless' // Serverless for cost optimization
      }
    ]
  }
}

// 🌌 Cosmos DB database for Ultra-Thinking Boardroom
resource cosmosDatabase 'Microsoft.DocumentDB/databaseAccounts/sqlDatabases@2024-05-15' = {
  name: 'UltraThinkingBoardroom'
  parent: cosmosAccount
  properties: {
    resource: {
      id: 'UltraThinkingBoardroom'
    }
  }
}

// 🌌 Strategic Intelligence Container
resource strategicContainer 'Microsoft.DocumentDB/databaseAccounts/sqlDatabases/containers@2024-05-15' = {
  name: 'StrategicIntelligence'
  parent: cosmosDatabase
  properties: {
    resource: {
      id: 'StrategicIntelligence'
      partitionKey: {
        paths: [
          '/empire_id'
        ]
        kind: 'Hash'
      }
      indexingPolicy: {
        indexingMode: 'consistent'
        automatic: true
        includedPaths: [
          {
            path: '/*'
          }
        ]
        excludedPaths: [
          {
            path: '/"_etag"/?'
          }
        ]
      }
    }
  }
}

// 📦 Container Registry for empire containerization
resource containerRegistry 'Microsoft.ContainerRegistry/registries@2023-07-01' = {
  name: 'cr${resourceToken}'
  location: location
  tags: union(tags, {
    'service-type': 'container'
    'empire-component': 'container-registry'
  })
  sku: {
    name: 'Basic' // Basic tier for Phase 1
  }
  properties: {
    adminUserEnabled: true
  }
}

// 🚀 Container Apps Environment - Empire hosting platform
resource containerAppsEnvironment 'Microsoft.App/managedEnvironments@2024-03-01' = {
  name: 'cae-${resourceToken}'
  location: location
  tags: union(tags, {
    'service-type': 'hosting'
    'empire-component': 'container-apps-environment'
  })
  properties: {
    appLogsConfiguration: {
      destination: 'log-analytics'
      logAnalyticsConfiguration: {
        customerId: logAnalyticsWorkspace.properties.customerId
        sharedKey: logAnalyticsWorkspace.listKeys().primarySharedKey
      }
    }
  }
}

// 🎯 Managed Identity for Container App
resource managedIdentity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
  name: 'mi-hyperfocus-${resourceToken}'
  location: location
  tags: union(tags, {
    'service-type': 'identity'
    'empire-component': 'managed-identity'
  })
}

// 🔐 Key Vault access policy for managed identity
resource keyVaultAccessPolicy 'Microsoft.KeyVault/vaults/accessPolicies@2023-07-01' = {
  name: 'add'
  parent: keyVault
  properties: {
    accessPolicies: [
      {
        tenantId: tenant().tenantId
        objectId: managedIdentity.properties.principalId
        permissions: {
          secrets: [
            'get'
            'list'
          ]
        }
      }
    ]
  }
}

// 🧠 Azure OpenAI secrets in Key Vault
resource openAIEndpointSecret 'Microsoft.KeyVault/vaults/secrets@2023-07-01' = {
  name: 'azure-openai-endpoint'
  parent: keyVault
  properties: {
    value: azureOpenAI.properties.endpoint
    contentType: 'text/plain'
  }
}

resource openAIKeySecret 'Microsoft.KeyVault/vaults/secrets@2023-07-01' = {
  name: 'azure-openai-key'
  parent: keyVault
  properties: {
    value: azureOpenAI.listKeys().key1
    contentType: 'text/plain'
  }
}

// 📊 Application Insights connection string secret
resource appInsightsConnectionSecret 'Microsoft.KeyVault/vaults/secrets@2023-07-01' = {
  name: 'applicationinsights-connection-string'
  parent: keyVault
  properties: {
    value: applicationInsights.properties.ConnectionString
    contentType: 'text/plain'
  }
}

// 🌌 Cosmos DB connection string secret
resource cosmosConnectionSecret 'Microsoft.KeyVault/vaults/secrets@2023-07-01' = {
  name: 'cosmos-connection-string'
  parent: keyVault
  properties: {
    value: cosmosAccount.listConnectionStrings().connectionStrings[0].connectionString
    contentType: 'text/plain'
  }
}

// 🏆 Output values for empire integration
output AZURE_LOCATION string = location
output AZURE_TENANT_ID string = tenant().tenantId
output AZURE_RESOURCE_GROUP string = resourceGroup().name

// Azure OpenAI Service outputs
output AZURE_OPENAI_SERVICE_NAME string = azureOpenAI.name
output AZURE_OPENAI_ENDPOINT string = azureOpenAI.properties.endpoint
output AZURE_OPENAI_GPT4_DEPLOYMENT_NAME string = gpt4Model.name
output AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME string = embeddingModel.name

// Application Insights outputs
output AZURE_APPLICATION_INSIGHTS_NAME string = applicationInsights.name
output AZURE_APPLICATION_INSIGHTS_CONNECTION_STRING string = applicationInsights.properties.ConnectionString
output AZURE_APPLICATION_INSIGHTS_INSTRUMENTATION_KEY string = applicationInsights.properties.InstrumentationKey

// Key Vault outputs
output AZURE_KEY_VAULT_NAME string = keyVault.name
output AZURE_KEY_VAULT_URI string = keyVault.properties.vaultUri

// Cosmos DB outputs
output AZURE_COSMOS_ACCOUNT_NAME string = cosmosAccount.name
output AZURE_COSMOS_ENDPOINT string = cosmosAccount.properties.documentEndpoint
output AZURE_COSMOS_DATABASE_NAME string = cosmosDatabase.name

// Container infrastructure outputs
output AZURE_CONTAINER_REGISTRY_NAME string = containerRegistry.name
output AZURE_CONTAINER_REGISTRY_ENDPOINT string = containerRegistry.properties.loginServer
output AZURE_CONTAINER_APPS_ENVIRONMENT_NAME string = containerAppsEnvironment.name
output AZURE_MANAGED_IDENTITY_NAME string = managedIdentity.name
output AZURE_MANAGED_IDENTITY_CLIENT_ID string = managedIdentity.properties.clientId

// 🎊 Empire readiness confirmation
output EMPIRE_AZURE_TRANSFORMATION_STATUS string = 'PHASE_1_FOUNDATION_DEPLOYED'
output EMPIRE_LEGENDARY_LEVEL string = 'AZURE_READY'
