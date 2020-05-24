GoogleCloudPlatform/berglas

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='137'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1177' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/berglas#berglas)Berglas

[![68747470733a2f2f696d672e736869656c64732e696f2f7472617669732f636f6d2f476f6f676c65436c6f7564506c6174666f726d2f626572676c61732f6d61737465722e7376673f7374796c653d666c61742d737175617265](../_resources/847c2782f28eb37d97fb8513e0221edb.png)](https://travis-ci.com/GoogleCloudPlatform/berglas)[![68747470733a2f2f696d672e736869656c64732e696f2f62616467652f676f2d646f63756d656e746174696f6e2d626c75652e7376673f7374796c653d666c61742d737175617265](:/bdcda2b9db44cb9dbcfded925ccab9c5)](https://godoc.org/github.com/GoogleCloudPlatform/berglas)

[![berglas.png](../_resources/9609fa9877d773f3e6a16e5d749825f8.png)](https://github.com/GoogleCloudPlatform/berglas/blob/master/logos/berglas.svg)

Berglas is a command line tool and library for storing and and retrieving secrets on Google Cloud. Secrets are encrypted with [Cloud KMS](https://cloud.google.com/kms) and stored in [Cloud Storage](https://cloud.google.com/storage).

- As a **CLI**, `berglas` automates the process of encrypting, decrypting, and storing data on Google Cloud.
- As a **library**, `berglas` automates the inclusion of secrets into various Google Cloud runtimes

**Berglas is not an officially supported Google product.**

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='138'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1188' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/berglas#setup)Setup

1. Install the [Cloud SDK](https://cloud.google.com/sdk) for your operating system. Alternatively, you can run these commands from [Cloud Shell](https://cloud.google.com/shell), which has the SDK and other popular tools pre-installed.

If you are running from your local machine, you also need Default Application Credentials:

	gcloud auth application-default login

This will open a web browser and prompt for a login to your Google account. On headless devices, you will need to create a service account. For more information, please see the [authentication](https://github.com/GoogleCloudPlatform/berglas#authentication) section.

2. Install the `berglas` CLI using **one** of the following methods:

    - Install a pre-compiled binary for your operating system:
        - [darwin/amd64](https://storage.googleapis.com/berglas/master/darwin_amd64/berglas)
        - [linux/amd64](https://storage.googleapis.com/berglas/master/linux_amd64/berglas)
        - [windows/amd64](https://storage.googleapis.com/berglas/master/windows_amd64/berglas)

This will download the latest version built against the master branch. To download a specific version, specify a git tag in place of "master" in the URL.

    - Use the official Docker container:

	docker pull gcr.io/berglas/berglas:latest

This will pull the latest version built against the master branch. To use a specific version, specify a git tag in place of "latest" in the URL.

    - Install from source (requires a working Go installation):

	go get github.com/GoogleCloudPlatform/berglas/...
	go install github.com/GoogleCloudPlatform/berglas

3. Export your project ID as an environment variable. The rest of this setup guide assumes this environment variable is set:

	export PROJECT_ID=my-gcp-project-id

Please note, this is the project *ID*, not the project *name* or project*number*. You can find the project ID by running `gcloud projects list` or in the web UI.

4. Export your desired Cloud Storage bucket name. The rest of this setup guide assumes this environment variable is set:

	export BUCKET_ID=my-secrets

Replace `my-secrets` with the name of your bucket. **This bucket should not exist yet!**

5. Enable required services on the project:

	gcloud services enable --project ${PROJECT_ID} \
	  cloudkms.googleapis.com \
	  storage-api.googleapis.com \
	  storage-component.googleapis.com

6. Bootstrap a Berglas environment. This will create a new Cloud Storage bucket for storing secrets and a Cloud KMS key for encrypting data.

	berglas bootstrap --project $PROJECT_ID --bucket $BUCKET_ID

This command uses the default values. You can customize the storage bucket and KMS key configuration using the optional flags. Run `berglas bootstrap -h` for more details.

If you want full control over the creation of the Cloud Storage and Cloud KMS keys, please see the [custom setup documentation](https://github.com/GoogleCloudPlatform/berglas/blob/master/doc/custom-setup.md).

7. *(Optional)* Enable [Cloud Audit logging](https://cloud.google.com/logging/docs/audit/configure-data-access#config-api) on the bucket:

Please note this will enable audit logging on all Cloud KMS keys and all Cloud Storage buckets in the project, which may incur additional costs.

    1. Download the exiting project IAM policy:

	gcloud projects get-iam-policy ${PROJECT_ID} > policy.yaml

    2. Add Cloud Audit logging for Cloud KMS and Cloud Storage:

	cat <<EOF >> policy.yaml
	auditConfigs:

	- auditLogConfigs:
	  - logType: DATA_READ
	  - logType: ADMIN_READ
	  - logType: DATA_WRITE

	  service: cloudkms.googleapis.com

	- auditLogConfigs:
	  - logType: ADMIN_READ
	  - logType: DATA_READ
	  - logType: DATA_WRITE

	  service: storage.googleapis.com
	EOF

    3. Submit the new policy:

	gcloud projects set-iam-policy ${PROJECT_ID} policy.yaml

    4. Remove the updated policy from local disk:

	rm policy.yaml

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='139'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1238' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/berglas#cli-usage)CLI Usage

1. Create a secret:

	berglas create my-secrets/foo my-secret-data \
	  --key projects/${PROJECT_ID}/locations/global/keyRings/my-keyring/cryptoKeys/my-key
	Successfully created secret: foo

2. Grant access to a secret:

	berglas grant my-secrets/foo --member user:user@mydomain.com

3. Access a secret's data:

	berglas access my-secrets/foo
	my-secret-data

4. Spawn a child process with secrets populated in the child's environment:

	berglas exec -- myapp --flag-a --flag-b

This will spawn `myapp` with an environment parsed by berglas. This will only work when run from a GCP resource. To parse local environment variables, use the `--local` flag. For more information, please run `berglas exec -h`.

5. Revoke access to a secret:

	berglas revoke my-secrets/foo --member user:user@mydomain.com

6. Delete a secret:

	berglas delete my-secrets/foo
	Successfully deleted secret if it existed: foo

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='140'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1254' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/berglas#integrations)Integrations

- **Cloud Run** - When invoked via [Cloud Run](https://cloud.google.com/run), Berglas resolves environment variables to their plaintext values using the [`berglas://`reference syntax](https://github.com/GoogleCloudPlatform/berglas/blob/master/doc/reference-syntax.md). This integration works with any language runtime because berglas serves as the entrypoint to the Docker container. See[examples/cloudrun](https://github.com/GoogleCloudPlatform/berglas/blob/master/examples/cloudrun) for examples and invocations.
- **Cloud Functions** - When invoked via [Cloud Functions](https://cloud.google.com/functions), Berglas resolves environment variables to their plainext values using the[`berglas://` reference syntax](https://github.com/GoogleCloudPlatform/berglas/blob/master/doc/reference-syntax.md). This integration only works with the Go language runtime because it requires importing the `auto/`package. See [examples/cloudfunctions](https://github.com/GoogleCloudPlatform/berglas/blob/master/examples/cloudfunctions) for examples and invocations.
- **Cloud Build** - When invoked via [Cloud Build](https://cloud.google.com/cloud-build), Berglas resolves environment variables to plainext values using the [`berglas://`reference syntax](https://github.com/GoogleCloudPlatform/berglas/blob/master/doc/reference-syntax.md). This integration only works with volume mounts, so all Berglas secrets need to specify the `?destination` parameter. See [examples/cloudbuild](https://github.com/GoogleCloudPlatform/berglas/blob/master/examples/cloudbuild) for examples and invocations.
- **Kubernetes** - Kubernetes pods can consume Berglas secrets by installing a[MutatingWebhook](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/). This webhook mutates incoming pods with the[`berglas://` reference syntax](https://github.com/GoogleCloudPlatform/berglas/blob/master/doc/reference-syntax.md) in environment references to resolve at runtime. This integration works with any container, but all pods requesting berglas secrets must set an command in their Kubernetes manifests. See [examples/kubernetes](https://github.com/GoogleCloudPlatform/berglas/blob/master/examples/kubernetes) for samples and installation instructions.
- **Anything** - Wrap any process with `berglas exec --local` and Berglas will parse any local environment variables with the [`berglas://` reference syntax](https://github.com/GoogleCloudPlatform/berglas/blob/master/doc/reference-syntax.md) and spawn your app as a subprocess with the plaintext environment replaced. This is great for initd, systemd, or non-containerized workloads.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='141'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1267' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/berglas#examples)Examples

Examples are available in the [`examples/` folder](https://github.com/GoogleCloudPlatform/berglas/blob/master/examples).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='142'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1270' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/berglas#library-usage)Library Usage

Berglas is also a Go library that can be imported in Go projects:
import (
_ "github.com/GoogleCloudPlatform/berglas/pkg/auto")
When imported, the `berglas` package will:

1. Detect the runtime environment and call the appropriate API to get the list of environment variables that were set on the resource at deploy time

2. Download and decrypt any secrets that match the [Berglas environment variable reference syntax](https://github.com/GoogleCloudPlatform/berglas/blob/master/doc/reference-syntax.md)

3. Replace the value for the environment variable with the decrypted secret
You can also opt out of auto-parsing and call the library yourself instead:

import ("context""log""os""github.com/GoogleCloudPlatform/berglas/pkg/berglas")func  main() {ctx  := context.Background()// This higher-level API parses the secret reference at the specified// environment variable, downloads and decrypts the secret, and replaces the// contents of the given environment variable with the secret result.if  err  := berglas.Replace(ctx, "MY_SECRET"); err != nil {

log.Fatal(err)

}// This lower-level API parses the secret reference, downloads and decrypts// the secret, and returns the result. This is useful if you need to mutate// the result.if  v  := os.Getenv("MY_SECRET"); v != "" {plaintext, err  := berglas.Resolve(ctx, v)if err != nil {

log.Fatal(err)
}
os.Unsetenv("MY_SECRET")
os.Setenv("MY_OTHER_SECRET", string(plaintext))
}
}

For more examples and documentation, please see the [godoc](https://godoc.org/github.com/GoogleCloudPlatform/berglas).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='143'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1285' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/berglas#authentication)Authentication

By default, Berglas uses Google Cloud Default Application Credentials. If you have [gcloud](https://cloud.google.com/sdk) installed locally, ensure you have application default credentials:

	gcloud auth application-default login

On GCP services (like Cloud Build, Compute, etc), it will use the service account attached to the resource.

To use a specific service account, set the `GOOGLE_APPLICATION_CREDENTIALS`environment variable to the *filepath* to the JSON file where your credentials reside on disk:

	export GOOGLE_APPLICATION_CREDENTIALS=/path/to/my/credentials.json

To learn more, please see the [Google Cloud Service Account documentation](https://cloud.google.com/iam/docs/service-accounts).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='144'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1292' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/berglas#authorization)Authorization

To control who or what has access to a secret, use `berglas grant` and `berglas revoke` or the associated API methods. These methods use [Cloud IAM](https://cloud.google.com/iam)internally. The following information is relevant only if you plan to grant IAM permissions manually:

Most operations require access to the Cloud KMS key and the Cloud Storage bucket. You can read more about [Cloud KMS IAM](https://cloud.google.com/kms/docs/iam) and [Cloud Storage IAM](https://cloud.google.com/storage/docs/access-control/iam) in the documentation.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='145'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1296' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/berglas#create)Create

To create a secret, the following role is required on the Cloud Storage bucket:

	roles/storage.objectCreator

To create a secret, the following role is required for the Cloud KMS key:

	roles/cloudkms.cryptoKeyEncrypter

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='146'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1300' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/berglas#access)Access

To access a secret, the following role is required on the Cloud Storage bucket:

	roles/storage.objectViewer

To access a secret, the following role is required for the Cloud KMS key:

	roles/cloudkms.cryptoKeyDecrypter

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='147'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1304' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/berglas#delete)Delete

To delete a secret, the following role is required on the Cloud Storage bucket:

	roles/storage.objectAdmin

To delete a secret, no permissions are needed on the Cloud KMS key.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='148'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1308' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/berglas#implementation)Implementation

This section describes the implementation. This knowledge is not required to use Berglas, but it is included for security-conscious/curious users who want to learn about how Berglas works internally to build a threat model.

When encrypting a secret:

1. Berglas generates an AES-256-GCM data encryption key (DEK) using [Go's crypto package](https://golang.org/pkg/crypto/) for each secret. (N.B. each secret has its own, unique DEK).

2. Berglas encrypts the plaintext data using the locally-generated DEK, producing encrypted ciphertext, prepended with the AES-GCM nonce.

3. Berglas encrypts the DEK using the specified Cloud KMS key, also known as a key encryption key (KEK). This process is called [envelope encryption](https://cloud.google.com/kms/docs/envelope-encryption).

4. Berglas stores the Cloud KMS key name, encrypted DEK, and encrypted ciphertext as a single blob in Cloud Storage.

When decrypting a secret:

1. Berglas downloads the blob from Cloud Storage and separates the Cloud KMS key name, encrypted DEK, and ciphertext out of the blob.

2. Berglas decrypts the DEK using Cloud KMS. This is part of [envelope encryption](https://cloud.google.com/kms/docs/envelope-encryption).

3. Berglas decrypts the ciphertext data locally using the decrypted DEK.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='149'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1329' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/berglas#security--threat-model)Security & Threat Model

Berglas makes certain security tradeoffs in exchange for a better UX. In particular, KMS crypto key IDs are stored on the secret object's metadata. **An attacker with permission to write objects to your Cloud Storage bucket could overwrite existing secrets.** As such, you should follow the principles of least privilege as revoke default ACLs on the bucket as described in the setup guide.

For more information, please see the [security and threat model](https://github.com/GoogleCloudPlatform/berglas/blob/master/doc/threat-model.md).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='150'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1333' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/berglas#faq)FAQ

**Q: Is there a size limit on the data I can encrypt?**

Berglas is targeted at application secrets like certificates, passwords, and API keys. While its possible to encrypt larger binary files like PDFs or images, Berglas uses a a GCM cipher mode to encrypt data, meaning the data must fit in memory and is [limited to 64GiB](https://crypto.stackexchange.com/questions/31793/plain-text-size-limits-for-aes-gcm-mode-just-64gb).

**Q: Why do you use [envelope encryption](https://cloud.google.com/kms/docs/envelope-encryption) instead of encrypting the data directly with [Cloud KMS](https://cloud.google.com/kms)?**

Envelope encryption allows for encrypting the data at the *application layer*, and it enables encryption of larger payloads, since Cloud KMS has a limit on the size of the payload it can encrypt. By using envelope encryption, Cloud KMS always encrypts a fixed size data (the AES-256-GCM key). This saves bandwidth (since large payloads are encrypted locally) and increases the size of the data which can be encrypted.

**Q: Why does Berglas need permission to view my GCP resource?**

Berglas communicates with the API to read the environment variables that were set on the resource at deploy time. Otherwise, a package could inject arbitrary environment variables in the Berglas format during application boot.

**Q: I renamed a secret in Cloud Storage and now it fails to decrypt - why?**

Berglas encrypts secrets with additional authenticated data including the name of the secret. This reduces the chance an attacker can escalate privilege by convincing someone to rename a secret so they can gain access.

**Q: Why is it named Berglas?**
Berglas is a famous magician who is best known for his secrets.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='151'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1346' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/berglas#contributing)Contributing

Please see the [contributing guidelines](https://github.com/GoogleCloudPlatform/berglas/tree/master/CONTRIBUTING.md).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='152'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1349' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/berglas#license)License

This library is licensed under Apache 2.0. Full license text is available in[LICENSE](https://github.com/GoogleCloudPlatform/berglas/tree/master/LICENSE).