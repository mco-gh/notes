MIMIC-CXR Database v2.0.0

 ** Database  ** Credentialed Access

# MIMIC-CXR Database

 **  [Alistair Johnson]()  ** ,  [Tom Pollard]()  ** ,  [Roger Mark]()  ** ,  [Seth Berkowitz]()  ** ,  [Steven Horng]()  **  **

Published: Sept. 19, 2019. Version: 2.0.0

* * *

 **When using this resource, please cite:**

Johnson, A., Pollard, T., Mark, R., Berkowitz, S., Horng, S. (2019). MIMIC-CXR Database. PhysioNet. doi:10.13026/C2JT1Q

 **Please include the standard citation for PhysioNet:**

Goldberger AL, Amaral LAN, Glass L, Hausdorff JM, Ivanov PCh, Mark RG, Mietus JE, Moody GB, Peng C-K, Stanley HE. PhysioBank, PhysioToolkit, and PhysioNet: Components of a New Research Resource for Complex Physiologic Signals (2003). Circulation. 101(23):e215-e220.

## Abstract

The MIMIC Chest X-ray (MIMIC-CXR) Database v2.0.0 is a large publicly available dataset of chest radiographs in DICOM format with free-text radiology reports. The dataset contains 377,110 images corresponding to 227,835 radiographic studies performed at the Beth Israel Deaconess Medical Center in Boston, MA. The dataset is de-identified to satisfy the US Health Insurance Portability and Accountability Act of 1996 (HIPAA) Safe Harbor requirements. Protected health information (PHI) has been removed. The dataset is intended to support a wide body of research in medicine including image understanding, natural language processing, and decision support.

* * *

## Background

Chest radiography is a common imaging modality used to assess the thorax and the most common medical imaging study in the world. Chest radiographs are used to identify acute and chronic cardiopulmonary conditions, verify that devices such as pacemakers, central lines, and tubes are correctly positioned, and to assist in related medical workups. In the U.S., the number of radiologists as a percentage of the physician workforce is decreasing [1]. and the geographic distribution of radiologists favors larger, more urban counties [2]. Delays and backlogs in timely medical imaging interpretation have demonstrably reduced care quality in such large health organizations as the U.K. National Health Service [3] and the U.S. Department of Veterans Affairs [4]. The situation is even worse in resource-poor areas, where radiology services are extremely scarce. As of 2015, only 11 radiologists served the 12 million people of Rwanda [5], while the entire country of Liberia, with a population of four million, had only two practicing radiologists [6]. Accurate automated analysis of radiographs has the potential to improve the efficiency of radiologist workflow and extend expertise to under-served regions.

* * *

## Methods

The creation of MIMIC-CXR required handling three distinct data modalities: electronic health record data, images (chest radiographs), and natural language (free-text reports). These three modalities were processed approximately independently and ultimately combined to create the database.

### Electronic health record

The BIDMC operates a locally built electronic health record (EHR) to store and process clinical data. A collection of images associated with a single report is referred to as a study. We queried the BIDMC EHR for chest x-ray studies made in the emergency department between 2011 - 2016, and extracted the set of patient identifiers associated with these studies. We subsequently extracted all chest x-ray studies for this set of patients between 2011 - 2016. For anonymization purposes, two sets of random identifiers were generated. First, a random identifier was generated for each patient in the range 10,000,000 - 19,999,999, which we refer to as the `subject_id`. Each patient was also assigned a date shift which mapped their first index admission year to a year between 2100 - 2200. This ensures anonymity of the data while preserving the relative chronology of patient information, which is crucial for appropriate processing of the data.  Second, each report was associated with a single unique identifier. We generated a random identifier for each study in the range 50,000,000 - 59,999,999. We refer to the anonymized study identifier as the `study_id`. As multiple images may be associated with the same study (e.g. one frontal and one lateral image), multiple images in MIMIC-CXR have the same `study_id`. Finally, a random 40 character hash was generated for each individual image file. These hashes are unique to each image.

### Chest radiographs

Chest radiographs were sourced from the hospital picture archiving and communication system (PACS) in Digital Imaging and Communications in Medicine (DICOM) format. DICOM is a common format for medical images which facilitates interoperability of many distinct medical devices. Put simply, the DICOM format contains structured meta-data associated with one or more images, and the DICOM standard stipulates strict rules around the structure of this information.

The acquired DICOM images contained PHI which required removal for conformance with HIPAA. Images sometimes contain ``burned in'' annotations: areas where pixel values have been modified after image acquisition in order to display text. Annotations contain relevant information including: image orientation, anatomical position of the subject, timestamp of image capture, and so on. The resulting image, with textual annotations encoded within the pixel themselves, is then transferred from the modality to PACS. Since the annotations are applied at the modality level, it is impossible to recover the original image without annotations.

