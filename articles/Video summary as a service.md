> Auto-generate visual summaries of videos, with a machine learning model and a serverless pipeline - PicardParis/cherry-on-py

# PicardParis/cherry-on-py
> _This is not an official Google product. This is a tutorial aiming at giving you ideas..._

[](#-hello)👋 Hello!
--------------------

Dear developers,

*   Do you like the adage _"a picture is worth a thousand words"_? I do!
*   Let's check if it also works for _"a picture is worth a thousand frames"_.
*   In this tutorial, you'll see the following:
    *   how to understand the content of a video in a blink,
    *   in less than 300 lines of Python (3.7) code.

Here is a visual summary example, generated from a 2'42" video made of 35 sequences (shots):

[![Video summary example](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/PicardParis/cherry-on-py/raw/master/gcf_video_summary/pics/JaneGoodall.mp4.summary035_still.jpeg)](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/PicardParis/cherry-on-py/blob/master/gcf_video_summary/pics/JaneGoodall.mp4.summary035_still.jpeg)

> Note: The summary is a grid where each cell is a frame representing a video shot.

[](#-objectives)🔭 Objectives
-----------------------------

This tutorial has 2 objectives, 1 practical and 1 technical:

*   Automatically generate visual summaries of videos
*   Build a processing pipeline with these properties:
    *   managed (always ready and easy to set up)
    *   scalable (able to ingest several videos in parallel)
    *   not costing anything when not used

[](#️-tools)🛠️ Tools
---------------------

A few tools are enough:

*   Storage space for videos and results
*   A serverless solution to run the code
*   A machine learning model to analyze videos
*   A library to extract frames from videos
*   A library to generate the visual summaries

[](#-architecture)🧱 Architecture
---------------------------------

Here is a possible architecture using 3 Google Cloud services ([Cloud Storage](https://cloud.google.com/storage/docs), [Cloud Functions](https://cloud.google.com/functions/docs), and [Video Intelligence API](https://cloud.google.com/video-intelligence/docs)):

> [![Architecture](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/PicardParis/cherry-on-py/raw/master/gcf_video_summary/pics/architecture_1.png)](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/PicardParis/cherry-on-py/blob/master/gcf_video_summary/pics/architecture_1.png)

The processing pipeline follows these steps:

1.  You upload a video to the 1st bucket (a bucket is a storage space in the cloud)
2.  The upload event automatically triggers the 1st function
3.  The function sends a request to the Video Intelligence API to detect the shots
4.  The Video Intelligence API analyzes the video and uploads the results (annotations) to the 2nd bucket
5.  The upload event triggers the 2nd function
6.  The function downloads both annotation and video files
7.  The function renders and uploads the summary to the 3rd bucket
8.  The video summary is ready!

[](#-python-libraries)🐍 Python libraries
-----------------------------------------

Open source client libraries let you interface with Google Cloud services in idiomatic Python. You'll use the following:

*   `Cloud Storage`
    *   To manage downloads and uploads
    *   [https://pypi.org/project/google-cloud-storage](https://pypi.org/project/google-cloud-storage)
*   `Video Intelligence API`
    *   To analyze videos
    *   [https://pypi.org/project/google-cloud-videointelligence](https://pypi.org/project/google-cloud-videointelligence)

Here is a choice of 2 additional Python libraries for the graphical needs:

*   `OpenCV`
    *   To extract video frames
    *   There's even a headless version (without GUI features), which is ideal for a service
    *   [https://pypi.org/project/opencv-python-headless](https://pypi.org/project/opencv-python-headless)
*   `Pillow`
    *   To generate the visual summaries
    *   `Pillow` is a very popular imaging library, both extensive and easy to use
    *   [https://pypi.org/project/Pillow](https://pypi.org/project/Pillow)

[](#️-project-setup)⚙️ Project setup
------------------------------------

Assuming you have a Google Cloud account, you can set up the architecture from Cloud Shell with the `gcloud` and `gsutil` commands. This lets you script everything from scratch in a reproducible way.

### [](#environment-variables)Environment variables

# Project
PROJECT\_NAME="Visual Summary"
PROJECT\_ID="visual-summary-REPLACE\_WITH\_UNIQUE\_SUFFIX"
# Cloud Storage region (https://cloud.google.com/storage/docs/locations)
GCS\_REGION="europe-west1"
# Cloud Functions region (https://cloud.google.com/functions/docs/locations)
GCF\_REGION="europe-west1"
# Source
GIT\_REPO="cherry-on-py"
PROJECT\_SRC=~/$PROJECT\_ID/$GIT\_REPO/gcf\_video\_summary

# Cloud Storage buckets (environment variables)
export VIDEO\_BUCKET="b1-videos\_${PROJECT\_ID}"
export ANNOTATION\_BUCKET="b2-annotations\_${PROJECT\_ID}"
export SUMMARY\_BUCKET="b3-summaries\_${PROJECT\_ID}"

> Note: You can use your GitHub username as a unique suffix.

### [](#new-project)New project

gcloud projects create $PROJECT\_ID \\
  --name="$PROJECT\_NAME" \\
  --set-as-default

    Create in progress for [https://cloudresourcemanager.googleapis.com/v1/projects/PROJECT_ID].
    Waiting for [operations/cp...] to finish...done.
    Enabling service [cloudapis.googleapis.com] on project [PROJECT_ID]...
    Operation "operations/acf..." finished successfully.
    Updated property [core/project] to [PROJECT_ID].
    

### [](#billing-account)Billing account

# Link project with billing account (single account)
BILLING\_ACCOUNT=$(gcloud beta billing accounts list \\
 --format 'value(name)')
# Link project with billing account (specific one among multiple accounts)
BILLING\_ACCOUNT=$(gcloud beta billing accounts list  \\
 --format 'value(name)' \\
 --filter "displayName='My Billing Account'")

gcloud beta billing projects link $PROJECT\_ID --billing-account $BILLING\_ACCOUNT

    billingAccountName: billingAccounts/XXXXXX-YYYYYY-ZZZZZZ
    billingEnabled: true
    name: projects/PROJECT_ID/billingInfo
    projectId: PROJECT_ID
    

### [](#buckets)Buckets

# Create buckets with uniform bucket-level access
gsutil mb -b on -c regional -l $GCS\_REGION gs://$VIDEO\_BUCKET
gsutil mb -b on -c regional -l $GCS\_REGION gs://$ANNOTATION\_BUCKET
gsutil mb -b on -c regional -l $GCS\_REGION gs://$SUMMARY\_BUCKET

    Creating gs://VIDEO_BUCKET/...
    Creating gs://ANNOTATION_BUCKET/...
    Creating gs://SUMMARY_BUCKET/...
    

You can check how it looks like in the [Cloud Console](https://console.cloud.google.com/storage/browser):

[![Cloud Storage buckets](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/PicardParis/cherry-on-py/raw/master/gcf_video_summary/pics/buckets.png)](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/PicardParis/cherry-on-py/blob/master/gcf_video_summary/pics/buckets.png)

### [](#service-account)Service account

Create a service account. This is for development purposes only (not needed for production). This provides you with credentials to run your code locally.

mkdir ~/$PROJECT\_ID
cd ~/$PROJECT\_ID

SERVICE\_ACCOUNT\_NAME="dev-service-account"
SERVICE\_ACCOUNT="${SERVICE\_ACCOUNT\_NAME}@${PROJECT\_ID}.iam.gserviceaccount.com"
gcloud iam service-accounts create $SERVICE\_ACCOUNT\_NAME
gcloud iam service-accounts keys create ~/$PROJECT\_ID/key.json --iam-account $SERVICE\_ACCOUNT

    Created service account [SERVICE_ACCOUNT_NAME].
    created key [...] of type [json] as [~/PROJECT_ID/key.json] for [SERVICE_ACCOUNT]
    

Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable and check that it points to the service account key. When you run the application code in the current shell session, client libraries will use these credentials for authentication. If you open a new shell session, set the variable again.

export GOOGLE\_APPLICATION\_CREDENTIALS=~/$PROJECT\_ID/key.json
cat $GOOGLE\_APPLICATION\_CREDENTIALS

    {
      "type": "service_account",
      "project_id": "PROJECT_ID",
      "private_key_id": "...",
      "private_key": "-----BEGIN PRIVATE KEY-----\n...",
      "client_email": "SERVICE_ACCOUNT",
      ...
    }
    

Authorize the service account to access the buckets:

IAM\_BINDING="serviceAccount:${SERVICE\_ACCOUNT}:roles/storage.objectAdmin"
gsutil iam ch $IAM\_BINDING gs://$VIDEO\_BUCKET
gsutil iam ch $IAM\_BINDING gs://$ANNOTATION\_BUCKET
gsutil iam ch $IAM\_BINDING gs://$SUMMARY\_BUCKET

### [](#apis)APIs

A few APIs are enabled by default:

    NAME                              TITLE
    bigquery.googleapis.com           BigQuery API
    bigquerystorage.googleapis.com    BigQuery Storage API
    cloudapis.googleapis.com          Google Cloud APIs
    clouddebugger.googleapis.com      Cloud Debugger API
    cloudtrace.googleapis.com         Cloud Trace API
    datastore.googleapis.com          Cloud Datastore API
    logging.googleapis.com            Cloud Logging API
    monitoring.googleapis.com         Cloud Monitoring API
    servicemanagement.googleapis.com  Service Management API
    serviceusage.googleapis.com       Service Usage API
    sql-component.googleapis.com      Cloud SQL
    storage-api.googleapis.com        Google Cloud Storage JSON API
    storage-component.googleapis.com  Cloud Storage
    

Enable the Video Intelligence and Cloud Functions APIs:

gcloud services enable \\
  videointelligence.googleapis.com \\
  cloudfunctions.googleapis.com

    Operation "operations/acf..." finished successfully.
    

### [](#source-code)Source code

Retrieve the source code:

cd ~/$PROJECT\_ID
git clone https://github.com/PicardParis/$GIT\_REPO.git

    Cloning into 'GIT_REPO'...
    ...
    

[](#-video-analysis)🧠 Video analysis
-------------------------------------

### [](#video-shot-detection)Video shot detection

The Video Intelligence API is a pre-trained machine learning model that can analyze videos. One of the multiple features is video shot detection. For the 1st Cloud Function, here is a possible core function calling `annotate_video()` with the `SHOT_CHANGE_DETECTION` feature:

from google.cloud import storage, videointelligence

def launch\_shot\_detection(video\_uri: str, annot\_bucket: str):
    """ Detect video shots (asynchronous operation)
 Results will be stored in <annot\_uri> with this naming convention:
 - video\_uri: gs://video\_bucket/path/to/video.ext
 - annot\_uri: gs://annot\_bucket/video\_bucket/path/to/video.ext.json
 """
    print(f'Launching shot detection for <{video\_uri}\>...')
    video\_blob \= storage.Blob.from\_string(video\_uri)
    video\_bucket \= video\_blob.bucket.name
    path\_to\_video \= video\_blob.name
    annot\_uri \= f'gs://{annot\_bucket}/{video\_bucket}/{path\_to\_video}.json'

    video\_client \= videointelligence.VideoIntelligenceServiceClient()
    features \= \[videointelligence.enums.Feature.SHOT\_CHANGE\_DETECTION\]
    video\_client.annotate\_video(input\_uri\=video\_uri,
                                features\=features,
                                output\_uri\=annot\_uri)

### [](#local-development-and-tests)Local development and tests

Before deploying the function, you need to develop and test it. Create a Python 3 virtual environment and activate it:

cd ~/$PROJECT\_ID
python3 -m venv venv
source venv/bin/activate

Install the dependencies:

pip install -r $PROJECT\_SRC/gcf1\_detect\_shots/requirements.txt

Check the dependencies:

    Package                        Version
    ------------------------------ ----------
    ...
    google-cloud-storage           1.28.1
    google-cloud-videointelligence 1.14.0
    ...
    

You can use the main scope to test the function in script mode:

import os

ANNOTATION\_BUCKET \= os.getenv('ANNOTATION\_BUCKET', '')
assert ANNOTATION\_BUCKET, 'Undefined ANNOTATION\_BUCKET environment variable'

if \_\_name\_\_ \== '\_\_main\_\_':
    """ Only for local tests """
    import argparse
    parser \= argparse.ArgumentParser()
    parser.add\_argument('video\_uri',
                        type\=str,
                        help\='gs://video\_bucket/path/to/video.ext')
    args \= parser.parse\_args()
    launch\_shot\_detection(args.video\_uri, ANNOTATION\_BUCKET)

> Note: You have already exported the `ANNOTATION_BUCKET` environment variable earlier in the shell session; you will also define it later at deployment stage. This makes the code generic and lets you reuse it independently of the output bucket.

Test the function:

VIDEO\_PATH="cloudmleap/video/next/gbikes\_dinosaur.mp4"
VIDEO\_URI="gs://$VIDEO\_PATH"
python $PROJECT\_SRC/gcf1\_detect\_shots/main.py $VIDEO\_URI

    Launching shot detection for <gs://cloudmleap/video/next/gbikes_dinosaur.mp4>...
    

> Note: The test video `<gbikes_dinosaur.mp4>` is located in an external bucket. This works because the video is publicly accessible.

Wait a moment and check that the annotations have been generated:

gsutil ls -r gs://$ANNOTATION\_BUCKET

    964  YYYY-MM-DDThh:mm:ssZ  gs://ANNOTATION_BUCKET/VIDEO_PATH.json
    TOTAL: 1 objects, 964 bytes (964 B)
    

Check the last 200 bytes of the annotation file:

gsutil cat -r -200 gs://$ANNOTATION\_BUCKET/$VIDEO\_PATH.json

}
    }, {
      "start\_time\_offset": {
        "seconds": 28,
        "nanos": 166666000
      },
      "end\_time\_offset": {
        "seconds": 42,
        "nanos": 766666000
      }
    } \]
  } \]
}

> Note: Those are the start and end positions of the last video shot. Everything seems fine.

Clean up when you're finished:

gsutil rm gs://$ANNOTATION\_BUCKET/$VIDEO\_PATH.json

deactivate

rm -rf venv

### [](#function-entry-point)Function entry point

def gcf\_detect\_shots(data, context):
    """ Cloud Function triggered by a new Cloud Storage object """
    video\_bucket \= data\['bucket'\]
    path\_to\_video \= data\['name'\]
    video\_uri \= f'gs://{video\_bucket}/{path\_to\_video}'
    launch\_shot\_detection(video\_uri, ANNOTATION\_BUCKET)

> Note: This function will be called whenever a video is uploaded to the bucket defined as a trigger.

### [](#function-deployment)Function deployment

Deploy the 1st function:

GCF\_NAME="gcf1\_detect\_shots"
GCF\_SOURCE="$PROJECT\_SRC/gcf1\_detect\_shots"
GCF\_ENTRY\_POINT="gcf\_detect\_shots"
GCF\_TRIGGER\_BUCKET="$VIDEO\_BUCKET"
GCF\_ENV\_VARS="ANNOTATION\_BUCKET=$ANNOTATION\_BUCKET"
GCF\_MEMORY="128MB"

gcloud functions deploy $GCF\_NAME \\
  --runtime python37  \\
  --source $GCF\_SOURCE \\
  --entry-point $GCF\_ENTRY\_POINT \\
  --update-env-vars $GCF\_ENV\_VARS \\
  --trigger-bucket $GCF\_TRIGGER\_BUCKET \\
  --region $GCF\_REGION \\
  --memory $GCF\_MEMORY \\
  --quiet

> Note: The default memory allocated for a Cloud Function is 256 MB (possible values are 128MB, 256MB, 512MB, 1024MB, and 2048MB). As the function has no memory or CPU needs (it sends a simple API request), the minimum memory setting is enough.

    Deploying function (may take a while - up to 2 minutes)...done.
    availableMemoryMb: 128
    entryPoint: gcf_detect_shots
    environmentVariables:
      ANNOTATION_BUCKET: b2-annotations...
    eventTrigger:
      eventType: google.storage.object.finalize
    ...
    status: ACTIVE
    timeout: 60s
    updateTime: 'YYYY-MM-DDThh:mm:ss.mmmZ'
    versionId: '1'
    

> Note: The `ANNOTATION_BUCKET` environment variable is defined with the `--update-env-vars` flag. Using an environment variable lets you deploy the exact same code with different trigger and output buckets.

Here is how it looks like in the [Cloud Console](https://console.cloud.google.com/functions/list):

[![Cloud Functions](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/PicardParis/cherry-on-py/raw/master/gcf_video_summary/pics/functions.png)](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/PicardParis/cherry-on-py/blob/master/gcf_video_summary/pics/functions.png)

### [](#production-tests)Production tests

Make sure to test the function in production. Copy a video into the video bucket:

VIDEO\_NAME="gbikes\_dinosaur.mp4"
SRC\_URI="gs://cloudmleap/video/next/$VIDEO\_NAME"
DST\_URI="gs://$VIDEO\_BUCKET/$VIDEO\_NAME"

gsutil cp $SRC\_URI $DST\_URI

    Copying gs://cloudmleap/video/next/gbikes_dinosaur.mp4 [Content-Type=video/mp4]...
    - [1 files][ 62.0 MiB/ 62.0 MiB]
    Operation completed over 1 objects/62.0 MiB.
    

Query the logs to check that the function has been triggered:

gcloud functions logs read --region $GCF\_REGION

    LEVEL  NAME               EXECUTION_ID  TIME_UTC  LOG
    D      gcf1_detect_shots  ...           ...       Function execution started
    I      gcf1_detect_shots  ...           ...       Launching shot detection for <gs://VIDEO_BUCKET/VIDEO_NAME>...
    D      gcf1_detect_shots  ...           ...       Function execution took 874 ms, finished with status: 'ok'
    

Wait a moment and check the annotation bucket:

gsutil ls -r gs://$ANNOTATION\_BUCKET

You should see the annotation file:

    gs://ANNOTATION_BUCKET/VIDEO_BUCKET/:
    gs://ANNOTATION_BUCKET/VIDEO_BUCKET/VIDEO_NAME.json
    

The 1st function is operational!

[](#️-visual-summary)🎞️ Visual Summary
---------------------------------------

### [](#code-structure)Code structure

It's interesting to split the code into 2 main classes:

*   `StorageHelper` for local file and cloud storage object management
*   `VideoProcessor` for graphical processings

Here is a possible core function:

class VideoProcessor:
    @staticmethod
    def generate\_summary(annot\_uri: str, output\_bucket: str):
        """ Generate a video summary from video shot annotations """
        try:
            with StorageHelper(annot\_uri, output\_bucket) as storage:
                with VideoProcessor(storage) as video\_proc:
                    print('Generating summary...')
                    image \= video\_proc.render\_summary()
                    video\_proc.upload\_summary\_as\_jpeg(image)
        except:
            logging.exception(
                'Could not generate summary from shot annotations <%s>',
                annot\_uri)

> Note: If exceptions are raised, it's handy to log them with `logging.exception()` to get a stack trace in production logs.

### [](#class-storagehelper)Class `StorageHelper`

The class manages the following:

*   The retrieval and parsing of video shot annotations
*   The download of source videos
*   The upload of generated visual summaries
*   File names

class StorageHelper:
    """ Local+Cloud storage helper
 - Uses a temp dir for local processing (e.g. video frame extraction)
 - Paths are relative to this temp dir (named after the output bucket)
 Naming convention:
 - video\_uri:                 gs://video\_bucket/path/to/video.ext
 - annot\_uri:    gs://annot\_bucket/video\_bucket/path/to/video.ext.json
 - video\_path:                     video\_bucket/path/to/video.ext
 - summary\_path:                   video\_bucket/path/to/video.ext.SUFFIX
 - summary\_uri: gs://output\_bucket/video\_bucket/path/to/video.ext.SUFFIX
 """
    client \= storage.Client()
    upload\_bucket: storage.Bucket
    shots: 'VideoShots'
    video\_path: Path
    video\_local\_path: Path

    ANNOT\_EXT \= '.json'
    VideoShots \= List\[VideoShot\]

    def \_\_init\_\_(self, annot\_uri: str, output\_bucket: str):
        if not annot\_uri.endswith(self.ANNOT\_EXT):
            raise RuntimeError(f'annot\_uri must end with <{self.ANNOT\_EXT}\>')
        self.upload\_bucket \= self.client.bucket(output\_bucket)
        self.shots \= self.load\_annotations(annot\_uri)
        self.video\_path \= self.video\_path\_from\_uri(annot\_uri)
        temp\_root \= Path(tempfile.gettempdir(), output\_bucket)
        temp\_root.mkdir(parents\=True, exist\_ok\=True)
        self.video\_local\_path \= temp\_root.joinpath(self.video\_path)

The source video is handled in the `with` statement context manager:

    def \_\_enter\_\_(self):
        self.download\_video()
        return self

    def \_\_exit\_\_(self, exc\_type, exc\_value, traceback):
        self.video\_local\_path.unlink()

> Note: Once downloaded, the video uses memory space in the `/tmp` RAM disk (the only writable space for the serverless function). It's best to delete temporary files when they're not needed anymore, to avoid potential out-of-memory errors on future invocations of the function.

Annotations are retrieved with the methods `storage.Blob.download_as_string()` and `json.loads()`:

    def load\_annotations(self, annot\_uri: str) -> VideoShots:
        json\_blob \= storage.Blob.from\_string(annot\_uri, self.client)
        api\_response \= json.loads(json\_blob.download\_as\_string())
        annotations: Dict \= api\_response\['annotation\_results'\]\[0\]\['shot\_annotations'\]
        return \[VideoShot.from\_dict(annotation) for annotation in annotations\]

The parsing is handled with this `VideoShot` helper class:

class VideoShot(NamedTuple):
    """ Video shot start/end positions in nanoseconds """
    pos1\_ns: int
    pos2\_ns: int
    NANOS\_PER\_SECOND \= 10\*\*9

    @classmethod
    def from\_dict(cls, annotation: Dict) -> 'VideoShot':
        def time\_offset\_in\_ns(time\_offset) -> int:
            seconds: int \= time\_offset.get('seconds', 0)
            nanos: int \= time\_offset.get('nanos', 0)
            return seconds \* cls.NANOS\_PER\_SECOND + nanos
        pos1\_ns \= time\_offset\_in\_ns(annotation\['start\_time\_offset'\])
        pos2\_ns \= time\_offset\_in\_ns(annotation\['end\_time\_offset'\])
        return cls(pos1\_ns, pos2\_ns)

Video shot info can be exposed with a getter and a generator:

    def shot\_count(self) -> int:
        return len(self.shots)

    def gen\_video\_shots(self) -> Iterator\[VideoShot\]:
        for video\_shot in self.shots:
            yield video\_shot

The naming convention was chosen to keep consistent object paths between the different buckets. This also lets you deduce the video path from the annotation URI:

    def video\_path\_from\_uri(self, annot\_uri: str) -> Path:
        annot\_blob \= storage.Blob.from\_string(annot\_uri)
        return Path(annot\_blob.name\[:\-len(self.ANNOT\_EXT)\])

The video is directly downloaded with `storage.Blob.download_to_filename()`:

    def download\_video(self):
        video\_uri \= f'gs://{self.video\_path.as\_posix()}'
        blob \= storage.Blob.from\_string(video\_uri, self.client)
        print(f'Downloading -> {self.video\_local\_path}')
        self.video\_local\_path.parent.mkdir(parents\=True, exist\_ok\=True)
        blob.download\_to\_filename(self.video\_local\_path)

On the opposite, results can be uploaded with `storage.Blob.upload_from_string()`:

    def upload\_summary(self, image\_bytes: bytes, image\_type: str):
        path \= self.summary\_path(image\_type)
        blob \= self.upload\_bucket.blob(path.as\_posix())
        content\_type \= f'image/{image\_type}'
        print(f'Uploading -> {blob.name}')
        blob.upload\_from\_string(image\_bytes, content\_type)

> Note: `from_string` means `from_bytes` here (Python 2 legacy). `Pillow` supports working with memory images, which avoids having to manage local files.

And finally, here is a possible naming convention for the summary files:

    def summary\_path(self, image\_type: str) -> Path:
        video\_name \= self.video\_path.name
        shot\_count \= self.shot\_count()
        suffix \= f'summary{shot\_count:03d}.{image\_type}'
        summary\_name \= f'{video\_name}.{suffix}'
        return Path(self.video\_path.parent, summary\_name)

### [](#class-videoprocessor)Class `VideoProcessor`

The class manages the following:

*   Video frame extraction
*   Visual summary generation

import cv2 as cv
from PIL import Image

from storage\_helper import StorageHelper

class VideoProcessor:
    class ImageSize(NamedTuple):
        w: int
        h: int

    storage: StorageHelper
    video: cv.VideoCapture
    cell\_size: ImageSize
    grid\_size: ImageSize

    def \_\_init\_\_(self, storage: StorageHelper):
        self.storage \= storage

Opening and closing the video is handled in the `with` statement context manager:

    def \_\_enter\_\_(self):
        video\_path \= self.storage.video\_local\_path
        self.video \= cv.VideoCapture(str(video\_path))
        if not self.video.isOpened():
            raise RuntimeError(f'Could not open video <{video\_path}\>')
        self.compute\_grid\_dimensions()
        return self

    def \_\_exit\_\_(self, exc\_type, exc\_value, traceback):
        self.video.release()

The video summary is a grid of cells which can be rendered in a single loop with two generators:

    def render\_summary(self, shot\_ratio: float \= 0.5) -> Image:
        grid\_img \= Image.new('RGB', self.grid\_size, self.RGB\_BACKGROUND)

        img\_and\_pos\_iter \= zip(self.gen\_cell\_img(shot\_ratio),
                               self.gen\_cell\_pos())
        for cell\_img, cell\_pos in img\_and\_pos\_iter:
            cell\_img.thumbnail(self.cell\_size)  \# Make it smaller if needed
            grid\_img.paste(cell\_img, cell\_pos)

        return grid\_img

> Note: `shot_ratio` is set to `0.5` by default to extract video shot middle frames.

The first generator yields cell images:

    def gen\_cell\_img(self, shot\_ratio: float) -> Iterator\['Image'\]:
        assert 0.0 <= shot\_ratio <= 1.0
        MS\_IN\_NS \= 10\*\*6
        for video\_shot in self.storage.gen\_video\_shots():
            pos1\_ns, pos2\_ns \= video\_shot
            pos\_ms \= (pos1\_ns + shot\_ratio\*(pos2\_ns\-pos1\_ns)) / MS\_IN\_NS
            yield self.image\_at\_pos(pos\_ms)

The second generator yields cell positions:

    def gen\_cell\_pos(self) -> Iterator\[Tuple\[int, int\]\]:
        cell\_x, cell\_y \= 0, 0
        while True:
            yield cell\_x, cell\_y
            cell\_x += self.cell\_size.w
            if self.grid\_size.w <= cell\_x:  \# Move to next row?
                cell\_x, cell\_y \= 0, cell\_y+self.cell\_size.h

`OpenCV` easily allows extracting video frames at a given position:

    def image\_at\_pos(self, pos\_ms: float) -> Image:
        self.video.set(cv.CAP\_PROP\_POS\_MSEC, pos\_ms)
        ok, cv\_frame \= self.video.read()
        if not ok:
            raise RuntimeError(f'Failed to get video frame @pos\_ms\[{pos\_ms}\]')
        return Image.fromarray(cv.cvtColor(cv\_frame, cv.COLOR\_BGR2RGB))

Choosing the summary grid composition is arbitrary. Here is an example to compose a summary preserving the video proportions:

    def compute\_grid\_dimensions(self):
        shot\_count \= self.storage.shot\_count()
        if shot\_count < 1:
            raise RuntimeError(f'Expected 1+ video shots (got {shot\_count})')
        \# Try to preserve the video aspect ratio
        \# Consider cells as pixels and try to fit them in a square
        cols \= rows \= int(shot\_count \*\* 0.5 + 0.5)
        if cols \* rows < shot\_count:
            cols += 1
        cell\_w \= int(self.video.get(cv.CAP\_PROP\_FRAME\_WIDTH))
        cell\_h \= int(self.video.get(cv.CAP\_PROP\_FRAME\_HEIGHT))
        if self.SUMMARY\_MAX\_SIZE.w < cell\_w\*cols:
            scale \= self.SUMMARY\_MAX\_SIZE.w / (cell\_w\*cols)
            cell\_w \= int(scale \* cell\_w)
            cell\_h \= int(scale \* cell\_h)
        self.cell\_size \= self.ImageSize(cell\_w, cell\_h)
        self.grid\_size \= self.ImageSize(cell\_w\*cols, cell\_h\*rows)

Finally, `Pillow` gives full control on image serializations:

    def upload\_summary\_as\_jpeg(self, image: Image):
        mem\_file \= BytesIO()
        image\_type \= 'jpeg'
        jpeg\_save\_parameters \= dict(optimize\=True, progressive\=True)
        image.save(mem\_file, format\=image\_type, \*\*jpeg\_save\_parameters)

        image\_bytes \= mem\_file.getvalue()
        self.storage.upload\_summary(image\_bytes, image\_type)

> Note: Working with in-memory images avoids managing local files and uses less memory.

### [](#local-development-and-tests-1)Local development and tests

You can use the main scope to test the function in script mode:

import os

from video\_processor import VideoProcessor

SUMMARY\_BUCKET \= os.getenv('SUMMARY\_BUCKET', '')
assert SUMMARY\_BUCKET, 'Undefined SUMMARY\_BUCKET environment variable'

if \_\_name\_\_ \== '\_\_main\_\_':
    """ Only for local tests """
    import argparse
    parser \= argparse.ArgumentParser()
    parser.add\_argument('annot\_uri',
                        type\=str,
                        help\='gs://annotation\_bucket/path/to/video.ext.json')
    args \= parser.parse\_args()
    VideoProcessor.generate\_summary(args.annot\_uri, SUMMARY\_BUCKET)

Test the function:

cd ~/$PROJECT\_ID
python3 -m venv venv
source venv/bin/activate

pip install -r $PROJECT\_SRC/gcf2\_generate\_summary/requirements.txt

VIDEO\_NAME="gbikes\_dinosaur.mp4"
ANNOTATION\_URI="gs://$ANNOTATION\_BUCKET/$VIDEO\_BUCKET/$VIDEO\_NAME.json"

python $PROJECT\_SRC/gcf2\_generate\_summary/main.py $ANNOTATION\_URI

    Downloading -> /tmp/SUMMARY_BUCKET/VIDEO_BUCKET/VIDEO_NAME
    Generating summary...
    Uploading -> VIDEO_BUCKET/VIDEO_NAME.summary004.jpeg
    

> Note: The uploaded video summary shows 4 shots.

Clean up:

### [](#function-entry-point-1)Function entry point

def gcf\_generate\_summary(data, context):
    """ Cloud Function triggered by a new Cloud Storage object """
    annotation\_bucket \= data\['bucket'\]
    path\_to\_annotation \= data\['name'\]
    annot\_uri \= f'gs://{annotation\_bucket}/{path\_to\_annotation}'
    VideoProcessor.generate\_summary(annot\_uri, SUMMARY\_BUCKET)

> Note: This function will be called whenever an annotation file is uploaded to the bucket defined as a trigger.

### [](#function-deployment-1)Function deployment

GCF\_NAME="gcf2\_generate\_summary"
GCF\_SOURCE="$PROJECT\_SRC/gcf2\_generate\_summary"
GCF\_ENTRY\_POINT="gcf\_generate\_summary"
GCF\_TRIGGER\_BUCKET="$ANNOTATION\_BUCKET"
GCF\_ENV\_VARS="SUMMARY\_BUCKET=$SUMMARY\_BUCKET"
GCF\_TIMEOUT="540s"
GCF\_MEMORY="512MB"

gcloud functions deploy $GCF\_NAME \\
  --runtime python37  \\
  --source $GCF\_SOURCE \\
  --entry-point $GCF\_ENTRY\_POINT \\
  --update-env-vars $GCF\_ENV\_VARS \\
  --trigger-bucket $GCF\_TRIGGER\_BUCKET \\
  --region $GCF\_REGION \\
  --timeout $GCF\_TIMEOUT \\
  --memory $GCF\_MEMORY \\
  --quiet

Notes:

*   The default timeout for a Cloud Function is 60 seconds. As you're deploying a background function with potentially long processings, set it to the maximum value (540 seconds = 9 minutes).
*   You also need to bump up the memory a little for the video and image processings. Depending on the size of your videos and the maximum resolution of your output summaries, or if you need to generate the summary faster (memory size and vCPU speed are correlated), you might use a higher value (1024MB or 2048MB).

    Deploying function (may take a while - up to 2 minutes)...done.
    availableMemoryMb: 512
    entryPoint: gcf_generate_summary
    environmentVariables:
      SUMMARY_BUCKET: b3-summaries...
    ...
    status: ACTIVE
    timeout: 540s
    updateTime: 'YYYY-MM-DDThh:mm:ss.mmmZ'
    versionId: '1'
    

Here is how it looks like in the [Cloud Console](https://console.cloud.google.com/functions/list):

[![Cloud Functions 2](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/PicardParis/cherry-on-py/raw/master/gcf_video_summary/pics/functions2.png)](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/PicardParis/cherry-on-py/blob/master/gcf_video_summary/pics/functions2.png)

### [](#production-tests-1)Production tests

Make sure to test the function in production. You can upload an annotation file in the 2nd bucket:

VIDEO\_NAME="gbikes\_dinosaur.mp4"
ANNOTATION\_FILE="$VIDEO\_NAME.json"
ANNOTATION\_URI="gs://$ANNOTATION\_BUCKET/$VIDEO\_BUCKET/$ANNOTATION\_FILE"
gsutil cp $ANNOTATION\_URI .
gsutil cp $ANNOTATION\_FILE $ANNOTATION\_URI
rm $ANNOTATION\_FILE

> Note: This reuses the previous local test annotation file and overwrites it. Overwriting a file in a bucket also triggers attached functions.

Wait a few seconds and query the logs to check that the function has been triggered:

gcloud functions logs read --region $GCF\_REGION

    LEVEL  NAME                   EXECUTION_ID  TIME_UTC  LOG
    ...
    D      gcf2_generate_summary  ...           ...       Function execution started
    I      gcf2_generate_summary  ...           ...       Downloading -> /tmp/SUMMARY_BUCKET/VIDEO_BUCKET/VIDEO_NAME
    I      gcf2_generate_summary  ...           ...       Generating summary...
    I      gcf2_generate_summary  ...           ...       Uploading -> VIDEO_BUCKET/VIDEO_NAME.summary004.jpeg
    D      gcf2_generate_summary  ...           ...       Function execution took 11591 ms, finished with status: 'ok'
    

The 2nd function is operational and the pipeline is in place! You can now do end-to-end tests by copying new videos in the 1st bucket.

### [](#results)Results

Download the generated summary on your computer:

cd ~/$PROJECT\_ID
gsutil cp -r gs://$SUMMARY\_BUCKET/\*\*.jpeg .
cloudshell download \*.jpeg

Here is the visual summary for `gbikes_dinosaur.mp4` (4 detected shots):

[![Visual summary for gbikes_dinosaur.mp4](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/PicardParis/cherry-on-py/raw/master/gcf_video_summary/pics/gbikes_dinosaur.mp4.summary004.jpeg)](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/PicardParis/cherry-on-py/blob/master/gcf_video_summary/pics/gbikes_dinosaur.mp4.summary004.jpeg)

You can also directly preview the file from the [Cloud Console](https://console.cloud.google.com/storage/browser/):

[![Video summary](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/PicardParis/cherry-on-py/raw/master/gcf_video_summary/pics/bucket_preview.png)](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/PicardParis/cherry-on-py/blob/master/gcf_video_summary/pics/bucket_preview.png)

* * *

[](#-cherry-on-the-py-)🍒 Cherry on the Py 🐍
---------------------------------------------

Now, the icing on the cake (or the "cherry on the pie" as we say in French)...

*   Based on the same architecture and code, you can add a few features:
    *   Trigger the processing for videos from other buckets
    *   Generate summaries in multiple formats (such as JPEG, PNG, WEBP)
    *   Generate animated summaries (also in multiple formats, such as GIF, PNG, WEBP)
*   Enrich the architecture to duplicate 2 items:
    *   The video shot detection function, to get it to run as an HTTP endpoint
    *   The summary generation function to handle animated images
*   Adapt the code to support the new features:
    *   An `animated` parameter to generate still or animated summaries
    *   Save and upload the results in multiple formats

### [](#architecture-v2)Architecture (v2)

[![Architecture (v2)](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/PicardParis/cherry-on-py/raw/master/gcf_video_summary/pics/architecture_2.png)](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/PicardParis/cherry-on-py/blob/master/gcf_video_summary/pics/architecture_2.png)

*   A. Video shot detection can also be triggered manually with an HTTP GET request
*   B. Still and animated summaries are generated in 2 functions in parallel
*   C. Summaries are uploaded in multiple image formats

### [](#http-entry-point)HTTP entry point

def gcf\_detect\_shots\_http(request):
    """ Cloud Function triggered by an HTTP GET request """
    if request.method != 'GET':
        return ('Please use a GET request', 403)
    if not request.args or 'video\_uri' not in request.args:
        return ('Please specify a "video\_uri" parameter', 400)
    video\_uri \= request.args\['video\_uri'\]
    launch\_shot\_detection(video\_uri, ANNOTATION\_BUCKET)
    return f'Launched shot detection for video\_uri <{video\_uri}\>'

> Note: This is the same code as `gcf_detect_shots` with the video URI parameter provided from a GET request.

### [](#function-deployment-2)Function deployment

GCF\_NAME="gcf1\_detect\_shots\_http"
GCF\_SOURCE="$PROJECT\_SRC/gcf1\_detect\_shots"
GCF\_ENTRY\_POINT="gcf\_detect\_shots\_http"
GCF\_TRIGGER\_BUCKET="$VIDEO\_BUCKET"
GCF\_ENV\_VARS="ANNOTATION\_BUCKET=$ANNOTATION\_BUCKET"
GCF\_MEMORY="128MB"

gcloud functions deploy $GCF\_NAME \\
  --runtime python37  \\
  --source $GCF\_SOURCE \\
  --entry-point $GCF\_ENTRY\_POINT \\
  --update-env-vars $GCF\_ENV\_VARS \\
  --trigger-http \\
  --region $GCF\_REGION \\
  --memory $GCF\_MEMORY \\
  --quiet

Here is how it looks like in the [Cloud Console](https://console.cloud.google.com/functions/list):

[![Cloud Functions 3](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/PicardParis/cherry-on-py/raw/master/gcf_video_summary/pics/functions3.png)](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/PicardParis/cherry-on-py/blob/master/gcf_video_summary/pics/functions3.png)

### [](#animation-support)Animation support

Add an `animated` option in the core function:

class VideoProcessor:
    @staticmethod
    def generate\_summary(annot\_uri: str, output\_bucket: str, animated=False):
        """ Generate a video summary from video shot annotations """
        try:
            with StorageHelper(annot\_uri, output\_bucket) as storage:
                with VideoProcessor(storage) as video\_proc:
                    print('Generating summary...')
\-                   image = video\_proc.render\_summary()
\-                   video\_proc.upload\_summary\_as\_jpeg(image)
+                   if animated:
+                       video\_proc.generate\_summary\_animations()
+                   else:
+                       video\_proc.generate\_summary\_stills()
        except:
            logging.exception(
                'Could not generate summary from shot annotations <%s>',
                annot\_uri)

Define the formats you're interested in generating:

    class ImageFormat:
        \# See https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html
        image\_format: str
        save\_parameters: Dict  \# Make a copy if updated

    class ImageJpeg(ImageFormat):
        image\_format \= 'jpeg'
        save\_parameters \= dict(optimize\=True, progressive\=True)

    class ImageGif(ImageFormat):
        image\_format \= 'gif'
        save\_parameters \= dict(optimize\=True)

    class ImagePng(ImageFormat):
        image\_format \= 'png'
        save\_parameters \= dict(optimize\=True)

    class ImageWebP(ImageFormat):
        image\_format \= 'webp'
        save\_parameters \= dict(lossless\=False, quality\=80, method\=1)

    SUMMARY\_STILL\_FORMATS \= (ImageJpeg, ImagePng, ImageWebP)
    SUMMARY\_ANIMATED\_FORMATS \= (ImageGif, ImagePng, ImageWebP)

Add support to generate still and animated summaries in different formats:

    def generate\_summary\_stills(self):
        image \= self.render\_summary()
        for image\_format in self.SUMMARY\_STILL\_FORMATS:
            self.upload\_summary(\[image\], image\_format)

    def generate\_summary\_animations(self):
        frame\_count \= self.ANIMATION\_FRAMES
        images \= \[\]
        for frame\_index in range(frame\_count):
            shot\_ratio \= (frame\_index+1) / (frame\_count+1)
            print(f'shot\_ratio: {shot\_ratio:.0%}')
            image \= self.render\_summary(shot\_ratio)
            images.append(image)
        for image\_format in self.SUMMARY\_ANIMATED\_FORMATS:
            self.upload\_summary(images, image\_format)

The serialization can still take place in a single function:

    def upload\_summary(self,
                       images: List\['Image'\],
                       image\_format: Type\[ImageFormat\]):
        if not images:
            raise RuntimeError('Empty image list')
        mem\_file \= BytesIO()
        image\_type \= image\_format.image\_format
        save\_parameters \= dict(image\_format.save\_parameters)  \# Copy
        animated \= 1 < len(images)
        if animated:
            save\_parameters.update(dict(
                save\_all\=True,
                append\_images\=images\[1:\],
                duration\=self.ANIMATION\_FRAME\_DURATION\_MS,
                loop\=0,  \# Infinite loop
            ))
        images\[0\].save(mem\_file, format\=image\_type, \*\*save\_parameters)

        image\_bytes \= mem\_file.getvalue()
        self.storage.upload\_summary(image\_bytes, image\_type, animated)

> Note: `Pillow` is both versatile and consistent, allowing for significant and clean code factorization.

Add an `animated` optional parameter to the `StorageHelper` class:

class StorageHelper:
\-    def upload\_summary(self, image\_bytes: bytes, image\_type: str):
\-       path = self.summary\_path(image\_type)
+    def upload\_summary(self, image\_bytes: bytes, image\_type: str, animated=False):
+       path = self.summary\_path(image\_type, animated)
        blob = self.upload\_bucket.blob(path.as\_posix())
        content\_type = f'image/{image\_type}'
        print(f'Uploading -> {blob.name}')
        blob.upload\_from\_string(image\_bytes, content\_type)

+   def summary\_path(self, image\_type: str, animated=False) -> Path:
        video\_name = self.video\_path.name
        shot\_count = self.shot\_count()
\-       suffix = f'summary{shot\_count:03d}.{image\_type}'
+       still\_or\_anim = 'anim' if animated else 'still'
+       suffix = f'summary{shot\_count:03d}\_{still\_or\_anim}.{image\_type}'
        summary\_name = f'{video\_name}.{suffix}'
        return Path(self.video\_path.parent, summary\_name)

And finally, add an `ANIMATED` optional environment variable in the entry point:

...
+ANIMATED = os.getenv('ANIMATED', '0') == '1'

def gcf\_generate\_summary(data, context):
    ...
\-   VideoProcessor.generate\_summary(annot\_uri, SUMMARY\_BUCKET)
+   VideoProcessor.generate\_summary(annot\_uri, SUMMARY\_BUCKET, ANIMATED)

if \_\_name\_\_ == '\_\_main\_\_':
    ...
\-   VideoProcessor.generate\_summary(args.annot\_uri, SUMMARY\_BUCKET)
+   VideoProcessor.generate\_summary(args.annot\_uri, SUMMARY\_BUCKET, ANIMATED)

### [](#function-deployment-3)Function deployment

Duplicate the 2nd function with the additional `ANIMATED` environment variable:

GCF\_NAME="gcf2\_generate\_summary\_animated"
GCF\_SOURCE="$PROJECT\_SRC/gcf2\_generate\_summary"
GCF\_ENTRY\_POINT="gcf\_generate\_summary"
GCF\_TRIGGER\_BUCKET="$ANNOTATION\_BUCKET"
GCF\_ENV\_VARS1="SUMMARY\_BUCKET=$SUMMARY\_BUCKET"
GCF\_ENV\_VARS2="ANIMATED=1"
GCF\_TIMEOUT="540s"
GCF\_MEMORY="2048MB"

gcloud functions deploy $GCF\_NAME \\
  --runtime python37  \\
  --source $GCF\_SOURCE \\
  --entry-point $GCF\_ENTRY\_POINT \\
  --update-env-vars $GCF\_ENV\_VARS1 \\
  --update-env-vars $GCF\_ENV\_VARS2 \\
  --trigger-bucket $GCF\_TRIGGER\_BUCKET \\
  --region $GCF\_REGION \\
  --timeout $GCF\_TIMEOUT \\
  --memory $GCF\_MEMORY \\
  --quiet

Here is how it looks like in the [Cloud Console](https://console.cloud.google.com/functions/list):

[![Cloud Functions 4](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/PicardParis/cherry-on-py/raw/master/gcf_video_summary/pics/functions4.png)](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/PicardParis/cherry-on-py/blob/master/gcf_video_summary/pics/functions4.png)

[](#-final-tests)🎉 Final tests
-------------------------------

The HTTP endpoint lets you trigger the pipeline with a GET request:

GCF\_NAME="gcf1\_detect\_shots\_http"
VIDEO\_URI="gs://cloudmleap/video/next/visionapi.mp4"
GCF\_URL="https://$GCF\_REGION\-$PROJECT\_ID.cloudfunctions.net/$GCF\_NAME?video\_uri=$VIDEO\_URI"

curl $GCF\_URL -H "Authorization: bearer $(gcloud auth print-identity-token)"

    Launched shot detection for video_uri <VIDEO_URI>
    

> Note: The test video `<visionapi.mp4>` is located in an external bucket but is publicly accessible.

In addition, copy one or several videos into the video bucket. You can drag and drop videos:

[![Dragging files to a bucket](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/PicardParis/cherry-on-py/raw/master/gcf_video_summary/pics/dragndrop.gif)](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/PicardParis/cherry-on-py/blob/master/gcf_video_summary/pics/dragndrop.gif)

The videos are then processed in parallel. Here are a few logs:

    LEVEL NAME                           EXECUTION_ID ... LOG
    ...
    D     gcf2_generate_summary_animated f6n6tslsfwdu ... Function execution took 49293 ms, finished with status: 'ok'
    I     gcf2_generate_summary          yd1vqabafn17 ... Uploading -> b1-videos.../JaneGoodall.mp4.summary035_still.png
    I     gcf2_generate_summary_animated qv9b03814jjk ... shot_ratio: 43%
    I     gcf2_generate_summary          yd1vqabafn17 ... Uploading -> b1-videos.../JaneGoodall.mp4.summary035_still.webp
    D     gcf2_generate_summary          yd1vqabafn17 ... Function execution took 54616 ms, finished with status: 'ok'
    I     gcf2_generate_summary_animated g4d2wrzxz2st ... shot_ratio: 71%
    ...
    D     gcf2_generate_summary          amwmov1wk0gn ... Function execution took 65256 ms, finished with status: 'ok'
    I     gcf2_generate_summary_animated 7pp882fz0x84 ... shot_ratio: 57%
    I     gcf2_generate_summary_animated i3u830hsjz4r ... Uploading -> b1-videos.../JaneGoodall.mp4.summary035_anim.png
    I     gcf2_generate_summary_animated i3u830hsjz4r ... Uploading -> b1-videos.../JaneGoodall.mp4.summary035_anim.webp
    D     gcf2_generate_summary_animated i3u830hsjz4r ... Function execution took 70862 ms, finished with status: 'ok'
    ...
    

In the 3rd bucket, you'll find all still and animated summaries:

[![Video summary](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/PicardParis/cherry-on-py/raw/master/gcf_video_summary/pics/bucket_details.png)](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/PicardParis/cherry-on-py/blob/master/gcf_video_summary/pics/bucket_details.png)

You've already seen the still summary for `<JaneGoodall.mp4>` as an introduction to this tutorial. In the animated version, and in only 6 frames, you get an even better idea of what the [whole video](https://storage.googleapis.com/cloudmleap/video/next/JaneGoodall.mp4) is about:

[![Video summary](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/PicardParis/cherry-on-py/raw/master/gcf_video_summary/pics/JaneGoodall.mp4.summary035_anim.gif)](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/PicardParis/cherry-on-py/blob/master/gcf_video_summary/pics/JaneGoodall.mp4.summary035_anim.gif)

If you don't want to keep your project, you can delete it:

    gcloud projects delete $PROJECT_ID
    

[](#-one-more-thing)➕ One more thing
------------------------------------

first\_line\_after\_licence=16
find $PROJECT\_SRC -name '\*.py' -exec tail -n +$first\_line\_after\_licence {} \\; | grep -v "^$" | wc -l
289

You did everything in under 300 lines of Python. Less lines, less bugs! 🔥🐍 **Mission accomplished!** 🐍🔥

[](#-see-you)🖖 See you
-----------------------

I hope you appreciated this tutorial and would love to read [your feedback](https://bit.ly/feedback-video-summary). You can also [follow me on Twitter](https://twitter.com/PicardParis).