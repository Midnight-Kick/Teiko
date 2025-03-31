Instructions:
Running P1.py will produce the results found in cell-count-relative.csv. 
Running P2.py will produce boxplots for each cell group. I also added the boxplots in a folder to refer to more easily.

Python
P2 part b:
    cd4 cell group has a significant difference in relative frequencies between responders and non-responders.
    Performing a t-test for cd4_t cells between responders and non-responders it yields a p-value of approximately 0.0210, which is less than the common significance level of 0.05.
    This means that it is statistically significantly different.

Databases
P1:
Tables:

Projects:
project_id (VARCHAR, PRIMARY KEY) - Unique identifier for the project

Subjects:
subject_id (VARCHAR, PRIMARY KEY) - Unique identifier for the subject
project_id (VARCHAR, FOREIGN KEY referencing Projects)
condition (VARCHAR) - The condition of the subject
age (INTEGER)
sex (VARCHAR(1)) - 'M' or 'F'

Treatments:
treatment_id (VARCHAR, PRIMARY KEY) - Unique identifier for the treatment

Samples:
sample_id (VARCHAR, PRIMARY KEY) - Unique identifier for the sample
subject_id (VARCHAR, FOREIGN KEY referencing Subjects)
time_from_treatment_start (INTEGER) - Time elapsed from the start of treatment (or 0 if no treatment/baseline)
sample_type (VARCHAR) - Type of sample (e.g., 'PBMC', 'tumor')
response (VARCHAR(1), NULLABLE) - 'y' for responder, 'n' for non-responder, NULL if not applicable
treatment_id (VARCHAR, FOREIGN KEY referencing Treatments, NULLABLE) - Link to the treatment the subject received for this sample.

CellCounts:
cell_count_id (INTEGER, PRIMARY KEY, AUTO_INCREMENT) - Unique identifier for each cell count record
sample_id (VARCHAR, FOREIGN KEY referencing Samples)
b_cell (INTEGER)
cd8_t_cell (INTEGER)
cd4_t_cell (INTEGER)
nk_cell (INTEGER)
monocyte (INTEGER)

Relationships:
A Project can have many Subjects.
A Subject belongs to one Project.
A Subject can have multiple Samples taken at different time points.
A Sample belongs to one Subject.
A Sample might be associated with a specific Treatment.
A Sample has one set of CellCounts.


P2:
Some advantages in capturing this information in a database would be data integrity and consistency, efficient data retrieval and querying, scalability, data management
and organization, reduced data redundancy, support for complex analytics, concurrency and multi-user access, and data security.

P3:
SELECT
    condition,
    COUNT(DISTINCT subject_id) AS number_of_subjects
FROM
    Subjects
GROUP BY
    condition
ORDER BY
    condition;

P4:
SELECT
    s.sample_id,
    s.subject_id,
    s.time_from_treatment_start,
    s.sample_type,
    sub.condition,
    t.treatment_name
FROM
    Samples s
JOIN
    Subjects sub ON s.subject_id = sub.subject_id
LEFT JOIN
    Treatments t ON s.treatment_id = t.treatment_id
WHERE
    sub.condition = 'melanoma'
    AND s.sample_type = 'PBMC'
    AND s.time_from_treatment_start = 0
    AND s.treatment_id = 'tr1';

P5: 
a:
SELECT
    p.project_id,
    COUNT(s.sample_id) AS number_of_samples
FROM
    Samples s
JOIN
    Subjects sub ON s.subject_id = sub.subject_id
JOIN
    Projects p ON sub.project_id = p.project_id
WHERE
    sub.condition = 'melanoma'
    AND s.sample_type = 'PBMC'
    AND s.time_from_treatment_start = 0
    AND s.treatment_id = 'tr1'
GROUP BY
    p.project_id;

b: 
SELECT
    s.response,
    COUNT(s.sample_id) AS number_of_samples
FROM
    Samples s
JOIN
    Subjects sub ON s.subject_id = sub.subject_id
WHERE
    sub.condition = 'melanoma'
    AND s.sample_type = 'PBMC'
    AND s.time_from_treatment_start = 0
    AND s.treatment_id = 'tr1'
GROUP BY
    s.response;


c:
SELECT
    sub.sex,
    COUNT(s.sample_id) AS number_of_samples
FROM
    Samples s
JOIN
    Subjects sub ON s.subject_id = sub.subject_id
WHERE
    sub.condition = 'melanoma'
    AND s.sample_type = 'PBMC'
    AND s.time_from_treatment_start = 0
    AND s.treatment_id = 'tr1'
GROUP BY
    sub.sex;