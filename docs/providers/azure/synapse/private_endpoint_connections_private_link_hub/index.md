---
title: private_endpoint_connections_private_link_hub
hide_title: false
hide_table_of_contents: false
keywords:
  - private_endpoint_connections_private_link_hub
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
<tr><td><b>Name</b></td><td><code>private_endpoint_connections_private_link_hub</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.private_endpoint_connections_private_link_hub</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateEndpointConnectionsPrivateLinkHub_List` | `SELECT` |  | Get all PrivateEndpointConnections in the PrivateLinkHub |
| `PrivateEndpointConnectionsPrivateLinkHub_Get` | `EXEC` |  | Get all PrivateEndpointConnection in the PrivateLinkHub by name |
