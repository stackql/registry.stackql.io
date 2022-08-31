---
title: single_sign_on
hide_title: false
hide_table_of_contents: false
keywords:
  - single_sign_on
  - dynatrace
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
<tr><td><b>Name</b></td><td><code>single_sign_on</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dynatrace.single_sign_on</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `singleSignOnUrl` | `string` | The login URL specific to this Dynatrace Environment |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `aadDomains` | `array` | array of Aad(azure active directory) domains |
| `enterpriseAppId` | `string` | Version of the Dynatrace agent installed on the VM. |
| `provisioningState` | `string` | Provisioning state of the monitoring resource |
| `singleSignOnState` | `string` | Various states of the SSO resource |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `SingleSignOn_List` | `SELECT` | `monitorName, resourceGroupName, subscriptionId` |
| `SingleSignOn_CreateOrUpdate` | `INSERT` | `configurationName, monitorName, resourceGroupName, subscriptionId` |
| `SingleSignOn_Get` | `EXEC` | `configurationName, monitorName, resourceGroupName, subscriptionId` |
