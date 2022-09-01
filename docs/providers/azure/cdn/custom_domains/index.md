---
title: custom_domains
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_domains
  - cdn
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
<tr><td><b>Name</b></td><td><code>custom_domains</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cdn.custom_domains</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `customHttpsProvisioningState` | `string` | Provisioning status of the custom domain. |
| `customHttpsProvisioningSubstate` | `string` | Provisioning substate shows the progress of custom HTTPS enabling/disabling process step by step. |
| `hostName` | `string` | The host name of the custom domain. Must be a domain name. |
| `provisioningState` | `string` | Provisioning status of Custom Https of the custom domain. |
| `resourceState` | `string` | Resource status of the custom domain. |
| `validationData` | `string` | Special validation or data may be required when delivering CDN to some regions due to local compliance reasons. E.g. ICP license number of a custom domain is required to deliver content in China. |
| `customHttpsParameters` | `object` | The JSON object that contains the properties to secure a custom domain. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `CustomDomains_ListByEndpoint` | `SELECT` | `endpointName, profileName, resourceGroupName, subscriptionId` | Lists all of the existing custom domains within an endpoint. |
| `CustomDomains_Create` | `INSERT` | `customDomainName, endpointName, profileName, resourceGroupName, subscriptionId` | Creates a new custom domain within an endpoint. |
| `CustomDomains_Delete` | `DELETE` | `customDomainName, endpointName, profileName, resourceGroupName, subscriptionId` | Deletes an existing custom domain within an endpoint. |
| `CustomDomains_DisableCustomHttps` | `EXEC` | `customDomainName, endpointName, profileName, resourceGroupName, subscriptionId` | Disable https delivery of the custom domain. |
| `CustomDomains_EnableCustomHttps` | `EXEC` | `customDomainName, endpointName, profileName, resourceGroupName, subscriptionId, data__certificateSource, data__protocolType` | Enable https delivery of the custom domain. |
| `CustomDomains_Get` | `EXEC` | `customDomainName, endpointName, profileName, resourceGroupName, subscriptionId` | Gets an existing custom domain within an endpoint. |
