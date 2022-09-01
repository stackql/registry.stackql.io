---
title: server_advisors
hide_title: false
hide_table_of_contents: false
keywords:
  - server_advisors
  - sql
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
<tr><td><b>Name</b></td><td><code>server_advisors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.server_advisors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `autoExecuteStatusInheritedFrom` | `string` | Gets the resource from which current value of auto-execute status is inherited. Auto-execute status can be set on (and inherited from) different levels in the resource hierarchy. Possible values are 'Subscription', 'Server', 'ElasticPool', 'Database' and 'Default' (when status is not explicitly set on any level). |
| `kind` | `string` | Resource kind. |
| `lastChecked` | `string` | Gets the time when the current resource was analyzed for recommendations by this advisor. |
| `location` | `string` | Resource location. |
| `recommendationsStatus` | `string` | Gets that status of recommendations for this advisor and reason for not having any recommendations. Possible values include, but are not limited to, 'Ok' (Recommendations available),LowActivity (not enough workload to analyze), 'DbSeemsTuned' (Database is doing well), etc. |
| `recommendedActions` | `array` | Gets the recommended actions for this advisor. |
| `advisorStatus` | `string` | Gets the status of availability of this advisor to customers. Possible values are 'GA', 'PublicPreview', 'LimitedPublicPreview' and 'PrivatePreview'. |
| `autoExecuteStatus` | `string` | Gets the auto-execute status (whether to let the system execute the recommendations) of this advisor. Possible values are 'Enabled' and 'Disabled' |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServerAdvisors_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets a list of server advisors. |
| `ServerAdvisors_Get` | `EXEC` | `advisorName, resourceGroupName, serverName, subscriptionId` | Gets a server advisor. |
| `ServerAdvisors_Update` | `EXEC` | `advisorName, resourceGroupName, serverName, subscriptionId` | Updates a server advisor. |
