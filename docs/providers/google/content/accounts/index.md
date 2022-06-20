---
title: accounts
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
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.content.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `resources` | `array` |  |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "`content#accountsListResponse`". |
| `nextPageToken` | `string` | The token for the retrieval of the next page of accounts. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountId, merchantId` | Retrieves a Merchant Center account. |
| `list` | `SELECT` | `merchantId` | Lists the sub-accounts in your Merchant Center account. |
| `insert` | `INSERT` | `merchantId` | Creates a Merchant Center sub-account. |
| `delete` | `DELETE` | `accountId, merchantId` | Deletes a Merchant Center sub-account. |
| `authinfo` | `EXEC` |  | Returns information about the authenticated user. |
| `claimwebsite` | `EXEC` | `accountId, merchantId` | Claims the website of a Merchant Center sub-account. |
| `custombatch` | `EXEC` |  | Retrieves, inserts, updates, and deletes multiple Merchant Center (sub-)accounts in a single request. |
| `link` | `EXEC` | `accountId, merchantId` | Performs an action on a link between two Merchant Center accounts, namely accountId and linkedAccountId. |
| `listlinks` | `EXEC` | `accountId, merchantId` | Returns the list of accounts linked to your Merchant Center account. |
| `requestphoneverification` | `EXEC` | `accountId, merchantId` | Request verification code to start phone verification. |
| `update` | `EXEC` | `accountId, merchantId` | Updates a Merchant Center account. Any fields that are not provided are deleted from the resource. |
| `updatelabels` | `EXEC` | `accountId, merchantId` | Updates labels that are assigned to the Merchant Center account by CSS user. |
| `verifyphonenumber` | `EXEC` | `accountId, merchantId` | Validates verification code to verify phone number for the account. If successful this will overwrite the value of `accounts.businessinformation.phoneNumber`. Only verified phone number will replace an existing verified phone number. |
