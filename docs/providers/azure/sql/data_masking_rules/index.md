---
title: data_masking_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - data_masking_rules
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
<tr><td><b>Name</b></td><td><code>data_masking_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.data_masking_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The rule Id. |
| `columnName` | `string` | The column name on which the data masking rule is applied. |
| `kind` | `string` | The kind of Data Masking Rule. Metadata, used for Azure portal. |
| `location` | `string` | The location of the data masking rule. |
| `replacementString` | `string` | If maskingFunction is set to Text, the character to use for masking the unexposed part of the string. Otherwise, this parameter will be ignored. |
| `suffixSize` | `string` | If maskingFunction is set to Text, the number of characters to show unmasked at the end of the string. Otherwise, this parameter will be ignored. |
| `tableName` | `string` | The table name on which the data masking rule is applied. |
| `prefixSize` | `string` | If maskingFunction is set to Text, the number of characters to show unmasked in the beginning of the string. Otherwise, this parameter will be ignored. |
| `ruleState` | `string` | The rule state. Used to delete a rule. To delete an existing rule, specify the schemaName, tableName, columnName, maskingFunction, and specify ruleState as disabled. However, if the rule doesn't already exist, the rule will be created with ruleState set to enabled, regardless of the provided value of ruleState. |
| `aliasName` | `string` | The alias name. This is a legacy parameter and is no longer used. |
| `numberTo` | `string` | The numberTo property of the data masking rule. Required if maskingFunction is set to Number, otherwise this parameter will be ignored. |
| `numberFrom` | `string` | The numberFrom property of the masking rule. Required if maskingFunction is set to Number, otherwise this parameter will be ignored. |
| `maskingFunction` | `string` | The masking function that is used for the data masking rule. |
| `schemaName` | `string` | The schema name on which the data masking rule is applied. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DataMaskingRules_ListByDatabase` | `SELECT` | `dataMaskingPolicyName, databaseName, resourceGroupName, serverName, subscriptionId` | Gets a list of database data masking rules. |
| `DataMaskingRules_CreateOrUpdate` | `INSERT` | `dataMaskingPolicyName, dataMaskingRuleName, databaseName, resourceGroupName, serverName, subscriptionId` | Creates or updates a database data masking rule. |