Due to the burned in annotations, image pixel values required de-identification. A custom algorithm was developed which removed dates and patient identifiers, but retained radiologically relevant information such as orientation. The algorithm applied an ensemble of image preprocessing and optical character recognition approaches to detect text within an image. Images were binarized to enhance contrast of the text with the background. Three thresholds were used to binarize the image: one based off maximum pixel intensity, one based upon minimum pixel intensity, and one using a fixed pixel value frequently used by the modality when adding text. Optical character recognition was performed using the tesseract library v3.05.02 [7]. Text was classified as PHI using a set of custom regular expressions which aimed to be conservative in removal of text and allow for errors in the optical character recognition. If a body of text was suspected to be PHI, all pixel values in a bounding box encompassing the PHI were set to black. For files cleaned of PHI, the DICOM header contains the location of any inserted black boxes.

### Radiology Reports

During routine clinical care, clinicians trained in interpreting imaging studies (radiologists) will summarize their findings for a particular image in a free-text note. Radiology reports for the images were identified and extracted from the hospital EHR system. The reports were de-identified using a rule-based approach based upon prior work [8] combined with a newly developed neural network approach. PHI has been replaced with three consecutive underscores ("___"). Study reports are stored in individual text files named using the anonymous study identifier. Note that one or more image files may be associated with a study, but only one radiology report is written.

* * *

## Data Description

### Overview

MIMIC-CXR v2.0.0 contains:

- A set of 10 folders (p10 - p19), each with ~6,500 sub-folders. Sub-folders are named according to the patient identifier, and contain free-text reports and DICOM files for all studies for that patient
- cxr-record-list.csv.gz - a compressed file providing the link between an image, its corresponding study identifier, and its corresponding patient identifier
- cxr-study-list.csv.gz - a compressed file providing a link between anonymous study and patient identifiers
- mimic-cxr-reports.tar.gz - for convenience, all free-text reports have been compressed in a single archive file

### Folder structure

Free-text reports and images are provided in individual folders. An example of the folder structure for a single patient's images is as follows:

files
└── p10
└── p10000032
├── s50414267
│   ├── 02aa804e-bde0afdd-112c0b34-7bc16630-4e384014.dcm
│   └── 174413ec-4ec4c1f7-34ea26b7-c5f994f8-79ef1962.dcm
├── s50414267.txt
├── s53189527
│   ├── 2a2277a9-b0ded155-c0de8eb9-c124d10e-82c5caab.dcm
│   └── e084de3b-be89b11e-20fe3f9f-9c8d8dfe-4cfd202c.dcm
├── s53189527.txt
├── s53911762
│   ├── 68b5c4b1-227d0485-9cc38c3f-7b84ab51-4b472714.dcm
│   └── fffabebf-74fd3a1f-673b6b41-96ec0ac9-2ab69818.dcm
├── s53911762.txt
├── s56699142
│   └── ea030e7a-2e3b1346-bc518786-7a8fd698-f673b44c.dcm
└── s56699142.txt

Above, we have a single patient, `p10000032`. Since the first three characters of the folder name are `p10`, the patient folder is in the `p10/` folder. This patient has four radiographic studies: `s50414267`, `s53189527`, `s53911762`, and `s56699142`. These study identifiers are completely random, and their order has no implications for the chronological order of the actual studies. Each study has two chest x-rays associated with it, except `s56699142`, which only has one study.

### Metadata files

The cxr-record-list.csv.gz file lists all DICOM images available in the dataset. It also provides a mapping of these DICOM images to their corresponding anonymous study and subject identifier.

The cxr-study-list.csv.gz lists all studies available in the dataset, and provides a mapping of these anonymous study identifiers to the patient identifier.

The mimic-cxr-reports.zip file is a compressed archive containing all text reports in the dataset. While the text reports are available within each patient folder, users may be interested in examining only the text without the images. This archive file is intended to make this process simpler.

* * *

## Usage Notes

Use of the dataset is free to all researchers after signing of a data use agreement which stipulates, among other items, that (1) the user will not share the data, (2) the user will make no attempt to reidentify individuals, and (3) any publication which makes use of the data will also make the relevant code available.

* * *

## Release Notes

### MIMIC-CXR v2.0

This is the second public release of MIMIC-CXR, which provides DICOM formatted image files, and free-text radiology reports. The images are identical to MIMIC-CXR v1.0, but have been reorganized into random study identifiers rather than sequential integers, and are in their native DICOM format.

* * *

## Acknowledgements

