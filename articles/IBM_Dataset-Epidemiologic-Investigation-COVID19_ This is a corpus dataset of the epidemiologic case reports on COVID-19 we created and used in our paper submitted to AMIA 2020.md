IBM/Dataset-Epidemiologic-Investigation-COVID19: This is a corpus dataset of the epidemiologic case reports on COVID-19 we created and used in our paper submitted to AMIA 2020

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='53'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' class='js-evernote-checked' data-evernote-id='701'%3e%3c/path%3e%3c/svg%3e)](https://github.com/IBM/Dataset-Epidemiologic-Investigation-COVID19#the-dataset-of-epidemiological-case-reports-for-covid-19)The Dataset of Epidemiological Case Reports for COVID-19

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='54'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' class='js-evernote-checked' data-evernote-id='703'%3e%3c/path%3e%3c/svg%3e)](https://github.com/IBM/Dataset-Epidemiologic-Investigation-COVID19#introduction)Introduction

This repository contains a dataset (named `ECR-COVID-19`) of epidemiological case reports with entity labeling which can be used for information extraction.

The motivation of creating and contributing the dataset is to trigger the research on epidemiologic investigation analysis and automation. COVID-19 is threatening the health of the entire human population. In order to control the spread of the disease, epidemiological investigations should be conducted, to trace the infection source of each confirmed patient and isolate their close contacts. However, the analysis on a mass of case reports in epidemiological investigation is extremely time-consuming and labor-intensive. Using the latest NLP technology to accelerate the information extraction from epidemiological case reports should be a feasible and good way. So we prepared the dataset, meanwhile we also submitted a paper to AMIA 2020, the title is "Accelerating Epidemiological Investigation Analysis by Using NLP and Knowledge Reasoning: A Case Study on COVID-19".

We collected the epidemiological case reports from Dec 19, 2019 to Feb 7, 2020 from the websites of China CDC and some main-stream news websites. This repository was created from the case reports which were labelled by manual with entities, relations, and events.

Special thanks to China CDC and the subbranchs in local cities. Lots of the data are from their announcements. We also appreciate the following news websites some of the data are from: sina.com.cn, people.com.cn, thepaper.cn and news.163.com etc.

If you use this dataset, please cite our paper:

	Wang J, Wang K, Li J, Jiang JM, Wang YF, Mei J, Accelerating Epidemiological Investigation Analysis by Using NLP and
	Knowledge Reasoning: A Case Study on COVID-19, AMIA 2020. (submission)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='55'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' class='js-evernote-checked' data-evernote-id='710'%3e%3c/path%3e%3c/svg%3e)](https://github.com/IBM/Dataset-Epidemiologic-Investigation-COVID19#data-format)Data Format

Each data file (train.txt, valid.txt, test.txt) in the folder `ECR-COVID-19` includes a list of lines. Each line is a string in JSON format and includes a case report and corresponding labels. The following are the description of json keys:

(1) doc_id : the ID of current document
(2) text: the original plain text of the case report

(3) entities: All labelled entities in the "text". In each entity, there are two numbers and one string, the first number is the starting position of the entity in "text", the second number is the ending position. The entity does not include the charactor at the ending position. The string indicates the entity type of the entities. Entity types include:

