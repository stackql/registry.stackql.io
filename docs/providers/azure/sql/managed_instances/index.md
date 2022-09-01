---
title: managed_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_instances
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
<tr><td><b>Name</b></td><td><code>managed_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `proxyOverride` | `string` | Connection type used for connecting to the instance. |
| `identity` | `object` | Azure Active Directory identity configuration for a resource. |
| `dnsZonePartner` | `string` | The resource id of another managed instance whose DNS zone this managed instance will share after creation. |
| `keyId` | `string` | A CMK URI of the key to use for encryption. |
| `maintenanceConfigurationId` | `string` | Specifies maintenance configuration id to apply to this managed instance. |
| `location` | `string` | Resource location. |
| `storageSizeInGB` | `integer` | Storage size in GB. Minimum value: 32. Maximum value: 8192. Increments of 32 GB allowed only. |
| `licenseType` | `string` | The license type. Possible values are 'LicenseIncluded' (regular price inclusive of a new SQL license) and 'BasePrice' (discounted AHB price for bringing your own SQL licenses). |
| `requestedBackupStorageRedundancy` | `string` | The storage account type to be used to store backups for this instance. The options are Local (LocallyRedundantStorage), Zone (ZoneRedundantStorage), Geo (GeoRedundantStorage) and GeoZone(GeoZoneRedundantStorage) |
| `dnsZone` | `string` | The Dns Zone that the managed instance is in. |
| `administratorLogin` | `string` | Administrator username for the managed instance. Can only be specified when the managed instance is being created (and is required for creation). |
| `restorePointInTime` | `string` | Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database. |
| `publicDataEndpointEnabled` | `boolean` | Whether or not the public data endpoint is enabled. |
| `zoneRedundant` | `boolean` | Whether or not the multi-az is enabled. |
| `subnetId` | `string` | Subnet resource ID for the managed instance. |
| `administrators` | `object` | Properties of a active directory administrator. |
| `instancePoolId` | `string` | The Id of the instance pool this managed server belongs to. |
| `primaryUserAssignedIdentityId` | `string` | The resource id of a user assigned identity to be used by default. |
| `administratorLoginPassword` | `string` | The administrator login password (required for managed instance creation). |
| `state` | `string` | The state of the managed instance. |
| `minimalTlsVersion` | `string` | Minimal TLS version. Allowed values: 'None', '1.0', '1.1', '1.2' |
| `fullyQualifiedDomainName` | `string` | The fully qualified domain name of the managed instance. |
| `currentBackupStorageRedundancy` | `string` | The storage account type used to store backups for this instance. The options are Local (LocallyRedundantStorage), Zone (ZoneRedundantStorage), Geo (GeoRedundantStorage) and GeoZone(GeoZoneRedundantStorage) |
| `privateEndpointConnections` | `array` | List of private endpoint connections on a managed instance. |
| `tags` | `object` | Resource tags. |
| `servicePrincipal` | `object` | The managed instance's service principal configuration for a resource. |
| `sku` | `object` | An ARM Resource SKU. |
| `sourceManagedInstanceId` | `string` | The resource identifier of the source managed instance associated with create operation of this instance. |
| `timezoneId` | `string` | Id of the timezone. Allowed values are timezones supported by Windows.<br />Windows keeps details on supported timezones, including the id, in registry under<br />KEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Time Zones.<br />You can get those registry values via SQL Server by querying SELECT name AS timezone_id FROM sys.time_zone_info.<br />List of Ids can also be obtained by executing [System.TimeZoneInfo]::GetSystemTimeZones() in PowerShell.<br />An example of valid timezone id is "Pacific Standard Time" or "W. Europe Standard Time". |
| `collation` | `string` | Collation of the managed instance. |
| `managedInstanceCreateMode` | `string` | Specifies the mode of database creation.<br /><br />Default: Regular instance creation.<br /><br />Restore: Creates an instance by restoring a set of backups to specific point in time. RestorePointInTime and SourceManagedInstanceId must be specified. |
| `provisioningState` | `string` |  |
| `vCores` | `integer` | The number of vCores. Allowed values: 8, 16, 24, 32, 40, 64, 80. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedInstances_List` | `SELECT` | `subscriptionId` | Gets a list of all managed instances in the subscription. |
| `ManagedInstances_ListByInstancePool` | `SELECT` | `instancePoolName, resourceGroupName, subscriptionId` | Gets a list of all managed instances in an instance pool. |
| `ManagedInstances_ListByManagedInstance` | `SELECT` | `managedInstanceName, resourceGroupName, subscriptionId` | Get top resource consuming queries of a managed instance. |
| `ManagedInstances_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of managed instances in a resource group. |
| `ManagedInstances_CreateOrUpdate` | `INSERT` | `managedInstanceName, resourceGroupName, subscriptionId, data__location` | Creates or updates a managed instance. |
| `ManagedInstances_Delete` | `DELETE` | `managedInstanceName, resourceGroupName, subscriptionId` | Deletes a managed instance. |
| `ManagedInstances_Failover` | `EXEC` | `managedInstanceName, resourceGroupName, subscriptionId` | Failovers a managed instance. |
| `ManagedInstances_Get` | `EXEC` | `managedInstanceName, resourceGroupName, subscriptionId` | Gets a managed instance. |
| `ManagedInstances_Update` | `EXEC` | `managedInstanceName, resourceGroupName, subscriptionId` | Updates a managed instance. |
