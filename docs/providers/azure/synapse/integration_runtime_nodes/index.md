---
title: integration_runtime_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_runtime_nodes
  - synapse
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
<tr><td><b>Name</b></td><td><code>integration_runtime_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.integration_runtime_nodes</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IntegrationRuntimeNodes_Delete` | `DELETE` | `integrationRuntimeName, nodeName, resourceGroupName, subscriptionId, workspaceName` | Delete an integration runtime node |
| `IntegrationRuntimeNodes_Get` | `EXEC` | `integrationRuntimeName, nodeName, resourceGroupName, subscriptionId, workspaceName` | Get an integration runtime node |
| `IntegrationRuntimeNodes_Update` | `EXEC` | `integrationRuntimeName, nodeName, resourceGroupName, subscriptionId, workspaceName` | Create an integration runtime node |