- 'LocalID' : the patient ID in a city
- 'Name' : the family name of the patient if there is,
- 'Age' : the age of the patient
- 'Gender' : the gender of the patient
- 'ResidencePlace' : the residence place of the patient
- 'SuspectedPatientContact' : if current patient has or has not the history of contacting suspected COVID-19 patient
- 'InfectionOriginContact' : if current patient has or has not the history of trip to the COVID-19 origin regions or contacting the passager(s) from COVID-19 origin regions
- 'Event' : a verb to indicate an activity in activity records
- 'Onset' : a verb to indicate the event of disease onset
- 'HospitalVisit' : a verb to indicate the event of seeing a doctor
- 'DiagnosisConfirmed' ：a verb to indicate the event of being confirmed as COVID-19 disease
- 'Inpatient' : a verb to indicate the event of admission as a COVID-19 patient
- 'Discharge' : a verb to indicate the event of discharging
- 'Death' : a verb to indicate the event of death
- 'Observed' : a verb to indicate the event of being observed as a suspected COVID-19 patient
- 'Date' : the date or time . or the start date/time for a duration
- 'EndDate' : the end date/time for a duration
- 'Symptom' : Symptom words
- 'LabTest' : Lab test
- 'ImagingExamination' : Imaging examination
- 'Location' : City or privince
- 'Spot' : a spot, such as hotel, building, station, home, etc.
- 'Vehicle' : a vehicle, such as train, bus, car, ship, airplan and so on.
- 'SocialRelation' : Social relations, such as relatives relation, classmate, colleague and so on.
- 'Negation' : negation words

(4) patient, relations and events : The three json elements define the structure of three tuples: Patient tuple, Social relation tuple and Event tuple. They seperately include the attributes for a patient, the attributes for social relations and the attributes for events. Actually we are using tuple structure to define the relations among named entities.

The following is one example of these lines

	{
	    "doc_id": 6886,
	    "text": "患者二十九，女，56岁，现住瑞安，无武汉外出史或旅游史，与确诊病例有接触史，1月20日发病，咳嗽咳痰、肌肉酸痛、气促，现在定点医疗机构隔离治疗。",
	    "entities": [
	        [
	            59,
	            61,
	            "Date"
	        ],
	        [
	            14,
	            16,
	            "ResidencePlace"
	        ],
	        [
	            67,
	            71,
	            "Inpatient"
	        ],
	        [
	            61,
	            67,
	            "Location"
	        ],
	        [
	            56,
	            58,
	            "Symptom"
	        ],
	        [
	            51,
	            55,
	            "Symptom"
	        ],
	        [
	            48,
	            50,
	            "Symptom"
	        ],
	        [
	            46,
	            48,
	            "Symptom"
	        ],
	        [
	            43,
	            45,
	            "Onset"
	        ],
	        [
	            38,
	            43,
	            "Date"
	        ],
	        [
	            28,
	            37,
	            "InfectionOriginContact"
	        ],
	        [
	            17,
	            27,
	            "InfectionOriginContact"
	        ],
	        [
	            8,
	            11,
	            "Age"
	        ],
	        [
	            6,
	            7,
	            "Gender"
	        ],
	        [
	            0,
	            5,
	            "LocalID"
	        ]
	    ],
	    "patient": [
	        [
	            0,
	            5,
	            "LocalID"
	        ],
	        [
	            14,
	            16,
	            "ResidencePlace"
	        ],
	        [
	            8,
	            11,
	            "Age"
	        ],
	        [
	            6,
	            7,
	            "Gender"
	        ],
	        [
	            17,
	            27,
	            "InfectionOriginContact"
	        ],
	        [
	            28,
	            37,
	            "InfectionOriginContact"
	        ]
	    ],
	    "relations": [],
	    "events": [
	        {
	            "type": [
	                43,
	                45,
	                "Onset"
	            ],
	            "tuple": [
	                [
	                    38,
	                    43,
	                    "Date"
	                ],
	                [
	                    46,
	                    48,
	                    "Symptom"
	                ],
	                [
	                    48,
	                    50,
	                    "Symptom"
	                ],
	                [
	                    51,
	                    55,
	                    "Symptom"
	                ],
	                [
	                    56,
	                    58,
	                    "Symptom"
	                ]
	            ]
	        },
	        {
	            "type": [
	                67,
	                71,
	                "Inpatient"
	            ],
	            "tuple": [
	                [
	                    59,
	                    61,
	                    "Date"
	                ],
	                [
	                    61,
	                    67,
	                    "Location"
	                ]
	            ]
	        }
	    ]
	}