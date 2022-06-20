---
title: liasettings
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and Deploy Cloud Infrastructure and Resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>liasettings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.content.liasettings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "`content#liasettingsListResponse`". |
| `nextPageToken` | `string` | The token for the retrieval of the next page of LIA settings. |
| `resources` | `array` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountId, merchantId` | Retrieves the LIA settings of the account. |
| `list` | `SELECT` | `merchantId` | Lists the LIA settings of the sub-accounts in your Merchant Center account. |
| `custombatch` | `EXEC` |  | Retrieves and/or updates the LIA settings of multiple accounts in a single request. |
| `getaccessiblegmbaccounts` | `EXEC` | `accountId, merchantId` | Retrieves the list of accessible Google My Business accounts. |
| `listposdataproviders` | `EXEC` |  | Retrieves the list of POS data providers that have active settings for the all eiligible countries. |
| `requestgmbaccess` | `EXEC` | `accountId, gmbEmail, merchantId` | Requests access to a specified Google My Business account. |
| `requestinventoryverification` | `EXEC` | `accountId, country, merchantId` | Requests inventory validation for the specified country. |
| `setinventoryverificationcontact` | `EXEC` | `accountId, contactEmail, contactName, country, language, merchantId` | Sets the inventory verification contract for the specified country. |
| `setposdataprovider` | `EXEC` | `accountId, country, merchantId` | Sets the POS data provider for the specified country. |
| `update` | `EXEC` | `accountId, merchantId` | Updates the LIA settings of the account. Any fields that are not provided are deleted from the resource. |
