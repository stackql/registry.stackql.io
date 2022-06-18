---
title: orders
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
<tr><td><b>Name</b></td><td><code>orders</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.content.orders</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "`content#ordersListResponse`". |
| `nextPageToken` | `string` | The token for the retrieval of the next page of orders. |
| `resources` | `array` |  |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `merchantId, orderId` | Retrieves an order from your Merchant Center account. |
| `list` | `SELECT` | `merchantId` | Lists the orders in your Merchant Center account. |
| `acknowledge` | `EXEC` | `merchantId, orderId` | Marks an order as acknowledged. |
| `advancetestorder` | `EXEC` | `merchantId, orderId` | Sandbox only. Moves a test order from state "`inProgress`" to state "`pendingShipment`". |
| `cancel` | `EXEC` | `merchantId, orderId` | Cancels all line items in an order, making a full refund. |
| `cancellineitem` | `EXEC` | `merchantId, orderId` | Cancels a line item, making a full refund. |
| `canceltestorderbycustomer` | `EXEC` | `merchantId, orderId` | Sandbox only. Cancels a test order for customer-initiated cancellation. |
| `captureOrder` | `EXEC` | `merchantId, orderId` | Capture funds from the customer for the current order total. This method should be called after the merchant verifies that they are able and ready to start shipping the order. This method blocks until a response is received from the payment processsor. If this method succeeds, the merchant is guaranteed to receive funds for the order after shipment. If the request fails, it can be retried or the order may be cancelled. This method cannot be called after the entire order is already shipped. A rejected error code is returned when the payment service provider has declined the charge. This indicates a problem between the PSP and either the merchant's or customer's account. Sometimes this error will be resolved by the customer. We recommend retrying these errors once per day or cancelling the order with reason `failedToCaptureFunds` if the items cannot be held. |
| `createtestorder` | `EXEC` | `merchantId` | Sandbox only. Creates a test order. |
| `createtestreturn` | `EXEC` | `merchantId, orderId` | Sandbox only. Creates a test return. |
| `getbymerchantorderid` | `EXEC` | `merchantId, merchantOrderId` | Retrieves an order using merchant order ID. |
| `gettestordertemplate` | `EXEC` | `merchantId, templateName` | Sandbox only. Retrieves an order template that can be used to quickly create a new order in sandbox. |
| `instorerefundlineitem` | `EXEC` | `merchantId, orderId` | Deprecated. Notifies that item return and refund was handled directly by merchant outside of Google payments processing (e.g. cash refund done in store). Note: We recommend calling the returnrefundlineitem method to refund in-store returns. We will issue the refund directly to the customer. This helps to prevent possible differences arising between merchant and Google transaction records. We also recommend having the point of sale system communicate with Google to ensure that customers do not receive a double refund by first refunding via Google then via an in-store return. |
| `refunditem` | `EXEC` | `merchantId, orderId` | Issues a partial or total refund for items and shipment. |
| `refundorder` | `EXEC` | `merchantId, orderId` | Issues a partial or total refund for an order. |
| `rejectreturnlineitem` | `EXEC` | `merchantId, orderId` | Rejects return on an line item. |
| `returnrefundlineitem` | `EXEC` | `merchantId, orderId` | Returns and refunds a line item. Note that this method can only be called on fully shipped orders. Please also note that the Orderreturns API is the preferred way to handle returns after you receive a return from a customer. You can use Orderreturns.list or Orderreturns.get to search for the return, and then use Orderreturns.processreturn to issue the refund. If the return cannot be found, then we recommend using this API to issue a refund. |
| `setlineitemmetadata` | `EXEC` | `merchantId, orderId` | Sets (or overrides if it already exists) merchant provided annotations in the form of key-value pairs. A common use case would be to supply us with additional structured information about a line item that cannot be provided via other methods. Submitted key-value pairs can be retrieved as part of the orders resource. |
| `shiplineitems` | `EXEC` | `merchantId, orderId` | Marks line item(s) as shipped. |
| `updatelineitemshippingdetails` | `EXEC` | `merchantId, orderId` | Updates ship by and delivery by dates for a line item. |
| `updatemerchantorderid` | `EXEC` | `merchantId, orderId` | Updates the merchant order ID for a given order. |
| `updateshipment` | `EXEC` | `merchantId, orderId` | Updates a shipment's status, carrier, and/or tracking ID. |
