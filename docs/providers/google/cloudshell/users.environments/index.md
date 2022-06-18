---
title: users.environments
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
<tr><td><b>Name</b></td><td><code>users.environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.cloudshell.users.environments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
| ---- | -------- | ----------- |
| `id` | `string` | Output only. The environment's identifier, unique among the user's environments. |
| `name` | `string` | Immutable. Full name of this resource, in the format `users/{owner_email}/environments/{environment_id}`. `{owner_email}` is the email address of the user to whom this environment belongs, and `{environment_id}` is the identifier of this environment. For example, `users/someone@example.com/environments/default`. |
| `publicKeys` | `array` | Output only. Public keys associated with the environment. Clients can connect to this environment via SSH only if they possess a private key corresponding to at least one of these public keys. Keys can be added to or removed from the environment using the AddPublicKey and RemovePublicKey methods. |
| `sshUsername` | `string` | Output only. Username that clients should use when initiating SSH sessions with the environment. |
| `state` | `string` | Output only. Current execution state of this environment. |
| `webHost` | `string` | Output only. Host to which clients can connect to initiate HTTPS or WSS connections with the environment. |
| `dockerImage` | `string` | Required. Immutable. Full path to the Docker image used to run this environment, e.g. "gcr.io/dev-con/cloud-devshell:latest". |
| `sshPort` | `integer` | Output only. Port to which clients can connect to initiate SSH sessions with the environment. |
| `sshHost` | `string` | Output only. Host to which clients can connect to initiate SSH sessions with the environment. |
## Methods
| Name | Accessible by | Required Params | Description |
| ---- | ------------- | --------------- | ----------- |
| `get` | `SELECT` | `environmentsId, usersId` | Gets an environment. Returns NOT_FOUND if the environment does not exist. |
| `addPublicKey` | `EXEC` | `environmentsId, usersId` | Adds a public SSH key to an environment, allowing clients with the corresponding private key to connect to that environment via SSH. If a key with the same content already exists, this will error with ALREADY_EXISTS. |
| `authorize` | `EXEC` | `environmentsId, usersId` | Sends OAuth credentials to a running environment on behalf of a user. When this completes, the environment will be authorized to run various Google Cloud command line tools without requiring the user to manually authenticate. |
| `removePublicKey` | `EXEC` | `environmentsId, usersId` | Removes a public SSH key from an environment. Clients will no longer be able to connect to the environment using the corresponding private key. If a key with the same content is not present, this will error with NOT_FOUND. |
| `start` | `EXEC` | `environmentsId, usersId` | Starts an existing environment, allowing clients to connect to it. The returned operation will contain an instance of StartEnvironmentMetadata in its metadata field. Users can wait for the environment to start by polling this operation via GetOperation. Once the environment has finished starting and is ready to accept connections, the operation will contain a StartEnvironmentResponse in its response field. |
