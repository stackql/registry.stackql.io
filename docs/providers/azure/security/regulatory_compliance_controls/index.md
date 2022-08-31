---
title: regulatory_compliance_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - regulatory_compliance_controls
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
<tr><td><b>Name</b></td><td><code>regulatory_compliance_controls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security.regulatory_compliance_controls</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| `name` | `string` | The name of the resource |
| `description` | `string` | The description of the regulatory compliance control |
| `skippedAssessments` | `integer` | The number of supported regulatory compliance assessments of the given control with a skipped state |
| `state` | `string` | Aggregative state based on the control's supported assessments states |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `failedAssessments` | `integer` | The number of supported regulatory compliance assessments of the given control with a failed state |
| `passedAssessments` | `integer` | The number of supported regulatory compliance assessments of the given control with a passed state |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RegulatoryComplianceControls_List` | `SELECT` | `api-version, regulatoryComplianceStandardName, subscriptionId` | All supported regulatory compliance controls details and state for selected standard |
| `RegulatoryComplianceControls_Get` | `EXEC` | `api-version, regulatoryComplianceControlName, regulatoryComplianceStandardName, subscriptionId` | Selected regulatory compliance control details and state |
