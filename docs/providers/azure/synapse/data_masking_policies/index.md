---
title: data_masking_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - data_masking_policies
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
<tr><td><b>Name</b></td><td><code>data_masking_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.data_masking_policies</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DataMaskingPolicies_CreateOrUpdate` | `INSERT` | `dataMaskingPolicyName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Creates or updates a Sql pool data masking policy |
| `DataMaskingPolicies_Get` | `EXEC` | `dataMaskingPolicyName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Gets a Sql pool data masking policy. |
