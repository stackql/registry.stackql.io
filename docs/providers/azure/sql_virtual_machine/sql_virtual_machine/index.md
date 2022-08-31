---
title: sql_virtual_machine
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_virtual_machine
  - sql_virtual_machine
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
<tr><td><b>Name</b></td><td><code>sql_virtual_machine</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql_virtual_machine.sql_virtual_machine</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `keyVaultCredentialSettings` | `object` | Configure your SQL virtual machine to be able to connect to the Azure Key Vault service. |
| `virtualMachineResourceId` | `string` | ARM Resource id of underlying virtual machine created from SQL marketplace image. |
| `provisioningState` | `string` | Provisioning state to track the async operation status. |
| `sqlImageSku` | `string` | SQL Server edition type. |
| `location` | `string` | The geo-location where the resource lives |
| `autoPatchingSettings` | `object` | Set a patching window during which Windows and SQL patches will be applied. |
| `wsfcDomainCredentials` | `object` | Domain credentials for setting up Windows Server Failover Cluster for SQL availability group. |
| `assessmentSettings` | `object` | Configure assessment for databases in your SQL virtual machine. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `wsfcStaticIp` | `string` | Domain credentials for setting up Windows Server Failover Cluster for SQL availability group. |
| `serverConfigurationsManagementSettings` | `object` | Set the connectivity, storage and workload settings. |
| `autoBackupSettings` | `object` | Configure backups for databases in your SQL virtual machine. |
| `sqlVirtualMachineGroupResourceId` | `string` | ARM resource id of the SQL virtual machine group this SQL virtual machine is or will be part of. |
| `sqlImageOffer` | `string` | SQL image offer. Examples include SQL2016-WS2016, SQL2017-WS2016. |
| `storageConfigurationSettings` | `object` | Storage Configurations for SQL Data, Log and TempDb. |
| `tags` | `object` | Resource tags. |
| `sqlManagement` | `string` | SQL Server Management type. |
| `sqlServerLicenseType` | `string` | SQL Server license type. |
| `identity` | `object` | Azure Active Directory identity configuration for a resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SqlVirtualMachines_List` | `SELECT` | `subscriptionId` | Gets all SQL virtual machines in a subscription. |
| `SqlVirtualMachines_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all SQL virtual machines in a resource group. |
| `SqlVirtualMachines_ListBySqlVmGroup` | `SELECT` | `resourceGroupName, sqlVirtualMachineGroupName, subscriptionId` | Gets the list of sql virtual machines in a SQL virtual machine group. |
| `SqlVirtualMachines_CreateOrUpdate` | `INSERT` | `resourceGroupName, sqlVirtualMachineName, subscriptionId, data__location` | Creates or updates a SQL virtual machine. |
| `SqlVirtualMachines_Delete` | `DELETE` | `resourceGroupName, sqlVirtualMachineName, subscriptionId` | Deletes a SQL virtual machine. |
| `SqlVirtualMachines_Get` | `EXEC` | `resourceGroupName, sqlVirtualMachineName, subscriptionId` | Gets a SQL virtual machine. |
| `SqlVirtualMachines_Redeploy` | `EXEC` | `resourceGroupName, sqlVirtualMachineName, subscriptionId` | Uninstalls and reinstalls the SQL Iaas Extension. |
| `SqlVirtualMachines_StartAssessment` | `EXEC` | `resourceGroupName, sqlVirtualMachineName, subscriptionId` | Starts Assessment on SQL virtual machine. |
| `SqlVirtualMachines_Update` | `EXEC` | `resourceGroupName, sqlVirtualMachineName, subscriptionId` | Updates a SQL virtual machine. |