Cloud Shell Tutorials: Learning experiences integrated into the Cloud Console

# Cloud Shell Tutorials: Learning experiences integrated into the Cloud Console

By Marc Cohen, Developer Advocate

A few weeks ago we released the [Open in Cloud Shell feature](https://cloudplatform.googleblog.com/2017/11/introducing-Open-in-Cloud-Shell-a-new-way-to-create-frictionless-tutorials.html), which lets a simple hyperlink open a cloud shell with an automatically cloned Github repo, preselected open files in the Cloud Editor and other features to make creating interactive content as easy as possible. Today we’re adding the ability to integrate your tutorials right into the [Google Cloud Platform Console](https://console.cloud.google.com/) and run them via the click of a link. Here’s a quick peek at the authoring and user experience:

Cloud Shell tutorials are authored in (CommonMark) Markdown syntax, with extensions to support capabilities to, for example:

- Create a new project
- Enable billing
- Open a file
- Highlight a UI element

Cloud Shell tutorials offer the ability to automate all of the above functions and more, via simple Markdown syntax.

In other words, instead of providing indirect instructions, like “open the file foo.txt by clicking the highlighted file in the image shown below,” your tutorial can, more directly and more simply, say “click **here** to open foo.txt.” Clicking that link will have the expected effect directly inside the Cloud Console.

Here are some examples of use cases:

- a tutorial for a service or product where a sample app lives in an associated repo
- a walkthrough of a repo that introduces people to the project structure
- a sequence of steps for installing prerequisites and building something interesting (akin to the `INSTALL` file found in some open source repos)

Cloud Shell tutorials make it easy for anyone to build compelling instructional material, integrated right into the Cloud Console. You can read more about this feature in the public documentation, which contains an example tutorial showing off all the new capabilities along with the corresponding Markdown syntax.

Here’s a [simple self-explanatory example](https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/GoogleCloudPlatform/cloud-shell-tutorials.git&page=editor&tutorial=tutorial.md). We hope you enjoy building some great tutorials using this feature and let us know about your experiences, good and bad, via the Feedback link on the bottom of the documentation page!