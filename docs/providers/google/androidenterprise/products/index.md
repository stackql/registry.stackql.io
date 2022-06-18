---
title: products
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
<tr><td><b>Name</b></td><td><code>products</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.androidenterprise.products</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `pageInfo` | `object` | Information about the current page. List operations that supports paging return only one "page" of results. This protocol buffer message describes the page that has been returned. |
| `product` | `array` | Information about a product (e.g. an app) in the Google Play store, for display to an enterprise admin. |
| `tokenPagination` | `object` | Pagination information returned by a List operation when token pagination is enabled. List operations that supports paging return only one "page" of results. This protocol buffer message describes the page that has been returned. When using token pagination, clients should use the next/previous token to get another page of the result. The presence or absence of next/previous token indicates whether a next/previous page is available and provides a mean of accessing this page. ListRequest.page_token should be set to either next_page_token or previous_page_token to access another page. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `enterpriseId, productId` | Retrieves details of a product for display to an enterprise admin. |
| `list` | `SELECT` | `enterpriseId` | Finds approved products that match a query, or all approved products if there is no query. |
| `approve` | `EXEC` | `enterpriseId, productId` |  Approves the specified product and the relevant app permissions, if any. The maximum number of products that you can approve per enterprise customer is 1,000. To learn how to use managed Google Play to design and create a store layout to display approved products to your users, see Store Layout Design.  |
| `generateApprovalUrl` | `EXEC` | `enterpriseId, productId` | Generates a URL that can be rendered in an iframe to display the permissions (if any) of a product. An enterprise admin must view these permissions and accept them on behalf of their organization in order to approve that product. Admins should accept the displayed permissions by interacting with a separate UI element in the EMM console, which in turn should trigger the use of this URL as the approvalUrlInfo.approvalUrl property in a Products.approve call to approve the product. This URL can only be used to display permissions for up to 1 day. |
| `getAppRestrictionsSchema` | `EXEC` | `enterpriseId, productId` | Retrieves the schema that defines the configurable properties for this product. All products have a schema, but this schema may be empty if no managed configurations have been defined. This schema can be used to populate a UI that allows an admin to configure the product. To apply a managed configuration based on the schema obtained using this API, see Managed Configurations through Play. |
| `getPermissions` | `EXEC` | `enterpriseId, productId` | Retrieves the Android app permissions required by this app. |
| `unapprove` | `EXEC` | `enterpriseId, productId` | Unapproves the specified product (and the relevant app permissions, if any) |