We would like to acknowledge Zhiyong Lu and Yifan Peng from the National Center for Biotechnology Information (NCBI) for their insight in the creation of MIMIC-CXR. Clinical We would like to acknowledge the Stanford Machine Learning Group and the Stanford AIMI center for useful discussions; in particular we would like to thank Jeremy Irvin, Pranav Rajpurkar, and Matthew Lungren.

We would also like to acknowledge the Beth Israel Deaconess Medical Center for their continued collaboration.

This work was supported by grant NIH-R01-EB017205 from the National Institutes of Health. The MIT Laboratory for Computational Physiology received funding from Philips Healthcare to create the database described in this paper.

* * *

## Conflicts of Interest

Philips Healthcare supported the creation of this resource.

* * *

## References

1. Margaret Douglass, Computer-assisted de-identification of free-text nursing notes. Master's Thesis, 2005. MIT.

2. Ray Smith. An overview of the tesseract OCR engine. In Ninth International Conference on Document Analysis and Recognition (ICDAR 2007), volume 2, pages 629–633. IEEE, 2007.

3. Farah S Ali, Samantha G Harrington, Stephen B Kennedy, and Sarwat Hussain. Diagnostic radiology in Liberia: a country report. Journal of Global Radiology, 1(2):6, 2015.

4. David A Rosman, Jean Jacques Nshizirungu, Emmanuel Rudakemwa, Crispin Moshi, Jean de Dieu Tuyisenge,Etienne Uwimana, and Louise Kalisa. Imaging in the land of 1000 hills: Rwanda radiology country report. Journal of Global Radiology, 1(1):5, 2015.

5. Sarah Bastawrous and Benjamin Carney. Improving patient safety: Avoiding unread imaging exams in the nationalva enterprise electronic health record. Journal of digital imaging, 30(3):309–313, 2017.

6. Abi Rimmer. Radiologist shortage leaves patient care at risk, warns royal college. BMJ: British Medical Journal(Online), 359, 2017.

7. Andrew B Rosenkrantz, Wenyi Wang, Danny R Hughes, and Richard Duszak Jr. A county-level analysis of theus radiologist workforce: physician supply and subspecialty characteristics. Journal of the American College of Radiology, 15(4):601–606, 2018.

8. Andrew B Rosenkrantz, Danny R Hughes, and Richard Duszak Jr. The US radiologist workforce: an analysis of temporal and geographic variation by using large national datasets. Radiology, 279(1):175–184, 2015.

* * *

##### Share

 [**](https://physionet.org/content/mimic-cxr/2.0.0/mailto:?subject=MIMIC-CXR%20Database&body=https://physionet.org/content/mimic-cxr/2.0.0/)  [**](http://www.facebook.com/sharer.php?u=https://physionet.org/content/mimic-cxr/2.0.0/)  [**](https://www.linkedin.com/shareArticle?url=https://physionet.org/content/mimic-cxr/2.0.0/)  [**](https://www.reddit.com/submit?url=https://physionet.org/content/mimic-cxr/2.0.0/&title=MIMIC-CXR%20Database)  [**](https://twitter.com/intent/tweet?text=MIMIC-CXR%20Database.%20https://physionet.org/content/mimic-cxr/2.0.0/)

##### Access

 **Access Policy:**

Only PhysioNet credentialed users who sign the specified DUA can access the files.

 **License (for files):**

 [PhysioNet Credentialed Health Data License 1.5.0](https://physionet.org/content/mimic-cxr/view-license/2.0.0/)

##### Discovery

**DOI:**
 https://doi.org/10.13026/C2JT1Q

**Topics:**

 [mimic](https://physionet.org/content/?topic=mimic)  [natural language processing](https://physionet.org/content/?topic=natural+language+processing)  [machine learning](https://physionet.org/content/?topic=machine+learning)  [computer vision](https://physionet.org/content/?topic=computer+vision)  [radiology](https://physionet.org/content/?topic=radiology)  [chest x-rays](https://physionet.org/content/?topic=chest+x-rays)

**Project Website:**
 [** https://mimic-cxr.mit.edu](https://mimic-cxr.mit.edu/)

##### Corresponding Author

 *You must be logged in to view the contact information.*

##### Versions

- [1.0.0](https://physionet.org/content/mimic-cxr/1.0.0/) - Aug. 2, 2019

- [2.0.0](https://physionet.org/content/mimic-cxr/2.0.0/) - Sept. 19, 2019

## Files

This is a restricted-access resource. To access the files, you must be a [credentialed user](https://physionet.org/settings/credentialing/) and [sign the data use agreement](https://physionet.org/sign-dua/mimic-cxr/2.0.0/) for the project.