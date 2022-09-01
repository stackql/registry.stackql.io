---
title: libraries
hide_title: false
hide_table_of_contents: false
keywords:
  - libraries
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
<tr><td><b>Name</b></td><td><code>libraries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.libraries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Name of the library. |
| `provisioningStatus` | `string` | Provisioning status of the library/package. |
| `type` | `string` | Type of the library. |
| `uploadedTimestamp` | `string` | The last update time of the library. |
| `containerName` | `string` | Storage blob container name. |
| `creatorId` | `string` | Creator Id of the library/package. |
| `path` | `string` | Storage blob path of library. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Libraries_ListByWorkspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` |
