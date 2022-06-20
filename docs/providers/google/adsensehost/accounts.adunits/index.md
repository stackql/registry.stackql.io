---
title: accounts.adunits
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
<tr><td><b>Name</b></td><td><code>accounts.adunits</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.adsensehost.accounts.adunits</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique identifier of this ad unit. This should be considered an opaque identifier; it is not safe to rely on it being in any particular format. |
| `name` | `string` | Name of this ad unit. |
| `mobileContentAdsSettings` | `object` | Settings specific to WAP mobile content ads (AFMC - deprecated). |
| `status` | `string` | Status of this ad unit. Possible values are:<br />NEW: Indicates that the ad unit was created within the last seven days and does not yet have any activity associated with it.<br /><br />ACTIVE: Indicates that there has been activity on this ad unit in the last seven days.<br /><br />INACTIVE: Indicates that there has been no activity on this ad unit in the last seven days. |
| `code` | `string` | Identity code of this ad unit, not necessarily unique across ad clients. |
| `contentAdsSettings` | `object` | Settings specific to content ads (AFC) and highend mobile content ads (AFMC - deprecated). |
| `customStyle` | `object` |  |
| `kind` | `string` | Kind of resource this is, in this case adsensehost#adUnit. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountId, adClientId, adUnitId` | Get the specified host ad unit in this AdSense account. |
| `list` | `SELECT` | `accountId, adClientId` | List all ad units in the specified publisher's AdSense account. |
| `insert` | `INSERT` | `accountId, adClientId` | Insert the supplied ad unit into the specified publisher AdSense account. |
| `delete` | `DELETE` | `accountId, adClientId, adUnitId` | Delete the specified ad unit from the specified publisher AdSense account. |
| `getAdCode` | `EXEC` | `accountId, adClientId, adUnitId` | Get ad code for the specified ad unit, attaching the specified host custom channels. |
| `patch` | `EXEC` | `accountId, adClientId, adUnitId` | Update the supplied ad unit in the specified publisher AdSense account. This method supports patch semantics. |
| `update` | `EXEC` | `accountId, adClientId` | Update the supplied ad unit in the specified publisher AdSense account. |
