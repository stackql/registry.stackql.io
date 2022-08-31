---
title: connector_applications
hide_title: false
hide_table_of_contents: false
keywords:
  - connector_applications
  - security
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
<tr><td><b>Name</b></td><td><code>connector_applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.connector_applications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `description` | `string` | description of the application |
| `sourceResourceType` | `string` | The application source, what it affects, e.g. Assessments |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `conditionSets` | `array` | The application conditionSets - see examples |
| `displayName` | `string` | display name of the application |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `SecurityConnectorApplications_List` | `SELECT` | `api-version, resourceGroupName, securityConnectorName, subscriptionId` |