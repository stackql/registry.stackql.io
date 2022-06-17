---
title: release_assets
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
<tr><td><b>Name</b></td><td><code>github.repos.release_assets</code></td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.release_assets</code></td></tr>
<tr><td><b>Description</b></td><td></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `integer` |  |
| `name` | `string` | The file name of the asset. |
| `created_at` | `string` |  |
| `node_id` | `string` |  |
| `size` | `integer` |  |
| `url` | `string` |  |
| `download_count` | `integer` |  |
| `uploader` | `object` | Simple User |
| `content_type` | `string` |  |
| `updated_at` | `string` |  |
| `browser_download_url` | `string` |  |
| `state` | `string` | State of the release asset. |
| `label` | `string` |  |
## Methods
| Name | Required Params | Description | Accessible by |
| ---- | --------------- | ----------- | ------------- |
| `get_release_asset` | `asset_id, owner, repo` | To download the asset's binary content, set the `Accept` header of the request to [`application/octet-stream`](https://docs.github.com/rest/overview/media-types). The API will either redirect the client to the location, or stream it directly if possible. API clients should handle both a `200` or `302` response. | SELECT |
| `list_release_assets` | `owner, release_id, repo` |  | SELECT |
| `delete_release_asset` | `asset_id, owner, repo` |  | DELETE |
| `update_release_asset` | `asset_id, owner, repo` | Users with push access to the repository can edit a release asset. | EXEC |
| `upload_release_asset` | `name, owner, release_id, repo` | This endpoint makes use of [a Hypermedia relation](https://docs.github.com/rest/overview/resources-in-the-rest-api#hypermedia) to determine which URL to access. The endpoint you call to upload release assets is specific to your release. Use the `upload_url` returned in<br />the response of the [Create a release endpoint](https://docs.github.com/rest/reference/repos#create-a-release) to upload a release asset.<br /><br />You need to use an HTTP client which supports [SNI](http://en.wikipedia.org/wiki/Server_Name_Indication) to make calls to this endpoint.<br /><br />Most libraries will set the required `Content-Length` header automatically. Use the required `Content-Type` header to provide the media type of the asset. For a list of media types, see [Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml). For example: <br /><br />`application/zip`<br /><br />GitHub expects the asset data in its raw binary form, rather than JSON. You will send the raw binary content of the asset as the request body. Everything else about the endpoint is the same as the rest of the API. For example,<br />you'll still need to pass your authentication to be able to upload an asset.<br /><br />When an upstream failure occurs, you will receive a `502 Bad Gateway` status. This may leave an empty asset with a state of `starter`. It can be safely deleted.<br /><br />**Notes:**<br />*   GitHub renames asset filenames that have special characters, non-alphanumeric characters, and leading or trailing periods. The "[List assets for a release](https://docs.github.com/rest/reference/repos#list-assets-for-a-release)"<br />endpoint lists the renamed filenames. For more information and help, contact [GitHub Support](https://support.github.com/contact?tags=dotcom-rest-api).<br />*   If you upload an asset with the same filename as another uploaded asset, you'll receive an error and must delete the old file before you can re-upload the new asset. | EXEC |
