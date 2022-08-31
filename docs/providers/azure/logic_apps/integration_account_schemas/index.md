---
title: integration_account_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_account_schemas
  - logic_apps
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>integration_account_schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.logic_apps.integration_account_schemas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource id. |
| `name` | `string` | Gets the resource name. |
| `metadata` | `object` | The metadata. |
| `contentType` | `string` | The content type. |
| `contentLink` | `object` | The content link. |
| `type` | `string` | Gets the resource type. |
| `tags` | `object` | The resource tags. |
| `changedTime` | `string` | The changed time. |
| `documentName` | `string` | The document name. |
| `fileName` | `string` | The file name. |
| `content` | `string` | The content. |
| `location` | `string` | The resource location. |
| `createdTime` | `string` | The created time. |
| `schemaType` | `string` | The schema type. |
| `targetNamespace` | `string` | The target namespace of the schema. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IntegrationAccountSchemas_List` | `SELECT` | `api-version, integrationAccountName, resourceGroupName, subscriptionId` | Gets a list of integration account schemas. |
| `IntegrationAccountSchemas_CreateOrUpdate` | `INSERT` | `api-version, integrationAccountName, resourceGroupName, schemaName, subscriptionId` | Creates or updates an integration account schema. |
| `IntegrationAccountSchemas_Delete` | `DELETE` | `api-version, integrationAccountName, resourceGroupName, schemaName, subscriptionId` | Deletes an integration account schema. |
| `IntegrationAccountSchemas_Get` | `EXEC` | `api-version, integrationAccountName, resourceGroupName, schemaName, subscriptionId` | Gets an integration account schema. |
| `IntegrationAccountSchemas_ListContentCallbackUrl` | `EXEC` | `api-version, integrationAccountName, resourceGroupName, schemaName, subscriptionId` | Get the content callback url. |